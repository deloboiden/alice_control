from flask import Flask, request
import json

app = Flask(__name__)
host = 'localhost'
port = 5000

@app.route('/post', methods=['POST'])
def main():
    responce = {
        'session': request.json['session'],
        'version': request.json['version'],
        'responce': {'end_session': False}
    }
    handle_dialog(responce, request.json)
    return json.dumps(responce)

def handle_dialog(res, req):
    if 'request' in req and 'original_utterance' in req['request'] and len(req['request']['original_utterance']) > 0:
        res['responce']['text'] = req['request']['original_utterance']
    else:
        res['responce']['text'] = 'echo'

if __name__ == '__main__':
    app.run(host=host, port=port)
