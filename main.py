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
    all_posts = soup.find_all("div", {"class": "x1yztbdb x1n2onr6 xh8yej3 x1ja2u2z"})
    for post in all_posts:
        try:
            name = post.find("a", {
                "class": "x1i10hfl xjbqb8w x1ejq31n xd10rxx x1sy0etr x17r0tee x972fbf xcfux6l x1qhh985 xm0m39n x9f619 x1ypdohk xt0psk2 xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x16tdsg8 x1hl2dhg xggy1nq x1a2a7pz xt0b8zv xzsf02u x1s688f"})
        except:
            name = "not found"
        print(name)
        try:
            content = post.find("span", {"class": "x193iq5w xeuugli x13faqbe x1vvkbs x10flsy6 x1lliihq x1s928wv xhkezso x1gmr53x x1cpjm7i x1fgarty x1943h6x x4zkp8e x41vudc x6prxxf xvq8zen xo1l8bm xzsf02u"})
        except:
            content = "not found"
        print(content)
        try:
            time = post.find("a", {"class": "x193iq5w xeuugli x13faqbe x1vvkbs x10flsy6 x1lliihq x1s928wv xhkezso x1gmr53x x1cpjm7i x1fgarty x1943h6x x4zkp8e x41vudc x6prxxf xvq8zen xo1l8bm xzsf02u"})
            print(time)
        except:
            time = "not found"

        content_list.append(content)
        time_list.append(time)
        name_list.append(name)

    df = pd.DataFrame({"name": name_list, "content": content_list, "time": time_list})
    df.drop_duplicates(subset="content", keep="first", inplace=True)
    df.to_csv("facebook_data2.csv")

    if df.shape[0] > 10:
        break

    sleep(2)
    y = 500
    for timer in range(0, 5):
        driver.execute_script("window.scrollTo(0, " + str(y) + ")")
        y += 500
        sleep(3)
