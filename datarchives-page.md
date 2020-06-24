## Data Archives Collection

In the table below...

* Clicking a size link downloads the data in the indicated format.
* Clicking a title or image link gives more info about the download.
* `.7z` is often 2-3x smaller but see [our guidance](help/7zip.md) for help with it.

<table>
  <caption>Data archives available here</caption>
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
    {% assign nk7z = darch.nbytes.p7z | divided_by: 1000 %}
    {% assign nMtgz = darch.nbytes.tgz | divided_by: 1000000 %}
    {% assign nMzip = darch.nbytes.zip | divided_by: 1000000 %}
    {% assign nM7z = darch.nbytes.p7z | divided_by: 1000000 %}
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
        <td style="text-align: left"><a href="{{ new_relative_path }}" title="Click for more info about this file"><img src="{{ new_relative_path }}_thumb.png" style="height:48px;"></a></td>
    {% else %}
        <td style="text-align: left">None</td>
    {% endif %}
    {% if darch.nbytes.p7z %}
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
