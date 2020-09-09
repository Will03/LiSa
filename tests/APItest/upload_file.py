import requests
import sys

if len(sys.argv) >= 2:
    file_path = sys.argv[1]
else:
    print("Help: ./upload_file.py <file>")
    exit()

my_file = {'file': open(file_path,'rb')}
my_params = {'pretty':'true'}


r = requests.post('http://127.0.0.1:4242/api/tasks/create/file',files=my_file ,params=my_params)

print(r.json())
