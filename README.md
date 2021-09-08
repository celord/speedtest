# Speedtest
**
This project is based on this other project: with this differences:
**

1. It does not uses the default dashboard from balena, instead it uses grafana but imports the dashboards from the balena project
2. It does not uses mqtt nor telegraf instead it uses the python script to publish to the Influxdb directly
3. This uses the linux docker branches of every part of the project
4. It uses the linux binary of the speedtest cli app