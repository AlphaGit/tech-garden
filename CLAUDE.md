# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What This Is

A fork of [Quartz v4](https://quartz.jzhao.xyz/) (`upstream` remote: jackyzha0/quartz) serving as Alpha's digital knowledge garden. The published content can be reviewed at **https://techgarden.alphasmanifesto.com/**. It is authored in [Obsidian](https://obsidian.md/) and complements Alpha's blog ([Alpha's Manifesto](https://blog.alphasmanifesto.com)): quick, informal, interlinked notes rather than polished long-form articles. Two distinct halves:

- `content/` — the Obsidian vault of markdown notes. This is what's actually authored here.
- `quartz/` — the static site generator engine (TypeScript/Preact). Mostly upstream code; merge from `upstream` to update Quartz itself.

Site customization lives in two root files, not in `quartz/`:

- `quartz.config.ts` — site metadata, theme, and the plugin pipeline (transformers/filters/emitters)
- `quartz.layout.ts` — which Preact components render where on each page type

The working/default branch is `v5` (the old `v4` branch is outdated — do not work there). Pushing to `v5` triggers GitHub Pages deployment via `.github/workflows/deploy.yml`.

## Commands

```bash
npx quartz build           # build site into public/
npx quartz build --serve   # build + local dev server with hot reload
npm run check              # tsc --noEmit + prettier --check
npm run format             # prettier --write
npm test                   # runs the two test files: quartz/util/path.test.ts and quartz/depgraph.test.ts
```

Tests use `tsx` directly (no test runner config); to run a single test file: `npx tsx ./quartz/util/path.test.ts`.

Node 20 or >=22 required (`.node-version`).

## Content: Organization

Notes live in `content/`, organized into topic folders: `ai/` (the largest — ML, LLMs, embeddings, benchmarks, course notes), `tools/`, `development/` (subfolders per language: python, javascript, typescript, css, sql, code_analysis), `architecture/`, `canada/`, `blender/`, `math/`, `security/`, `databases/`, `mac/`, `finance/`, `formats/`, `ux/`, `management/`, `serverless/`, `links/`, `self-improvement/`, `android/`, `health/`, and `projects/`. A few miscellaneous notes live at the root of `content/`. New folders can be created freely when a topic doesn't fit existing categories.

Not published: `private/`, `templates/`, `.obsidian/` (via `ignorePatterns`), and any note with `draft: true` frontmatter. The `.smart-env/` directory contains AI embedding data from an Obsidian plugin and is not part of published content.

## Content: Note Format

Every note is markdown with YAML frontmatter (template skeleton at `content/templates/entry.md`):

```yaml
---
title: "Note Title"
tags:
  - tag1
  - tag2
---
```

Some notes also include `date created` / `date modified` timestamps. Tags are freeform and topic-based (e.g., `ai`, `llm`, `algorithms`, `unix`, `probability`); they can cross-cut folder boundaries — a note in `math/` might be tagged `probability` and `ai`.

### Tone and style

Notes are concise, practical, and informal — quick explanations, useful code snippets, and key takeaways over long prose. First-person voice when opinions appear, but most notes are reference-style: a definition or explanation followed by an example. Common structure:

- Short explanation of the concept at the top (sometimes a blockquote from an external source).
- Code blocks with syntax highlighting when demonstrating tools or techniques.
- LaTeX math (KaTeX) for formulas.
- A **"Sources"** section at the bottom with links or footnotes (`[^label]` style).

### Obsidian markdown specifics

- **Wiki-links** `[[Note Title]]` — the primary linking mechanism; `[[Note Title|display text]]` for custom text. Resolved with shortest-path matching, so folder paths aren't needed.
- **Embeds** `![[image.png]]` for images and note transclusion.
- **Footnotes** `[^label]` / `[^label]: text`, frequently used in Sources sections.
- **Blockquotes** (`>`) to quote external sources verbatim, usually with a footnote citation.
- **Callouts** (`> [!type]`) used sparingly.
- **Tags in frontmatter** (YAML list), not inline `#tag` syntax.
- **LaTeX** via `$...$` / `$$...$$`.

When creating or editing notes, prefer linking to existing notes whenever a related concept already has its own page — cross-folder links are what make the vault a "garden" rather than a flat collection.

## Architecture (Quartz Engine)

Only relevant when modifying the generator, not when writing notes.

- `quartz/build.ts` orchestrates the build: parse all markdown in `content/` → filter → emit. Uses `workerpool` for parallel parsing and a dependency graph (`quartz/depgraph.ts`) for incremental rebuilds during `--serve`.
- The plugin pipeline (configured in `quartz.config.ts`) has three stages:
  - **Transformers** (`quartz/plugins/transformers/`) — unified/remark/rehype plugins that mutate markdown→HTML ASTs (frontmatter, Obsidian-flavored markdown, syntax highlighting, KaTeX, link crawling).
  - **Filters** (`quartz/plugins/filters/`) — drop content from publishing (e.g. `RemoveDrafts`).
  - **Emitters** (`quartz/plugins/emitters/`) — produce output files (content pages, tag/folder pages, RSS/sitemap via `ContentIndex`, static assets, 404).
- `quartz/components/` — Preact components rendered server-side to static HTML; client interactivity (search, graph, dark mode) ships as separate inline scripts per component.
- Obsidian wiki-links (`[[Note]]`) are resolved by the `CrawlLinks` transformer with `shortest` path matching.

## Workflow Notes

- Commit messages for content syncs follow the existing pattern: `Quartz sync: <date>`.
