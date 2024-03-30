from selenium import webdriver
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from dotenv import load_dotenv
from time import sleep
from bs4 import BeautifulSoup
import pandas as pd
import os

# get info from dotenv file
profile_path = os.getenv('FIREFOX_PROFILE_PATH')
facebook_group_url = os.getenv('FACEBOOK_GROUP_URL') + '?sorting_setting=CHRONOLOGICAL'

# css class names
all_post_classnames = os.getenv('ALL_POST_CLASSNAMES')
all_names_classname = os.getenv('ALL_NAMES_CLASSNAME')
all_content_classname = os.getenv('ALL_CONTENT_CLASSNAME')
all_timestamps_classname = os.getenv('ALL_TIMESTAMPS_CLASSNAME')

# firefox driver options: disable notifs, path to profile to use
firefox_options = Options()
firefox_options.add_argument("--disable-notifications")
firefox_options.add_argument("-profile")
firefox_options.add_argument(profile_path)

content_list = []
time_list = []
name_list = []

service = Service(GeckoDriverManager().install())
firefox_profile = FirefoxProfile()

driver = webdriver.Firefox(service=service, options=firefox_options)
driver.get(facebook_group_url)
driver.maximize_window()


# give time for page to load
sleep(2)

while True:
    soup = BeautifulSoup(driver.page_source, "html.parser")
    all_posts = soup.find_all("div", {"class": all_post_classnames})
    for post in all_posts:
        try:
            name = post.find("a", {
                "class": all_names_classname}).get_text()
        except:
            name = "not found"
        print(name)
        try:
            name = post.find("a", {
                "class": all_names_classname}).get_text()
        except:
            name = "not found"
        print(name)
        try:
            content = post.find("span", {
                "class": all_content_classname}).get_text()
        except:
            content = "not found"
        print(content)
        try:
            time = post.find("a", {
                "class": all_timestamps_classname}).get_text()
            print(time)
        except:
            time = "not found"

        content_list.append(content)
        time_list.append(time)
        name_list.append(name)

    df = pd.DataFrame({"name": name_list, "content": content_list, "time": time_list})
    df.drop_duplicates(subset="content", keep="first", inplace=True)
    df.to_csv("facebook_data.csv")

    if df.shape[0] > 10:
        break

    sleep(2)
    y = 500
    for timer in range(0, 5):
        driver.execute_script("window.scrollTo(0, " + str(y) + ")")
        y += 500
        sleep(3)
