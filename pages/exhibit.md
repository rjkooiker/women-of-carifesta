---
title: Exhibit
layout: about
permalink: /exhibit.html
# include CollectionBuilder info at bottom
credits: false
---

<body data-bs-spy="scroll" data-bs-target="#navbar" data-bs-offset="0" data-bs-root-margin="0px 0px -40%" data-bs-smooth-scroll="true">

<nav id="navbar" class="navbar bg-body-tertiary px-3 mb-3 sticky-top">
  <a class="navbar-brand" href="#">Exhibit Navigation</a>
  <ul class="nav nav-pills">
    {% for section in site.sections %}
      <li class="nav-item">
        <a class="nav-link" href="#{{ section.title | slugify }}">{{ section.title }}</a>
      </li>
    {% endfor %}
    <li class="nav-item">
      <a class="nav-link" href="#contact-button-bottom">Contact</a>
      </li>
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

<div id="contact-button-bottom" class="text-center mt-4">
  <div class="container">
    <a href="https://forms.gle/RE9TZP1bGGCAoFfe9" class="btn btn-primary btn-lg" role="button" target="_blank" style="width: 100%;">Contact Us</a>
  </div>
</div>

</body>