FROM ubuntu:latest AS base
ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt-get install -y --no-install-recommends libcurl4-openssl-dev autoconf automake \
    build-essential wget curl ca-certificates bzip2 gnupg git libssl-dev libffi-dev libbz2-dev  \
    python3-setuptools python3-dev lsb-release apt-transport-https python3-pip libz-dev zlib1g-dev &&  \
    rm -rf /var/lib/apt/lists/* && \
    mkdir -p /ref/ /script/ /raw_data/ /outdir/ /software && \
    wget -q -O /miniforge.sh https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-Linux-x86_64.sh && \
    bash /miniforge.sh -b -p /opt/conda && rm /miniforge.sh && \
    /opt/conda/bin/mamba create --name python3 --channel conda-forge --channel bioconda --channel nanoporetech --channel defaults python==3.11 pyvcf pod5 pybind11 catch2 gsl-lite pandas ezcharts pysam matplotlib dominate flye filtlong nanoplot biopython &&  \
    /opt/conda/bin/conda create -n biosoftware -c conda-forge -c nanoporetech -c bioconda medaka prokka resfinder seqsero2 fastcat mlst mosdepth pomoxis &&  \
    /opt/conda/bin/conda clean -a -y && \
    cd /software/ && wget https://cdn.oxfordnanoportal.com/software/analysis/dorado-1.0.2-linux-x64.tar.gz && tar xzvf dorado-1.0.2-linux-x64.tar.gz && rm -rf dorado-1.0.2-linux-x64.tar.gz
