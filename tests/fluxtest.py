from influxdb import InfluxDBClient
client = InfluxDBClient(host='localhost', port=8086)
client = InfluxDBClient(host='localhost', port=8086, username='root', password='root', ssl=False, verify_ssl=False)
print(client.get_list_database())
client.switch_database('balena')

#print(client.write_points(json_body))
q = client.query(
    'SELECT "value" FROM "balena"."autogen"."download"')
print(q)
