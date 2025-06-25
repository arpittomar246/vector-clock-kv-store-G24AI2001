
from flask import Flask, request, jsonify
from vector_clock import VectorClock
import os
import requests

app = Flask(__name__)
data_store = {}
buffer = []

NODE_ID = os.environ["NODE_ID"]
PEERS = os.environ["PEERS"].split(',')
vc = VectorClock(NODE_ID, PEERS + [NODE_ID])

@app.route('/write', methods=['POST'])
def write():
    key, value = request.json['key'], request.json['value']
    vc.increment()
    data_store[key] = value
    propagate_write(key, value, vc.get())
    return jsonify(success=True, vc=vc.get())

@app.route('/replicate', methods=['POST'])
def replicate():
    msg = request.json
    if vc.is_causally_ready(msg['vc'], msg['sender']):
        apply_write(msg['key'], msg['value'], msg['vc'], msg['sender'])
    else:
        buffer.append(msg)
    return '', 204

@app.route('/read')
def read():
    key = request.args.get('key')
    return data_store.get(key, '')

def apply_write(key, value, incoming_vc, sender):
    vc.update(incoming_vc)
    data_store[key] = value
    check_buffer()

def check_buffer():
    for msg in buffer[:]:
        if vc.is_causally_ready(msg['vc'], msg['sender']):
            apply_write(msg['key'], msg['value'], msg['vc'], msg['sender'])
            buffer.remove(msg)

def propagate_write(key, value, clock):
    for peer in PEERS:
        try:
            requests.post(f"http://{peer}:5000/replicate", json={
                "key": key, "value": value, "vc": clock, "sender": NODE_ID
            })
        except:
            continue

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
