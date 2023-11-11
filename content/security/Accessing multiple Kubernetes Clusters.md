---
title: Accessing multiple Kubernetes clusters
tags:
- kubernetes
- security
- clusters
---

This is my trick for configuring and switching between multiple kubernetes clusters. We'll use `myCluster` as an example cluster name.

1. Have all of the kubectl acess files (YAML files) added into `~/.kube`, and named `myCluster.config`.

2. Ensure that each of them have a readable and rememberable context name:
   ```yaml
   apiVersion: v1
   clusters:
   - cluster:
       certificate-authority-data: [REDACTED]
       server: [REDACTED]
     name: [REDACTED]
   contexts:
   - context:
       cluster: [REDACTED]
       user: [REDACTED]
     name: myCluster
   current-context: myCluster
   kind: Config
   preferences: {}
   users:
   - name: [REDACTED]
     user:
       token: [REDACTED]
   ```

3. Ensure that when initializing your console, you reference those files and add them to the `KUBECONFIG` variable. I do this through a local-only file that I source from [my dotFiles](https://github.com/AlphaGit/dotfiles). Of course, this can be done programatically but you might not want access to clusters to be added dynamically to your console. Up to you.
   ```zsh
   export KUBECONFIG=$KUBECONFIG:~/.kube/cluster1.config:~/.kube/myCluster.config
   ```

4. Setup a quick alias just to switch between clusters. I have this setup from [my dotFiles](https://github.com/AlphaGit/dotfiles).
   ```zsh
   alias k='kubectl'
   alias kswitch='k config use-context'
   ```

5. Now just load a console and you can do:
   ```zsh
   kswitch cluster1
   # Switched to context "cluster1".
   
   kswitch myCluster
   # Switched to context "myCluster".
   ```
