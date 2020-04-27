import falcon

from .ImageStore import ImageStore
from .images import Image

api = application = falcon.API()
image_directory = "D:\\mahadev\\python\\uploader\\data\\images"
images = Image(image_directory)
image_store = ImageStore(image_directory)
api.add_route('/images', images)
api.add_route('/images/{name}', image_store)
