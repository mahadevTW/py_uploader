import os

import falcon

from .ImageStore import ImageStore
from .images import Image

api = application = falcon.API()


def get_default_data_dir():
    dir = "data/uploader/images"
    if not os.path.exists(dir):
        os.makedirs(dir)
    return dir


image_directory = os.environ[
    'IMAGE_DIR'] if 'IMAGE_DIR' in os.environ else get_default_data_dir()
images = Image(image_directory)
image_store = ImageStore(image_directory)
api.add_route('/images', images)
api.add_route('/images/{name}', image_store)
