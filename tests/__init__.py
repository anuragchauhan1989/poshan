import pytest, config, time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


@pytest.mark.usefixtures("setup")
class BaseClass:
    def get_element(self, element):
        ''' Returns the element by finding from the page
        Parameters:
        element: The element finder tuple eg: (By.NAME,'ELEMENT_NAME') '''
        time.sleep(config.ACTION_DELAY)
        myElem = WebDriverWait(self.driver, config.WEB_DRIVER_WAIT).until(EC.presence_of_element_located(element))
        return myElem

    def selectByVisibleText(self, locator, text):
        #self.scrollIntoView(locator)       
        sel = Select(self.get_element(locator))
        sel.select_by_visible_text(text)

        
    def scrollIntoView(self, locator):
           element = self.get_element(locator)
           time.sleep(config.ACTION_DELAY)
           self.driver.execute_script("arguments[0].scrollIntoView();", element)
    
       



