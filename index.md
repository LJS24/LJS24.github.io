---
layout: default
title: Home
---
{% assign learn_posts = site.posts | where_exp: "post", "post.categories contains 'learn'" %}
{% assign research_posts = site.posts | where_exp: "post", "post.categories contains 'research'" %}
{% assign project_posts = site.posts | where_exp: "post", "post.categories contains 'projects'" %}

<section class="hero-card">
  <p class="hero-label">Research-driven Tech Blog</p>
  <h2>A technical journal for learning notes, research reports, and project sharing.</h2>
  <p class="hero-text">
    Posts on this blog are based on personal learning, research, and development. There may be expressive and technical deficiencies.
  </p>
  <div class="hero-actions">
    <a class="btn btn-primary" href="{{ '/learn/' | relative_url }}">Explore Learning</a>
    <a class="btn btn-primary" href="{{ '/research/' | relative_url }}">Explore Research</a>
    <a class="btn btn-primary" href="{{ '/projects/' | relative_url }}">Explore Projects</a>
  </div>
  <ul class="hero-metrics">
    <li><strong>{{ learn_posts | size }}</strong><span>Learning Notes</span></li>
    <li><strong>{{ research_posts | size }}</strong><span>Research Reports</span></li>
    <li><strong>{{ project_posts | size }}</strong><span>Project Posts</span></li>
  </ul>
</section>

<section class="section-card">
  <div class="section-head">
    <h2>Learning Notes</h2>
    <a class="text-link" href="{{ '/learn/' | relative_url }}">View All</a>
  </div>
  {% include post-list.html posts=learn_posts empty_message="No learning notes yet." %}
</section>

<section class="section-card">
  <div class="section-head">
    <h2>Research Reports</h2>
    <a class="text-link" href="{{ '/research/' | relative_url }}">View All</a>
  </div>
  {% include post-list.html posts=research_posts empty_message="No research reports yet." %}
</section>

<section class="section-card">
  <div class="section-head">
    <h2>Project Sharing</h2>
    <a class="text-link" href="{{ '/projects/' | relative_url }}">View All</a>
  </div>
  {% include post-list.html posts=project_posts empty_message="No project posts yet." %}
</section>
