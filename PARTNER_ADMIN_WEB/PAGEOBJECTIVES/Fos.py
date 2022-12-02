from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.keys import Keys

class Fos:
    """PAGEOBJECTIVES"""
    FOS_MENUITEM_XPATH="//div[@class='sidebar-parent']//li[@class='pro-menu-item'][3]//span[@class='pro-item-content']"
    ADD_NEW_BTN_XPATH="//button[@type='button']/span[@class='MuiButton-label']"
    NAME_TXT_XPATH="//input[@type='text'][@name='name']"
    MOBILE_TXT_XPATH="//input[@type='number'][@name='mobile']"
    EMAIL_TXT_XPATH="//input[@type='text'][@name='email']"
    REGION_DROP_XPATH="//div[@role='button'][@aria-haspopup='listbox']"
    REGIONS_LIST_XPATH="//ul[@role='listbox']"
    SUBMIT_BTN_XPATH="//button[@type='submit']/span[text()='Submit']"

    FOS_EMAIL_LIST_XPATH="//table//tbody//tr/td[4]"

    PAGES_XPATH="//nav[@aria-label='pagination navigation']/ul/li"
    PAGINATION_NEXT_BTN_XPATH="//nav[@aria-label='pagination navigation']/ul/li[last()]"
    MAX_NUMBER_OF_PAGE="//nav[@aria-label='pagination navigation']/ul/li[last()-1]"



    "METHODS"
    def __init__(self,driver):
        self.driver=driver

    def Select_menu_item(self):
        self.driver.find_element(By.XPATH, value=self.FOS_MENUITEM_XPATH).click()

    def Click_Add_button(self):
        self.driver.find_element(By.XPATH, value=self.ADD_NEW_BTN_XPATH).click()

    def Add_name(self,Name):
        self.driver.find_element(By.XPATH, value=self.NAME_TXT_XPATH).click()
        self.driver.find_element(By.XPATH, value=self.NAME_TXT_XPATH).send_keys(Name)

    def Add_Mobile_num(self,Name):
        self.driver.find_element(By.XPATH, value=self.MOBILE_TXT_XPATH).click()
        self.driver.find_element(By.XPATH, value=self.MOBILE_TXT_XPATH).send_keys(Name)

    def Add_Email(self,Name):
        self.driver.find_element(By.XPATH, value=self.EMAIL_TXT_XPATH).click()
        self.driver.find_element(By.XPATH, value=self.EMAIL_TXT_XPATH).send_keys(Name)

    def Select_region(self,REGION):
        self.driver.find_element(By.XPATH, value=self.REGION_DROP_XPATH).click()
        sleep(1)
        self.driver.find_element(By.XPATH, value="//ul[@role='listbox']/li[text()='"+REGION+"']").click()
    
    def Click_Submit(self):
            self.driver.find_element(By.XPATH, value=self.SUBMIT_BTN_XPATH).click()

    
    def Check_Fos_found(self,EMAIL):
        sleep(3)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        Page=self.driver.find_elements(By.XPATH, value=self.PAGES_XPATH)
        Page_count=Page.__len__() - 2
        #Page=self.driver.find_element(By.XPATH, value=self.PAGES_XPATH).text
        #Page_count=int(Page)
        #print(Page_count)
        x = 0
        for i in range(Page_count):
            FOS_List=self.driver.find_elements(By.XPATH, value=self.FOS_EMAIL_LIST_XPATH)
            for Fos in FOS_List:
                FOS_name = Fos.text
                if FOS_name==EMAIL:
                    x = 1
                    return x
                if x==1:
                    break
            if x==1:
                break
            self.driver.find_element(By.XPATH, value=self.PAGINATION_NEXT_BTN_XPATH).click()


    def Fos_Edit_btn_click(self,EMAIL):
        sleep(3)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        Page=self.driver.find_elements(By.XPATH, value=self.PAGES_XPATH)
        Page_count=Page.__len__() - 2
        #Page=self.driver.find_element(By.XPATH, value=self.PAGES_XPATH).text
        #Page_count=int(Page)
        #print(Page_count)
        x = 0
        for i in range(Page_count):
            FOS_List=self.driver.find_elements(By.XPATH, value=self.FOS_EMAIL_LIST_XPATH)
            i = 1
            for Fos in FOS_List:
                FOS_name = Fos.text
                if FOS_name==EMAIL:
                    x = 1
                    self.driver.find_elements(By.XPATH, value= "//table//tbody//tr["+str(i)+"]/td[8]/a/button/span").click()
                if x==1:
                    break
                i=i+1
            if x==1:
                break
            self.driver.find_element(By.XPATH, value=self.PAGINATION_NEXT_BTN_XPATH).click()
