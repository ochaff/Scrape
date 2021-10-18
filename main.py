# Importations
from selenium import webdriver
import json
import time
# Definition des fonctions


def login(cred):
    driver.get(url)
    try:
        time.sleep(2)
        cookies = driver.find_element_by_xpath(
            "/html/body/div/main/div[1]/div/section/div/div[2]/button[2]")
        cookies.click()
        time.sleep(1)
    except:
        pass
    username = driver.find_element_by_id("username")
    password = driver.find_element_by_id("password")
    login_button = driver.find_element_by_xpath(
        "/html/body/div/main/div[2]/div[1]/form/div[3]/button")
    username.send_keys(cred['username'])
    password.send_keys(cred['password'])
    login_button.click()
    time.sleep(2)
    close_message = driver.find_element_by_xpath(
        "/html/body/div[6]/aside/div[1]/header/section[2]/button[2]")
    close_message.click()

    return None


def reshare():
    button = driver.find_elements_by_css_selector("[aria-label='']")
    i = 0
    while i < len(button):
        button[i].click()
        time.sleep(1)
        post = driver.find_element_by_xpath(
            "/html/body/div[3]/div/div/div[2]/div/div/div[2]/div[2]/div[3]/button")
        post.click()
        time.sleep(1)
        try:
            error = driver.find_element_by_xpath(
                "/html/body/div[1]/section/ul/li/button")
            error.click()
            time.sleep(1)
            close = driver.find_element_by_xpath(
                "/html/body/div[3]/div/div/button")
            close.click()
            time.sleep(1)
            close2 = driver.find_element_by_xpath(
                "/html/body/div[3]/div[2]/div/div[3]/button[2]")
            close2.click()
            time.sleep(1)
        except:
            break
        i += 1
    return None

# Main code


if __name__ == "__main__":
    url = 'https://www.linkedin.com/uas/login?session_redirect=https%3A%2F%2Fwww%2Elinkedin%2Ecom%2Ffeed%2F&fromSignIn=true&trk=cold_join_sign_in'
    driver = webdriver.Chrome()
    with open('credentials.json') as f:
        cred = json.load(f)
    login(cred)
    reshare()
