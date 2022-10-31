## Python Easy Facebook API

Make requests to the facebook graph api easily.

## Docs

### Instantiate the class
```
from python_easy_facebook_apy import FbApi

# We recommend seriously use a library like python_dotenv to store the facebook access token and the page id.
# To learn how to get access_token and page_id read "Get Access Token and Page ID" below.
access_token = "<your access token>"
page_id = "<your page id>"

api = FbApi(
    access_token=access_token
    page_id=page_id
)

# ...
```

### To add a Text Post

```
api.TextPost(
    content="<your post content>"
)
```

### To add a Photo Post

```
api.PhotoPost(
    # You can use any framework or library like Flask or Django to store your image and upload to facebook
    # Example:
    # image_url="https://example.com/image.jpg"
    image_url="<your image url>"
)
```

### To add a Text with Photo Post

```
api.TextWithPhotoPost(
    content="<your post content>"
    image_url="<your image url>"
)
```
