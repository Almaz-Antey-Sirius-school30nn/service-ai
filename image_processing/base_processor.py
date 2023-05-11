import threading
import os


class ImageProcessor:
    """
    Base class for all image processors
    @:param callback - callback function on process end

    """

    def __init__(self):
        self.callback = None
        self.result: dict = {}

    def _process(self, path: str):
        pass

    def start_async_process(self, path: str):
        thread = threading.Thread(target=self.__tread_task, args=(path,))
        thread.start()

    def _delete_file_after_process(self, path: str):
        os.remove(path)

    def _after_process(self, path: str):
        pass

    def __tread_task(self, path: str):
        self._process(path)
        self._after_process(path)
        self._delete_file_after_process(path)

        if self.callback is not None:
            self.callback(self.result)
