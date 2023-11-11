---
title: Texture Painting
tags:
- blender
- texture
---

Texture painting is the practice of applying images or paint onto a texture image.

To be able to texture paint, the following three things need to happen:

1. **The object has to be already [[Sculpting|sculpted]].**

   You can always apply sculpting deformations later, but it likely to deform the mesh in ways that will not match up to the texture correctly.

   It is also very important that the sculpting final mesh has enough polygons for the level of detail that the texture requires. This doesn't mean that you can't paint between edges of a polygon, but the shape won't follow that.

2. **The object needs to have a [[UV Mapping|UV Map]] already configured.**

3. **The material for the object needs to be set to Single Image and the texture needs to be selected**, so that it appears in the [[Rendering]] result.

   Of course, you can do this later, and even apply more nodes or modifications to the final rendering. This is just another element that will be used in the [[Rendering workflow]].

