from app import create_app
import config
import os

config_class = os.getenv('FLASK_CONFIG', 'config.DevelopmentConfig')
app = create_app(config_class=config_class)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
