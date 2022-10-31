## Python Easy Facebook API

Make requests to the facebook graph api easily.

## Docs

### Instantiate the class
```
from python_easy_facebook_apy import FbApi

# We recommend seriously use a library like python_dotenv to store the facebook access token and the page id.
# To learn how to get access_token and page_id read "Get Access Token and Page ID" in the end of this file.
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
post = api.TextPost(
    content="<your post content>"
)
```

### To add a Photo Post

```
post = api.PhotoPost(
    # You can use any framework or library like Flask or Django to store your image and upload to facebook
    # Example:
    # image_url="https://example.com/image.jpg"
    image_url="<your image url>"
)
```

### To add a Text with Photo Post

```
post = api.TextWithPhotoPost(
    content="<your post content>"
    image_url="<your image url>"
)
```

### Submitting the post
```
# Makes the POST request to the Facebook Graph API
response = post.submitPost()

# Prints the id of the post, or instead, if you had an error with the `access token` or with the `page id` it will show the error details
print(response.text)
```

## Getting the Access Token

- Firstly, go to [Facebook Developer](https://developers.facebook.com/)

- Create a developer account

- Then, create an application and select that the app type is `Business app`, or something like this

- After you created an application, hover with the mouse the `Tools` menu and select `Api Graph Explorer`

- In the `App Meta` field, select your app that you already created

- Then, in the permissions field, you need to select theese permissions:
    - pages_show_list
    - pages_read_engagement
    - pages_manage_posts
    - public_profile

- After selected the permissions, click on the `Generate Access Token` button, you will see a new window that you have to agree everything and select the Facebook Page that you want to connect, **NOTE: below the name of any page, is the page id, you must copy and save on a secure place**, if you're using `dotenv` (I seriously recommend use that), you must save the `page id`, with a key like `PAGE_ID=<your page id>` in a `.env` file.

- And, finally, the last step, after generating the token, you must click on the `User or page` field and select your page, the token will change and you have to copy it and save to use on your app (that token is really sensitive, you have to store it on a environment variable, using `dotenv`)
