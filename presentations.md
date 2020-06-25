## Presentations Collection

In the table below...

* Clicking a size link downloads the data in the indicated format.
* Clicking a title or image link gives more info about the download.
* See [our guidance](help/7zip.md) for help with any `.7z` content.

{% assign pres_coll = 0 %} 
{% for coll in site.collections %}
    {% if coll.label == "presentations" %}
        {% assign pres_coll = coll %}
        {% break %}
    {% endif %}
{% endfor %}

{% assign ncols = pres_coll.formats | size | minus: 1 %}

<table>
  <caption>Presentations available here</caption>
  <tr>
    <th style="text-align: left">Title</th>
    <th style="text-align: left">Thumbnail</th>
    {% for i in (0..ncols) %}
      <th style="text-align: right" title="{{pres_coll.format_remarks[i]}}"><code>{{pres_coll.formats[i]}}</code></th>
    {% endfor %}
  </tr>

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

    <td style="text-align: right"><a href="{{ site.rawdata_baseurl }}/{{ pres.stem }}{{pres_coll.formats[i]}}?raw=true" title="Click to download {{pres_coll.formats[i]}} file now">{{ nsize }}</a></td>
    {% endfor %}

    </tr>

{% endfor %}

</table>
