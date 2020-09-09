import requests
import sys

my_params = {}
if len(sys.argv) >= 2:
    task_id = sys.argv[1]
else:
    print("Help: ./get_report.py < task id >")
    exit()
r = requests.get('http://127.0.0.1:4242/api/report/{}'.format(task_id) ,params=my_params)

print(r.json())
