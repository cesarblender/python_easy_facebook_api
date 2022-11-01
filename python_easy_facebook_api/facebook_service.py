import requests

from .types import RequestType


class FacebookService():
    api_route = ''
    api_action = ''
    access_token = ''

    def __init__(self, page_id="", access_token="", request_type=RequestType.TEXT_POST, custom_endpoint=None):
        if request_type == RequestType.TEXT_POST:
            self.api_action = 'feed'
        elif request_type == RequestType.PHOTO_POST or request_type == RequestType.TEXT_WITH_PHOTO_POST:
            self.api_action = 'photos'

        if custom_endpoint is not None:
            self.api_action = custom_endpoint

        self.api_route = 'https://graph.facebook.com/{}/{}' \
            .format(
                page_id,
                self.api_action
            )

        self.access_token = access_token

    def submit_request(self, body):
        payload = {
            **body,
            'access_token': self.access_token
        }

        response = requests.post(self.api_route, data=payload)

        return response


# # POST: https://graph.facebook.com/<page_id>/<custom_endpoint>
# custom_request = FacebookService(
#     access_token="",
#     page_id="",
#     custom_endpoint="feed"
# )

# response = custom_request.submit_request(
#     {
#         'message': 'hi'
#     }
# )

# print(response.text)
