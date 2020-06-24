---
layout: presentation
---
## Presentations Collection

In the table below...

* Clicking a size link downloads the data in the indicated format.
* Clicking a title or image link gives more info about the download.
* For any `.7z` content see [our guidance](help/7zip.md) for help with it.

<table>
  <caption>Presentations available here</caption>
  <tr>
    <th style="text-align: left">Title</th>
    <th style="text-align: left">Thumbnail</th>
    {% for fmt in layout.formats %}
      <th style="text-align: right"><code>{{fmt}}</code></th>
    {% endfor %}
  </tr>

{% assign ncols = layout.formats | size %}

{% for pres in site.presentations %}

  {% assign len = pres.relative_path | size %}
  {% assign len2 = len | minus: 3 %}
  {% assign new_relative_path = pres.relative_path | truncate: len2, "" | remove_first: "_" %}
  <tr>
     <td style="text-align: left"><a href="{{ new_relative_path }}" title="Click for more info about this file">{{ pres.title }}</a></td>
  {% if pres.has_image %}
     <td style="text-align: left"><a href="{{ new_relative_path }}" title="Click for more info about this file"><img src="{{ new_relative_path }}_thumb.png" style="height:48px;"></a></td>
  {% else %}
     <td style="text-align: left">None</td>
  {% endif %}

  {% for i in (0..ncols) %}

    {% assign nksize = pres.nbytes[i] | divided_by: 1000 %}
    {% assign nMsize = pres.nbytes[i] | divided_by: 1000000 %}
    {% if nksize < 1000 %}
        {% assign nsize = nksize | append: "KB" %}
    {% else %}
        {% assign nsize = nMsize | append: "MB" %}
    {% endif %}

    <td style="text-align: right"><a href="{{ site.rawdata_baseurl }}/{{ pres.stem }}{{layout.formats[i]}}?raw=true" title="Click to download file now">{{ nsize }}</a></td>
    {% endfor %}

    </tr>

{% endfor %}

</table>
