# pytest -v -s --html=Reports/test_fos.html --self-contained-html PARTNER_ADMIN/TESTCASES/test_fos.py --browser Chrome
#  pytest -v -s PARTNER_ADMIN/TESTCASES/test_fos.py --browser Firefox
#  pytest -v -s PARTNER_ADMIN/TESTCASES/test_fos.py --browser Chrome

#import Statements
from HELPER.helper import HELPER
from PARTNER_ADMIN_WEB.PAGEOBJECTIVES.Fos import Fos

import pytest
import inspect
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

##Message validations In page
Field_missing_error_msg="//*[text()='This field is required']"
Mobile_validation_error_message_xpath="//*[text()='Maximum 10 numbers allowed']"
Email_validation_error_message_xpath="//*[text()='Email is not valid.']"



class Test_Add_FOS:

    @pytest.mark.sanity
    @pytest.mark.regression
    @pytest.mark.skip
    def test_Add_FOS_success(self,setup):
        self.driver = setup

        #ClassObjects
        self.FO=Fos(self.driver)

        ##ADD REGION
        REGION_ADDED = HELPER.Add_Region_success(self,setup)

        #Testcases Starts Here
        HELPER.Partner_login_success(self,setup)
        self.FO.Select_menu_item()
        self.FO.Click_Add_button()

        ##CREATE RANDOM NAME
        NAME = "Name_" + HELPER.random_generator(self)
        self.FO.Add_name(NAME)

        ##CREATE RANDOM NAME
        MOBILE = HELPER.random_generator_mobile_num(self)
        self.FO.Add_Mobile_num(MOBILE)

        ##CREATE RANDOM NAME
        EMAIL = "email" + HELPER.random_generator_4char(self)+"@metrictreelabs.com"
        self.FO.Add_Email(EMAIL)

        self.FO.Select_region(REGION_ADDED)
        self.FO.Click_Submit()

        ##Check FOS Added or not
        self.RE.Select_menu_item()
        Found=self.FO.Check_Fos_found(EMAIL)
        if Found==1:
            assert True
            self.driver.close()
        else:
            # To take the Screenshote
            FunName = inspect.currentframe().f_code.co_name
            HELPER.TAKE_SCREENSHOT(self, FunName)
            assert False


    @pytest.mark.regression
    @pytest.mark.skip
    def test_Add_FOS_fail_with_empty_data(self,setup):
        self.driver = setup

        #ClassObjects
        self.FO=Fos(self.driver)

        #Testcases Starts Here
        HELPER.Partner_login_success(self,setup)
        self.FO.Select_menu_item()
        self.FO.Click_Add_button()
        self.FO.Click_Submit()

        try:
            self.driver.find_element(By.XPATH, value= Field_missing_error_msg)
            assert True
            self.driver.close()
        except:
            # To take the Screenshote
                FunName = inspect.currentframe().f_code.co_name
                HELPER.TAKE_SCREENSHOT(self, FunName)
                assert False

    
    @pytest.mark.regression
    @pytest.mark.skip
    def test_Add_FOS_fail_with_invalid_mobile_num(self,setup):
        self.driver = setup

        #ClassObjects
        self.FO=Fos(self.driver)

        ##ADD REGION
        REGION_ADDED = HELPER.Add_Region_success(self,setup)

        #Testcases Starts Here
        HELPER.Partner_login_success(self,setup)
        self.FO.Select_menu_item()
        self.FO.Click_Add_button()

        ##CREATE RANDOM NAME
        NAME = "Name_" + HELPER.random_generator(self)
        self.FO.Add_name(NAME)

        ##CREATE RANDOM NAME
        MOBILE = HELPER.random_generator_mobile_num_12dig(self)
        self.FO.Add_Mobile_num(MOBILE)

        ##CREATE RANDOM NAME
        EMAIL = "email" + HELPER.random_generator_4char(self)+"@metrictreelabs.com"
        self.FO.Add_Email(EMAIL)

        self.FO.Select_region(REGION_ADDED)
        self.FO.Click_Submit()

        try:
            self.driver.find_element(By.XPATH, value= Mobile_validation_error_message_xpath)
            assert True
            self.driver.close()
        except:
            # To take the Screenshote
                FunName = inspect.currentframe().f_code.co_name
                HELPER.TAKE_SCREENSHOT(self, FunName)
                assert False


    @pytest.mark.regression
    @pytest.mark.skip
    def test_Add_FOS_fail_with_invalid_email_id(self,setup):
        self.driver = setup

        #ClassObjects
        self.FO=Fos(self.driver)

        ##ADD REGION
        REGION_ADDED = HELPER.Add_Region_success(self,setup)

        #Testcases Starts Here
        HELPER.Partner_login_success(self,setup)
        self.FO.Select_menu_item()
        self.FO.Click_Add_button()

        ##CREATE RANDOM NAME
        NAME = "Name_" + HELPER.random_generator(self)
        self.FO.Add_name(NAME)

        ##CREATE RANDOM NAME
        MOBILE = HELPER.random_generator_mobile_num(self)
        self.FO.Add_Mobile_num(MOBILE)

        ##CREATE RANDOM NAME
        EMAIL = "email" + HELPER.random_generator_4char(self)+"metrictreelabs.com"
        self.FO.Add_Email(EMAIL)

        self.FO.Select_region(REGION_ADDED)
        self.FO.Click_Submit()

        try:
            self.driver.find_element(By.XPATH, value= Email_validation_error_message_xpath)
            assert True
            self.driver.close()
        except:
            # To take the Screenshote
                FunName = inspect.currentframe().f_code.co_name
                HELPER.TAKE_SCREENSHOT(self, FunName)
                assert False


class Test_Edit_FOS:
    pass
