import hashlib
import json
import sqlite3
from pathlib import Path
import streamlit as st
import pandas as pd

# Setup
import streamlit as st
from streamlit_extras.app_logo import add_logo
from streamlit.source_util import _on_pages_changed, get_pages
from streamlit_extras.switch_page_button import switch_page
from PIL import Image

st.set_page_config(
    page_title="Login/Signup",
    page_icon="🏀",
    layout='wide'
)

DEFAULT_PAGE = "auth"
SECOND_PAGE_NAME = "app"


def get_all_pages():
    default_pages = get_pages(DEFAULT_PAGE)

    pages_path = Path("pages.json")

    if pages_path.exists():
        saved_default_pages = json.loads(pages_path.read_text())
    else:
        saved_default_pages = default_pages.copy()
        pages_path.write_text(json.dumps(default_pages, indent=4))

    return saved_default_pages


def clear_all_but_first_page():
    current_pages = get_pages(DEFAULT_PAGE)

    if len(current_pages.keys()) == 1:
        return

    get_all_pages()

    # Remove all but the first page
    key, val = list(current_pages.items())[0]
    current_pages.clear()
    current_pages[key] = val

    _on_pages_changed.send()


def show_all_pages():
    current_pages = get_pages(DEFAULT_PAGE)

    saved_pages = get_all_pages()

    # Replace all the missing pages
    for key in saved_pages:
        if key not in current_pages:
            current_pages[key] = saved_pages[key]

    _on_pages_changed.send()


def hide_page(name: str):
    current_pages = get_pages(DEFAULT_PAGE)

    for key, val in current_pages.items():
        if val["page_name"] == name:
            del current_pages[key]
            _on_pages_changed.send()
            break


clear_all_but_first_page()


# Convert Pass into hash format
def make_hashes(password):
    return hashlib.sha256(str.encode(password)).hexdigest()


# Check password matches during login
def check_hashes(password, hashed_text):
    if make_hashes(password) == hashed_text:
        return hashed_text
    return False


# DB Management

conn = sqlite3.connect("user_data.db")
c = conn.cursor()


# DB Functions for create table
def create_usertable():
    c.execute(
        "CREATE TABLE IF NOT EXISTS userstable(username TEXT,email TEXT, password TEXT)"
    )


# Insert the data into table
def add_userdata(username, email, password):
    c.execute(
        "INSERT INTO userstable(username,email,password) VALUES (?,?,?)",
        (username, email, password),
    )
    conn.commit()


# Password and email fetch
def login_user(email, password):
    c.execute(
        "SELECT * FROM userstable WHERE email =? AND password = ?", (
            email, password)
    )
    data = c.fetchall()
    return data


def view_all_users():
    c.execute("SELECT * FROM userstable")
    data = c.fetchall()
    return data


if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False

img = Image.open("abresp.png")
#st.image(img, width=150)
img1 = Image.open("LIVE BETS.png")

# Main function


def main():
    # """Login page"""
    st.title("Welcome to Live Bet Calculators!")
    st.image(img1)
    menu = ["Login", "SignUp"]
    choice = st.selectbox(
        "Select Login or SignUp from dropdown box ▾",
        menu,
    )

    if choice == "":
        st.subheader("Login")
    elif choice == "Login":
        st.markdown(
            "<h10 style='text-align: left; color: #ffffff;'> If you do not have an account, create an accouunt by select SignUp option from above dropdown box.</h10>",
            unsafe_allow_html=True,
        )
        st.write("-------")
        st.subheader("Log in to your account")

        left_column, right_column = st.columns(2)
        with left_column:
            email = st.text_input("Email", placeholder="Enter your Email")
        with right_column:
            password = st.text_input(
            "Password", type="password", placeholder="Enter your password")

        if st.button("Login"):
            # if password == '12345':
            # Hash password creation and store in a table
            create_usertable()
            hashed_pswd = make_hashes(password)

            result = login_user(email, check_hashes(password, hashed_pswd))
            if result:
                st.session_state["logged_in"] = True

                st.success("Logged In as {}".format(email))

                if st.success:
                    st.subheader("User Profiles")
                    user_result = view_all_users()
                    clean_db = pd.DataFrame(
                        user_result, columns=["Username", "Email", "Password"]
                    )
                    st.dataframe(clean_db)
            else:
                st.warning("Incorrect Username/Password")
    elif choice == "SignUp":
        st.write("-----")
        st.subheader("Create New Account")
        
        left_column, middle_column, right_column = st.columns(3)
        with left_column:
            new_user = st.text_input("Username", placeholder="E.g. Steve Harris")
        with middle_column:
            new_user_email = st.text_input("Email", placeholder="Enter your Email")
        with right_column:
            new_password = st.text_input("Password (Must be 6 letters)", type="password", placeholder="Enter your Password")

        if st.button("Signup"):
            if len(new_password) < 6:
                st.error("Password must be atleast 6 letters")
            elif new_user == "":  # if user name empty then show the warnings
                st.warning("Inavlid user name")
            elif '@' not in new_user_email:
                st.warning("Inavlid user email")
            elif '.com' not in new_user_email:
                st.warning("Inavlid user email")
            elif new_user_email == "":  # if email empty then show the warnings
                st.warning("Invalid email id")
            elif new_password == "":  # if password empty then show the warnings
                st.warning("Invalid password")
            else:
                create_usertable()
                add_userdata(new_user, new_user_email,
                             make_hashes(new_password))
                st.success("Account created successfully")
                st.info("Go up and Login to your account")

    if st.session_state["logged_in"]:
        show_all_pages()
        hide_page(DEFAULT_PAGE.replace("auth.py", ""))
        switch_page(SECOND_PAGE_NAME)
    else:
        clear_all_but_first_page()


if __name__ == "__main__":
    main()

st.markdown("""
    <style>
    .css-184tjsw p{
        color: blue;
    }
    .css-1xarl3l{
        color: black;
    }

    [data-testid = "stAppViewContainer"] {
    background-image: url("https://static.vecteezy.com/system/resources/thumbnails/002/018/246/original/abstract-colorful-pastel-gradient-background-free-video.jpg");
    background-size: cover;
    }
    .css-tic8ca {
        background-color: white;
    }
    [data-baseweb = "popover"] {
        background-color: #fcc86d;
    }
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)
