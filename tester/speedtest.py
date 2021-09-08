import os
import subprocess
import time
import json
from influxdb import InfluxDBClient

class speedtest():
    def test(self):
        args = ['speedtest', '-a', '-f', 'json', '--accept-license', '--accept-gdpr']

        if os.environ.get('SERVER_ID') != None:
            args.append('-s')
            args.append(os.environ.get('SERVER_ID'))

        p = subprocess.Popen(args , shell=False, stdout=subprocess.PIPE)
        response = p.communicate()
        result = json.loads(response[0])
        print ("Timestamp = " + str(result['timestamp']))
        print ("Down = " + str(result['download']['bandwidth']))
        print ("Up = " + str(result['upload']['bandwidth']))
        print ("Latency = " + str(result['ping']['latency']))
        print ("Jitter = " + str(result['ping']['jitter']))
        print ("Interface = " + str(result['interface']))
        print ("Server = " + str(result['server']))
        return result


influx_client = InfluxDBClient(host='influxdb', port=8086, username='root',
                        password='root', ssl=False, verify_ssl=False)
influx_client.switch_database('balena')
speedtest = speedtest()
frequency = os.environ.get('FREQUENCY') or 3600

while True:
    result = speedtest.test()
    json_body = [
        {
            "measurement": "download",
            "time": str(result['timestamp']),
            "fields": {
                "value": int(str(result['download']['bandwidth'])),
                "up": int(result['upload']['bandwidth']),
                "latency": float(result['ping']['latency']),
                "jitter": float(result['ping']['jitter']),
                "interface": str(result['interface']['name']),
                "server": str(result['server']['host'])
            }
        }
    ]

    print("JSON body = " + str(json_body))
    try:
        influx_client.write_points(json_body)
        print("to db...")
    except:
      print('An exception occurred')
    
    time.sleep(int(frequency))
