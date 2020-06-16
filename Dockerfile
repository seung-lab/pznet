FROM ubuntu:20.04
LABEL maintainer = "Jingpeng Wu" \
    email = "jingpeng.wu@gmail.com"


WORKDIR ${HOME}/workspace/pznet
COPY . .

ENV LC_ALL C.UTF-8
ENV LANG C.UTF-8
ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update && \
    apt-get install -y -qq --no-install-recommends \
        apt-utils \
        bzip2 \
        ca-certificates \
        libxext6 \
        libsm6 \
        libxrender1 \
        wget && \
    echo "setting up minicoda..." && \
    wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/anaconda.sh && \
    echo "downloaded miniconda, start installing..." && \
    /bin/bash ~/anaconda.sh -b -p /opt/conda && \
    rm ~/anaconda.sh && \
    ln -s /opt/conda/etc/profile.d/conda.sh /etc/profile.d/conda.sh && \
    echo ". /opt/conda/etc/profile.d/conda.sh" >> ~/.bashrc && \
    echo "conda activate base" >> ~/.bashrc && \
    # clean up the apt installation
    apt-get clean && \
    apt-get autoremove --purge -y && \
    rm -rf /var/lib/apt/lists/* 

# eactivate the conda environment
RUN exec bash && \
    conda create -f environment.yml 
