import streamlit as st
from few_shot import FewShotPosts
from post_generator import generate_post


def main ():
    st.title("LinkedIn Post Generator")
    col1, col2, col3 = st.columns(3)
    fs = FewShotPosts()

    length_options = ["Short", "Medium", "Long"]  # length options define kiye
    language_options = ["English", "Hinglish"]  # language options define kiye

    with col1:
        selected_tag = st.selectbox("Title", options=sorted(list(fs.get_tags())))

    with col2:
        selected_length = st.selectbox("Length", options=length_options)

    with col3:
        selected_language = st.selectbox("Language", options=language_options)

    if st.button("Generate"):
        post = generate_post(selected_length, selected_language, selected_tag)  # output store karo
        st.write(post)  # generated post show karo


if __name__ == "__main__":
    main()