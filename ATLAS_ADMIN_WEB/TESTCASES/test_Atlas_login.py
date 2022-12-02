#  pytest -v -s --html=Reports/test_Login.html --self-contained-html ATLAS_ADMIN_WEB/TESTCASES/test_Atlas_login.py --browser Chrome
#  pytest -v -s ATLAS_ADATLAS_ADMIN_WEBMIN/TESTCASES/test_Atlas_login.py --browser Firefox
#  pytest -v -s ATLAS_ADMIN_WEB/TESTCASES/test_Atlas_login.py --browser Chrome

#import Statements
from ATLAS_ADMIN_WEB.PAGEOBJECTIVES.Atlas_Login import Login
from UTIL.readproperties import ReadConfig
from HELPER.helper import HELPER

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import pytest
import inspect

ATLAS_ADMIN_BASEURL = ReadConfig.get_ATLAS_ADMIN_BaseURL()
ATLAS_ADMIN_USERNAME = ReadConfig.get_ATLAS_ADMIN_USERNAME()
ATLAS_ADMIN_EMAIL=ReadConfig.get_ATLAS_ADMIN_EMAIL()
ATLAS_ADMIN_PASSWORD = ReadConfig.get_ATLAS_ADMIN_PASSWORD()
PARTNER_ADMIN_USERNAME = ReadConfig.get_PARTNER_ADMIN_USERNAME()
PARTNER_ADMIN_PASSWORD = ReadConfig.get_PARTNER_ADMIN_PASSWORD()
PARTNER_ADMIN_EMAIL=ReadConfig.get_PARTNER_ADMIN_EMAIL()
FOS_USER_ID = ReadConfig.get_FOS_USER_ID()
FOS_USER_PASSWORD = ReadConfig.get_FOS_USER_PASSWORD()
CUSTOMER_USER_ID = ReadConfig.get_CUSTOMER_USER_ID()
CUSTOMER_USER_PASSWORD = ReadConfig.get_CUSTOMER_USER_PASSWORD()


ATLAS_ADMIN_Login_success_EXPECTED_URL=ReadConfig.get_ATLAS_ADMIN_Login_success_EXPECTED_URL()
ATLAS_ADMIN_Forget_Password_Diection_URL=ReadConfig.get_ATLAS_ADMIN_Forgetpassword_URL()

#Texts
Atlas_Invalid_login_msg1_XPATH="//*[text()='This field is required']"
Atlas_Invalid_login_msg2_XPATH="//*[text()='Username is not found. Invalid login credentials.']"

