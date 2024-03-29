FROM registry1.ctdn.net/library/python:3.10.6-alpine3.16 as builder

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apk update

COPY ./requirements.txt requirements.txt

RUN pip install --user -r requirements.txt

FROM registry1.ctdn.net/library/python:3.10.6-alpine3.16

ENV PYTHONUNBUFFERED 1

WORKDIR /app

ENV PATH=/root/.local/bin:$PATH
COPY --from=builder /root/.local /root/.local

COPY . .

ENTRYPOINT ["python3", "-u", "app.py"]
