document.addEventListener("DOMContentLoaded", () => {
  const searchRoot = document.querySelector("[data-post-search]");
  const listRoot = document.querySelector("[data-post-list]");

  if (!searchRoot || !listRoot) {
    return;
  }

  const input = searchRoot.querySelector("[data-post-search-input]");
  const resetButton = searchRoot.querySelector("[data-post-search-reset]");
  const chipList = searchRoot.querySelector("[data-post-search-chips]");
  const status = searchRoot.querySelector("[data-post-search-status]");
  const items = Array.from(listRoot.querySelectorAll("[data-post-item]"));

  const allTags = [...new Set(
    items.flatMap((item) =>
      (item.dataset.tags || "")
        .split(",")
        .map((tag) => tag.trim())
        .filter(Boolean)
    )
  )].sort((a, b) => a.localeCompare(b));

  let activeTag = "";

  const updateStatus = (visibleCount) => {
    if (!status || !input) {
      return;
    }

    if (!input.value.trim()) {
      status.textContent = `Showing ${visibleCount} post${visibleCount === 1 ? "" : "s"}.`;
      return;
    }

    status.textContent = `Found ${visibleCount} post${visibleCount === 1 ? "" : "s"} for "${input.value.trim()}".`;
  };

  const filterPosts = (query) => {
    const normalizedQuery = query.trim().toLowerCase();
    let visibleCount = 0;

    items.forEach((item) => {
      const title = (item.dataset.title || "").trim();
      const tags = (item.dataset.tags || "")
        .split(",")
        .map((tag) => tag.trim())
        .filter(Boolean);

      const isVisible = !normalizedQuery
        || title.includes(normalizedQuery)
        || tags.some((tag) => tag.includes(normalizedQuery));

      item.hidden = !isVisible;

      if (isVisible) {
        visibleCount += 1;
      }
    });

    updateStatus(visibleCount);
  };

  const updateChipState = () => {
    if (!chipList) {
      return;
    }

    chipList.querySelectorAll("[data-tag-chip]").forEach((button) => {
      button.classList.toggle("is-active", button.dataset.tagChip === activeTag);
    });
  };

  if (chipList) {
    if (allTags.length === 0) {
      const emptyState = document.createElement("p");
      emptyState.className = "post-search-empty";
      emptyState.textContent = "No tags available yet.";
      chipList.appendChild(emptyState);
    } else {
      allTags.forEach((tag) => {
        const button = document.createElement("button");
        button.type = "button";
        button.className = "post-search-chip";
        button.textContent = tag;
        button.dataset.tagChip = tag;
        button.addEventListener("click", () => {
          if (!input) {
            return;
          }

          activeTag = activeTag === tag ? "" : tag;
          input.value = activeTag;
          updateChipState();
          filterPosts(activeTag);
        });
        chipList.appendChild(button);
      });
    }
  }

  if (input) {
    input.addEventListener("input", (event) => {
      activeTag = event.target.value.trim().toLowerCase();
      updateChipState();
      filterPosts(event.target.value);
    });
  }

  if (resetButton) {
    resetButton.addEventListener("click", () => {
      activeTag = "";
      if (input) {
        input.value = "";
      }
      updateChipState();
      filterPosts("");
    });
  }

  filterPosts("");
});
