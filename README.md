## Welcome to VisIt Large Data

This [website](https://visit-dav.github.io/largedata/) and the
[GitHub repo](https://github.com/visit-dav/largedata/) that backs it up
is where the VisIt project hosts large datasets used in examples, tutorials
and for other purposes. These datasets are managed using
[GitHub's Large File Support (LFS)](https://git-lfs.github.com) but are also
available to download individually via HTTPs from this website.

For help using or contributing, see these resources...

* [Adding files here](help/adding-download-files.md)
* [Specifying download links](help/about-download-links.md)
* [How to upload files to VisIt developers](help/using-for-uploads.md)
* [Using 7zip](help/7zip.md)
* [Markdown primer](help/markdown.md) 
* [Notes about the GH pages theme](help/about-theme.md)

### Available Collections

{% for coll in site.collections %}
* [{{coll.label}}]({{coll.label}}.md)
{% endfor %}
