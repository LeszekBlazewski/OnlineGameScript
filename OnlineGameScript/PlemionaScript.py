#!/usr/bin/env python3
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
import time


def SetWebDriverOptions():
    """Sets the option to enable headles browser.
       Headles allows running the browser in background.
    """
    options = Options()
    options.set_headless(headless=True)
    return options


def ChooseBrowser(userSettings, options):
    """open the equivalent browser based on
        the config file provided by the user
    """
    browserName = userSettings.get('InternetBrowser')
    result = {
        'firefox': lambda x: webdriver.Firefox(options=options),
        'opera': lambda x: webdriver.Opera(options=options),
        'chrome': lambda x: webdriver.Chrome(chrome_options=options)
    }[browserName.lower()](x=1)
    if result == None:
        print('Browser could not be specified.\n Please check your config.txt file.\n Supported browsers are:\nFirefox\nOpera\nChrome')
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


def LoginIntoTheGame(userSettings, browser):
    """Function handles the process of locating and filling in the form
       which allows script to access the map where attacks are sent.
    """
    # navigate to game site
    browser.get('https://www.plemiona.pl/')
    usernameObject = browser.find_element_by_id('user')
    passwordObject = browser.find_element_by_id('password')
    usernameObject.send_keys(userSettings['Username'])
    passwordObject.send_keys(userSettings['Password'])
    passwordObject.submit()
    try:
        browser.find_element_by_class_name('auto-hide-box')
        print('Login into the game site aborted.\n Please check whether your credentials:\nUsername: %s\nPassword: %s' % (
            userSettings['Username'], userSettings['Password']))
    except NoSuchElementException:
        print('Login into the game site successful.')


def SelectActiveWorld(browser, userSettings):
    """Select the world where the attacks should be carried out
       Active world is choosen based on the config.txt file and proceed
       to the map panel.
    """
    try:
        worldButtons = WebDriverWait(browser, 10).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, "world_button_active")))
    except NoSuchElementException:
        print('You do not have any active worlds where you can send your troops\n Please choose a world in the game and activate the script again.')
        print('Note: Remember to specify the world number in the config.txt file')
        return False
    for activeWorldButton in worldButtons:
        activeWorldNumber = activeWorldButton.get_attribute('innerHTML').split()[1]
        if activeWorldNumber == userSettings['ActiveWorld']:
            activeWorldButton.click()
            CheckIfDailyLoginPopupisDisplayed(browser)
            mapButton = browser.find_element_by_id("header_menu_link_map")
            mapButton.click()
            return True


def CheckIfDailyLoginPopupisDisplayed(browser):
    """On the first login on the day the popup bonus appears
       This popup hovers the map button. Function checks whether
       element is displayed and if so then closes it.
    """
    try:
        popupCloseButton = browser.find_element_by_class_name("popup_box_close")
        popupCloseButton.click()
    except NoSuchElementException:
        return


def DisableHoveringJavaScriptObjects(browser):
    """Disables the two elements which prevent the script from
       selecting the villages correctly.
    """
    browser.execute_script("document.getElementById('map_mover').outerHTML = ''")
    browser.execute_script("document.getElementById('special_effects_container').outerHTML = ''")
    # for the headles option
    browser.execute_script("document.getElementById('linkContainer').outerHTML = ''")
    browser.execute_script("document.getElementById('footer').outerHTML = ''")


def CenterTheMapOnTargetVillageLocation(browser, villageLocation, locationInputBoxes):
    """Centers the map on the village which is the target of the attack.
       While selecting the village in next step map must
       be centered otherwise the locations of the villages do not correctly
       respond to the images which represent them on the map. If the map
       wouldn't be centered the script wouldn't be able to click on the targeted village.
    """
    for (locationInputBox, locationCordinateXY) in zip(locationInputBoxes, range(0, 2)):
        locationInputBox.clear()
        locationInputBox.send_keys(villageLocation.split("x")[locationCordinateXY])
        browser.find_element_by_class_name('btn').click()
        time.sleep(0.5)


def LocateTheVillageOnTheMap(browser, villageId):
    """Searches for the village based on the villageId provided in barbarianVillageIdList.txt.
       Then opens the attack form.
    """
    villagePosition = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.ID, "map_village_" + villageId))
    )
    villagePosition.click()
    attackButton = browser.find_element_by_id('mp_att')
    attackButton.click()


def CheckIfUserHasSufficientArmyUnits(browser, villageId, villageLocation):
    """Checks whether user poses enough units to perform attack he requsted.
    """
    try:
        browser.find_element_by_class_name('autoHideBox')
    except NoSuchElementException:
        return True

    print('Troops to village under %s id located at %s has not been sent because you do not own enough army units!' % (
        villageId, villageLocation))
    return False


def CheckIfUserAllowsSendingSingleTroops(browser, villageId, villageLocation, userSettings):
    """Check whether user allow sending single troops to targeted village.
    """
    try:
        popupWarnning = browser.find_element_by_class_name('troop_confirm_go')
    except NoSuchElementException:
        print('Troops to village under %s id located at %s has been successfully sent.' % (
            villageId, villageLocation))
        return
    if userSettings['AllowSendingOneTroopToTargetVillage'].lower() == 'yes':
        popupWarnning.click()
        print('One unit send to village under id %s located at %s ' % (
            villageId, villageLocation))
    else:
        browser.find_element_by_class_name('popup_box_close').click()
        print('Troop has not been sent becasue AllowSendingOneTroopToTargetVillag is disabled in config.txt.')
        print('If you want to enable this option please change it in config.txt to Yes')


def FillTheAttackForm(browser, armyUnits, userSettings, villageLocation, villageId):
    """Fills the attack form with equivalent quantity of units stored in the
       attackSettings.txt file provided by user.
    """
    unitsObjectInputList = browser.find_elements_by_class_name('unitsInput')
    for (inputObject, unitsQuantity) in zip(unitsObjectInputList, armyUnits):
        inputObject.send_keys(unitsQuantity)
    browser.find_element_by_id("target_attack").click()
    # Check whether this benefits for the script
    if CheckIfUserHasSufficientArmyUnits(browser, villageId, villageLocation):
        CheckIfUserAllowsSendingSingleTroops(browser, villageId, villageLocation, userSettings)
    else:
        browser.find_element_by_class_name('popup_box_close').click()


def main():
    options = SetWebDriverOptions()
    userSettings = CreateDictionaryWithData("config.txt")
    barbarianVillageIdList = CreateDictionaryWithData("barbarianVillageIdList.txt")
    barbarianVillageLocations = CreateDictionaryWithData("barbarianVillageLocations.txt")
    armyUnits = CreateDictionaryWithData("attackSettings.txt")
    browser = ChooseBrowser(userSettings, options)
    if browser:
        browser.maximize_window()
        LoginIntoTheGame(userSettings, browser)
        if SelectActiveWorld(browser, userSettings):
            DisableHoveringJavaScriptObjects(browser)
            locationInputBoxes = browser.find_elements_by_class_name("centercoord")
            for (villageLocation, villageId) in zip(barbarianVillageLocations.values(), barbarianVillageIdList.values()):
                CenterTheMapOnTargetVillageLocation(browser, villageLocation, locationInputBoxes)
                LocateTheVillageOnTheMap(browser, villageId)
                FillTheAttackForm(browser, armyUnits.values(),
                                  userSettings, villageLocation, villageId)
        browser.quit()
    else:
        print('An error occured please check the log displayed in your console.')


if __name__ == "__main__":
    main()
