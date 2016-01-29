import sys
import json
import requests

status_url = "https://33yy6hwxnwr3.statuspage.io/api/v2/summary.json"
status_data = requests.get(status_url)
status_json = json.loads(status_data.text)

if status_json['status']['indicator'] == 'none':
   exit_code = 0
   message = "Pager Duty is online"
else:
   exit_code = 2
   message = "Pager Duty is offline"

print message
sys.exit(exit_code)