class Test_login:

    @pytest.mark.run(order=1)
    @pytest.mark.sanity
    @pytest.mark.regression
    def test_Atlas_login_success(self,setup):
        self.driver = setup
        self.driver.get(ATLAS_ADMIN_BASEURL)
        #ClassObjects
        self.LO=Login(self.driver)

        #Testcases Starts Here

        self.LO.Sent_username(ATLAS_ADMIN_USERNAME)
        self.LO.Sent_password(ATLAS_ADMIN_PASSWORD)
        self.LO.Click_signin()

        try:
            WebDriverWait(self.driver, 10).until(EC.url_to_be(ATLAS_ADMIN_Login_success_EXPECTED_URL))  # Wait for the next page to load
            self.driver.close()
            assert True
        except:
            # To take the Screenshote
            FunName = inspect.currentframe().f_code.co_name
            HELPER.TAKE_SCREENSHOT(self, FunName)
            assert False





    @pytest.mark.run(order=2)
    @pytest.mark.regression
    def test_Atlas_login_failed_with_no_input(self,setup):
        self.driver = setup
        self.driver.get(ATLAS_ADMIN_BASEURL)
        #ClassObjects
        self.LO=Login(self.driver)

        #Testcases Starts Here

        self.LO.Sent_username("")
        self.LO.Sent_password("")
        self.LO.Click_signin()

        try:
            self.driver.find_element(By.XPATH, value= Atlas_Invalid_login_msg1_XPATH )
            try:
                WebDriverWait(self.driver, 5).until(EC.url_to_be(ATLAS_ADMIN_Login_success_EXPECTED_URL))  # Wait for the next page to load
                # To take the Screenshote
                FunName = inspect.currentframe().f_code.co_name
                HELPER.TAKE_SCREENSHOT(self, FunName)
                assert False
            except:
                self.driver.close()
                assert True
        except:
            # To take the Screenshote
            FunName = inspect.currentframe().f_code.co_name
            HELPER.TAKE_SCREENSHOT(self, FunName)
            assert False





    @pytest.mark.run(order=3)
    @pytest.mark.regression
    def test_Atlas_login_failed_with_no_negative_input(self,setup):
        self.driver = setup
        self.driver.get(ATLAS_ADMIN_BASEURL)
        #ClassObjects
        self.LO=Login(self.driver)

        #Testcases Starts Here

        self.LO.Sent_username("uygfy")
        self.LO.Sent_password("wukehfiue")
        self.LO.Click_signin()

        try:
            self.driver.find_element(By.XPATH, value= Atlas_Invalid_login_msg2_XPATH)
            try:
                WebDriverWait(self.driver, 5).until(EC.url_to_be(ATLAS_ADMIN_Login_success_EXPECTED_URL))  # Wait for the next page to load
                # To take the Screenshote
                FunName = inspect.currentframe().f_code.co_name
                HELPER.TAKE_SCREENSHOT(self, FunName)
                assert False
            except:
                self.driver.close()
                assert True
        except:
            # To take the Screenshote
            FunName = inspect.currentframe().f_code.co_name
            HELPER.TAKE_SCREENSHOT(self, FunName)
            assert False





    @pytest.mark.run(order=4)
    @pytest.mark.regression
    def test_Atlas_login_failed_with_credentials_of_PARTNER_ADMIN(self,setup):
        self.driver = setup
        self.driver.get(ATLAS_ADMIN_BASEURL)
        #ClassObjects
        self.LO=Login(self.driver)

        #Testcases Starts Here

        self.LO.Sent_username(PARTNER_ADMIN_USERNAME)
        self.LO.Sent_password(PARTNER_ADMIN_PASSWORD)
        self.LO.Click_signin()

        try:
            self.driver.find_element(By.XPATH, value= Atlas_Invalid_login_msg2_XPATH)
            try:
                WebDriverWait(self.driver, 5).until(EC.url_to_be(ATLAS_ADMIN_Login_success_EXPECTED_URL))  # Wait for the next page to load
                # To take the Screenshote
                FunName = inspect.currentframe().f_code.co_name
                HELPER.TAKE_SCREENSHOT(self, FunName)
                assert False
            except:
                self.driver.close()
                assert True
        except:
            # To take the Screenshote
            FunName = inspect.currentframe().f_code.co_name
            HELPER.TAKE_SCREENSHOT(self, FunName)
            assert False





    @pytest.mark.run(order=5)
    @pytest.mark.regression
    @pytest.mark.skip
    def test_Atlas_login_failed_with_credentials_of_FOS(self,setup):
        self.driver = setup
        self.driver.get(ATLAS_ADMIN_BASEURL)
        #ClassObjects
        self.LO=Login(self.driver)

        #Testcases Starts Here

        self.LO.Sent_username(FOS_USER_ID)
        self.LO.Sent_password(FOS_USER_PASSWORD)
        self.LO.Click_signin()

        try:
            self.driver.find_element(By.XPATH, value= Atlas_Invalid_login_msg2_XPATH)
            try:
                WebDriverWait(self.driver, 5).until(EC.url_to_be(ATLAS_ADMIN_Login_success_EXPECTED_URL))  # Wait for the next page to load
                # To take the Screenshote
                FunName = inspect.currentframe().f_code.co_name
                HELPER.TAKE_SCREENSHOT(self, FunName)
                assert False
            except:
                self.driver.close()
                assert True
        except:
            # To take the Screenshote
            FunName = inspect.currentframe().f_code.co_name
            HELPER.TAKE_SCREENSHOT(self, FunName)
            assert False





    @pytest.mark.run(order=6)
    @pytest.mark.regression
    @pytest.mark.skip
    def test_Atlas_login_failed_with_credentials_of_Customer(self,setup):
        self.driver = setup
        self.driver.get(ATLAS_ADMIN_BASEURL)
        #ClassObjects
        self.LO=Login(self.driver)

        #Testcases Starts Here

        self.LO.Sent_username(CUSTOMER_USER_ID)
        self.LO.Sent_password(CUSTOMER_USER_PASSWORD)
        self.LO.Click_signin()

        try:
            self.driver.find_element(By.XPATH, value= Atlas_Invalid_login_msg2_XPATH)
            try:
                WebDriverWait(self.driver, 5).until(EC.url_to_be(ATLAS_ADMIN_Login_success_EXPECTED_URL))  # Wait for the next page to load
                # To take the Screenshote
                FunName = inspect.currentframe().f_code.co_name
                HELPER.TAKE_SCREENSHOT(self, FunName)
                assert False
            except:
                self.driver.close()
                assert True
        except:
            # To take the Screenshote
            FunName = inspect.currentframe().f_code.co_name
            HELPER.TAKE_SCREENSHOT(self, FunName)
            assert False



class Test_forget_password:

    @pytest.mark.run(order=14)
    @pytest.mark.regression
    def test_Atlas_Forget_password_success(self,setup):
        self.driver = setup
        self.driver.get(ATLAS_ADMIN_BASEURL)
        #ClassObjects
        self.LO=Login(self.driver)

        #Testcases Starts Here
        self.LO.Click_forget_link()
        try:
            WebDriverWait(self.driver, 5).until(EC.url_to_be(ATLAS_ADMIN_Forget_Password_Diection_URL))  # Wait for the next page to load
            self.LO.Submit_email(ATLAS_ADMIN_EMAIL)
            self.driver.close()
            assert True
        except:
            # To take the Screenshote
            FunName = inspect.currentframe().f_code.co_name
            HELPER.TAKE_SCREENSHOT(self, FunName)
            assert False
            
