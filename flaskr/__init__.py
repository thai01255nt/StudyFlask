import os

from flask import Flask

def create_app(test_config=None):
    app = Flask(__name__)
    config = {
        "SECRET_KEY":"dev",
        "DATABASE":os.path.join(app.instance_path,"")
    }
    if test_config is None:
        app.config.from_pyfile("config.py")
    else:
        app.config.from_mapping(test_config)

    try:
        os.mkdir(app.instance_path)
    except:
        pass

    @app.route('/home')
    def home_page():
        return "Hello!"

    return app