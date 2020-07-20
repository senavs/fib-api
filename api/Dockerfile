FROM ubuntu:18.04

# SO installation
RUN apt-get update && apt-get install -y \
        software-properties-common
RUN add-apt-repository ppa:deadsnakes/ppa \
    && apt-get update \
    && apt-get install -y \
        python3.8 \
        python3-pip \
        python3-setuptools \
        python3.8-dev
RUN apt-get install -y libmysqlclient-dev
RUN rm -rf /var/lib/apt/lists/*

# project root files
RUN mkdir /code

# requirements.txt
COPY requirements.txt /code
RUN python3.8 -m pip install -r /code/requirements.txt && rm /code/requirements.txt

# api
COPY . /code

# ports
EXPOSE 5000

# run
RUN chmod +x -R /code/
WORKDIR /code
CMD ["bash", "project/run.sh"]