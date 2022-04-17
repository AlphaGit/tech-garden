---
title: UV Mapping
tags:
- blender
- shading
---

UV Mapping is the process of mapping a 2D texture to use onto a 3D object.

![[notes/blender/UV Mapping on Globe.png]]

When UV Mapping and [[Texture Painting]], there is sometimes a "bleeding" issue. This happens because some points of the UV map end up very close to other parts mapped to topologically-distant elements.

To prevent that issue, increase the Island Margin Value while creating the UV map, which will just create a space between those elements in the UV Map.

![[notes/blender/Smart UV Project options.png]]

Sources:
- [UV Mapping, Simply Explained by All3DP](https://all3dp.com/2/blender-uv-mapping-simply-explained/)
- [Reducing the Bleeding issue while Texture Painting](https://www.youtube.com/watch?v=Dh4qpJIt24s)