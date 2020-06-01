---
---

<!--
We're using Liquid here somewhat unusually to have it output MARKDOWN instead
of the usual HTML. But, the challenge is that Markdown is highly sensitive to
newlines and Liquid is somewhat unpredictable in the creation of newlines.
So, first, we need to create a Liquid variable that represents
a NEWLINE. That is that the first capture block is all about. Then, we capture
the entire Markdown table as a single Liquid string variable, tabletxt, with
'EOL' representing the end of each line of the table. Finally, we output the
Markdown table, striping all newlines that Liquid may have inserted, replacing
any HTML <p> and </p> that Liquid may have inserted with spaces and then finally
replacing the EOLs with real newlines.
-->
{% capture newline %}
{% endcapture %}

{% capture tabletxt %}
| Title | `.7z` | `.tar.gz` | `.zip` |EOL|:---|---:|---:|---:|EOL
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
| {{ darch.title }} | [{{n7z}}]({{site.rawdata_baseurl}}/{{darch.stem}}.7z?raw=true) | [{{ntgz}}]({{site.rawdata_baseurl}}/{{darch.stem}}.tar.gz?raw=true) | [{{nzip}}]({{site.rawdata_baseurl}}/{{darch.stem}}.zip?raw=true) | EOL
{% endfor %}
{% endcapture %}
{{tabletxt | replace: "<p>, " " | replace "</p>, " " | strip_newlines | replace: "EOL", newline}}


<!-- Here is the normal HTML way -->
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

{% for darch in site.datarchives %}
<p>content: {{ darch.content }}</p>
<p>path: {{ darch.path }}</p>
<p>relative_path: {{ darch.relative_path }}</p>
<p>url: {{ url.path }}</p>
<p>collection: {{ url.collection }}</p>

<p>title: {{ darch.title }}</p>
<p>stem: {{ darch.stem }}</p>
<p>Sizes:</p>
<ul>
<li>7z: {{ darch.nbytes.7z}}</li>
<li>tgz: {{ darch.nbytes.tgz}}</li>
<li>zip: {{ darch.nbytes.zip}}</li>
</ul>
<p>sha256:</p>
<ul>
<li>7z: {{ darch.sha256.7z}}</li>
<li>tgz: {{ darch.sha256.tgz}}</li>
<li>zip: {{ darch.sha256.zip}}</li>
</ul>
{% endfor %}

### Static files list
<ul>
{% for file in site.static_files %}
<li>{{ file.modified_time | date: "%s" }}: {{ file.path }}</li>
{% endfor %}
</ul>

