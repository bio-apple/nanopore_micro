FROM ubuntu:latest AS base
ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt-get install -y --no-install-recommends  libcurl4-openssl-dev  autoconf automake \
    build-essential wget curl ca-certificates bzip2 gnupg git libssl-dev libffi-dev libz-dev libbz2-dev && rm -rf /var/lib/apt/lists/* && \
    mkdir -p /ref/ /script/ /raw_data/ /outdir/ /software && \
    wget -q -O /miniforge.sh https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-Linux-x86_64.sh && \
    bash /miniforge.sh -b -p /opt/conda && rm /miniforge.sh &&  \
    cd /software/ && wget https://cdn.oxfordnanoportal.com/software/analysis/dorado-1.0.0-linux-x64.tar.gz && tar xzvf dorado-1.0.0-linux-x64.tar.gz
#/opt/conda/bin/mamba install bioconda::flye bioconda::filtlong bioconda::nanoplot && \