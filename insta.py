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
        followers_1_accounts = [entry['string_list_data'][0]['value'] for entry in followers_1_data['data']['user']['edge_followed_by']['edges']]

        # Extract accounts from following.json
        following_accounts = [entry['username'] for entry in following_data['data']['user']['edge_follow']['edges']]

        # Create a list of accounts in following but not in followers_1
        accounts_not_followers = ["[instagram.com/" + account + "](https://www.instagram.com/" + account + ")" for account in following_accounts if account not in followers_1_accounts]

        st.write("Accounts that don't follow you back:")
        for account_link in accounts_not_followers:
            st.markdown(account_link, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
