import json
import requests
from flask import Flask, request, jsonify
from g4f.Provider import *
from g4f import Model
import socket
import random

# Get the hostname
hostname = socket.gethostname()

# Get the IP address
ip_address = socket.gethostbyname(hostname)

# Print the IP address
print('Host IP Address: ', ip_address)

app = Flask(__name__)

@app.route('/')
async def index():
    return str(random.randint(1, 100))

@app.route('/chat/acytoo', methods=['POST', 'GET'])
async def acytoo():
    messages = request.get_json().get('messages', [])

    response = Acytoo._create_completion(model=Model.gpt_35_turbo.name, messages=messages, stream=False)

    return response

@app.route('/chat/aichat', methods=['POST', 'GET'])
async def aichat():
    messages = request.get_json().get('messages', [])

    response = Aichat._create_completion(model=Model.gpt_35_turbo.name, messages=messages, stream=False)

    return response


@app.route('/chat/ails', methods=['POST', 'GET'])
async def ails():
    messages = request.get_json().get('messages', [])

    response = Ails._create_completion(model=Model.gpt_35_turbo.name, messages=messages, stream=False)

    return response


@app.route('/chat/altianhu', methods=['POST', 'GET'])
async def altianhu():
    messages = request.get_json().get('messages', [])

    response = AItianhu._create_completion(model=Model.gpt_35_turbo.name, messages=messages, stream=False)

    return response


@app.route('/chat/chatgptai', methods=['POST', 'GET'])
async def chatgptai():
    messages = request.get_json().get('messages', [])

    response = ChatgptAi._create_completion(model=Model.gpt_4.name, messages=messages, stream=False) 

    return response


@app.route('/chat/chatgptlogin', methods=['POST', 'GET'])
async def chatgptlogin():
    messages = request.get_json().get('messages', [])

    response = ChatgptLogin._create_completion(model=Model.gpt_35_turbo.name, messages=messages, stream=False)

    return response


@app.route('/chat/deepai', methods=['POST', 'GET'])
async def deepai():
    messages = request.get_json().get('messages', [])

    response = DeepAi._create_completion(model=Model.gpt_35_turbo.name, messages=messages, stream=False)

    return response


@app.route('/chat/dfehub', methods=['POST', 'GET'])
async def dfehub():
    messages = request.get_json().get('messages', [])

    response = DFEHub._create_completion(model=Model.gpt_35_turbo.name, messages=messages, stream=False)

    return response


@app.route('/chat/easychat', methods=['POST', 'GET'])
async def easychat():
    messages = request.get_json().get('messages', [])

    response = EasyChat._create_completion(model=Model.gpt_35_turbo.name, messages=messages, stream=False)

    return response


@app.route('/chat/forefront', methods=['POST', 'GET'])
async def forefront():
    messages = request.get_json().get('messages', [])

    response = Forefront._create_completion(model=Model.gpt_35_turbo.name, messages=messages, stream=False)

    return response


@app.route('/chat/getgpt', methods=['POST', 'GET'])
async def getgpt():
    messages = request.get_json().get('messages', [])

    response = GetGpt._create_completion(model=Model.gpt_35_turbo.name, messages=messages, stream=False)

    return response


@app.route('/chat/h2o', methods=['POST', 'GET'])
async def h2o():
    messages = request.get_json().get('messages', [])

    response = H2o._create_completion(model=Model.llama_13b.name, messages=messages, stream=False)

    return response


@app.route('/chat/liaobots', methods=['POST', 'GET'])
async def liaobots():
    messages = request.get_json().get('messages', [])

    response = Liaobots._create_completion(model=Model.gpt_4.name, messages=messages, stream=False)

    return response


@app.route('/chat/lockchat', methods=['POST', 'GET'])
async def lockchat():
    messages = request.get_json().get('messages', [])

    response = Lockchat._create_completion(model=Model.gpt_4.name, messages=messages, stream=False)

    return response


@app.route('/chat/theb', methods=['POST', 'GET'])
async def theb():
    messages = request.get_json().get('messages', [])

    response = Theb._create_completion(model=Model.gpt_35_turbo.name, messages=messages, stream=False)

    return response


@app.route('/chat/you', methods=['POST', 'GET'])
async def you():
    messages = request.get_json().get('messages', [])

    response = You._create_completion(model=Model.gpt_35_turbo.name, messages=messages, stream=False)

    return response


@app.route('/chat/yqcloud', methods=['POST', 'GET'])
async def yqcloud():
    messages = request.get_json().get('messages', [])

    response = Yqcloud._create_completion(model=Model.gpt_35_turbo.name, messages=messages, stream=False)

    return response



if __name__ == '__main__':
    print('Server is running on port 0000')
    app.run(host='0.0.0.0', port=0000, debug=True)
