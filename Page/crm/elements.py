from selenium.webdriver.common.by import By

BASE_URL = "https://qcloud-passport-rd.jiediankeji.com"


class LoginPageElements:
    # 页面地址
    url = BASE_URL + "/stark/auth?from=crm"

    # 页面元素
    email = (By.ID, "email")
    password = (By.ID, "password")
    code = (By.ID, "code")
    submit = (By.XPATH, '//*[@id="root"]/div/div/div[2]/div[2]/div/form/div[4]/div/div/span/button/span')


class HomePageElements:
    # 页面地址
    url = BASE_URL + "/stark/crm/home"

    # 页面元素
    ankerbox = (By.XPATH, '//*[@id="root"]/div/div/div/section/section/header[2]/div/div[2]/div/button/span')
