FROM python:3.6-alpine

LABEL maintainer="Peng Xiao <penxiao@cisco.com>"

RUN apk add --no-cache gcc musl-dev

COPY requirements.txt /{{cookiecutter.module_name}}/requirements.txt

WORKDIR /{{cookiecutter.module_name}}

RUN pip install -r requirements.txt

RUN python compile.py -y

EXPOSE 8000

CMD []
