from .facebook_service import FacebookService
from .types import RequestType


class TextWithPhotoPost(FacebookService):
    post_image_url = ''
    post_content = ''

    def __init__(self, page_id="", access_token="", post_image_url="", post_content=""):
        FacebookService.__init__(
            self,
            page_id,
            access_token,
            request_type=RequestType.TEXT_WITH_PHOTO_POST
        )

        self.post_image_url = post_image_url
        self.post_content = post_content

    def submit_post(self):
        body = {
            'url': self.post_image_url,
            'message': self.post_content + ' [Creado por bot]',
        }

        return self.submit_request(body)
