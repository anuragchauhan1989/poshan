import os
BASE_DIRECTORY = os.getcwd()
BASE_URL = "https://www.google.com/"

#DRIVER
DRIVER_PATH = os.path.join(BASE_DIRECTORY, 'src', 'drivers') #use os.path.join to create a path
WEB_DRIVER_WAIT = 2
HEADLESS = False
ACTION_DELAY = 1
DOWNLOAD_WAIT_TIME = 2
LOG_FOLDER = os.path.join(BASE_DIRECTORY, 'src', 'logs')
DOWNLOAD_FOLDER = os.path.join(BASE_DIRECTORY,'src', 'media','download')
