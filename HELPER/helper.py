#import Statements

from PARTNER_ADMIN_WEB.PAGEOBJECTIVES.Partner_Login import Login
from ATLAS_ADMIN_WEB.PAGEOBJECTIVES.Atlas_Login import Login
from PARTNER_ADMIN_WEB.PAGEOBJECTIVES.Region import Region
from PARTNER_ADMIN_WEB.PAGEOBJECTIVES.Fos import Fos
from UTIL.readproperties import ReadConfig

import datetime
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import pytest
import inspect
import string
import random


"""CONFIGURATIONS"""
PARTNER_ADMIN_BASEURL = ReadConfig.get_PARTNER_ADMIN_BASEURL()
PARTNER_ADMIN_USERNAME = ReadConfig.get_PARTNER_ADMIN_USERNAME()
PARTNER_ADMIN_PASSWORD = ReadConfig.get_PARTNER_ADMIN_PASSWORD()
ATLAS_ADMIN_BASEURL = ReadConfig.get_ATLAS_ADMIN_BaseURL()
ATLAS_ADMIN_EMAIL=ReadConfig.get_ATLAS_ADMIN_EMAIL()
ATLAS_ADMIN_USERNAME = ReadConfig.get_ATLAS_ADMIN_USERNAME()
ATLAS_ADMIN_PASSWORD = ReadConfig.get_ATLAS_ADMIN_PASSWORD()
PARTNER_ADMIN_EMAIL=ReadConfig.get_PARTNER_ADMIN_EMAIL()
FOS_USER_ID = ReadConfig.get_FOS_USER_ID()
FOS_USER_PASSWORD = ReadConfig.get_FOS_USER_PASSWORD()
CUSTOMER_USER_ID = ReadConfig.get_CUSTOMER_USER_ID()
CUSTOMER_USER_PASSWORD = ReadConfig.get_CUSTOMER_USER_PASSWORD()

PARTNER_ADMIN_Login_success_EXPECTED_URL=ReadConfig.get_PARTNER_ADMIN_Login_success_EXPECTED_URL()
PARTNER_ADMIN_Forget_Password_Diection_URL=ReadConfig.get_PARTNER_ADMIN_Forgetpassword_URL()
ATLAS_ADMIN_Login_success_EXPECTED_URL=ReadConfig.get_ATLAS_ADMIN_Login_success_EXPECTED_URL()
ATLAS_ADMIN_Forget_Password_Diection_URL=ReadConfig.get_ATLAS_ADMIN_Forgetpassword_URL()


class HELPER:

    @staticmethod
    def TAKE_SCREENSHOT(self,Methodname):
        # To take the Screenshot
        now = datetime.datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        #date_stamp = str(datetime.dat
        # etime.now()).split('//')[1].split('.')[0]
        filename = "NBFC_"+dt_string
        self.driver.save_screenshot("C:/Users/NITHIN/PycharmProjects/NBFC/Screenshots/"+Methodname+".png")

    @staticmethod
    def random_generator(size=7, chars=string.ascii_uppercase):
        return ''.join(random.choice(chars) for x in range(7))

    @staticmethod
    def random_generator_10char(size=10, chars=string.ascii_uppercase):
        return ''.join(random.choice(chars) for x in range(10))

    @staticmethod
    def random_generator_4char(size=4, chars=string.ascii_uppercase):
        return ''.join(random.choice(chars) for x in range(4))

    @staticmethod
    def random_generator_mobile_num(size=10, chars=string.digits):
        return ''.join(random.choice(chars) for x in range(10))

    @staticmethod
    def random_generator_mobile_num_12dig(size=12, chars=string.digits):
        return ''.join(random.choice(chars) for x in range(12))

    #Partner Login
    @staticmethod
    def Partner_login_success(self,setup):
        self.driver = setup
        self.driver.get(PARTNER_ADMIN_BASEURL)
        #ClassObjects
        self.LO=Login(self.driver)

        #Testcases Starts Here

        self.LO.Sent_username(PARTNER_ADMIN_USERNAME)
        self.LO.Sent_password(PARTNER_ADMIN_PASSWORD)
        self.LO.Click_signin()

        try:
            WebDriverWait(self.driver, 10).until(EC.url_to_be(PARTNER_ADMIN_Login_success_EXPECTED_URL))  # Wait for the next page to load

        except:
            # To take the Screenshote
            FunName = inspect.currentframe().f_code.co_name
            HELPER.TAKE_SCREENSHOT(self, FunName)
            assert False
    
    #Atlas Login
    @staticmethod
    def Atlas_login_success(self,setup):
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
        except:
            # To take the Screenshote
            FunName = inspect.currentframe().f_code.co_name
            HELPER.TAKE_SCREENSHOT(self, FunName)
            assert False

    

    #Add Region
    @staticmethod
    def Add_Region_success(self,setup):
        self.driver = setup

        #ClassObjects
        self.RE=Region(self.driver)

        #Testcases Starts Here
        HELPER.Partner_login_success(self,setup)
        self.RE.Select_menu_item()
        self.RE.Click_Add_button()
        self.RE.Click_on_sate()
        self.RE.Select_State("Kerala")

        #Create a Random Region Name
        Region_Name = "REG_" + HELPER.random_generator(self)
        self.RE.Enter_Region_name(Region_Name)
        self.RE.Click_Submit()

        #Verify Region Added OR Not
        self.RE.Select_menu_item()
        Found=self.RE.Check_Region_found(Region_Name)
        if Found==1:
            #self.driver.close()
            return Region_Name
        else:
            # To take the Screenshote
            FunName = inspect.currentframe().f_code.co_name
            HELPER.TAKE_SCREENSHOT(self, FunName)
            assert False


    #Add FOS
    @staticmethod
    def Add_FOS_success(self,setup):
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
            return EMAIL
            self.driver.close()
        else:
            # To take the Screenshote
            FunName = inspect.currentframe().f_code.co_name
            HELPER.TAKE_SCREENSHOT(self, FunName)
            assert False