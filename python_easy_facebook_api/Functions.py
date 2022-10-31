from enum import Enum
import requests


class RequestType(Enum):
    TEXT_POST = 0
    PHOTO_POST = 1
    TEXT_WITH_PHOTO_POST = 2


class FacebookService():
    api_route = ''
    api_action = ''
    access_token = ''

    def __init__(self, page_id="", access_token="", request_type=RequestType.TEXT_POST):
        if request_type == RequestType.TEXT_POST:
            self.api_action = 'feed'
        elif request_type == RequestType.PHOTO_POST or request_type == RequestType.TEXT_WITH_PHOTO_POST:
            self.api_action = 'photos'

        self.api_route = 'https://graph.facebook.com/{}/{}' \
            .format(
                page_id, self.api_action
            )

        self.access_token = access_token

    def __submit__(self, body):
        payload = {
            **body,
            'access_token': self.access_token
        }

        response = requests.post(self.api_route, data=payload)

        return response


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

    def submitPost(self):
        body = {
            'url': self.post_image_url
        }

        return self.__submit__(body)


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

    def submitPost(self):
        body = {
            'message': self.post_content + ' [Creado por bot]'
        }

        return self.__submit__(body)


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

    def submitPost(self):
        body = {
            'url': self.post_image_url,
            'message': self.post_content + ' [Creado por bot]',
        }

        return self.__submit__(body)


class FbApi():
    access_token = ""
    page_id = ""

    def __init__(self, access_token="", page_id=""):
        self.access_token = access_token
        self.page_id = page_id

    def PhotoPost(self, image_url=""):
        return PhotoPost(self.page_id, access_token=self.access_token, post_image_url=image_url)

    def TextPost(self, content=""):
        return TextPost(self.page_id, access_token=self.access_token, post_content=content)

    def TextWithPhotoPost(self, content="", image_url=""):
        return TextWithPhotoPost(
            self.page_id,
            access_token=self.access_token,
            post_content=content,
            post_image_url=image_url
        )
