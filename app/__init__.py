from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    with app.app_context():
        # Import parts of our application
        from .routes import main

        # Register Blueprints
        app.register_blueprint(main.main_bp)

        return app
