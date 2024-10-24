import requests
from flask import Flask
from app.Config import Config

class Api:
    config: Config
    app: Flask

    def __init__(self, config: Config, app: Flask) -> None:
        self.config = config
        self.app = app
        self.define_routes()

    def define_routes(self) -> None:
        self.app.add_url_rule('/api/sprints', view_func=self.get_sprints)

    def get_sprints(self):
        return self.app.json.response(['things'])

    def run(self) -> None:
        self.app.run(debug=True)