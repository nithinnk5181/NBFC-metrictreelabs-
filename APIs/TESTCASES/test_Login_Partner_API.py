# pytest APIs/TESTCASES/test_Login_Partner_API.py


#import Statements

import requests
import json
import  jsonpath
from UTIL.readproperties import ReadConfig
import pytest



PARTNER_API_BASEURL = ReadConfig.get_PARTNER_API_BASEURL()

class Test_Login:

    #@pytest.mark.skip
    def test_Login_Patner_admin_success(self):

        Headers = {
                  "Accept": "application/json"
                  }
        params= {
                "userid":"ecapsadmin",
                "password":"100thousand@"
                }

        response=requests.post(PARTNER_API_BASEURL+"/login/superadmin",headers=Headers,data=params)

        st_cd = response.status_code
        response_json = json.loads(response.content)
        Message = response_json["message"]

        if st_cd == 200:
            if Message=="Hurry! you are now logged in.":
                assert True
            else:
                assert False
        else:
            assert False

    #@pytest.mark.skip
    def test_Login_Patner_admin_fail_with_incorrect_password(self):
    
        Headers = {
                  "Accept": "application/json"
                  }
        params= {
                "userid":"ecapsadmin",
                "password":"test"
                }

        response=requests.post(PARTNER_API_BASEURL+"/login/superadmin",headers=Headers,data=params)

        st_cd = response.status_code
        response_json = json.loads(response.content)
        Message = response_json["message"]

        if st_cd == 200:
            assert False
        else:
            if Message=="Incorrect password":
                assert True
            else:
                assert False

    #@pytest.mark.skip
    def test_Login_Patner_admin_fail_with_credentials_of_Atlas_Admin(self):
    
        Headers = {
                  "Accept": "application/json"
                  }
        params= {
                "userid":"atlasadmin",
                "password":"100thousand@"
                }

        response=requests.post(PARTNER_API_BASEURL+"/login/superadmin",headers=Headers,data=params)

        st_cd = response.status_code
        response_json = json.loads(response.content)
        Message = response_json["message"]
        print(Message)

        if st_cd == 200:
            assert False
        else:
            if Message=="Invalid login credentials.":
                assert True
            else:
                assert False

    #@pytest.mark.skip
    def test_Login_Patner_admin_fail_with_credentials_of_FOS(self):
    
        Headers = {
                  "Accept": "application/json"
                  }
        params= {
                "userid":"FOS1001",
                "password":"123456"
                }

        response=requests.post(PARTNER_API_BASEURL+"/login/superadmin",headers=Headers,data=params)

        st_cd = response.status_code
        response_json = json.loads(response.content)
        Message = response_json["message"]

        if st_cd == 200:
            assert False
        else:
            if Message=="Invalid login credentials.":
                assert True
            else:
                assert False


    #@pytest.mark.skip
    def test_Login_Patner_admin_fail_with_empty_data(self):
    
        Headers = {
                  "Accept": "application/json"
                  }
        params= {
                "userid":"",
                "password":""
                }

        response=requests.post(PARTNER_API_BASEURL+"/login/superadmin",headers=Headers,data=params)

        st_cd = response.status_code
        response_json = json.loads(response.content)
        Message = response_json["message"]

        if st_cd == 200:
            assert False
        else:
            if Message=="Invalid login credentials.":
                assert True
            else:
                assert False