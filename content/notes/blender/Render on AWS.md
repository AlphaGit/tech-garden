---
title: Render on AWS
tags:
- blender
- rendering
- aws
---

Create a p2.xlarge instance, which I found is the best balance between performance and price. Make sure it's ubuntu based.

Once ready, SSH into it and prepare it to render scenes:

```bash
sudo apt-get update

# need the same gcc-compiler as the kernel uses, or so NVidia says
sudo apt install -y gcc=4:9.3.0-1ubuntu2 make libgl1-mesa-glx libxi6 libxrender1

# download and install the NVidia drivers
wget https://us.download.nvidia.com/XFree86/Linux-x86_64/470.94/NVIDIA-Linux-x86_64-470.94.run
chmod +x NVIDIA-Linux-x86_64-470.94.run
sudo ./NVIDIA-Linux-x86_64-470.94.run

# manually go through the install options

# install latest Blender
sudo snap install blender --classic

# create the enable-gpu.py script to force the use of GPU
cat << 'EOF' > enable-gpu.py
import bpy

prop = bpy.context.preferences.addons['cycles'].preferences
prop.get_devices()
prop.compute_device_type = 'CUDA'

for device in prop.devices:
    if device.type == 'CUDA':
        device.use = True

bpy.context.scene.cycles.device = 'GPU'

for scene in bpy.data.scenes:
    scene.cycles.device = 'GPU'
EOF
```

To upload files into it: [[Uploading files to AWS instances]].

To render a scene:

```bash
# start a detached screen so you won't lose progress when disconnecting
screen -S myRenderingSession

# start blender rendering
blender -b blenderFile.blend -P enable-gpu.py -a

# if you had lost the connection and need to reconnect to that screen session
screen -d -r

# if you need to start blender again but don't want to start from scratch, but instead, frame 10
blender -b blenderFile.blend -P enable-gpu.py -s 10 -a
```
