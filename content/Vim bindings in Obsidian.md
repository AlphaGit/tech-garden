---
title: Vim bindings in Obsidian
date created: 2025-05-30T23:03:41-04:00
date modified: 2025-05-30T23:03:57-04:00
tags:
  - vim
  - obsidian
---
This is a document about me learning VIM Key bindings as I try them out in Obsidian.

Nouns ([source](https://github.com/iggredible/Learn-Vim/blob/master/ch04_vim_grammar.md)):
- `h` left
- `j` down
- `k` up
- `l` right
- ... (directions in navigation)
- word: anything composed of `a-zA-Z0-9`
- WORD: anything but spaces (space, tab, EOL)

Navigation:
- `h` character left
- `j` character down
- `k` character up
	- `14k` 14 lines up
- `l` character right
- `w` forward one word (beginning)
- `W` forward one WORD (anything but space) 
- `b` back one word (beginning)
- `B` back one WORD (beginning)
- `e` forward one word (end)
- `E` forward to next WORD (end)
- `$` end of line
- `0` beginning of line
- `gg` beginning of document
- `G` end of document
	- `15G` go to line 15 in document
- `H` top of screen
- `M` middle of screen
- `L`? bottom of screen
- `fx` search for x in current line (single character)
- `F` same but backwards
- `tx` search for x in current line (single character) but select previous
- `T` same but backwards
- `(` previous sentence
- `)` next sentence
- `}` next paragraph
- `{` previous paragraph

Editing:
- `i` insert mode: insert at the beginning of cursor
- `a` insert mode: append at the next character
- `I` insert mode: insert at the beginning of the line
- `A` insert mode: append at the end of the line
- `o` insert mode: insert into new line after current one 
- `O` insert mode: insert into new line prior to the current one
- `dd` delete entire line
- `r` replace character
- `x` delete character`
- `v` start selection
- `gU` change selection to uppercase
- `gu` change selection to lowercase
- `cc` delete line and enter edit mode (replace line)
- `s` delete selection and enter edit mode (replace selection)
- `y` "yank" text (copy, view mode)
	- `2yy` copy two lines
- `p` paste (view mode)
- `>>` indent
	- `2>>` indent two lines
- `<<` de-indent
- `/` enter search mode
- `n` get next search result
- `N` get previous search result

Mixing editing verbs and nouns:
- `y$` yank until the end of line
- `d2w` delete two words forward
- `c}` change everything from current location to end of paragraph

Text objects delimiters:
- `i + delimiter`: inner text object (anything inside the group)
	- `di(` deletes text inside the parenthesis  
	- `da{` deletes everything contained in braces
- `a + delimiter`: outer text object (group and delimiters)
- `w` words
- `p` paragraph
- `s` sentence
- `(` or `)` parenthesized text
- `{` or `}` text between braces
- `[` or `]` text between brackets
- `<` or `>` text between angled brackets
- `t` XML tags (applies to HTML too)
- `"` text in double quotes
- `'` text in single quotes
- `` ` `` text in backticks

Mixing with previous:
- `gUiw` uppercase current word

Commands:
- `:%s/a/b/g` substitute all instances of "a" for "b"
- `:%s/a/b/gc` substitute all instances "a" for "b", but ask for confirmation

Sources:
- [How to use VIM Bindings in Obsidian | Beginners Guide](https://www.youtube.com/watch?v=yX_Qdr9-7kg), Antone Heyward
- [Learn-Vim](https://github.com/iggredible/Learn-Vim)
- [Object motions - Vim help](https://vimhelp.org/motion.txt.html#object-motions)
