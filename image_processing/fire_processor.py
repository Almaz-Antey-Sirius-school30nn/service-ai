from image_processing import ImageProcessor
from predict import predict_fire
from module_mchs import MCHS


class FireProcessor(ImageProcessor):

    def _process(self, path: str):
        # super()._process(path)
        fires = predict_fire(path)
        if fires > 0:
            MCHS.send_fire("{}")
            print("detected")
        pass

    def _delete_file_after_process(self, path: str):
        # super()._delete_file_after_process(path)
        pass
