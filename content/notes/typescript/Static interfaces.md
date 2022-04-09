---
title: Static interfaces
tags:
- typescript
- types
---

In Typescript it is possible to define static interfaces and even reference them and pass the classes as objects to be used.

```typescript
interface Instance {}

interface IStaticClass {
  new (): Instance;
  static start();
  static show();
  static end();
}

class StaticMembersClass implements IStaticClass {
  static start() {};
  static show() {};
  static end() {};
}

// in some code
function myFunction (staticClass: IStaticClass) {
  staticClass.start();
}

myFunction(StaticMembersClass);
```

Some more info: https://stackoverflow.com/a/43674389/147507