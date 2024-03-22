---
title: Exhibit
layout: about
permalink: /exhibit.html
# include CollectionBuilder info at bottom
credits: false
# Edit the markdown on in this file to describe your collection
# Look in _includes/feature for options to easily add features to the page
---

<!---

banner image here
{% include feature/jumbotron.html objectid="https://cdil.lib.uidaho.edu/images/palouse_sm.jpg" %} 

nav menu on top
{% include feature/nav-menu.html sections="Introduction: Women of Carifesta;Lynette Dolphin;Louise Bennett;Lorna Goodison;Guyana Drums;Notes" %}
--> 

<body data-bs-spy="scroll" data-bs-target="#navbar" data-bs-offset="0" data-bs-root-margin="0px 0px -40%" data-bs-smooth-scroll="true">

<nav id="navbar" class="navbar bg-body-tertiary px-3 mb-3 sticky-top">
  <a class="navbar-brand" href="#">Exhibit Navigation</a>
  <ul class="nav nav-pills">
    {% for section in site.sections %}
      <li class="nav-item">
        <a class="nav-link" href="#{{ section.title | slugify }}">{{ section.title }}</a>
      </li>
    {% endfor %}
  </ul>
</nav>

<div class="scrollspy-example bg-body-tertiary p-3 rounded-2" tabindex="0">
  {% for section in site.sections %}
  <div id="{{ section.title | slugify }}">
    <h2>{{ section.title }}</h2>
    {{ section.content | markdownify }}
  </div>
  {% endfor %}
</div>

<!-- Including Bootstrap -->
<script src="https://stackpath.bootstrapcdn.com/bootstrap/5.1.3/js/bootstrap.bundle.min.js"></script>

</body>