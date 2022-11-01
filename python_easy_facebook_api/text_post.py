from .facebook_service import FacebookService
from .types import RequestType


class TextPost(FacebookService):
    post_content = ''

    def __init__(self, page_id="", access_token="", post_content=""):
        FacebookService.__init__(
            self,
            page_id,
            access_token,
            request_type=RequestType.TEXT_POST
        )

        self.post_content = post_content

    def submit_post(self):
        body = {
            'message': self.post_content + ' [Creado por bot]'
        }

        return self.submit_request(body)
