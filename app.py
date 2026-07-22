from flask import Flask
from config import Config
from extensions import db, jwt
from auth.models import User
from auth.routes import auth_bp


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialize Extensions
    db.init_app(app)
    jwt.init_app(app)

    # Register Blueprint
    app.register_blueprint(auth_bp)

    @app.route("/")
    def home():
        return "<h1>JWT Team Management System</h1>"

    with app.app_context():
        db.create_all()

    return app


app = create_app()

if __name__ == "__main__":
    app.run(debug=True)