import io
import json
import mimetypes
import os
import uuid

import falcon


class Image(object):
    def __init__(self, base_dir):
        self.base_dir = base_dir

    def on_get(self, req, resp):
        doc = {
            'images': [
                {
                    'href': '/images/1eaf6ef1-7f2d-4ecc-a8d5-6e8adba7cc0e.png'
                }
            ]
        }
        resp.body = json.dumps(doc, ensure_ascii=False)
        resp.status = falcon.HTTP_200

    def on_post(self, req, resp):
        print(req.content_type)
        name = self.save(req.stream, req.content_type)
        resp.status = falcon.HTTP_201
        resp.location = '/images/' + name

    def save(self, image_stream, image_content_type):
        ext = mimetypes.guess_extension(image_content_type)
        name = '{uuid}{ext}'.format(uuid=uuid.uuid4(), ext=ext)
        image_path = os.path.join(self.base_dir, name)

        with io.open(image_path, 'wb') as image_file:
            while True:
                chunk = image_stream.read()
                if not chunk:
                    break

                image_file.write(chunk)

        return name
