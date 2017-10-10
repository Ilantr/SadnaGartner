import logging
import os
import settings as Config
from web.server import Server

logging.basicConfig(level=logging.DEBUG)

# pylint: disable=invalid-name
server = Server()
if __name__ == '__main__':
    server.app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 5000)))