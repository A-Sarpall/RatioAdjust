import streamlit as st
import json
st.title("Ratio Adjuster")
st.text("See which Instagram accounts you follow that don't follow you back")
st.divider()
st.text("Upload the followers_1.json and following.json files")
st.text("by downloading your Instagram data")

# File upload for followers_1.json
st.sidebar.title('Upload followers_1.json')
followers_file = st.sidebar.file_uploader("Choose a JSON file", key="followers", type=["json"])

# File upload for following.json
st.sidebar.title('Upload following.json')
following_file = st.sidebar.file_uploader("Choose a JSON file", key="following", type=["json"])

if followers_file is not None and following_file is not None:
    followers_1_data = json.load(followers_file)
    following_data = json.load(following_file)

    # Extract accounts from followers_1.json
    followers = [entry['string_list_data'][0]['value'] for entry in followers_1_data]

    # Extract accounts from following.json
    following = [entry['string_list_data'][0]['value'] for entry in following_data['relationships_following']]

    # Create a list of accounts in following but not in followers_1
    not_following = [account for account in following if account not in followers]

    st.divider()
    st.write("Accounts that don't follow you back:")
    for account in not_following:
        st.markdown(f"[instagram.com/{account}](https://www.instagram.com/{account})")
else:
    st.divider()
    st.title("How to Download")
    st.write("On your phone open the Instagram App")
    st.write("Profile->Three lines at the top right")
    st.write("Your Activity->Download Your Information")
    st.write("Download or transfer info->Select the account you want")
    st.write("Some of your information->Followers and following")
    st.write("Download to device->Date Range: *All Time*")
    st.write("In the notify section, make sure it's an email you have access to")
    st.write("Format: *JSON*->Create Files")
    st.divider()
    st.write("Files are Empty :(")
