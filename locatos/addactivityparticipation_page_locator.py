from selenium.webdriver.common.by import By

SELECT_THEME_ELEMENT = (By.XPATH, "//select[@name='SelectTheme']")
LEVEL_ELEMENT = (By.XPATH, "//select[@name='SelectLevel']")
SELECT_ACTIVITY_ELEMENT = (By.XPATH, "//select[@name='SelectActivity']")
SELECT_AWC_ELEMENT = (By.XPATH, "//select[@name='awc_center']")
FROM_DATE_ELEMENT = (By.XPATH, "//input[@name='SelectDateFrom']")
TO_DATE_ELEMENT = (By.XPATH, "//input[@name='SelectDateTo']")

ADULT_MALE_COUNT = (By.XPATH, "//input[@name='CountAdultMale']")
ADULT_FEMALE_COUNT = (By.XPATH, "//input[@name='CountAdultFemale']")
CHILDREN_MALE_COUNT = (By.XPATH, "//input[@name='CountChildMale']")
CHILDREN_FEMALE_COUNT = (By.XPATH, "//input[@name='CountChildFemale']")

SUBMIT_BUTTON = (By.XPATH, "//button[@type='submit']//img")