FROM jenkins/jenkins:lts as builder
USER root

RUN apt-get update && apt-get install -y python3 python3-pip python3-venv && \
    rm -rf /var/lib/apt/lists/*

RUN python3 -m venv /opt/venv

COPY requirements /tmp/requirements
RUN /opt/venv/bin/pip install -r /tmp/requirements/dev.txt --no-cache-dir

FROM jenkins/jenkins:lts
COPY --from=builder /opt/venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

ARG PYTHON_VERSION=3.9
RUN apt-get update && apt-get install -y python${PYTHON_VERSION}
