---
---

<ul>
{% for file in site.static_files %}
<li>{{ file.modified_time | date: "%s" }}: {{ file.path }}</li>
{% endfor %}
</ul>

