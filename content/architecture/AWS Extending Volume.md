---
title: AWS Extending Volume
date created: 2025-12-13T22:03:14-05:00
date modified: 2025-12-14T11:34:09-05:00
tags:
  - how_to
  - infrastructure
  - cloud
  - aws
---

After changing the volume size and committing to it, once it's in completed status or in optimized status, run the following commands:

```bash
lsblk

# example output
NAME         MAJ:MIN RM  SIZE RO TYPE MOUNTPOINTS
loop0          7:0    0 27.6M  1 loop /snap/amazon-ssm-agent/11797
loop1          7:1    0   74M  1 loop /snap/core22/2163
loop2          7:2    0 73.9M  1 loop /snap/core22/2139
loop3          7:3    0 50.8M  1 loop /snap/snapd/25202
loop4          7:4    0 50.9M  1 loop /snap/snapd/25577
nvme0n1      259:0    0   20G  0 disk
├─nvme0n1p1  259:2    0    7G  0 part /
├─nvme0n1p14 259:3    0    4M  0 part
├─nvme0n1p15 259:4    0  106M  0 part /boot/efi
└─nvme0n1p16 259:5    0  913M  0 part /boot
nvme1n1      259:1    0  300G  0 disk /mnt/media
```

Confirm which is the partition to change. In this case, it was `/`, under `nvme0n1p1`. Thi sis, device `nvme0n1`, partition `1`.

```bash
sudo growpart /dev/nvme0n1 1

# example output
CHANGED: partition=1 start=2099200 old: size=14677983 end=16777182 new: size=39843807 end=41943006
```

Confirm which is the filesystem for the partition (if there is any), in which case you want to use a filesystem-specific tool for growing it:

```bash
sudo lsblk -f

# example output
NAME         FSTYPE   FSVER LABEL           UUID                                 FSAVAIL FSUSE% MOUNTPOINTS
loop0        squashfs 4.0                                                              0   100% /snap/amazon-ssm-agent/11797
loop1        squashfs 4.0                                                              0   100% /snap/core22/2163
loop2        squashfs 4.0                                                              0   100% /snap/core22/2139
loop3        squashfs 4.0                                                              0   100% /snap/snapd/25202
loop4        squashfs 4.0                                                              0   100% /snap/snapd/25577
nvme0n1
├─nvme0n1p1  ext4     1.0   cloudimg-rootfs 41a438f9-9b73-40e9-9093-3c0a3ce03d5c  525.9M    92% /
├─nvme0n1p14
├─nvme0n1p15 vfat     FAT32 UEFI            0007-49CF                              98.2M     6% /boot/efi
└─nvme0n1p16 ext4     1.0   BOOT            fc01183f-27c0-4f69-b1c0-fb1c01e8fe57  664.2M    18% /boot
nvme1n1      ext4     1.0                   81447281-c51f-4589-855d-8c5dfe30e113   11.6G    89% /mnt/media
```

In this example, the partition we want to grow, mounted on `/` is an `ext4`, so we'll use `resize2fs`.

```bash
sudo resize2fs /dev/nvme0n1p1

# example output
resize2fs 1.47.0 (5-Feb-2023)
Filesystem at /dev/nvme0n1p1 is mounted on /; on-line resizing required
old_desc_blocks = 1, new_desc_blocks = 3
The filesystem on /dev/nvme0n1p1 is now 4980475 (4k) blocks long.
```

And done!

For any other situations, consider reviewing [Extend the file system after resizing an Amazon EBS volume](https://docs.aws.amazon.com/ebs/latest/userguide/recognize-expanded-volume-linux.html) on AWS Documentation.
