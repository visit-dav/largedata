---
---

| Title | `.7z` | `.tar.gz` | `.zip` |
|:---|:---:|:---:|:---:|
|a|b|c|d|



| Title | `.7z` | `.tar.gz` | `.zip` |
|:---|:---:|:---:|:---:|
{% for darch in site.datarchives -%}
    {%- assign nktgz = darch.nbytes.tgz | divided_by: 1000 -%}
    {%- assign nkzip = darch.nbytes.zip | divided_by: 1000 -%}
    {%- assign nk7z = darch.nbytes.7z | divided_by: 1000 -%}
    {%- assign nMtgz = darch.nbytes.tgz | divided_by: 1000000 -%}
    {%- assign nMzip = darch.nbytes.zip | divided_by: 1000000 -%}
    {%- assign nM7z = darch.nbytes.7z | divided_by: 1000000 -%}
    {%- if nktgz < 1000 -%}
        {% assign ntgz = nktgz | append: "KB" -%}
    {%- else -%}
        {% assign ntgz = nMtgz | append: "MB" -%}
    {%- endif -%}
    {%- if nkzip < 1000 -%}
        {% assign nzip = nkzip | append: "KB" -%}
    {%- else -%}
        {% assign nzip = nMzip | append: "MB" -%}
    {%- endif -%}
    {%- if nk7z < 1000 -%}
        {% assign n7z = nk7z | append: "KB" -%}
    {%- else -%}
        {% assign n7z = nM7z | append: "MB" -%}
    {%- endif -%}
| {{- darch.title -}} | [{{-n7z-}}]({{-darch.stem-}}.7z) | [{{-ntgz-}}]({{-darch.stem-}}.tar.gz) | [{{-nzip-}}]({{-darch.stem-}}.zip) |
{%- endfor -%}

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

### Static files list
<ul>
{% for file in site.static_files %}
<li>{{ file.modified_time | date: "%s" }}: {{ file.path }}</li>
{% endfor %}
</ul>

