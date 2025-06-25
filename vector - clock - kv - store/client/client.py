
import requests
import time

print("Writing x=1 to node1...")
resp = requests.post("http://localhost:5001/write", json={"key": "x", "value": "1"})
print("Response:", resp.json())

time.sleep(1)

print("Reading x from node2...")
resp = requests.get("http://localhost:5002/read?key=x")
print("Value at node2:", resp.text)
