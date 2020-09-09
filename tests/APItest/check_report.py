import requests,json
import sys

my_params = {}
if len(sys.argv) >= 2:
    task_id = sys.argv[1]
else:
    print("Help: ./check_report.py < task id >")
    exit()
resp = requests.get('http://127.0.0.1:4242/api/tasks/view/{}'.format(task_id))
json_resp = resp.content
# print(json_resp)
j = json.loads(json_resp)
print(j['status'])