## About Download Links

Once files have been [added](adding-download-files.md) to this repository,
the files you see on GitHub or when the repository is cloned will be
[LFS *pointer* files ](https://help.github.com/en/github/managing-large-files/about-git-large-file-storage#pointer-file-format).

A question is, how do you specify a download link to the actual data files?

### A quick note about cloning and git lfs pull

First, anyone cloning the repo will get only LFS *pointer* files and not the actual
data files. To get to the actual data files in a cloned repository, a
`git lfs pull` operation is needed. But, **BE CAREFUL**!! An unqualified `git lfs pull`
operation downloads *every* LFS file in the repo which could take hours. If you are
interested in only specific files, use the `--include` option to `git lfs pull` to
identify the specific file(s) you want to fully download.

### Links to download specific files

When writing emails or documentation which includes links to files to be
downloaded, cloning and git lfs is not used. Instead, we we provide HTTPs access
to those files through the website that is hosted from this repository using GitHub
*magic* URL to access their *raw* contents.

The download path for `foo_data.tar.gz` (not the LFS *pointer* file), for example,
will look something like...

```
https://github.com/visit-dav/largedata/blob/master/bindata/foo_data.tar.gz?raw=true
```

You can use this link anywhere including in email to give users the link to get that
specific data file. Users do not require a GitHub account in order to access data
through this link.

Better still, give them a link to the *landing page* for the file, which will
look something like...

```
https://visit-dav.github.io/largedata/datarchives/foo
```

This takes users to a page with more information about the file including all the
download format options (e.g. `.7z`, `.tar.gz`, `.zip`, etc.) and their integrity checks.
