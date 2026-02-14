# CLAUDE.md — Alpha's Tech Garden

## Overview

This is a **digital knowledge garden** — a collection of interconnected notes on technical and personal-interest topics. It is authored in [Obsidian](https://obsidian.md/) and published as a static website using [Quartz v4](https://quartz.jzhao.xyz/). The live site is at **techgarden.alphasmanifesto.com**.

The author is Alpha, who also runs [Alpha's Manifesto](https://blog.alphasmanifesto.com). The garden exists as a complement to the blog: it holds quick, informal, interlinked notes rather than polished long-form articles.

## Repository Structure

```
├── content/          ← Obsidian vault (all notes live here)
│   ├── _index.md     ← Landing page for the site
│   ├── templates/    ← Obsidian note template(s), excluded from publishing
│   └── <topic dirs>/ ← Notes organized by subject folder
├── quartz/           ← Quartz engine (components, plugins, styles, static assets)
├── quartz.config.ts  ← Site configuration (title, URL, theme, plugins)
├── quartz.layout.ts  ← Page layout configuration
├── docs/             ← Quartz documentation
└── package.json      ← Node dependencies (Quartz build toolchain)
```

## Content Organization

Notes live inside `content/` and are organized into topic folders: `ai/` (the largest — ML, LLMs, embeddings, benchmarks, course notes from MIT 6.0002), `tools/`, `development/` (with subfolders per language: python, javascript, typescript, css, sql, code_analysis), `architecture/`, `canada/`, `blender/`, `math/`, `security/`, `databases/`, `mac/`, `finance/`, `formats/`, `ux/`, `management/`, `serverless/`, `links/`, `self-improvement/`, `android/`, `health/`, and `projects/`. A few miscellaneous notes live at the root of `content/`.

New folders can be created freely when a topic doesn't fit existing categories.

## Tone and Style

Notes are concise, practical, and informal. They favor quick explanations, useful code snippets, and key takeaways over long prose. The voice is first-person when opinions appear, but most notes are reference-style: a definition or explanation followed by an example.

Common patterns in notes:

- A short explanation of the concept at the top (sometimes a blockquote from an external source).
- Code blocks with syntax highlighting when demonstrating tools or techniques.
- LaTeX math (rendered via KaTeX) for formulas and equations.
- A **"Sources"** section at the bottom with links or footnotes (`[^label]` style) pointing to the original references.
- Notes are self-contained but link outward to related notes and external resources.

## Note Format and Frontmatter

Every note is a standard markdown file with YAML frontmatter:

```yaml
---
title: "Note Title"
tags:
  - tag1
  - tag2
---
```

Some notes also include `date created` and `date modified` timestamps. Tags are freeform and topic-based (e.g., `ai`, `llm`, `data_structures`, `algorithms`, `tools`, `unix`, `probability`, `technique`). A note can have tags that cross-cut folder boundaries — for instance, a note in `math/` might be tagged `probability` and `ai`.

The template at `content/templates/entry.md` provides the base frontmatter skeleton (`title` and `tags`).

## How Notes Relate to Each Other

Obsidian uses **wiki-links** (`[[Note Title]]`) to create connections between notes. This vault uses them extensively:

- `[[Note Title]]` links to another note by its title. Quartz resolves these using shortest-path matching, so the folder path is not needed.
- `[[Note Title|display text]]` links to a note but renders custom display text.
- `![[image.png]]` embeds an image stored in the vault.
- Notes often reference related concepts in other folders (e.g., a math note linking to `[[PCA]]`, a tools note linking to `[[xargs]]`, a Canada note linking to `[[Parliament]]`). These cross-folder links are what make the vault a "garden" rather than a flat collection.

When creating or editing notes, prefer linking to existing notes whenever a related concept already has its own page. This keeps the knowledge graph connected and navigable.

## Obsidian Markdown Specifics

Obsidian extends standard markdown in several ways used throughout this vault:

- **Wiki-links** (`[[...]]`) as described above — the primary linking mechanism.
- **Embedded content** (`![[...]]`) for images and note transclusion.
- **Footnotes** using `[^label]` / `[^label]: text` syntax, frequently used in the Sources section.
- **Blockquotes** (`>`) used to quote external sources verbatim, usually with a footnote citation.
- **Callouts** (`> [!type]`) for highlighted boxes (though used sparingly here).
- **Tags in frontmatter** (`tags:` YAML list) rather than inline `#tag` syntax.
- **LaTeX** via `$...$` (inline) and `$$...$$` (block) — rendered by KaTeX through Quartz.

## Quartz Configuration Highlights

- SPA mode and popovers are enabled for smooth navigation.
- Ignored patterns: `private`, `templates`, `.obsidian` (excluded from the published site).
- Drafts are filtered out via the `RemoveDrafts` plugin.
- Sitemap and RSS feed are generated automatically.
- Link resolution uses "shortest" path matching, so wiki-links don't require full paths.

## Smart Environment

The `.smart-env/` directory inside `content/` contains AI embedding data (`.ajson` files) from an Obsidian plugin that generates vector embeddings for semantic search across notes. This folder is not part of the published content.
