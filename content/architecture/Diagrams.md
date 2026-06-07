---
title: Diagrams
tags:
  - python
  - architecture
  - tools
---

[Diagrams](https://github.com/mingrammer/diagrams) is a python project that can be used to generate architectural or system design diagrams from python code.

As an example, executing the following code will generate and show the following image:

```python
from diagrams import Diagram, Cluster
from diagrams.digitalocean.network import LoadBalancer
from diagrams.digitalocean.database import DbaasPrimaryStandbyMore
from diagrams.digitalocean.compute import K8SCluster, K8SNodePool
from diagrams.digitalocean.storage import Volume

with Diagram("Services"):
    lb = LoadBalancer("Load Balancer")

    with Cluster("Internal Network"):
        node_pool = K8SNodePool("Node Pool")
        k8s = K8SCluster("Cluster")
        k8s - node_pool

    lb >> k8s

    with Cluster("Databases"):
        db = DbaasPrimaryStandbyMore("Database")
        volume = Volume("Persistent volume")
        node_pool >> db
        db - volume
```

![[DiagramsExample.png]]
