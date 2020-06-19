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

In the table below...

* Clicking a size link downloads the data in the indicated format.
* Clicking a title or image link gives more info about the download.
* `.7z` is often 2-3x smaller but see [our guidance](help/7zip.md) for help with it.

<table>
  <caption>Data downloads available here</caption>
  <tr>
    <th style="text-align: left">Title</th>
    <th style="text-align: left">Thumbnail</th>
    <th style="text-align: right"><code>.7z</code></th>
    <th style="text-align: right"><code>.tar.gz</code></th>
    <th style="text-align: right"><code>.zip</code></th>
  </tr>
{% for darch in site.datarchives %}
    {% assign nktgz = darch.nbytes.tgz | divided_by: 1000 %}
    {% assign nkzip = darch.nbytes.zip | divided_by: 1000 %}
    {% assign nk7z = darch.nbytes.7z | divided_by: 1000 %}
    {% assign nMtgz = darch.nbytes.tgz | divided_by: 1000000 %}
    {% assign nMzip = darch.nbytes.zip | divided_by: 1000000 %}
    {% assign nM7z = darch.nbytes.7z | divided_by: 1000000 %}
    {% if nktgz < 1000 %}
        {% assign ntgz = nktgz | append: "KB" %}
    {% else %}
        {% assign ntgz = nMtgz | append: "MB" %}
    {% endif %}
    {% if nkzip < 1000 %}
        {% assign nzip = nkzip | append: "KB" %}
    {% else %}
        {% assign nzip = nMzip | append: "MB" %}
    {% endif %}
    {% if nk7z < 1000 %}
        {% assign n7z = nk7z | append: "KB" %}
    {% else %}
        {% assign n7z = nM7z | append: "MB" %}
    {% endif %}
    {% assign len = darch.relative_path | size %}
    {% assign len2 = len | minus: 3 %}
    {% assign new_relative_path = darch.relative_path | truncate: len2, "" | remove_first: "_" %}
    <tr>
        <td style="text-align: left"><a href="{{ new_relative_path }}" title="Click for more info about this file">{{ darch.title }}</a></td>
    {% if darch.has_image %}
        <td style="text-align: left"><a href="{{ new_relative_path }}" title="Click for more info about this file"><img src="{{ new_relative_path }}_thumb.png" style="height=48;"></a></td>
    {% else %}
        <td style="text-align: left">None</td>
    {% endif %}
    {% if darch.nbytes.7z %}
        <td style="text-align: right"><a href="{{ site.rawdata_baseurl }}/{{ darch.stem }}.7z?raw=true" title="Click to download .7z file now">{{ n7z }}</a></td>
    {% else %}
        <td style="text-align: right">N/A</td>
    {% endif %}
    {% if darch.nbytes.tgz %}
        <td style="text-align: right"><a href="{{ site.rawdata_baseurl }}/{{ darch.stem }}.tar.gz?raw=true" title="Click to download .tar.gz file now">{{ ntgz }}</a></td>
    {% else %}
        <td style="text-align: right">N/A</td>
    {% endif %}
    {% if darch.nbytes.zip %}
        <td style="text-align: right"><a href="{{ site.rawdata_baseurl }}/{{ darch.stem }}.zip?raw=true" title="Click to ownload .zip file now">{{ nzip }}</a></td>
    {% else %}
        <td style="text-align: right">N/A</td>
    {% endif %}
    </tr>
{% endfor %}
</table>
