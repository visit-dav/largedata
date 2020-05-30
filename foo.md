---
---

### Data Archive List

{% for darch in site.datarchives %}
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

