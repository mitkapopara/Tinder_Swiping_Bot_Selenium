from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
from selenium.webdriver.common.keys import Keys
import time

FB_EMAIL = "mitp9090@gmail.com"
FB_PASSWORD = "jack@2050"

service = Service("C:/Users/meet/Desktop/Development/chromedriver.exe")
driver = webdriver.Chrome(service=service)
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)

driver.get("https://tinder.com/app/recs")

log_in = driver.find_element(by="xpath", value='//*[@id="u490315748"]/div/div[1]/div/main/div['
                                               '1]/div/div/div/div/header/div/div[2]/div[2]/a/div[2]/div[2]')
log_in.click()
time.sleep(1)
facebook_log_in = driver.find_element(by="xpath", value='//*[@id="u-1238065328"]/main/div[1]/div/div[1]/div/div/div['
                                                        '2]/div[2]/span/div[2]/button/div[2]/div[2]/div/div')
facebook_log_in.click()
time.sleep(2)

base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)
print(driver.title)

# Login and hit enter
email = driver.find_element(by="xpath", value='//*[@id="email"]')
password = driver.find_element(by="xpath", value='//*[@id="pass"]')
email.send_keys(FB_EMAIL)
password.send_keys(FB_PASSWORD)
password.send_keys(Keys.ENTER)

# Switch back to Tinder window
driver.switch_to.window(base_window)
print(driver.title)
time.sleep(5)

allow_cookies = driver.find_element(by="xpath", value='//*[@id="u-1238065328"]/main/div[2]/div/div/div[1]/div['
                                                      '1]/button/div[2]/div[2]')
allow_cookies.click()
time.sleep(3)
allow_location = driver.find_element(by="xpath", value='//*[@id="u-1238065328"]/main/div[1]/div/div/div[3]/button['
                                                       '1]/div[2]/div[2]')
allow_location.click()
time.sleep(3)
notification_disable = driver.find_element(by="xpath",
                                           value='//*[@id="u-1238065328"]/main/div/div/div/div[3]/button[2]/div['
                                                 '2]/div[2]')
notification_disable.click()

# Tinder free tier only allows 100 "Likes" per day. If you have a premium account, feel free to change to a while loop.
for n in range(100):

    # Add 2 second delay between likes
    time.sleep(3)

    try:
        print("called")
        body = driver.find_element(by="css selector", value="body")
        body.send_keys(Keys.LEFT)

    # Catches the cases where there is a "Matched" pop-up in front of the "Like" button:
    except ElementClickInterceptedException:
        try:
            match_popup = driver.find_element(by="css selector", value=".itsAMatch a")
            match_popup.click()

        # Catches the cases where the "Like" button has not yet loaded, so wait 2 seconds before retrying.
        except NoSuchElementException:
            time.sleep(2)

driver.quit()
