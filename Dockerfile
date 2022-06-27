FROM mcr.microsoft.com/playwright:focal
# assuming repo is up to date on host machine
RUN apt update -y && apt-get install -y \
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

WORKDIR /app
COPY . /app

RUN pip install pip --upgrade && \
    pip install -r requirements.txt

RUN playwright install

RUN chmod +x ./entrypoint.sh

ENTRYPOINT ["./entrypoint.sh"]