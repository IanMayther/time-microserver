import os
import requests
import datetime

from flask import Flask

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY').encode()

@app.route('/')
def get_time():
    clock = datetime.datetime.now().timestamp()
    print(clock)
    return str(clock)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 6738))
    app.run(host='0.0.0.0', port= port)