def create_app():
    from flask import Flask
    import os

    app = Flask(__name__)
    app.config.from_mapping(SECKRET_KEY=os.environ.get("SECKRET_KEY"))

    from .handlers import bp
    app.register_blueprint(bp)

    return app
