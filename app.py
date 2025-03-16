from flask import Flask
# Importing blueprints from other files
from login import login_bp
from register import register_bp
from user_profile import user_profile_bp



app = Flask(__name__)


# Registering blueprints
app.register_blueprint(login_bp)
app.register_blueprint(register_bp, url_prefix="/register")
app.register_blueprint(user_profile_bp, url_prefix="/profile")



if __name__ == "__main__":
