---
title: Exhibit
layout: default
permalink: /exhibit.html
# include CollectionBuilder info at bottom
credits: false
---

<body data-bs-spy="scroll" data-bs-target="#sidebar" data-bs-offset="0">

<div class="wrapper">

<!-- Sidebar Collapse Button -->
<button 
        type="button" id="sidebarToggle"  class="sidebarToggle"  onclick="toggleNav()" aria-label="Exhibit Navigation">
        <i class="fa-solid fa-list"></i>
</button>

<!-- Sidebar -->

  <nav id="sidebar" class="sidebar bg-body-primary px-3">
        <a class="navbar-brand" href="#">Exhibit Navigation</a>
          <ul class="nav nav-pills flex-column">
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

<!-- Main Text Content -->

  <div id="content">

  {% for section in site.sections %}
    <div id="{{ section.title | slugify }}">
      <h2>{{ section.title }}</h2>
      {{ section.content | markdownify }}
    </div>
  {% endfor %}
    <div id="contact-button-bottom" class="text-center mt-4">
      <div class="container">
        <a href="https://forms.gle/RE9TZP1bGGCAoFfe9" class="btn btn-primary btn-lg" role="button" target="_blank" style="width: 100%;">Contact Us</a>
      </div>
    </div>
  </div>

</div>

<!-- Sidebar Collapse Scripts -->

<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/js/bootstrap.bundle.min.js"></script>

<script>
function toggleNav() {
  const sidebar = document.getElementById('sidebar');
  sidebar.classList.toggle('active');
}
</script>

</body>