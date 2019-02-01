from app.app import create_app
from app.config import config

app = create_app()
if __name__ == '__main__':
    app.run(host=config.HOST, port=config.PORT, debug=config.DEBUG)
