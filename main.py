from app import create_app
from app.config import config_by_name
import os

env_name = os.environ.get("FLASK_ENV", "development")
app = create_app(config_by_name[env_name])


if __name__ == "__main__":
    app.run(debug=True)