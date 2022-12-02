#  pytest -v -s --html=Reports/test_region.html --self-contained-html PARTNER_ADMIN/TESTCASES/test_region.py --browser Chrome
#  pytest -v -s PARTNER_ADMIN/TESTCASES/test_region.py --browser Firefox
#  pytest -v -s PARTNER_ADMIN/TESTCASES/test_region.py --browser Chrome

#import Statements
from HELPER.helper import HELPER
from PARTNER_ADMIN_WEB.PAGEOBJECTIVES.Region import Region

import pytest
import inspect
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep


##Message validations In page
Region_already_present_error_msg="//*[text()='region name is already taken.']"
Field_missing_error_msg="//*[text()='This field is required']"
Duplicate_data_error_msg="//*[text()='Duplicate entry']"
Null_data_in_table_error_msg="//*[text()='No Data to Show']"



class Test_Add_region:
    
    @pytest.mark.sanity
    @pytest.mark.regression
    @pytest.mark.skip
    def test_Add_Region_success(self,setup):
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
            assert True
            self.driver.close()
        else:
            # To take the Screenshote
            FunName = inspect.currentframe().f_code.co_name
            HELPER.TAKE_SCREENSHOT(self, FunName)
            assert False


    @pytest.mark.regression
    @pytest.mark.skip
    def test_Add_Region_Fail_with_already_present_Region(self,setup):
        
        self.driver = setup
        #ClassObjects
        self.RE=Region(self.driver)

        #Testcases Starts Here
        REGION_ADDED = HELPER.Add_Region_success(self,setup)

        HELPER.Partner_login_success(self,setup)
        self.RE.Select_menu_item()
        self.RE.Click_Add_button()
        self.RE.Click_on_sate()
        self.RE.Select_State("Kerala")

        #Add Already added region
        self.RE.Enter_Region_name(REGION_ADDED)
        self.RE.Click_Submit()

        try:
            self.driver.find_element(By.XPATH, value= Region_already_present_error_msg)
            assert True
            self.driver.close()
        except:
            # To take the Screenshote
                FunName = inspect.currentframe().f_code.co_name
                HELPER.TAKE_SCREENSHOT(self, FunName)
                assert False


    @pytest.mark.regression
    @pytest.mark.skip
    def test_Add_Region_Fail_with_No_values(self,setup):
        self.driver = setup

        #ClassObjects
        self.RE=Region(self.driver)

        #Testcases Starts Here
        HELPER.Partner_login_success(self,setup)
        self.RE.Select_menu_item()
        self.RE.Click_Add_button()

        self.RE.Click_Submit()

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
    def test_Add_Region_Fail_with_No_state_selected(self,setup):
        self.driver = setup

        #ClassObjects
        self.RE=Region(self.driver)

        #Testcases Starts Here
        HELPER.Partner_login_success(self,setup)
        self.RE.Select_menu_item()
        self.RE.Click_Add_button()


        #Create a Random Region Name
        Region_Name = "REG_" + HELPER.random_generator(self)
        self.RE.Enter_Region_name(Region_Name)
        self.RE.Click_Submit()

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
    def test_Add_Region_Fail_with_No_Region_Entered(self,setup):
        self.driver = setup

        #ClassObjects
        self.RE=Region(self.driver)

        #Testcases Starts Here
        HELPER.Partner_login_success(self,setup)
        self.RE.Select_menu_item()
        self.RE.Click_Add_button()
        self.RE.Click_on_sate()
        self.RE.Select_State("Kerala")

        self.RE.Click_Submit()

        try:
            self.driver.find_element(By.XPATH, value= Field_missing_error_msg)
            assert True
            self.driver.close()
        except:
            # To take the Screenshote
                FunName = inspect.currentframe().f_code.co_name
                HELPER.TAKE_SCREENSHOT(self, FunName)
                assert False


