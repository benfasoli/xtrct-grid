FROM python:3.7.4

WORKDIR /src

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        libnuma-dev \
    && rm -rf /var/lib/apt/lists/*

COPY EXTRACT.CFG xtrct_grid /src/
RUN chmod +x xtrct_grid

VOLUME ["/input", "/output"]

COPY entrypoint.py /src
ENTRYPOINT ["python", "entrypoint.py"]
