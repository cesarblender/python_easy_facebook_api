from .facebook_service import FacebookService
from .types import RequestType


class VideoPost(FacebookService):
    video_url = ""
    video_title = ""

    def __init__(self, page_id="", access_token="", video_url="", video_title=""):
        FacebookService.__init__(
            self,
            page_id,
            access_token,
            request_type=RequestType.VIDEO_POST,
        )

        self.video_url = video_url
        self.video_title = video_title

    def submit_post(self):
        body = {
            "file_url": self.video_url,
            "title": self.video_title + " [Created by bot]"
        }

        self.submit_request(body)
