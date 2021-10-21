FROM ubuntu:18.04
RUN (apt update && \
    apt list --upgradable && \
    apt-get install -y wget openssl linux-libc-dev ca-certificates apt-transport-https libssl1.0.0 python3.7 python3-distutils python3-pip locales && \
    apt-get autoremove) || exit 1
WORKDIR /opt/bits/todo
COPY . /opt/bits/todo
RUN pip3 install -r requirement.txt
EXPOSE 5000
CMD ["python3", "app.py"]
