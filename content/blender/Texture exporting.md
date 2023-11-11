---
title: Texture exporting
tags:
- blender
- texturing
---

Different formats have different ways, but for [[OBJ]] and [[FBX]] exports (what I needed) with textures, not only you'll need the file itself, but also the texture files (images, if any), and, alternatively, a material files that maps between the two of them.

For [[OBJ]] files, you'll also have a [[MTL]] file that has that mapping between objects and the textures. [[OBJ]] files are also text-readable, so you can do that without any importing/exporting if you dare, but it might be very tricky identifying the right objects.

For [[FBX]] files, the paths to the textures can be embedded. Notice that they include both the relative and absolute file to the path. Having the absolute path means that you can move the [[FBX]] around in your same computer and it will find the textures anyway, but if you send this file to someone else, they can see the folder structure where you used the files. (Just the folder names.) For the relative paths, it means you can share the [[FBX]] files and the texture files, just ensuring they are in the same place, relative to one another.

As an example, my [[FBX]] file had a tex folder where all the texture images where stored.

My [[OBJ]] file had a [[MTL]] file of the same name, and also the text folder with all the texture images.