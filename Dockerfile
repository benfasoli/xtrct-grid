FROM python:3.7.4-alpine3.10

WORKDIR /src

COPY EXTRACT.CFG xtrct_grid /src/
RUN chmod +x xtrct_grid

VOLUME ["/input", "/output"]

COPY entrypoint.py /src
ENTRYPOINT ["python", "entrypoint.py"]
