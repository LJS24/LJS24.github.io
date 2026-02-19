---
layout: default
title: Research
permalink: /research/
---
{% assign posts = site.posts | where_exp: "post", "post.categories contains 'research'" %}

<section class="section-card">
  <h2>Research Reports</h2>
  {% include post-list.html posts=posts empty_message="No research reports yet." %}
</section>
