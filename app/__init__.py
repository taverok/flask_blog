from flask import Flask, jsonify, abort
from konfig import Config
from werkzeug.exceptions import HTTPException, default_exceptions

from app.routes import routes_main


def JsonApp(app):
    def error_handling(error):
        if isinstance(error, HTTPException):
            result = {'code': error.code, 'description': error.description, 'message': str(error)}
        else:
            description = abort.mapping[500].description
            result = {'code': 500, 'description': description, 'message': str(error)}
            resp = jsonify(result)
            resp.status_code = result['code']
            return resp

    for code in default_exceptions.keys():
        app.register_error_handler(code, error_handling)

    return app


app = JsonApp(Flask(__name__))

config = Config('settings.ini')
app.config.update(config.get_map('blog'))

app.register_blueprint(routes_main)
