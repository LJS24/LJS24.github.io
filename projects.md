---
layout: default
title: Projects
permalink: /projects/
post_search: true
---
{% assign posts = site.posts | where_exp: "post", "post.categories contains 'projects'" %}

<section class="hero-card hero-card-sub">
  <p class="hero-label">Project Sharing</p>
  <h2>Architecture and implementation decisions</h2>
  <p class="hero-text">This section focuses on goals, design choices, metrics, and technical retrospectives.</p>
</section>

{% include post-search.html title="Search Project Posts" description="Find project posts by title keyword or tag." input_id="project-tag-search" placeholder="Search project titles or tags" %}

<section class="section-card">
  <h2>Project Sharing</h2>
  {% include post-list.html posts=posts empty_message="No project posts yet." %}
</section>
