from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.keys import Keys

class Region:
    """PAGEOBJECTIVES"""
    REGION_MENUITEM_XPATH="//div[@class='sidebar-parent']//li[@class='pro-menu-item'][2]//span[@class='pro-item-content']"
    ADD_NEW_BTN_XPATH="//button[@type='button']/span[@class='MuiButton-label']"
    STATE_MENUBAR_XPATH="//div[@id='demo-simple-select']"
    STATES_XPATH="//ul[@role='listbox']/li"
    NAME_TXT_XPATH="//input[@id='myInput'][@name='name']"
    SUBMIT_BTN_XPATH="//button[@type='submit']/span[text()='Submit']"
    REGION_LIST_XPATH="//table//tbody//tr/td[3]"

    REGION_EDIT_BUTTON_XPATH="//table//tbody//tr/td[4]"

    PAGES_XPATH="//nav[@aria-label='pagination navigation']/ul/li"
    PAGINATION_NEXT_BTN_XPATH="//nav[@aria-label='pagination navigation']/ul/li[last()]"
    MAX_NUMBER_OF_PAGE="//nav[@aria-label='pagination navigation']/ul/li[last()-1]"

    SEARCH_FIELD_TXT_XPATH="//input[@id='standard-bare'][@type='text']"
    SEARCH_DATA_FOUND="//table//tbody/tr/td[3]"



    "METHODS"
    def __init__(self,driver):
        self.driver=driver

    def Select_menu_item(self):
        self.driver.find_element(By.XPATH, value=self.REGION_MENUITEM_XPATH).click()
    def Click_Add_button(self):
        self.driver.find_element(By.XPATH, value=self.ADD_NEW_BTN_XPATH).click()
    def Click_on_sate(self):
        self.driver.find_element(By.XPATH, value=self.STATE_MENUBAR_XPATH).click()

    def Select_State(self,Name):
        self.driver.find_element(By.XPATH, value="//ul[@role='listbox']/li[text()='"+Name+"']").click()
    
    def Enter_Region_name(self,Region):
        self.driver.find_element(By.XPATH, value=self.NAME_TXT_XPATH).click()
        sleep(2)
        self.driver.find_element(By.XPATH, value=self.NAME_TXT_XPATH).send_keys(Keys.CONTROL + "a")
        self.driver.find_element(By.XPATH, value=self.NAME_TXT_XPATH).send_keys(Keys.DELETE)
        self.driver.find_element(By.XPATH, value=self.NAME_TXT_XPATH).send_keys(Region)

    def Click_Submit(self):
        self.driver.find_element(By.XPATH, value=self.SUBMIT_BTN_XPATH).click()


    def Check_Region_found(self,Name):
        sleep(3)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        Page=self.driver.find_elements(By.XPATH, value=self.PAGES_XPATH)
        Page_count=Page.__len__() - 2
        #Page=self.driver.find_element(By.XPATH, value=self.PAGES_XPATH).text
        #Page_count=int(Page)
        #print(Page_count)
        x = 0
        for i in range(Page_count):
            Regions=self.driver.find_elements(By.XPATH, value=self.REGION_LIST_XPATH)
            for Region in Regions:
                Reg_name = Region.text
                if Reg_name==Name:
                    x = 1
                    return x
                if x==1:
                    break
            if x==1:
                break
            self.driver.find_element(By.XPATH, value=self.PAGINATION_NEXT_BTN_XPATH).click()




    def Edit_Region_btn_click(self,Name):
        sleep(3)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        Page=self.driver.find_elements(By.XPATH, value=self.PAGES_XPATH)
        Page_count=Page.__len__() - 2
        #Page=self.driver.find_element(By.XPATH, value=self.PAGES_XPATH).text
        #Page_count=int(Page)
        #print(Page_count)
        x = 0
        for i in range(Page_count):
            Regions=self.driver.find_elements(By.XPATH, value=self.REGION_LIST_XPATH)
            i = 1
            for Region in Regions:
                Reg_name = Region.text
                if Reg_name==Name:
                    x = 1
                    self.driver.find_element(By.XPATH, value="//table//tbody//tr["+str(i)+"]/td[4]/a/button/span").click()
                if x==1:
                    break
                i=i+1
            if x==1:
                break
            self.driver.find_element(By.XPATH, value=self.PAGINATION_NEXT_BTN_XPATH).click()


    def Search_data(self,Data):
        self.driver.find_element(By.XPATH, value=self.SEARCH_FIELD_TXT_XPATH).click()
        self.driver.find_element(By.XPATH, value=self.SEARCH_FIELD_TXT_XPATH).send_keys(Data)

    def Search_data_found(self,Data):
        sleep(1)
        Text = self.driver.find_element(By.XPATH, value=self.SEARCH_DATA_FOUND).text
        print(Text)
        if Text == Data:
            return 1
        else:
            return 0
