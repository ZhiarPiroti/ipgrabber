from flask import Flask, request
app = Flask(__name__)

@app.route('/')
def index():
    ip = request.remote_addr
    with open('ips.txt', 'a') as f:
        f.write(ip + '\n')
    return "hello you have been scammed!"
