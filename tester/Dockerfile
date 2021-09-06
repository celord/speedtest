FROM python:3.7-alpine
RUN pip3 install paho-mqtt 
RUN wget https://install.speedtest.net/app/cli/ookla-speedtest-1.0.0-i386-linux.tgz -O speedtest.tgz
RUN tar -xvf speedtest.tgz
RUN mv speed* /usr/bin/
