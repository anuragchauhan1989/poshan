from selenium.webdriver.common.keys import Keys
from locatos.login_page_locator import *
from locatos.addactivityparticipation_page_locator import *
from tests import BaseClass
from selenium.webdriver.support.select import Select
import config, time
from selenium.common.exceptions import StaleElementReferenceException

CURRENT_DATE = '2023-09-18'
ADULT_MALE_COUNT_DATA = 1
ADULT_FEMALE_COUNT_DATA = 2
CHILDREN_MALE_COUNT_DATA = 3
CHILDREN_FEMALE_COUNT_DATA = 4
CURRENTTHEME = ""
ISSTALE = False
THEMEATSTALE = ""
AWCLASTSELECTEDTHEME =""
AWCCURRENT = ""
# awcList = ["Balmiki Basti 1", "Balmiki Basti 2", "Laxminagar", "Nai Basti", "Nai Basti Pachimi", "Panjabi Colony" , "Ward No 1/2", "Ward No 1/3", "Ward No 1/4", "Ward No 1/5" ,"Ward No 1/6", 
#            "Ward No 10/1", "Ward No 10/2", "Ward No 10/3", "Ward No 10/4", "Ward No 10/5", "Ward No 11/1", "Ward No 11/2", "Ward No 11/3", "Ward No 11/4", "Ward No 11/5", "Ward No 11/6", 
#            "Ward No 12/1", "Ward No 12/2", "Ward No 12/3", "Ward No 12/4", "Ward No 12/5", "Ward No 12/6", "Ward No 12/7", "Ward No 13/1", "Ward No 13/2", "Ward No 13/3", "Ward No 13/4",
#            "Ward No 13/5", "Ward No 13/6", "Ward No 13/7", "Ward No 2/1", "Ward No 2/2", "Ward No 2/3", "Ward No 2/4", "Ward No 2/5", "Ward No 2/6", "Ward No 3/1", "Ward No 3/2", "Ward No 3/3",
#            "Ward No 3/4", "Ward No 3/5", "Ward No 3/6", "Ward No 4/1", "Ward No 4/2", "Ward No 4/3", "Ward No 4/4", "Ward No 4/5", "Ward No 4/6", "Ward No 5/1", "Ward No 5/2", "Ward No 5/3", "Ward No 5/4",
#            "Ward No 5/5", "WWard No 6/1", "Ward No 6/2", "Ward No 6/3", "Ward No 6/4", "Ward No 6/5", "Ward No 7/1", "Ward No 7/2", "Ward No 7/3", "Ward No 7/4", "Ward No 7/5", "Ward No 7/6",
#             "Ward No 7/7", "Ward No 8/1", "Ward No 8/2", "Ward No 8/3", "Ward No 8/4", "Ward No 8/5", "Ward No 8/6", "Ward No 9/1", "Ward No 9/2", "Ward No 9/3", "Ward No 9/4", "Ward No 9/5"]

# awcList = ["Balmiki Basti 1", "Balmiki Basti 2", "Laxminagar", "Nai Basti", "Nai Basti Pachimi", "Panjabi Colony" , "Ward No 1/2", "Ward No 1/3", "Ward No 1/4", "Ward No 1/5" ,"Ward No 1/6", 
#            "Ward No 10/1", "Ward No 10/2", "Ward No 10/3", "Ward No 10/4", "Ward No 10/5", "Ward No 11/1", "Ward No 11/2", "Ward No 11/3", "Ward No 11/4", "Ward No 11/5", "Ward No 11/6", 
#            "Ward No 12/1", "Ward No 12/2", "Ward No 12/3", "Ward No 12/4", "Ward No 12/5", "Ward No 12/6", "Ward No 12/7", "Ward No 13/1", "Ward No 13/2", "Ward No 13/3", "Ward No 13/4",
#            "Ward No 13/5", "Ward No 13/6", "Ward No 13/7", "Ward No 2/1", "Ward No 2/2", "Ward No 2/3", "Ward No 2/4", "Ward No 2/5", "Ward No 2/6", "Ward No 3/1", "Ward No 3/2", "Ward No 3/3",
#            "Ward No 3/4", "Ward No 3/5", "Ward No 3/6", "Ward No 4/3", "Ward No 4/4", "Ward No 4/5", "Ward No 4/6", "Ward No 5/1", "Ward No 5/2", "Ward No 5/3", "Ward No 5/4",
#            "Ward No 5/5", "WWard No 6/1", "Ward No 6/2", "Ward No 6/3", "Ward No 6/4", "Ward No 6/5", "Ward No 7/2", "Ward No 7/3", "Ward No 7/4", "Ward No 7/5", "Ward No 7/6",
#             "Ward No 7/7", "Ward No 8/1", "Ward No 8/2", "Ward No 8/3", "Ward No 8/5", "Ward No 9/1", "Ward No 9/2", "Ward No 9/3", "Ward No 9/4", "Ward No 9/5" --- "Ward No 2/2", "Ward No 2/3", "Ward No 2/4", "Ward No 2/5", ]

