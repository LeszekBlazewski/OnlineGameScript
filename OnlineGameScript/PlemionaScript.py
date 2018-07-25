#!/usr/bin/python3.6
"""
    File name: PlemionaScript.py
    Author: Leszek Błażewski
    Description: The main purpose of this script is to automate the boring
    process of sending troops to other barbarian villages.
"""

# Modules needed to execute the script correctly
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options
from selenium.common.exceptions import NoSuchElementException
import itertools

# Set headless view
options = Options()
options.set_headless(headless=True)


# Extraction of the .txt files wich contain user data, settings, locations of the villages etc.
userSettings = CreateDictionaryWithData("config.txt")
barbarianVillageIdList = CreateDictionaryWithData("barbarianVillageIdList.txt")
barbarianVillageLocations = CreateDictionaryWithData("barbarianVillageLocations.txt")
armyUnits = CreateDictionaryWithData("attackSettings.txt")


def ChooseBrowser(userSettings):
    """open the equivalent browser based on
        the config file provided by the user
    """
    browserName = userSettings.get('InternetBrowser')
    result = {
        'Firefox': lambda x: webdriver.Firefox(),
        'Opera': lambda x: webdriver.Opera(options=options),
        'Chrome': lambda x: webdriver.Chrome(chrome_options=options)
    }[browserName](x=1)
    return result


def CreateDictionaryWithData(fileName):
    """Creates dictionary wich contains data extracted
       from the .txt file passed as arg.
    """
    dictionary = {}
    with open(fileName) as file:
        for line in file:
            (key, value) = line.split("-")
            dictionary[key] = value.strip("\n")
    return dictionary


def LoginIntoTheGame(userSettings):
    """Function handles the process of locating and filling in the form
       which allows script to access the map where attacks are sent.
    """
    usernameObject = browser.find_element_by_id('user')
    passwordObject = browser.find_element_by_id('password')
    usernameObject.send_keys(userSettings['Username'])
    passwordObject.send_keys(userSettings['Password'])
    passwordObject.submit()


def CheckIfDailyLoginPopupisDisplayed():
    """On the first login on the day the popup bonus appears
       This popup hovers the map button. Function checks whether
       element is displayed and if so then closes it.
    """
    try:
        popupCloseButton = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "popup_box_close")))
        popupCloseButton.click()
    except NoSuchElementException:
        return


# Based on the config file chooses the supported browser.
browser = ChooseBrowser(userSettings)

# navigate to game site
browser.get('https://www.plemiona.pl/')

# Fill the loggin form with valid credentials


# In case the bonus window opens (to receive daily login reward)


LoginIntoTheGame(userSettings)
# navigate to choosen active world


##### MARK THIS WORKS FOR NOW FOR ONLY ONE ACTIVE WORLD ! #############
## WAIT IS CRUCIAL BECAUSE PAGE MUST VERIFY YOUR CREDENCTIALS #####

worldButton = WebDriverWait(browser, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, "world_button_active")))
worldButton.click()

CheckIfDailyLoginPopupisDisplayed()
# navigate to map in order to select barbarian villages
# this also works but other option is more safe mapButton = browser.find_element_by_id("header_menu_link_map")

mapButton = WebDriverWait(browser, 10).until(
    EC.presence_of_element_located((By.ID, "header_menu_link_map")))
mapButton.click()

"""
    This step is the biggest trouble for the whole application. The developers of the website did not make any special characteristics which could be used to define ONLY the barbarian villages or any specific village tbh.
    The only specification which differs the villages is the 5 digit id stated on the end of link to the image.
    Therefore the only solution which came to my mind is to provide the script (from user input) the id's of the villages where you want to send tropps to automatically.
    You will have to get the id's of the villages by yoursefl (see appendix for instructions).

                            ANOTHER TRY TO MAKE IT WORK ( TO MANY REQUESTS PER SECOND)
    select input type to search based on name of the village
    targetTypeRadioButtoon = browser.find_element_by_css_selector('[value=village_name]')
    targetTypeRadioButtoon.click()
    The input box is automatically focused so no need to select it just type in the barbarian village name
    FOR POLISH VERSION = wioska barbarzynska
    ###### HERE REQUEST ERROR HAPPENS BECAUSE FUCKY SHITY TEMPLATE WAS IMPLEMENTED ON SITE WHILE SEARCHING FOR VILLAGES (THE DROPDOWN MENU) //EVERY LETTER = NEW REQUEST
    browser.switch_to_active_element().send_keys('wioska barb')
"""

# TODO add a file to read data from it (user will input there the last 5 digits of the id of each barbarian village he wants to send troops to)

# maybe change only to read mode, create config file where everyting will be specified
# allow access to the debugger sudo chmod -R a+rwx APPNAME/file
######### Id's of the villages where you want to send troops to (the id ALWAYS consist of 5 digits), please enter each id in separate new line. ######
"""
    Here comes even more trouble. The map was designed this way that you are not able to click onto certain elements on the site without moving your mouse onto that element.
    Basically the whole map is hovered by a map_mover, which disallows the script for clicking onto the target village instantly. Instead there must be a pop-up (a js event) triggered
    to show the window which enables clicking onto the desired village.
    SOLUTION 1
    expliticly control the mouse, hover on the vilage and send troops (ActionChain)
    SOLUTION 2
    Still under progress ( try to fire JS event from selenium (browser.execute())) which will directly open certain popup ( not sure if this is even possible)
"""
####################################################  SOLUTION 2 ######################################################

browser.execute_script("document.getElementById('map_mover').outerHTML = ''")
browser.execute_script("document.getElementById('special_effects_container').outerHTML = ''")

# TODO split this code into two separate functions and first one will be calling the second one.

locationInputBoxes = browser.find_elements_by_class_name("centercoord")


for (villageLocation, villageId, locationInputBox, numberOfLocation) in itertools.zip_longest(barbarianVillageLocations.values(), barbarianVillageIdList.values(), locationInputBoxes, range(0, 2)):
        # 1. Center the map to not screw up the locations
    locationInputBox.clear()
    locationInputBox.send_keys(villageLocation.split("x")[numberOfLocation])
    browser.find_element_by_class_name('btn').click()
    villagePosition = browser.find_element_by_id("map_village_" + villageId)
    villagePosition.click()
    attackButton = browser.find_element_by_id('mp_att')
    attackButton.click()
    unitsObjectInputList = browser.find_elements_by_class_name('unitsInput')
    for (inputObject, unitsQuantity) in zip(unitsObjectInputList, armyUnits.values()):
        inputObject.send_keys(unitsQuantity)
    browser.find_element_by_id("target_attack").click()

# TODO Try to finalize the whole script that will automatically send troops for each id numer used
# TODO create tutorial how to extract the 5 digit id numer from users browser

# TODO Polish the code (maybe add some functions, split it, make it more clear)

# TODO commit the code to github repository
