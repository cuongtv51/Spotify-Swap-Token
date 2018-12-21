from flask import Flask, request, make_response
import json
import requests

# https://developer.spotify.com/web-api/authorization-guide/

app = Flask(__name__)

#  Client Keys
CLIENT_ID = ""
CLIENT_SECRET = ""
CLIENT_CALLBACK_URL = ""
SPOTIFY_ACCOUNTS_ENDPOINT = "https://accounts.spotify.com"


@app.route("/")
def index():
    return 'hello world!'


@app.route("/swap", methods=['POST'])
def swap():
    auth_code = request.form['code']
    print('-------------auth_code from client ----')
    print(auth_code)
    print('-----------------')

    params = {
        "grant_type": "authorization_code",
        "redirect_uri": CLIENT_CALLBACK_URL,
        "code": auth_code,
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET
    }
    r = requests.post(SPOTIFY_ACCOUNTS_ENDPOINT + "/api/token", data=params)

    print('-------------Status code----')
    print(r.status_code)
    print(r.content)
    print('-----------------')

    response = make_response()
    if r.status_code == 200:
        token_data = json.loads(r.content)
        response.data = json.dumps(token_data)

    response.headers["Access-Control-Allow-Origin"] = '*'
    response.headers['Content-Type'] = 'application/json'
    return response, int(r.status_code)


@app.route('/refresh', methods=['POST'])
def refresh():
    refresh_token = request.form['refresh_token']
    print('-------------refresh_token from client ----')
    print(refresh_token)
    print('-----------------')

    params = {
        "grant_type": "refresh_token",
        "refresh_token": refresh_token,
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET
    }
    r = requests.post(SPOTIFY_ACCOUNTS_ENDPOINT + "/api/token", data=params)

    print('-------------Status code----')
    print(r.status_code)
    print(r.content)
    print('-----------------')

    response = make_response()
    if r.status_code == 200:
        token_data = json.loads(r.content)
        response.data = json.dumps(token_data)

    response.headers["Access-Control-Allow-Origin"] = '*'
    response.headers['Content-Type'] = 'application/json'
    return response, int(r.status_code)


if __name__ == "__main__":
    app.run(debug=False)
