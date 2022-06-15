import asyncio
import websockets
import requests
import json
import pandas as pd
from urllib.request import urlopen


response = urlopen("https://api.shasta.trongrid.io/v1/accounts/TSaJqQ1AZ2bEYyqBwBmJqCBSPv8KPRTAdv/transactions")
data_json = json.loads(response.read())


async def time(websocket, path):
          await websocket.send(json.dumps(data_json,indent=4, skipkeys = True))
               

start_server = websockets.serve(time, '127.0.0.1', 5678)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()