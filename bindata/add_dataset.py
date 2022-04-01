#!/usr/bin/env python3 -u

import hashlib, os, re, shutil, sys, tarfile, zipfile
from optparse import OptionParser

# run ./add_dataset.py --help for documentation
def usage():
    return \
"""
%prog args [test-file1 test-file2 ...]

Add comments here

"""

def confirm_startup_dir():
    retval = True

    if not os.getcwd().split('/')[-1] == 'bindata':
        print('"bindata" does not appear to be current working directory name.')
        retval = False

    if not retval:
        print('Run this script only from the "bindata" directory.')
        sys.exit(1)
    return True

def parse_args():
    """
    Parses arguments.
    """
    parser = OptionParser(usage())
    parser.add_option("-t",
                      "--title",
                      dest="title",
                      help="[Required]: String for dataset title.")
    parser.add_option("-i",
                      "--image",
                      dest="image",
                      help="[Optional] Filename for the dataset image file.")
    parser.add_option("-m",
                      "--markdown",
                      dest="markdown",
                      help="[Required] Filename for a markdown file holding description of dataset.")
    opts, files = parser.parse_args()
    return opts, files

def generate_file_cksum(filename, hashmode=hashlib.md5(), blocksize=2**20):
    with open(filename, "rb" ) as f:
        while True:
            buf = f.read(blocksize)
            if not buf:
                break
            hashmode.update(buf)
    return hashmode.hexdigest()

def archive_stem(s):

    # Remove all non-word characters (everything except numbers and letters)
    s = re.sub(r"[^\w\s]", '', s)

    # Replace all runs of whitespace with a single underscore
    s = re.sub(r"\s+", '_', s)

    return s.lower()

def create_tar_gz_archive(title, files):
    aname = archive_stem(title)+'.tar.gz'
    with tarfile.open(aname, 'w:gz',
        compresslevel=9) as tf:
        print('Creating .tar.gz archive...',end='')
        for f in files:
            tf.add(f)
        print('done')
    size = os.path.getsize(aname)
    md5 = generate_file_cksum(aname)
    sha256 = generate_file_cksum(aname, hashlib.sha256())
    return size, md5, sha256
    
def create_tar_xz_archive(title, files):
    aname = archive_stem(title)+'.tar.xz'
    with tarfile.open(aname, 'w:xz',
        preset=9) as tf:
        print('Creating .tar.xz archive...',end='')
        for f in files:
            tf.add(f)
        print('done')
    size = os.path.getsize(aname)
    md5 = generate_file_cksum(aname)
    sha256 = generate_file_cksum(aname, hashlib.sha256())
    return size, md5, sha256

def create_zip_archive(title, entries):
    aname = archive_stem(title)+'.zip'
    with zipfile.ZipFile(aname, 'w',
        compression=zipfile.ZIP_DEFLATED, compresslevel=9) as zf:
        print('Creating .zip archive...',end='')
        for e in entries:
            if os.path.isdir(e):
                for root, dirs, files in os.walk(e):
                    for f in files:
                        zf.write(os.path.join(root,f))
            else:
                zf.write(e)
        print('done')
    size = os.path.getsize(aname)
    md5 = generate_file_cksum(aname)
    sha256 = generate_file_cksum(aname, hashlib.sha256())
    return size, md5, sha256


def create_thumbnail(imfile):
    from PIL import Image
    im = Image.open(imfile)
    scale = float(im.size[1])/64.0
    tsize = (int(im.size[0]/scale), int(im.size[1]/scale))
    imthumb = im.resize(tsize,resample=Image.BICUBIC)
    imthumb.save('../_datarchives/%s_thumb.png'%os.path.splitext(imfile)[0],'PNG')

#
# Output a markdown file
#
def create_md_landing_page(vopts, gzcks, xzcks, zpcks):

    with open('../_datarchives/%s.md'%archive_stem(vopts['title']),'w') as mdfile:
        mdfile.write('---\n')
        mdfile.write('layout: datarchive\n')
        mdfile.write('title: %s\n'%vopts['title'])
        mdfile.write('stem: %s\n'%archive_stem(vopts['title']))
        if vopts['image']:
            mdfile.write('has_image: true\n')
        mdfile.write('nbytes:\n')
        mdfile.write('  - %d\n'%int(xzcks[0]))
        mdfile.write('  - %d\n'%int(gzcks[0]))
        mdfile.write('  - %d\n'%int(zpcks[0]))
        mdfile.write('md5:\n')
        mdfile.write('  - %s\n'%xzcks[1])
        mdfile.write('  - %s\n'%gzcks[1])
        mdfile.write('  - %s\n'%zpcks[1])
        mdfile.write('sha256:\n')
        mdfile.write('  - %s\n'%xzcks[2])
        mdfile.write('  - %s\n'%gzcks[2])
        mdfile.write('  - %s\n'%zpcks[2])
        mdfile.write('---\n')
        if vopts['markdown']:
            with open(vopts['markdown'], 'r') as txt:
                mdfile.writelines(txt.readlines())

def add_dataset_main(vopts, files):

    #
    # Create the archive files
    #
    gzcks = create_tar_gz_archive(vopts['title'], files)
    xzcks = create_tar_xz_archive(vopts['title'], files)
    zpcks = create_zip_archive(vopts['title'], files)

    #
    # Create thumbnail from given image
    #
    if vopts['image']:
        create_thumbnail(vopts['image'])

    #
    # Create markdown landing page for dataset
    #
    create_md_landing_page(vopts, gzcks, xzcks, zpcks)

#
# So this python script can be used both as a shell command
# and as an imported python module.
#
if __name__ == '__main__':

    #
    # Confirm we are in correct dir
    #
    confirm_startup_dir()
    
    #
    # Read the command line
    #
    opts, files = parse_args()
    vopts = vars(opts)

    add_dataset_main(vopts, files)

