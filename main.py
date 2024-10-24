import os
from flask import Flask
from dotenv import load_dotenv

from app.Config import Config
from app.Api import Api

def init():
    load_dotenv()
    config = Config(os.environ)
    return Api(config, Flask(__name__))

if __name__ == '__main__':
    app = init()
    app.run()