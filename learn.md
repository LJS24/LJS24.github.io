---
layout: default
title: Learn
permalink: /learn/
---
{% assign posts = site.posts | where_exp: "post", "post.categories contains 'learn'" %}

<section class="hero-card hero-card-sub">
  <p class="hero-label">Learning Notes</p>
  <h2>Concept summaries and implementation notes</h2>
  <p class="hero-text">This section stores reusable learning records from study and practice.</p>
</section>

<section class="section-card">
  <h2>Learning Notes</h2>
  {% include post-list.html posts=posts empty_message="No learning notes yet." %}
</section>
