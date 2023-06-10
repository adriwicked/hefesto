from flask import Flask, request, make_response
from flask_cors import CORS
from google.auth.transport import requests
from google.oauth2.id_token import verify_firebase_token

app = Flask(__name__)
CORS(app)

firebase_request = requests.Request()

@app.route('/login', methods=['POST'])
def login():
    token = request.headers.get('Authentication').replace('Bearer ', '')

    try:
        claims = verify_firebase_token(token, firebase_request)
        print('claims', claims)
    except ValueError as exc:
        error_message = str(exc)
        print('error_message', error_message)

    return make_response('ok', 200)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
