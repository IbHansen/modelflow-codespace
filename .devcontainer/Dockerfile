# Ubuntu + Miniforge + conda env "modelflow" (built from ../environment.yml)
FROM mcr.microsoft.com/devcontainers/base:ubuntu-24.04

ENV CONDA_DIR=/opt/conda
# The modelflow env comes first on PATH, so python/jupyter work without activation
ENV PATH=/opt/conda/envs/modelflow/bin:/opt/conda/bin:$PATH

# Miniforge is owned by the non-root user 'vscode' so `conda install` works without sudo
RUN mkdir -p $CONDA_DIR && chown vscode:vscode $CONDA_DIR
USER vscode

RUN curl -fsSL -o /tmp/miniforge.sh \
        "https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-Linux-$(uname -m).sh" \
 && bash /tmp/miniforge.sh -b -u -p $CONDA_DIR \
 && rm /tmp/miniforge.sh

COPY --chown=vscode:vscode environment.yml /tmp/environment.yml
RUN conda env create -f /tmp/environment.yml \
 && conda clean -afy \
 && rm /tmp/environment.yml

# `conda activate` works in terminals, and new terminals start in the modelflow env
RUN conda init bash \
 && echo "conda activate modelflow" >> ~/.bashrc
