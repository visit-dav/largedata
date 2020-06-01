## Welcome to the VisIt Large Data Repo

This is where the VisIt project hosts large datasets used in examples, tutorials
and for other purposes. These datasets are managed using
[GitHub's Large File Support (LFS)](https://git-lfs.github.com).

To facilitate HTTPs access to datasets hosted here, this respository is also generated
as a website and hosted at
[https://visit-dav.github.io/largedata/](https://visit-dav.github.io/largedata/).

For help adding to this repo see these resources...

* [Guidance for 7-zip](7zip-help.md)
* [Instructions for adding new data here](adding-data-help.md)
* [Instructions for composing content in markdown](markdown-help.md) 

<table>
  <tr>
    <th style="text-align: left">Title</th>
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
        <td style="text-align: left"><a href="{{ new_relative_path }}">{{ darch.title }}</a></td>
        <td style="text-align: right"><a href="{{ site.rawdata_baseurl }}/{{ darch.stem }}.7z?raw=true">{{ n7z }}</a></td>
        <td style="text-align: right"><a href="{{ site.rawdata_baseurl }}/{{ darch.stem }}.tar.gz?raw=true">{{ ntgz }}</a></td>
        <td style="text-align: right"><a href="{{ site.rawdata_baseurl }}/{{ darch.stem }}.zip?raw=true">{{ nzip }}</a></td>
    </tr>
{% endfor %}
</table>
