---
layout: default
title: Learn
permalink: /learn/
---
{% assign posts = site.posts | where_exp: "post", "post.categories contains 'learn'" %}

<section class="section-card">
  <h2>Learning Notes</h2>
  {% include post-list.html posts=posts empty_message="No learning notes yet." %}
</section>
