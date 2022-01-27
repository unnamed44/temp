#!/usr/bin/python3

import sys
import json
import requests
import time

url = 'http://localhost/api/status'

status = ''
players = ''
counter = 0
sleep = 1
wait_time = 600
while (not status=='waiting') or (not players=='0'):
    try:
      data = requests.get(url=url)
      output = json.loads(data.content)
      name = str(output['name'])
      status = str(output['status'])
      players = str(output['players'])
      counter = counter + 1
      print('status: ',status,'/','players: ',players,'/','counter: ',counter)
      if counter == wait_time:
          break
      time.sleep(sleep)
    except Exception as e:
      print ('error:',e)
      sys.exit(1)
