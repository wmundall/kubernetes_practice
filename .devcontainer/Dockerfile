FROM mcr.microsoft.com/devcontainers/python:3.11-bookworm

# Install essential command-line tools and Kubernetes utilities
RUN apt-get update && export DEBIAN_FRONTEND=noninteractive \
    && apt-get -y install --no-install-recommends \
       curl \
       git \
       apt-transport-https \
       ca-certificates \
       gnupg \
       lsb-release
       
RUN mkdir -p /etc/apt/keyrings \
    && curl -fsSL https://download.docker.com/linux/debian/gpg | gpg --dearmor -o /etc/apt/keyrings/docker.gpg \
    && echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/debian $(lsb_release -cs) stable" | tee /etc/apt/sources.list.d/docker.list > /dev/null \
    && apt-get update && apt-get -y install --no-install-recommends docker-ce-cli

# Install kubectl
RUN curl -sLo /usr/local/bin/kubectl https://dl.k8s.io/release/v29.0/bin/linux/amd64/kubectl \
    && chmod +x /usr/local/bin/kubectl

# Install Kind (Kubernetes in Docker)
RUN curl -sLo /usr/local/bin/kind https://kind.sigs.k8s.io/dl/v0.24.0/kind-linux-amd64 \
    && chmod +x /usr/local/bin/kind

# Install Helm
RUN curl https://raw.githubusercontent.com/helm/helm/main/scripts/get-helm-3 | bash