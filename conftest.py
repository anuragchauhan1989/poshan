import pytest
from selenium import webdriver
import config
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


def pytest_addoption(parser):
    ''' This function adds a argument to choose the broweser '''
    parser.addoption(
        "--browser_name", action="store", default="firefox"
    )


@pytest.fixture(scope="class")
def setup(request):
    ''' Here we are doing setup for broweser and the url '''
    global driver
    #Getting the driver name and instantiating the driver
    browser_name=request.config.getoption("browser_name")
    if browser_name == "chrome":
        #Configuring the Chrome browser
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("prefs", {
        "download.default_directory": config.DOWNLOAD_FOLDER, 
        "download.prompt_for_download": False,
        "download.directory_upgrade": True,
        "safebrowsing.enabled": True,       
        })
        if config.HEADLESS:
            chrome_options.add_argument('--headless')
        #Instantiating the driver with the options
        print("====================",config.DRIVER_PATH)
        chrome_service = ChromeService(executable_path = f"{config.DRIVER_PATH}\\chromedriver.exe")
        driver = webdriver.Chrome(service = chrome_service, options=chrome_options)

    elif browser_name == "firefox":
       firefox_capabilities = DesiredCapabilities.FIREFOX
       firefox_capabilities['marionette'] = True
       firefox_service = FirefoxService(executable_path = f"{config.DRIVER_PATH}\\geckodriver.exe")
       driver = webdriver.Firefox(service = firefox_service, capabilities=firefox_capabilities)
    elif browser_name == "IE":
        edge_service = EdgeService(executable_path=f"{config.DRIVER_PATH}\\msedgedriver.exe")
        driver = webdriver.Edge(service=edge_service)

    driver.get(config.BASE_URL)
    driver.maximize_window()
    request.cls.driver = driver
    yield
    #driver.close()

