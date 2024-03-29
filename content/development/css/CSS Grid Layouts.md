---
title: CSS Grid Layouts
tags: 
- css
- design
---

This seems to be a very simple approach to grid layouts. ([Source](https://www.digitalocean.com/community/tutorials/css-css-grid-holy-grail-layout))

```html
<div class="container">
  <header>
    <!-- Header content -->
  </header>

  <nav>
    <!-- Navigation -->
  </nav>

  <main>
    <!-- Main content -->
  </main>

  <aside>
    <!-- Sidebar / Ads -->
  </aside>

  <footer>
    <!-- Footer content -->
  </footer>
</div>
```

```css
.container {
  display: grid;

  grid-template-areas:
    "header header header"
    "nav content side"
    "footer footer footer";

  grid-template-columns: 200px 1fr 200px;
  grid-template-rows: auto 1fr auto;
  grid-gap: 10px;

  height: 100vh;
}

header {
  grid-area: header;
}

nav {
  grid-area: nav;
  margin-left: 0.5rem;
}

main {
  grid-area: content;
}

aside {
  grid-area: side;
  margin-right: 0.5rem;
}

footer {
  grid-area: footer;
}

@media (max-width: 768px) {
  .container {
    grid-template-areas:
      "header"
      "nav"
      "content"
      "side"
      "footer";

    grid-template-columns: 1fr;
    grid-template-rows:
      auto /* Header */
      minmax(75px, auto) /* Nav */
      1fr /* Content */
      minmax(75px, auto) /* Sidebar */
      auto; /* Footer */
  }

  nav, aside {
    margin: 0;
  }
}
```

