import logging

from flask import request

from app import app
from image_processing import processor


def photo_analyze_manager(proc, path):
    logging.info(f"AI started ({path})")

    def callback(result):
        logging.info(f"AI success end ({path})")

    proc.callback = callback
    proc.start_async_process(path)


@app.route("/api/photo", methods=['POST'])
def photo_analyze():
    l_processor = processor()

    data = request.data
    fname = request.headers['fname']

    file_path = f"files/{fname}"

    with open(file_path, "wb") as f:
        f.write(data)

    photo_analyze_manager(l_processor, file_path)

    return "OK"
