FROM python:3.7-alpine
WORKDIR /app
RUN pip3 install influxdb 
RUN wget https://install.speedtest.net/app/cli/ookla-speedtest-1.0.0-i386-linux.tgz -O speedtest.tgz
RUN tar -xvf speedtest.tgz
RUN mv speed* /usr/bin/
RUN apk add tzdata
RUN cp /usr/share/zoneinfo/America/Costa_Rica /etc/localtime
COPY . /app
ENV FREQUENCY=300
CMD ["/bin/sh", "run.sh"]
