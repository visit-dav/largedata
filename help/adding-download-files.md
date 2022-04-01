---
layout: default
---
## How to add files

This repository can be used to host many kinds of large files including
PowerPoint presentations, data archives, movies, 3D object files, etc.
The repository is configured to treat files with
[various extensions](https://raw.githubusercontent.com/visit-dav/largedata/master/.gitattributes)
using
[GitHub's Large File Support](https://help.github.com/en/github/managing-large-files/about-git-large-file-storage).

Currently, there are layouts defined for data archives and presentations. See
the [section on adding an new file type](#how-to-add-new-collections) if you
need to expand the kinds of files hosted here. 

### Adding a presentation

[Below](#adding-a-data-archive), we provide instructions for adding binary
data archives. Apart from perhaps skipping the first step to create and
compress an archive file, the same procedure can be used to add presentations,
movies, etc.

### Adding a data archive

The instructions below are written assuming all data files to be added are stored
in a directory named `foo_data`. When creating archives, it is a best practice to
ensure all files in the archive expand into a single top-level directory which is
the same name as the archive file name without the extension. For example, all
files in the `foo_data.tar.gz` file would expand into a directory named `foo_data.`

1. It is not a *requirement* but please try to create all download format options,
`.tar.xz`, `.tar.gz` and `.zip` whenever possible. If you provide only one option, `.tar.gz`
is probably the best because all platforms have ubiquitous tools to process that
format. The advantages of the various formats are...
   * `.tar.xz`
     * Usually the smallest files by 2-3x.
     * Tools are not *pre-built* on all systems so users may wind up
       having to download and install them prior to use.
     * A command to produce a maximally compressed `.tar.xz` data file using
       4 threads...

   ```
   tar cvf - foo_dir | xz -9e -T4 - > foo_dir.tar.xz
   ```
   * `.tar.gz` (aka `.tgz`, [tarball](https://en.wikipedia.org/wiki/Tar_(computing)))
     * Most commonly used on Linux/Unix systems.
     * Windows and Mac tools often handle `.tar.gz` files.
     * Best format if you only provide one download option.
     * A command to produce a `.tar.gz` compressed data file...

   ```
   tar cvf - foo_data | gzip --best > foo_data.tar.gz
   ```
   * `.zip` ([zip](https://en.wikipedia.org/wiki/Zip_(file_format)))
     * Most commonly used on Windows systems.
     * Linux/Unix and Mac tools often handle `.zip` files.
     * A command to produce a `.zip` compressed data file...

   ```
   zip -9 foo_data.zip foo_data 
   ```

1. Add your data files to the `bindata` directory. Because we don't expect content here
to be simultaneously revised by multiple developers or to be changing on a frequent basis,
it is perfectly fine to do all the work here directly on the `master` branch.
   ```
   git pull
   git add bindata/foo_data.tar.xz
   git add bindata/foo_data.tar.gz
   git add bindata/foo_data.zip
   git commit -a -m 'adding foo data'
   git push
   ```
1. Pushing your added data files to GitHub can take a long time depending on file
sizes. Once the operation completes, be aware that the files you see in the repo
on GitHub will be
[LFS *pointer* files ](https://help.github.com/en/github/managing-large-files/about-git-large-file-storage#pointer-file-format).
See instructions regarding [download links](about-download-links.md) about how
to define links to LFS'd content.
1. Create the dataset's landing page by creating a markdown file, `foo.md`, in the
`_datarchives` *collection* directory. In the
front-matter for this file, you may optionally define the file sizes, sha256 and md5
checksums for the formats you host. If you don't host a specific format,
then don't include lines for `nbytes` member of that format in the front-matter.
Also, feel free to include a detailed description of the data in the *body* of the file.
1. You may optionally add an image for the data. Be sure to create one about 300-600
pixels in *width* and another, thumbnail, about 64 pixels in *height*. Be sure to
name the files `foo.png` and `foo_thumbnail.png` and put these files in the
`_datarchives` collection directory allong with the `foo.md` markdown file. If you do
this, be sure to set the variable `has_image: true` in `foo.md`
[frontmatter](https://jekyllrb.com/docs/front-matter/).
   ```
   git add _datarchives/foo.md
   git add _datarchives/foo.png
   git add _datarchives/foo_thumbnail.png
   git commit -a -m 'adding foo data'
   git push
   ```
1. Wait for the site to rebuild. This usually takes less than a few minutes after
your push.

## Adding a whole new *collection*

Currently, the repository is configured to handle two kinds of file types,
data archives and presentations. The steps below outline the process to add
a new file type.

1. Edit `_config.yml` to define the new *collection*. For example, to add
a new `gorfos` collection, add a new member to the `collection` member like
so...

   ```
   collections:
     gorfos:
       output: true
       formats:
         - .foo
         - .bar
       format_remarks:
         - "foo is for foobirds."
         - "bar is for barbees."
   ```

The `output: true` tells GitHub/Jekyll site generator to *output* an
`html` file for each *member* of the `gorfo` collection. The `formats`
member lists the possible file extensions for this class of file.
The `format_remarks` is short text that will appear as a tool-tip in
a web browser when a user hovers the mouse over the format options
on various pages.
1. Add the file extensions to the `.gitattributes` file like so...

   ```
   *.foo filter=lfs diff=lfs merge=lfs -text
   *.bar filter=lfs diff=lfs merge=lfs -text
   ```

1. Create a *layout* for this new class of file in the `_layouts` directory
named `gorfo.html`. This layout will define how *landing pages* for instances
of the *gorfo* class will appear. These *landing pages* capture information
about a *gorfo* file instance being hosted such as the size in bytes, sha256
and md5 checksums for various formats. Use the existing layouts as examples
to see how this is done.
1. Create a top level directory named `_gorfo`. This is where markdown
files used to describe each instance of a `gorfo` file will be placed
along with whatever additional assets they may need like images or
whatever. For example, if you add a new member to the `gorfo` collection
named `fred`, there would be a `fred.md` file in the `_gorfo` directory
that describes information about the file as well as the file sizes
and integrity checks captured as `front-matter`.
1. Create a top level directory, such as `bingorfo` where the actual *gorfo*
files will be stored (as LFS'd content).
1. Now, you are free to add members to the `_gorfo` directory. Each
will involve a new `.md` file. See the examples in the `datarchives`
collection.
