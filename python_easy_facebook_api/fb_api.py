from .photo_post import PhotoPost
from .text_post import TextPost
from .text_with_photo_post import TextWithPhotoPost
from .video_post import VideoPost


class FbApi():
    access_token = ""
    page_id = ""

    def __init__(self, access_token="", page_id=""):
        self.access_token = access_token
        self.page_id = page_id

    def photo_post(self, image_url=""):
        return PhotoPost(self.page_id, access_token=self.access_token, post_image_url=image_url)

    def text_post(self, content=""):
        return TextPost(self.page_id, access_token=self.access_token, post_content=content)

    def text_with_photo_post(self, content="", image_url=""):
        return TextWithPhotoPost(
            self.page_id,
            access_token=self.access_token,
            post_content=content,
            post_image_url=image_url
        )

    def video_post(self, url="", title=""):
        return VideoPost(self.page_id, access_token=self.access_token, video_url=url, video_title=title)
