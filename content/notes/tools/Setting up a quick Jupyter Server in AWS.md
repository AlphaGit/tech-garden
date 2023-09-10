---
title: Setting up a quick Jupyter Server in AWS
tags:
  - jupyter
  - aws
  - guides
  - ec2
  - infrastructure
---
This guide walks through creating a quick instance of CUDA-enabled Jupyter notebook server using AWS EC2. There are better automated ways of doing this (like SageMaker, or Terraform, CDK, docker, etc), but as a quick first approach, this works.

In my case, I needed a [CUDA-supported GPU](https://developer.nvidia.com/cuda-gpus) attached to the instance, so I chose a  [`g5.xlarge`](), which is the cheapest I could find to scale later on when the PoC is done.

You might want it in cases where, like me, you need this as a configurable scratch-server that you can use to modify this to your needs. For instance, as a setup with other databases or software to be contained in a single instance.
## 1. Create instance

Create a Ubuntu-based EC2 instance, start it. Write down the IP address, and the root pass you created for it.

You can probably adapt these instructions to Amazon-Linux instances, but they won't work with `apt-get`.

Make sure to enable `TCP:8888` and `SSH` ports in the security groups for inbound connections. Ideally, from your IP only.

Make sure to have at least 20-30 GBs of storage mounted in root for installing dependencies. I used 128 GBs.

## 2. First time setup

Once it's created, connect to it and do a first time setup.

In your local computer:

```bash
ssh -i <pemFile> ubuntu@<publicIP>
```

After successfully connecting, run on the remote instance:

```bash
sudo apt-get update
sudo apt-get upgrade -y
sudo apt-get install -y python3 python3-pip
sudo pip3 install --upgrade pip virtualenv

sudo adduser jupyter
# Give it a password, write it down

sudo su jupyter
```

## 3. Setup a user-specific virtual environment

```bash
cd ~
virtualenv venv
source venv/bin/activate
pip install jupyter
mkdir workdir
jupyter notebook --generate-config
nano ~/.jupyter/jupyter_notebook_config.py
```

Add the following line:

```python
c.NotebookApp.ip = '0.0.0.0'
```

Then keep executing as the `jupyter` user:

```bash
jupyter-notebook password
# Type a password for the notebooks
```

## 4. Setup Jupyter Notebook as a service

Back to the `ubuntu` user:

```
nano jupyter-notebook.service
```

Add the following contents to the `jupyter.service` file:

```ini
[Unit]
Description=Jupyter Notebook Server

[Service]
Type=simple
ExecStart=/bin/bash -c "source /home/jupyter/venv/bin/activate && jupyter-notebook --config=/home/jupyter/.jupyter/jupyter_notebook_config.py --no-browser --notebook-dir=/home/jupyter"
WorkingDirectory=/home/jupyter
User=jupyter
Group=jupyter
PIDFile=/run/jupyter-notebook.pid
Restart=on-failure
RestartSec=60s

[Install]
WantedBy=multi-user.target
```

Finally, enable the service:

```bash
sudo cp jupyter-notebook.service /etc/systemd/system/
sudo systemctl enable jupyter-notebook.service
sudo systemctl daemon-reload
sudo systemctl restart jupyter-notebook.service
sudo service jupyter-notebook status
```

At this point, the jupyter notebook server should be running.

## 5. Setup CUDA

From your own local machine, visit `<ip>:8888`. You should be able to see the notebook server at this point.

```bash
sudo apt autoremove nvidia* --purge
sudo apt-get install ubuntu-drivers-common
```

You should be able to see an NVIDIA device installed. Look for the device driver line that says `recommended`.

```bash
sudo ubuntu-drivers autoinstall
sudo apt install nvidia-driver-525 # or whatever your recommended was
sudo reboot
```

Reconnect and continue:

```bash
nvidia-smi
```

This should show you stats about the NVIDIA device.

```bash
sudo apt install -y nvidia-cuda-toolkit
nvcc --version
```

This should show you an NVIDIA CUDA compiler version information, meaning that everything works.
## Sources

- [Run Jupyter Notebook as a background service](https://towardsdatascience.com/run-jupyter-notebook-as-a-background-service-on-ubuntu-c5d6298ed1e)
- [How to install CUDA & cuDNN on Ubuntu 22.04](https://gist.github.com/denguir/b21aa66ae7fb1089655dd9de8351a202)