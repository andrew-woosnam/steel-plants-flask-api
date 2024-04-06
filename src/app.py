from flask import Flask
from src.config import Config
from src.database import init_db
from src.api.blueprints import api_blueprint


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    init_db(app)
    app.register_blueprint(api_blueprint, url_prefix='/api')

    return app


if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', port=5000)
