from selenium.webdriver.common.by import By

class Login:
    """PAGEOBJECTIVES"""

    USERNAME_TXT_XPATH="//input[@name='username']"
    PASSWORD_TXT_XPATH="//input[@name='password']"
    LOGIN_BTN_XPATH="//button[@type='submit']"
    BODY_XPATH="//body"
    FORGET_PASS_LINK_XPATH="//div//a[@id='forgot']"
    FORGET_PASSWORD_EMAIL_TXT_XPATH="//input[@name='email']"
    FORGET_PASSWORD_SUBMIT_BTN="//button[@type='submit']"


    "METHODS"
    def __init__(self,driver):
        self.driver=driver

    def Sent_username(self,username):
        self.driver.find_element(By.XPATH, value=self.USERNAME_TXT_XPATH).click()
        self.driver.find_element(By.XPATH, value=self.USERNAME_TXT_XPATH).send_keys(username)

    def Sent_password(self,password):
        self.driver.find_element(By.XPATH, value=self.PASSWORD_TXT_XPATH).click()
        self.driver.find_element(By.XPATH, value=self.PASSWORD_TXT_XPATH).send_keys(password)

    def Click_signin(self):
        self.driver.find_element(By.XPATH, value=self.LOGIN_BTN_XPATH).click()

    def Check_text_found(self,text):
        try:
            self.driver.find_element(By.XPATH, value=self.BODY_XPATH).contains("text")
            assert True
        except:
            assert False

    def Click_forget_link(self):
        self.driver.find_element(By.XPATH, value=self.FORGET_PASS_LINK_XPATH).click()

    def Submit_email(self,email):
        self.driver.find_element(By.XPATH, value=self.FORGET_PASSWORD_EMAIL_TXT_XPATH).click()
        self.driver.find_element(By.XPATH, value=self.FORGET_PASSWORD_EMAIL_TXT_XPATH).send_keys(email)
        self.driver.find_element(By.XPATH, value=self.FORGET_PASSWORD_SUBMIT_BTN).click()
