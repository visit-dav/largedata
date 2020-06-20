## How to add files

This repository can be used to host many kinds of large files including
PowerPoint presentations, data archives, movies, 3D object files, etc.
The repository is configured to treat files with
[various extensions](https://raw.githubusercontent.com/visit-dav/largedata/master/.gitattributes)
using
[GitHub's Large File Support](https://help.github.com/en/github/managing-large-files/about-git-large-file-storage).

Below, we provide instructions for adding binary data archives. Apart from
perhaps skipping the first step to create and compress an archive file, the
same procedure can be used to add PowerPoint presentations, movies, etc.

### Adding a data archive

The instructions below are written assuming all data files to be added are stored
in a directory named `foo_data`. When creating archives, it is a best practice to
ensure all files in the archive expand into a single top-level directory which is
the same name as the archive file name without the extension. For example, all
files in the `foo_data.tar.gz` file would expand into a directory named `foo_data.`

1. It is not a *requirement* but please try to create all download format options,
`.7z`, `.tar.gz` and `.zip` whenever possible. If you provide only one option, `.tar.gz`
is probably the best because all platforms have ubiquitous tools to process that
format. The advantages of the various formats are...
   * `.7z` ([7-zip.org](https://www.7-zip.org/download.html))
     * Usually the smallest files by 2-3x.
     * Tools are available for [Windows](https://www.7-zip.org/download.html),
       [Mac](https://apps.apple.com/us/app/the-unarchiver/id425424353) and
       [Linux](https://www.7-zip.org/download.html).
     * Tools are not often *pre-built* on most systems so users wind up
       having to download and install them prior to use.
     * A command to produce a `7z` compressed data file...

```
7z a -y -m0=lzma2 -mx=9 foo_data.7z foo_data
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
   git add bindata/foo_data.7z
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
   git commit -a -m 'adding foo page datarchives collection'
   git push
   ```
1. Wait for the site to rebuild. This usually takes less than a few minutes after
your push.
