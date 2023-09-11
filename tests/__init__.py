import pytest, config, time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


@pytest.mark.usefixtures("setup")
class BaseClass:
    def get_element(self, element):
        ''' Returns the element by finding from the page
        Parameters:
        element: The element finder tuple eg: (By.NAME,'ELEMENT_NAME') '''
        time.sleep(config.ACTION_DELAY)
        myElem = WebDriverWait(self.driver, config.WEB_DRIVER_WAIT).until(EC.presence_of_element_located(element))  
        return myElem

    def selectByIndex(self, locator ,index):       
        sel = Select(self.get_element(locator))
        sel.select_by_index(index)


    def selDateFromDatePicker(self, locator, desired_date):
    
        self.get_element(locator).click()
        self.driver.execute_script("arguments[0].value = '11-09-2023';", self.get_element(locator))
        time.sleep(config.ACTION_DELAY)
        self.get_element(locator).send_keys(Keys.TAB)