class Test_Edit_region:

    @pytest.mark.regression
    @pytest.mark.skip
    def test_Edit_Region_success(self,setup):
        self.driver = setup
        #ClassObjects
        self.RE=Region(self.driver)

        #Testcases Starts Here
        REGION_ADDED = HELPER.Add_Region_success(self,setup)

        HELPER.Partner_login_success(self,setup)
        self.RE.Select_menu_item()
        #Click on the edit button of already added region
        self.RE.Edit_Region_btn_click(REGION_ADDED)

        #Create a new Random Region Name
        New_Region_Name = "REG_" + HELPER.random_generator(self)
        self.RE.Enter_Region_name(New_Region_Name)

        self.RE.Click_Submit()

        #Verify previouse Region present OR Not
        self.RE.Select_menu_item()
        Found=self.RE.Check_Region_found(REGION_ADDED)
        if Found==1:
            # To take the Screenshote
            FunName = inspect.currentframe().f_code.co_name
            HELPER.TAKE_SCREENSHOT(self, FunName)
            assert False
        else:
            #Verify New Region Added OR Not
            self.RE.Select_menu_item()
            self.driver.refresh()
            Found1=self.RE.Check_Region_found(New_Region_Name)
            if Found1==1:
                assert True
                self.driver.close()
            else:
                # To take the Screenshote
                FunName = inspect.currentframe().f_code.co_name
                HELPER.TAKE_SCREENSHOT(self, FunName)
                assert False

    @pytest.mark.regression
    @pytest.mark.skip
    def test_Edit_Region_fail_with_no_data(self,setup):
        self.driver = setup
        #ClassObjects
        self.RE=Region(self.driver)

        #Testcases Starts Here
        REGION_ADDED = HELPER.Add_Region_success(self,setup)

        HELPER.Partner_login_success(self,setup)
        self.RE.Select_menu_item()
        #Click on the edit button of already added region
        self.RE.Edit_Region_btn_click(REGION_ADDED)

        #Submit Region with no data
        self.RE.Enter_Region_name("")

        self.RE.Click_Submit()

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
    def test_Edit_Region_with_already_present_data(self,setup):
        self.driver = setup
        #ClassObjects
        self.RE=Region(self.driver)

        #Testcases Starts Here
        REGION_ADDED = HELPER.Add_Region_success(self,setup)
        #Add another region
        REGION_ADDED1 = HELPER.Add_Region_success(self,setup)

        HELPER.Partner_login_success(self,setup)
        self.RE.Select_menu_item()
        #Click on the edit button of already added region
        self.RE.Edit_Region_btn_click(REGION_ADDED)

        #Create a new Random Region Name
        self.RE.Enter_Region_name(REGION_ADDED1)

        self.RE.Click_Submit()

        try:
            self.driver.find_element(By.XPATH, value= "//*[text()='Duplicate entry, "+REGION_ADDED1+" is already exists']")
            assert True
            self.driver.close()
        except:
            # To take the Screenshote
            FunName = inspect.currentframe().f_code.co_name
            HELPER.TAKE_SCREENSHOT(self, FunName)
            assert False



class Test_Search:
    @pytest.mark.regression
    @pytest.mark.skip
    def test_search_data_success(self,setup):
        self.driver=setup

        #classObject
        self.RE=Region(self.driver)

        #Testcases Starts Here
        REGION_ADDED = HELPER.Add_Region_success(self,setup)

        HELPER.Partner_login_success(self,setup)
        self.RE.Select_menu_item()
        self.RE.Search_data(REGION_ADDED)

        #cHECK IF SEARCH FOUND
        Data_found = self.RE.Search_data_found(REGION_ADDED)

        if Data_found==1:
            assert True
            self.driver.close()
        else:
            # To take the Screenshote
            FunName = inspect.currentframe().f_code.co_name
            HELPER.TAKE_SCREENSHOT(self, FunName)
            assert False

    @pytest.mark.regression
    #@pytest.mark.skip
    def test_search_data_fail(self,setup):
        self.driver=setup

        #classObject
        self.RE=Region(self.driver)

        Dummy_region = "REG_" + HELPER.random_generator_10char(self)

        HELPER.Partner_login_success(self,setup)
        self.RE.Select_menu_item()
        self.RE.Search_data(Dummy_region)

        try:
            self.driver.find_element(By.XPATH, value= Null_data_in_table_error_msg)
            assert True
            self.driver.close()
        except:
            # To take the Screenshote
                FunName = inspect.currentframe().f_code.co_name
                HELPER.TAKE_SCREENSHOT(self, FunName)
                assert False


