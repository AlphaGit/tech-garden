---
title: Creating a new user with SSH access in Linux
tags:
- ssh
- security
- linux
- bash
---

Create a user and give it a password that expires, so that they can change it when they login:

```bash
sudo useradd username
passwd username
# set password
passwd -e username
```

Make it a sudoer:

```bash
sudo usermod -a -G sudo username
```

Using SSH Keys: [Source](https://humanwhocodes.com/snippets/2021/03/create-user-linux-ssh-key/)

```bash
# ensure the directory ir owned by the new user
chown -R username:username /home/username/.ssh

# make sure only the new user has permissions
chmod 700 /home/username/.ssh
chmod 600 /home/username/.ssh/authorized_keys
```