awcList = ["Ward No 2/5", "Ward No 2/6", "Ward No 3/1", "Ward No 3/2", "Ward No 3/3",
           "Ward No 3/4", "Ward No 3/5", "Ward No 3/6","Ward No 4/3", "Ward No 4/4", "Ward No 4/5", "Ward No 4/6", "Ward No 5/1", "Ward No 5/2", "Ward No 5/3", "Ward No 5/4",
           "Ward No 5/5", "WWard No 6/1", "Ward No 6/2", "Ward No 6/3", "Ward No 6/4", "Ward No 6/5", "Ward No 7/2", "Ward No 7/3", "Ward No 7/4", "Ward No 7/5", "Ward No 7/6",
            "Ward No 7/7",  "Ward No 8/2", "Ward No 8/3",  "Ward No 9/2", "Ward No 9/3", "Ward No 9/4", "Ward No 9/5"]

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
        time.sleep(config.ACTION_DELAY)
        self.submitAcitvityParticipationForm(SELECT_THEME_ELEMENT, LEVEL_ELEMENT, SELECT_ACTIVITY_ELEMENT, SELECT_AWC_ELEMENT )    

    def submitAcitvityParticipationForm(self, themeLocator, levelLocator, activityLocator, awcLocator):
        global ISSTALE
        global THEMEATSTALE
        global AWCATSTALE
        global CURRENT_DATE
        global AWCLASTSELECTEDTHEME
        global AWCCURRENT
        global awcList
        themeSelect = Select(self.get_element(themeLocator))
        levelSelect = Select(self.get_element(levelLocator))
        activitySelect = Select(self.get_element(activityLocator))

        for awc in awcList:
          # Iterate through each option in the select element
          if ISSTALE:
             AWCCURRENT = AWCATSTALE
          else:
             AWCCURRENT = awc
          for themeoption in themeSelect.options:
            # Print the text of each option
            print("theme options are: ", themeoption.text)
            CURRENTTHEME = themeoption.text
            if ISSTALE:
               CURRENTTHEME = THEMEATSTALE
            else:
              CURRENTTHEME = themeoption.text

            if(themeoption.text != "Select Theme" and themeoption.text == CURRENTTHEME):
                self.selectByVisibleText(SELECT_THEME_ELEMENT, themeoption.text)
                for levelOption in levelSelect.options:
                    # Print the text of each option
                    print("level options are: ", levelOption.text)
                    if(levelOption.text != "Select Level"):
                          if(levelOption.text == "AWC" and themeoption.text != "Select Theme"):
                            self.selectByVisibleText(LEVEL_ELEMENT, levelOption.text)
                            COUNT = 0;
                            activitySelectNew = Select(self.get_element(activityLocator))
                            for activityOptionNew in activitySelectNew.options:
                              try:
                               #Print the text of each option
                               if ISSTALE:
                                  CURRENTACTIVITY = AWCLASTSELECTEDTHEME
                               else:
                                  CURRENTACTIVITY = activityOptionNew.text
                               print("activity options are: ", CURRENTACTIVITY)
                               if(activityOptionNew.text != "Select Activity" and activityOptionNew.text == CURRENTACTIVITY):
                                 self.selectByVisibleText(SELECT_THEME_ELEMENT, themeoption.text)
                                 self.selectByVisibleText(LEVEL_ELEMENT, levelOption.text)
                                 if(levelOption.text == "AWC"):
                                  awcSelect = Select(self.get_element(awcLocator))
                                  for awcOptionNew in awcSelect.options:
                                    print("awc options are: ", awcOptionNew.text)
                                    if(awcOptionNew.text != "Select a AWC"):
                                      if(awcOptionNew.text != "" and awcOptionNew.text == AWCCURRENT):
                                        self.selectByVisibleText(SELECT_AWC_ELEMENT, awcOptionNew.text)
                                        break;                                              
                                  self.selectByVisibleText(SELECT_ACTIVITY_ELEMENT, CURRENTACTIVITY)
                                  AWCLASTSELECTEDTHEME = CURRENTACTIVITY
                                  AWCCURRENT = awcOptionNew.text
                                  COUNT = COUNT + 1
                                  self.enterFormData(FROM_DATE_ELEMENT, TO_DATE_ELEMENT, ADULT_MALE_COUNT, ADULT_FEMALE_COUNT, CHILDREN_MALE_COUNT, CHILDREN_FEMALE_COUNT, SUBMIT_BUTTON, CURRENT_DATE, ADULT_MALE_COUNT_DATA, ADULT_FEMALE_COUNT_DATA,CHILDREN_MALE_COUNT_DATA, CHILDREN_FEMALE_COUNT_DATA, COUNT)  
                              except StaleElementReferenceException:
                                ISSTALE = True
                                AWCATSTALE = AWCCURRENT
                                THEMEATSTALE = themeoption.text
                                self.driver.refresh()
                                self.submitAcitvityParticipationForm(SELECT_THEME_ELEMENT, LEVEL_ELEMENT, SELECT_ACTIVITY_ELEMENT, SELECT_AWC_ELEMENT)
                            ISSTALE = False
                            #awcList = awcList.remove(AWCCURRENT)   
                          elif(levelOption.text == 'Black'):
                               self.selectByVisibleText(LEVEL_ELEMENT, levelOption.text)
                               COUNT = 0;
                               for activityOption in activitySelect.options:
                                    print("activity options are: ", activityOption.text)
                                    if(activityOption.text != "Select Activity"):
                                      self.selectByVisibleText(SELECT_THEME_ELEMENT, themeoption.text)
                                      self.selectByVisibleText(SELECT_ACTIVITY_ELEMENT, activityOption.text)
                                      #CURRENT_DATE = '2023-09-20'
                                      COUNT = COUNT + 1
                                      self.enterFormData(FROM_DATE_ELEMENT, TO_DATE_ELEMENT, ADULT_MALE_COUNT, ADULT_FEMALE_COUNT, CHILDREN_MALE_COUNT, CHILDREN_FEMALE_COUNT, SUBMIT_BUTTON, CURRENT_DATE, ADULT_MALE_COUNT_DATA, ADULT_FEMALE_COUNT_DATA,CHILDREN_MALE_COUNT_DATA, CHILDREN_FEMALE_COUNT_DATA, COUNT )
                          
          awcList = awcList.remove(AWCCURRENT)                          


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

          #self.get_element(CHILDREN_MALE_COUNT).send_keys(Keys.CONTROL + "a")
          #self.get_element(CHILDREN_MALE_COUNT).send_keys(Keys.DELETE)
          self.clearElement(CHILDREN_MALE_COUNT)
          self.get_element(CHILDREN_MALE_COUNT).send_keys(CHILDREN_MALE_COUNT_DATA)

          #self.get_element(CHILDREN_FEMALE_COUNT).send_keys(Keys.CONTROL + "a")
          #self.get_element(CHILDREN_FEMALE_COUNT).send_keys(Keys.DELETE)
          self.clearElement(CHILDREN_FEMALE_COUNT)
          self.get_element(CHILDREN_FEMALE_COUNT).send_keys(CHILDREN_FEMALE_COUNT_DATA)

          # self.get_element(CHILDREN_MALE_COUNT).send_keys(Keys.CONTROL,"a", Keys.DELETE)
          # self.get_element(CHILDREN_MALE_COUNT).send_keys(CHILDREN_MALE_COUNT_DATA)

          self.scrollIntoView(SUBMIT_BUTTON)
          self.get_element(SUBMIT_BUTTON).click()
          time.sleep(config.ACTION_DELAY)
          self.driver.execute_script("window.scrollTo(0, -document.body.scrollHeight)")
          time.sleep(config.ACTION_DELAY)
          


    def SelectAWCOption(self, levelOption, awcLocator):
        if(levelOption.text == "AWC"):                           
           awcSelect = Select(self.get_element(awcLocator))
           for awcOptionNew in awcSelect.options:
            print("awc options are: ", awcOptionNew.text)
            if(awcOptionNew.text != "Select a AWC"):
              if(awcOptionNew.text != ""):
                selectedoption = awcSelect.options[i+1]
                self.selectByVisibleText(SELECT_AWC_ELEMENT, selectedoption.text)
                break;
        

    
       
        



    
    
    
        
 
