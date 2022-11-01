from .facebook_service import FacebookService
from .types import RequestType


class PhotoPost(FacebookService):
    post_image_url = ''

    def __init__(self, page_id="", access_token="", post_image_url=""):
        FacebookService.__init__(
            self,
            page_id,
            access_token,
            request_type=RequestType.PHOTO_POST
        )

        self.post_image_url = post_image_url

    def submit_post(self):
        body = {
            'url': self.post_image_url
        }

        return self.submit_request(body)
