## Welcome to the VisIt Large Data Repo

This [website](https://visit-dav.github.io/largedata/) and the
[GitHub repo that backs it up](https://visit-dav.github.io/largedata/)
is where the VisIt project hosts large datasets used in examples, tutorials
and for other purposes. These datasets are managed using
[GitHub's Large File Support (LFS)](https://git-lfs.github.com) but are also
available to download individually via HTTPs from this website.

For help contributing to this repo see these resources...

* [Adding data files](help/adding-data-help.md)
* [Markdown primer](help/markdown-help.md) 


In the table below...

* Clicking a size link will download the file in the indicated format.
* Clicking the title link will give more information about the download.
* To use `.7z`, see [our guidance for 7-zip](help/7zip-help.md).

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
        <td style="text-align: left"><a href="{{ new_relative_path }}" title="Click for more info about this file"><img src="datarchives/aneurysm_thumb.png" style="height=64;"></a></td>
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
