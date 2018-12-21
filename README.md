Spotify swap token
==================

Spotify swap token with Flask and Python.

##Install virtualenv
virtualenv --python=/usr/local/bin/python3 venv
source venv/bin/active
pip install -r requirements.txt
deactivate

##Step
Fill in your credentials in main.py.
This includes the CLIENT_ID, CLIENT_SECRET and CLIENT_CALLBACK_URL, which is left blank. 
You can obtain this by going to [Spotify Developers](https://developer.spotify.com/my-applications/#!/).

##Run
./run.sh

##Deploy on PythonAnywhere
[Setting up Flask applications on PythonAnywhere](https://help.pythonanywhere.com/pages/Flask/#!/)