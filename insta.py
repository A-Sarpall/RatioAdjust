import streamlit as st
import json
def main():
    st.title("Ratio Adjuster")
    st.text("See which Instagram accounts you follow that don't follow you back")
    st.text("Upload the followers_1.json and following.json files")
    st.text("by downloading your Instagram data")
    
    # File upload for followers_1.json
    st.sidebar.header('Upload followers_1.json')
    followers_file = st.sidebar.file_uploader("Choose a JSON file", key="followers", type=["json"])

    # File upload for following.json
    st.sidebar.header('Upload following.json')
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

        st.write("Accounts that don't follow you back:")
        for account in not_following:
            st.markdown(f"[instagram.com/{account}](https://www.instagram.com/{account})")

if __name__ == "__main__":
    main()
