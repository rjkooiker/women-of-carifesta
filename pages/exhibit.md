---
title: Exhibit
layout: about
permalink: /exhibit.html
# include CollectionBuilder info at bottom
credits: true
# Edit the markdown on in this file to describe your collection
# Look in _includes/feature for options to easily add features to the page
---

<!---

banner image here
{% include feature/jumbotron.html objectid="https://cdil.lib.uidaho.edu/images/palouse_sm.jpg" %} 

nav menu on top
{% include feature/nav-menu.html sections="Introduction: Women of Carifesta;Lynette Dolphin;Louise Bennett;Lorna Goodison;Guyana Drums;Notes" %}
--> 


<!---experimenting with nav scrollspy on bootstrap-->

<!---
<nav id="navbar-example2" class="navbar bg-body-tertiary px-3 mb-3">
  <a class="navbar-brand" href="#">Navigation</a>
  <ul class="nav nav-pills">
    <li class="nav-item">
      <a class="nav-link" href="#scrollspyHeading1">Introduction: Women of Carifesta</a>
    </li>
    <li class="nav-item">
      <a class="nav-link" href="#scrollspyHeading2">Lynette Dolphin</a>
    </li>
    <li class="nav-item">
      <a class="nav-link" href="#scrollspyHeading3">Louise Bennett</a>
    </li>
    <li class="nav-item">
      <a class="nav-link" href="#scrollspyHeading4">Lorna Goodison</a>
    </li>
    <li class="nav-item">
      <a class="nav-link" href="#scrollspyHeading5">Guyana Drums</a>
    </li>
    <li class="nav-item">
      <a class="nav-link" href="#scrollspyHeading6">Notes</a>
    </li>
  </ul>
</nav>
-->

<!---
<div data-bs-spy="scroll" data-bs-target="#navbar-example2" data-bs-root-margin="0px 0px -40%" data-bs-smooth-scroll="true" class="scrollspy-example bg-body-tertiary p-3 rounded-2" tabindex="0">
  <h2 id="scrollspyHeading1">Introduction: Women of Carifesta</h2>
  <p>...</p>
  <h2 id="scrollspyHeading2">Lynette Dolphin</h2>
  <p>...</p>
  <h2 id="scrollspyHeading3">Louise Bennett</h2>
  <p>...</p>
  <h2 id="scrollspyHeading4">Lorna Goodison</h2>
  <p>...</p>
  <h2 id="scrollspyHeading5">Guyana Drums</h2>
  <p>...</p>
  <h2 id="scrollspyHeading6">Notes</h2>
  <p>...</p>
</div>
-->

<!---
<body>

<nav id="navbar" class="navbar bg-body-tertiary px-3 mb-3">
  <a class="navbar-brand" href="#">Exhibit Navigation</a>
  <ul class="nav nav-pills">
    {% for section in site.sections %}
      <li class="nav-item">
        <a class="nav-link" href="#{{ section.id }}">{{ section.title }}</a>
      </li>
    {% endfor %}
  </ul>
</nav>



<div data-bs-spy="scroll" data-bs-target="#navbar" data-bs-root-margin="0px 0px -40%" data-bs-smooth-scroll="true" class="scrollspy-example bg-body-tertiary p-3 rounded-2" tabindex="0">
  {% for section in site.sections %}
  <div id="{{ section.id }}">
    {{ section.content | markdownify }}
  </div>
  {% endfor %}
</div>

<!-- Including Bootstrap
<script src="https://stackpath.bootstrapcdn.com/bootstrap/5.1.3/js/bootstrap.bundle.min.js"></script>

</body>
--->

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
