import requests
from app import collect_metrics
'''
response = requests.get('http://localhost:8080/collect_metrics')
metrics = response.json()

# Access and use metrics json.
cpu_usage = metrics['cpu_usage']
memory = metrics['memory_usage']
disk_usage = metrics['disk_usage']

print('CPU: ', cpu_usage)
print('memory:', memory)
print('Disk usage: ', disk_usage)
'''
metrics = collect_metrics()
print(metrics)