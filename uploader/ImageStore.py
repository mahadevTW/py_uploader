import mimetypes
import os
import uuid
import io

import falcon


class ImageStore(object):
    def __init__(self, base_dir):
        self.base_dir = base_dir

    def on_get(self, req, resp, name):
        resp.content_type = mimetypes.guess_type(name)[0]
        image_path = os.path.join(self.base_dir, name)
        if not os.path.exists(image_path):
            resp.status = falcon.HTTP_404
            return
        stream = io.open(image_path, 'rb')
        length = os.path.getsize(image_path)
        resp.stream, resp.content_length = stream, length
