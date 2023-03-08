FROM mcr.microsoft.com/playwright:focal

ARG PIP_EXTRA_INDEX_URL=https://pypi.org/simple
ARG BUILD_DEPS="build-essential curl git libffi-dev cmake libssl-dev libpq-dev gcc"
# assuming repo is up to date on host machine

RUN apt update -y && apt-get install -y --no-install-recommends \
    $BUILD_DEPS \
    apt-transport-https \
    software-properties-common \
    ca-certificates  \
    curl \
    build-essential \
    vim \
    libicu-dev \
    libpcre3 \
    libpcre3-dev \
    python3-pip \
    wget

RUN wget -O- https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor | tee /usr/share/keyrings/microsoft-edge.gpg
RUN echo 'deb [arch=amd64 signed-by=/usr/share/keyrings/microsoft-edge.gpg] https://packages.microsoft.com/repos/edge stable main' | tee /etc/apt/sources.list.d/microsoft-edge.list
RUN apt update -y && apt install -y microsoft-edge-stable

RUN add-apt-repository ppa:deadsnakes/ppa
RUN apt update \
    && apt -y install python3.11-full python3.11-dev python3.11-venv python3.11-distutils \
    && curl -sS https://bootstrap.pypa.io/get-pip.py | python3.11 \
    && python3.11 -m ensurepip

WORKDIR /app
COPY . /app

RUN apt update \
    && python3.11 -m pip install --upgrade pip \
    && python3.11 -m pip install -r requirements/common.txt --no-cache-dir

RUN apt -y remove $BUILD_DEP

RUN playwright install

RUN chmod +x ./entrypoint.sh

ENTRYPOINT ["./entrypoint.sh"]
