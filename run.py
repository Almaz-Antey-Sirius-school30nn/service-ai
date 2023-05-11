import logging
import os

from datetime import datetime

from api import *


def create_folders():
    try:
        os.mkdir("files")
    except:
        pass


def config_logging():
    path = f"logs/{datetime.now().strftime('%d.%m.%Y_%H.%M.%S')}.log"

    logging.basicConfig(
        level=logging.INFO,
        filename=path,
        filemode="w",
        format="%(asctime)s [%(threadName)-12.12s] [%(levelname)-5.5s]  %(message)s"
    )


if __name__ == '__main__':
    # config_logging()
    # logging.info("App starting")
    # create_folders()

    app.run(port="5001")
