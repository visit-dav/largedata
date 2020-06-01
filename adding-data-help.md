### How to add data files to this repo

Assume all your data files are stored in a directory named `foo_data`.

1.  It is not a *requirement* but please try to create all download format options,
`.7z`, `.tar.gz` and `.zip` whenever possible. The advantages of the various
formats are...
  * `.7z` ([7-zip.org](https://www.7-zip.org/download.html))
     * Usually the smallest files by 2-3x so faster to download.
     * Decompression tools are available for [Windows](https://www.7-zip.org/download.html),
       [Mac](https://apps.apple.com/us/app/the-unarchiver/id425424353) and
       [Linux](https://www.7-zip.org/download.html).
     * However decompression tools are not often *pre-built* on most systems and instead
       need to be downloaded and installed.
  * `.tar.gz` (aka `.tgz`, [tarball](https://en.wikipedia.org/wiki/Tar_(computing)))
     * Most commonly used on Linux/Unix systems
     * Windows and Mac tools often handle `.tar.gz` files
  * `.zip` ([zip](https://en.wikipedia.org/wiki/Zip_(file_format)))
     * Most commonly used on Windows systems.
     * Linux/Unix and Mac tools often handle `.zip` files.
  ```
     7z a -y -m0=lzma2 -mx=9 foo_data.7z foo_data
     tar cvf - foo_data | gzip --best > foo_data.tar.gz
     zip -9 foo_data.zip foo_data 
  ```
1. Add your data files to the `bindata` directory.
   ```
   git add foo.7z
   git add foo.tar.gz
   git add foo.zip
   git commit -a -m 'adding foo data'
   git push
   ```
1. Pushing your added files to GitHub can take a long time depending on file sizes.
Once the operation is completed, the files you see in the repo on GitHub will be
[LFS *pointer* files ](https://help.github.com/en/github/managing-large-files/about-git-large-file-storage#pointer-file-format).
Anyone cloning the repo will get only these *pointer* files. To get the actual data
files these LFS *pointer* files reference to appear in a cloned repo, a `git-lfs pull`
operation is required. A problem with this operation is that it cannot be used to
selectively download only one of the data files here. To allow users to selectively
download specific files here, we provide access to those files *raw blobs* through
GitHub *magic* URL. We provide access to the data this way through the
[website](https://visit-dav.github.io/largedata/) we host from this repo.
1. Create a new markdown file in the `_datarchive` *collection* directory. In the
front-matter for that file, you optionally define the file sizes, sha256 and md5
checksums for various of the formats you host. If you don't host a specific format,
then don't include lines for `nbytes` member of that format in the front-matter.
Also, feel free to include a description of the data in the *body* of the file.
   ```
   git add _datarchive/foo.md
   git commit -a -m 'adding foo to collection'
   git push
   ```
1. Take note that the download path to your data file (not the LFS *pointer* file)
will be `https://github.com/visit-dav/largedata/blob/master/bindata/foo_data.7z?raw=true`
You can use this link anywhere including in email to tell users how to get this
data. Users do not requie a GitHub account in order to access data through this link.
1. Wait for the site to rebuild. This usually takes less than a few minutes after
your push.