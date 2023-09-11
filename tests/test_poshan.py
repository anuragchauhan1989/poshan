import pytest
from selenium.webdriver.common.keys import Keys
from locatos.login_page_locator import *
from locatos.addactivityparticipation_page_locator import *
from tests import BaseClass
from selenium.webdriver.support.select import Select

ADULT_MALE_COUNT_DATA = 1
ADULT_FEMALE_COUNT_DATA = 2
CHILDREN_MALE_COUNT_DATA = 3
CHILDREN_FEMALE_COUNT_DATA = 4

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

        self.submitAcitvityParticipationForm(SELECT_THEME_ELEMENT, LEVEL_ELEMENT, SELECT_ACTIVITY_ELEMENT )
        

    def submitAcitvityParticipationForm(self, themeLocator, levelLocator, activityLocator):
        themeSelect = Select(self.get_element(themeLocator))
        levelSelect = Select(self.get_element(levelLocator))
        activitySelect = Select(self.get_element(activityLocator))

        # Iterate through each option in the select element
        for themeoption in themeSelect.options:
            # Print the text of each option
            print("theme options are: ", themeoption.text)
            if(themeoption.text != "Select Theme"):
                self.selectByVisibleText(SELECT_THEME_ELEMENT, themeoption.text)
                for levelOption in levelSelect.options:
                    # Print the text of each option
                    print("level options are: ", levelOption.text)
                    if(levelOption.text != "Select Level"):
                          self.selectByVisibleText(LEVEL_ELEMENT, levelOption.text)
                          COUNT = 0;
                          for activityOption in activitySelect.options:
                              #Print the text of each option
                              print("activity options are: ", activityOption.text)
                              if(activityOption.text != "Select Activity"):
                                self.selectByVisibleText(SELECT_ACTIVITY_ELEMENT, activityOption.text)
                                CURRENT_DATE = '2023-09-12'
                                COUNT = COUNT + 1
                                self.enterFormData(FROM_DATE_ELEMENT, TO_DATE_ELEMENT, ADULT_MALE_COUNT, ADULT_FEMALE_COUNT, CHILDREN_MALE_COUNT, CHILDREN_FEMALE_COUNT, SUBMIT_BUTTON, CURRENT_DATE, ADULT_MALE_COUNT_DATA, ADULT_FEMALE_COUNT_DATA,CHILDREN_MALE_COUNT_DATA, CHILDREN_FEMALE_COUNT_DATA, COUNT )
                                


    def enterFormData(self, FROM_DATE_ELEMENT, TO_DATE_ELEMENT, ADULT_MALE_COUNT, ADULT_FEMALE_COUNT, CHILDREN_MALE_COUNT, CHILDREN_FEMALE_COUNT, SUBMIT_BUTTON, CURRENT_DATE, ADULT_MALE_COUNT_DATA, ADULT_FEMALE_COUNT_DATA,CHILDREN_MALE_COUNT_DATA, CHILDREN_FEMALE_COUNT_DATA, COUNT):
          ADULT_MALE_COUNT_DATA = ADULT_MALE_COUNT_DATA + COUNT
          ADULT_FEMALE_COUNT_DATA = ADULT_FEMALE_COUNT_DATA + COUNT
          CHILDREN_MALE_COUNT_DATA = CHILDREN_MALE_COUNT_DATA + COUNT
          CHILDREN_FEMALE_COUNT_DATA = CHILDREN_FEMALE_COUNT_DATA + COUNT

          self.get_element(FROM_DATE_ELEMENT).send_keys(CURRENT_DATE)
          self.get_element(TO_DATE_ELEMENT).send_keys(CURRENT_DATE)
     
          self.get_element(ADULT_MALE_COUNT).clear()
          self.get_element(ADULT_MALE_COUNT).send_keys(ADULT_MALE_COUNT_DATA)

          self.get_element(ADULT_FEMALE_COUNT).clear()
          self.get_element(ADULT_FEMALE_COUNT).send_keys(ADULT_FEMALE_COUNT_DATA)

          self.get_element(CHILDREN_MALE_COUNT).clear()
          self.get_element(CHILDREN_MALE_COUNT).send_keys(CHILDREN_MALE_COUNT_DATA)

          self.get_element(CHILDREN_MALE_COUNT).clear() 
          self.get_element(CHILDREN_FEMALE_COUNT).send_keys(CHILDREN_FEMALE_COUNT_DATA)

          self.get_element(CHILDREN_MALE_COUNT).clear()
          self.get_element(CHILDREN_MALE_COUNT).send_keys(CHILDREN_MALE_COUNT_DATA)

          self.scrollIntoView(SUBMIT_BUTTON)
          self.get_element(SUBMIT_BUTTON).click()

    
       
        



    
    
    
        
 
