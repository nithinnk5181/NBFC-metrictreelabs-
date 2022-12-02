import configparser

config=configparser.RawConfigParser()
config.read("CONFIG/config.ini")


class ReadConfig():
    ###ATLAS####
    @staticmethod
    def get_ATLAS_ADMIN_BaseURL():
        URL=config.get('ATLAS','ATLAS_ADMIN_BASEURL')
        return URL

    @staticmethod
    def get_ATLAS_ADMIN_USERNAME():
        USR=config.get('ATLAS','ATLAS_ADMIN_USERNAME')
        return USR
    
    @staticmethod
    def get_ATLAS_ADMIN_PASSWORD():
        PASS=config.get('ATLAS','ATLAS_ADMIN_PASSWORD')
        return PASS


    @staticmethod
    def get_ATLAS_ADMIN_EMAIL():
        email = config.get('ATLAS', 'ATLAS_ADMIN_EMAIL')
        return email

    @staticmethod
    def get_ATLAS_ADMIN_Login_success_EXPECTED_URL():
        URL = config.get('ATLAS', 'Atlas_Admin_LOGIN_EXPECTED_URL')
        return URL

    @staticmethod
    def get_ATLAS_ADMIN_Forgetpassword_URL():
        URL = config.get('ATLAS', 'Atlas_Admin_Forget_password_URL')
        return URL







    ###PARTNER###
    @staticmethod
    def get_PARTNER_ADMIN_BASEURL():
        URL = config.get('PARTNER', 'PARTNER_ADMIN_BASEURL')
        return URL

    @staticmethod
    def get_PARTNER_ADMIN_USERNAME():
        Username = config.get('PARTNER', 'PARTNER_ADMIN_USERNAME')
        return Username

    @staticmethod
    def get_PARTNER_ADMIN_PASSWORD():
        password = config.get('PARTNER', 'PARTNER_ADMIN_PASSWORD')
        return password

    @staticmethod
    def get_PARTNER_ADMIN_EMAIL():
        email = config.get('PARTNER', 'PARTNER_ADMIN_EMAIL')
        return email

    @staticmethod
    def get_PARTNER_ADMIN_Login_success_EXPECTED_URL():
        URL = config.get('PARTNER', 'Partner_Admin_LOGIN_EXPECTED_URL')
        return URL

    @staticmethod
    def get_PARTNER_ADMIN_Forgetpassword_URL():
        URL = config.get('PARTNER', 'Partner_Admin_Forget_password_URL')
        return URL





    ###FOS###
    @staticmethod
    def get_FOS_USER_ID():
        Username = config.get('FOS', 'FOS_USER_ID')
        return Username

    @staticmethod
    def get_FOS_USER_PASSWORD():
        password = config.get('FOS', 'FOS_USER_PASSWORD')
        return password



    ###CUSTOMER###
    @staticmethod
    def get_CUSTOMER_USER_ID():
        Username = config.get('CUSTOMER', 'CUSTOMER_USER_ID')
        return Username

    @staticmethod
    def get_CUSTOMER_USER_PASSWORD():
        password = config.get('CUSTOMER', 'CUSTOMER_USER_PASSWORD')
        return password


    ###API###
    @staticmethod
    def get_PARTNER_API_BASEURL():
        URL = config.get('API', 'PARTNER_API_BASEURL')
        return URL


    @staticmethod
    def get_ATLAS_API_BASEURL():
        URL = config.get('API', 'ATLAS_API_BASEURL')
        return URL




