---
layout: default
---
## Data Archives Collection

In the table below...

* Clicking a size link downloads the data in the indicated format.
* Clicking a title or image link gives more info about the download.

{% assign darch_coll = 0 %} 
{% for darch in site.collections %}
    {% if darch.label == "datarchives" %}
        {% assign darch_coll = darch %}
        {% break %}
    {% endif %}
{% endfor %}

{% assign ncols = darch_coll.formats | size | minus: 1 %}

<table>
  <caption>Data archives available here</caption>
  <tr>
    <th style="text-align: left">Title</th>
    <th style="text-align: left">Thumbnail</th>
    {% for i in (0..ncols) %}
      <th style="text-align: right" title="{{darch_coll.format_remarks[i]}}"><code>{{darch_coll.formats[i]}}</code></th>
    {% endfor %}
  </tr>

{% for pres in site.datarchives %}

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

    <td style="text-align: right"><a href="{{ site.rawdata_baseurl }}/bindata/{{ pres.stem }}{{darch_coll.formats[i]}}?raw=true" title="Click to download {{darch_coll.formats[i]}} file now">{{ nsize }}</a></td>
    {% endfor %}

    </tr>

{% endfor %}

</table>
