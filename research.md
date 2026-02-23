---
layout: default
title: Research
permalink: /research/
---
{% assign posts = site.posts | where_exp: "post", "post.categories contains 'research'" %}

<section class="hero-card hero-card-sub">
  <p class="hero-label">Research Reports</p>
  <h2>From problem framing to result interpretation</h2>
  <p class="hero-text">Reports in this section state hypothesis, method, result, and limitation explicitly.</p>
</section>

<section class="section-card">
  <h2>Research Reports</h2>
  {% include post-list.html posts=posts empty_message="No research reports yet." %}
</section>
