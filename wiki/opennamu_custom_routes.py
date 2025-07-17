import flask
import jwt

from . import wiki_set  # 기존 OpenNAMU 구조에 따라 import

def register_routes(app):
    @app.route('/sso-login', methods=["POST"])
    def sso_login():
        token = flask.request.json.get("token")
        try:
            payload = jwt.decode(token, "THOTH_SECRET", algorithms=["HS256"])
            flask.session['id'] = payload['username']
            return flask.jsonify({"status": "success"})
        except jwt.exceptions.InvalidTokenError:
            return flask.jsonify({"error": "Invalid token"}), 401