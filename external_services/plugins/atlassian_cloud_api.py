import sys
import json
import requests

status_url = "https://x67gp49yvrzv.statuspage.io/api/v2/summary.json"
status_data = requests.get(status_url)
status_json = json.loads(status_data.text)

exit_code = 3
message = "UNKNOWN"

for component in status_json['components']:
    if component['name'] == 'API':
        if component['status'] == 'operational':
           exit_code = 0
           message = "Atlassian API is online"
        else:
           exit_code = 2
           message = "Atlassian API is experiencing issues"

print message
sys.exit(exit_code)
