from selenium.webdriver.common.by import By

SELECT_THEME_ELEMENT = (By.XPATH, "//select[@name='SelectTheme']")
LEVEL_ELEMENT = (By.XPATH, "//select[@name='SelectLevel']")
SELECT_ACTIVITY_ELEMENT = (By.XPATH, "//select[@name='SelectActivity']")
FROM_DATE_ELEMENT = (By.XPATH, "//*[@id='root']/div/div[2]/div/div/div/div/form/div[1]/div/div[6]/div/div/input")
TO_DATE_ELEMENT = (By.XPATH, "//*[@id='root']/div/div[2]/div/div/div/div/form/div[1]/div/div[7]/div/div/input")

ADULT_MALE_COUNT = (By.XPATH, "//input[@name='CountAdultMale']")
ADULT_FEMALE_COUNT = (By.XPATH, "//input[@name='CountAdultFemale']")
CHILDREN_MALE_COUNT = (By.XPATH, "//input[@name='CountChildMale']")
CHILDREN_FEMALE_COUNT = (By.XPATH, "//input[@name='CountChildFemale']")

SUBMIT_BUTTON = (By.XPATH, "//button[@type='submit']//img")