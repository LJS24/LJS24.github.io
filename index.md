---
layout: default
title: Home
---
Welcome to the blog. This site is organized around three tracks.

{% assign learn_posts = site.posts | where_exp: "post", "post.categories contains 'learn'" %}
{% assign research_posts = site.posts | where_exp: "post", "post.categories contains 'research'" %}
{% assign project_posts = site.posts | where_exp: "post", "post.categories contains 'projects'" %}

<section class="section-card">
  <h2>Learning Notes</h2>
  {% include post-list.html posts=learn_posts empty_message="No learning notes yet." %}
  <p><a href="{{ '/learn/' | relative_url }}">View all learning posts</a></p>
</section>

<section class="section-card">
  <h2>Research Reports</h2>
  {% include post-list.html posts=research_posts empty_message="No research reports yet." %}
  <p><a href="{{ '/research/' | relative_url }}">View all research posts</a></p>
</section>

<section class="section-card">
  <h2>Project Sharing</h2>
  {% include post-list.html posts=project_posts empty_message="No project posts yet." %}
  <p><a href="{{ '/projects/' | relative_url }}">View all project posts</a></p>
</section>
