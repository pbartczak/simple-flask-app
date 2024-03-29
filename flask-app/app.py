import os
from flask import Flask, render_template
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

@app.route('/', methods = ['GET'])
def index():
    return render_template('index.html', app_version=os.getenv('APP_VERSION'))


app.run(host='0.0.0.0', port=8080)

