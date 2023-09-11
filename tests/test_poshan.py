import pytest
from selenium.webdriver.common.keys import Keys
from locatos.login_page_locator import *
from locatos.addactivityparticipation_page_locator import *
from tests import BaseClass


class TestPoshanPage(BaseClass):
    def test_poshan_login_page(self):
        ''' This is a test case to test the Github Login Page Bad case page. '''
        # Opening poshanabhiyaan url
        self.driver.get("https://poshanabhiyaan.gov.in/login")
          #accessing the username and password field and sending text to that
        self.get_element(USERNAME_INPUT).clear()
        self.get_element(PASSWORD_INPUT).clear()
        self.get_element(USERNAME_INPUT).send_keys('mow&cd-506704') #right Username
        self.get_element(PASSWORD_INPUT).send_keys('mow&cd-506704') #right Password    
        self.get_element(LOGIN_BUTTON).submit()
        self.selectByIndex(SELECT_THEME_ELEMENT,3)
        self.selectByIndex(SELECT_ACTIVITY_ELEMENT,3)
        self.selDateFromDatePicker(FROM_DATE_ELEMENT,'11-09-2023')
        
        
 
