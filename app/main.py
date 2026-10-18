"""Sample Flask application used to demonstrate the Woodpecker CI/CD pipeline."""
import os

from flask import Flask, jsonify, request


def create_app() -> Flask:
    app = Flask(__name__)

    @app.get("/")
    def index():
        return jsonify(message="Hello from the Woodpecker CI/CD demo!", version=os.getenv("APP_VERSION", "dev"))

    @app.get("/health")
    def health():
        return jsonify(status="ok")

    @app.get("/add")
    def add():
        try:
            a = float(request.args["a"])
            b = float(request.args["b"])
        except (KeyError, ValueError):
            return jsonify(error="query params 'a' and 'b' must be numbers"), 400
        return jsonify(result=a + b)

    return app


app = create_app()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
