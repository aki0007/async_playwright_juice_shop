FROM mcr.microsoft.com/playwright:focal
# assuming repo is up to date on host machine
RUN apt update -y && apt-get install -y \
    software-properties-common \
    build-essential \
    vim \
    libicu-dev \
    build-essential \
    libpcre3 \
    libpcre3-dev \
    python3-pip


WORKDIR /app
COPY . /app

RUN pip install pip --upgrade && \
    pip install -r requirements.txt

RUN chmod +x ./entrypoint.sh

ENTRYPOINT ["./entrypoint.sh"]