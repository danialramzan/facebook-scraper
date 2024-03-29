# Importing selenium and the necessary options options to login to FB
from selenium import webdriver
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
# from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

# Importing time libraries to add wait times

# Importing beautiful soup to read the page html source code

# To create csv file where we'll scrape the content

# We'll also add the options functionality to disable notifications

# chrome_options = Options()
firefox_options = Options()
# Disable notifications
# chrome_options.add_argument("--disable-notifications")
# git test line
# git test line2


profile_path = '/home/danialramzan/snap/firefox/common/.mozilla/firefox/NOOOOOOOOOOOOO'

firefox_options.add_argument("--disable-notifications")

firefox_options.add_argument("-profile")
firefox_options.add_argument(profile_path)

content_list = []
time_list = []
name_list = []

service = Service(GeckoDriverManager().install())
firefox_profile = FirefoxProfile()

# driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)

driver = webdriver.Firefox(service=service, options=firefox_options)
# driver = webdriver.Firefox(service=GeckoDriverManager().install(), options = firefox_options)
driver.get("https://www.facebook.com")
driver.maximize_window()

# sleep(2)
#
# # Accept cookies
# cookies = WebDriverWait(driver, 30).until(
#     EC.element_to_be_clickable((By.XPATH, '//button[@class="_42ft _4jy0 _9o-t _4jy3 _4jy1 selected _51sy"]')))
# cookies.click()
#
# email = driver.find_element_by_id("email")
# email.send_keys("YOUR_EMAIL_HERE")  # replace YOUR_EMAIL_HERE with your email
# password = driver.find_element_by_id("pass")
# password.send_keys("YOUR_PASSWORD_HERE")  # replace YOUR_PASSWORD_HERE with your password
# sleep(1)
# login = driver.find_element_by_name("login")
# login.click()
# sleep(2)
# driver.get("https://www.facebook.com/groups/YOUR_GROUP_HERE")  # replace YOUR_GROUP_HERE with your group
# sleep(4)
#
# while True:
#     soup = BeautifulSoup(driver.page_source, "html.parser")
#     all_posts = soup.find_all("div", {"class": "du4w35lb k4urcfbm l9j0dhe7 sjgh65i0"})
#     for post in all_posts:
#         try:
#             name = post.find("a", {
#                 "class": "oajrlxb2 gs5ia77u qu0x051f esr5mh6w e9989ue4 r7d6kgcz rq0escxv nhd2j8a9 alzwoclg mc1re8zz eojpzvty tkr6xdv7"})
#         except:
#             name = "not found"
#         print(name)
#         try:
#             content = post.find("span", {"class": "d2edcug0 hpfvmrgz qv66sw1b c1et5uql o1r32d6d ik7dh3pa hts83030"})
#         except:
#             content = "not found"
#         print(content)
#         try:
#             time = post.find("a", {"class": "oajrlxb2 gs5ia77u qu0x051f esr5mh6w e9989ue4 r7d6kgcz rq0escxv nhd2j8a9"})
#             print(time)
#         except:
#             time = "not found"
#
#         content_list.append(content)
#         time_list.append(time)
#         name_list.append(name)
#
#     df = pd.DataFrame({"name": name_list, "content": content_list, "time": time_list})
#     df.drop_duplicates(subset="content", keep="first", inplace=True)
#     df.to_csv("facebook_data2.csv")
#
#     if df.shape[0] > 10:
#         break
#
#     sleep(5)
#     y = 500
#     for timer in range(0, 25):
#         driver.execute_script("window.scrollTo(0, " + str(y) + ")")
#         y += 500
#         sleep(3)
