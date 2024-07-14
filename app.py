import streamlit as st
import requests

#@st.cache(allow_output_mutation=True)
@st.cache_data
def post_an_image_to_instagram(image_url, ig_user_id, access_token, caption=None):
    api_version = 'v20.0'

    # Step one: Upload the image
    upload_url = f'https://graph.facebook.com/{api_version}/{ig_user_id}/media'
    upload_params = {
        'image_url': image_url,
        'caption': caption,
        'access_token': access_token
    }
    response_upload = requests.post(upload_url, params=upload_params)

    if 'id' in response_upload.json():
        creation_id = response_upload.json()['id']
    else:
        return "Error uploading image to Instagram"

    # Step two: Publish the image
    publish_url = f'https://graph.facebook.com/{api_version}/{ig_user_id}/media_publish'
    publish_params = {
        'creation_id': creation_id,
        'access_token': access_token
    }
    response_publish = requests.post(publish_url, params=publish_params)

    if response_publish.status_code == 200:
        return "Success, image posted on Instagram!"
    else:
        return "Error publishing image on Instagram"

st.title("Instagram Image Posting")

image_url = st.text_input("Image URL", "https://i.postimg.cc/d11PMKdZ/Designer.jpg")
caption = st.text_input("Caption", "My first automatic post on Instagram!")
ig_user_id = st.text_input("Instagram User ID", "17841468053205975")
access_token = st.text_input("Access Token", "EAAGcry2OyuEBO6E6tyvkS5NqVUzXNaAJVFYZBe1wwBNqvhfRbDmB9CjIOE201RyNf8ePOpvC5zDzcEglwZC7ZCLFrkJa6x7Q9oiW3ya7ZCllLOfxFdSiJQXE6P8k21pJIYehzvLrWrbCxEVNMweZAdLVMCqOf5faIpJi7HOlZAIaigtZCdCLvnwdUqUNooLjbazDXyw3ZBbpTjRdIMMfU6U7sm145aVoQfTF14QZD")

if st.button("Post to Instagram"):
    with st.spinner("Posting image to Instagram..."):
        result = post_an_image_to_instagram(image_url, ig_user_id, access_token, caption)
        st.write(result)
