FROM ubuntu:latest

# Install OpenJDK 8
RUN \
    apt-get update && \
    apt-get install -y openjdk-8-jdk && \
    rm -rf /var/lib/apt/lists/*

# Install Python
RUN \
    apt-get update && \
    apt-get install -y python3 python3-dev python3-pip python3-virtualenv && \
    rm -rf /var/lib/apt/lists/*

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PIP_FORMAT=legacy

RUN apt-get -y update && apt-get install -y libzbar-dev bash gcc git libc-dev

RUN apt-get install -y netcat && apt-get autoremove -y

RUN adduser --disabled-password --gecos '' myuser

RUN apt-get install -y build-essential
RUN pip3 install jupyterlab

RUN pip3 install pyspark
ENV PYSPARK_PYTHON=/usr/bin/python3


COPY requirements.txt /requirements.txt
RUN pip3 install --no-cache-dir -r /requirements.txt

RUN mkdir -p /spark_yarn
WORKDIR /spark_yarn

COPY dockerfiles/spark_yarn/run.sh /run.sh
RUN chmod +x /run.sh

# Copy Hadoop files and export path
COPY spark/config /usr/bin/spark/config
ENV YARN_CONF_DIR=/usr/bin/spark/config
COPY spark/spark_dummy_code.py /spark_yarn/test_spark.py
RUN chmod -R 777 ./

RUN useradd airflow && chown -R airflow /spark_yarn
USER airflow