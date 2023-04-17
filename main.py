import streamlit as st
import random
import requests


def get_data(session, animal):
    try:
        if animal == "cat":
            random_id = random.randint(0, 90) #api has 91 random facts from id 0-90
            url_request = f"https://meowfacts.herokuapp.com/?id={random_id}"
            result = session.get(url_request).json()
            output = result['data'][0] #api object has only one key (data) that has a list as a value containing a single string
            return output
        if animal == "dog":
            url_request = "https://dogapi.dog/api/v2/facts"
            result = session.get(url_request).json()
            output = result['data'][0]['attributes']['body'] # api returns an object with one key ('data') that contains a list that contains
            # a dict at index 0. One of the keys in that dict is 'attributes' which contains a dict with a key('body') and the value is the desired fact string.
            return output
    except Exception:
        return {}



def main():
    st.set_page_config(page_title="Random facts for Dogs and Cats!")
    st.title("Random facts about Dogs and Cats!")
    session = requests.Session()

    hide_fullscreen_button_css = """
    <style>
    button[title="View fullscreen"] {
        visibility:hidden;
    }
    button[title="View fullscreen"]:hover {
        visibility: hidden;
        }
    </style>
    """
    st.markdown(hide_fullscreen_button_css, unsafe_allow_html=True)

    with st.form(key="my_form"): 
        choice = st.selectbox("Choose your furry friend!", ["dog", "cat"], key="choice")
        submit = st.form_submit_button(label="Generate Random Fact")

    if submit:
        col1, col2 = st.columns(2, gap="medium")
        col1.image(f"images/{choice}.jpg", use_column_width=True)
        animal_to_display = get_data(session, choice)
        if animal_to_display:
            col2.write(animal_to_display)
        else:
            col2.error("Error")


if __name__ == '__main__':
    main()



