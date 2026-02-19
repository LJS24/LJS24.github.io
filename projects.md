---
layout: default
title: Projects
permalink: /projects/
---
{% assign posts = site.posts | where_exp: "post", "post.categories contains 'projects'" %}

<section class="section-card">
  <h2>Project Sharing</h2>
  {% include post-list.html posts=posts empty_message="No project posts yet." %}
</section>
