import requests
import sys

# python list_report.py { finished | failed | pending }

my_params = {'limit': '300'}
my_params = {}
if len(sys.argv) >= 2:
    status = sys.argv[1]
else:
    print("Help: ./check_report.py < finished | failed | pending >")
    exit()
r = requests.get('http://127.0.0.1:4242/api/tasks/{}'.format(status) ,params=my_params)

print(r.json())
