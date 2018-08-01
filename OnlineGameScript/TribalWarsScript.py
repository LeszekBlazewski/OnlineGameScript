#!/usr/bin/env python3
"""
    File name: PlemionaScript.py
    Author: Leszek Błażewski
    Description: The main purpose of this script is to automate the boring
    process of sending troops to barbarian villages.
"""

# Modules needed to execute the script correctly
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import InvalidArgumentException
import time


def SetWebDriverOptions(userSettings):
    """Sets the option to enable headles browser.
       Headles allows running the browser in background.
    """
    browserName = userSettings.get('InternetBrowser').lower()
    if browserName == 'firefox':
        options = Options()
        options.set_headless(headless=True)
    elif browserName == 'chrome':
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        options.add_argument('--headless')
    elif browserName == 'opera':
        options = webdriver.ChromeOptions()
        options.binary_location = "C:\Program Files\Opera\launcher.exe"

    return options


def ChooseBrowser(userSettings, options):
    """open the equivalent browser based on
        the config file provided by the user
    """
    browserName = userSettings.get('InternetBrowser').lower()
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
       Also opens the game website based on the URL provided in config.txt file.
    """
    # navigate to game site
    # This operation is necessary becasue accounts are not shared between servers.
    # Therefore website must be opened in specify language in order to successfully login in to the game.
    websiteLink = userSettings.get('LinkToGameWebsite')
    try:
        browser.get(websiteLink)
    except InvalidArgumentException:
        print("Link to website specified in config.txt file does not match any website!\nPlease check whether %s  specified in config.txt file is correct." % websiteLink)
        return False

    usernameObject = browser.find_element_by_id('user')
    passwordObject = browser.find_element_by_id('password')
    usernameObject.send_keys(userSettings['Username'])
    passwordObject.send_keys(userSettings['Password'])
    passwordObject.submit()
    try:
        WebDriverWait(browser, 1).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '.auto-hide-box.error-box'))
        )
    except (TimeoutException):
        print('Login into the game site successful.')
        return True
    else:
        print('Login into the game site aborted.\n Please check whether your credentials are valid:\nUsername: %s\nPassword: %s' % (
            userSettings['Username'], userSettings['Password']))
        return False


def SelectActiveWorld(browser, userSettings):
    """Select the world where the attacks should be carried out
       Active world is choosen based on the config.txt file and proceed
       to the map panel.
    """
    try:
        worldButtons = WebDriverWait(browser, 1).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, "world_button_active"))
        )
    except (TimeoutException):
        print('You do not have any active worlds where you can send your troops\n Please choose a world in the game and activate the script again.')
        print('Note: Remember to specify the world number in the config.txt file')
        return False
    else:
        for activeWorldButton in worldButtons:
            activeWorldNumber = activeWorldButton.get_attribute('innerHTML').split()[1]
            if activeWorldNumber == userSettings['ActiveWorld']:
                activeWorldButton.click()
                print('world %s has been selected.' % activeWorldNumber)
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
    except NoSuchElementException:
        return
    else:
        popupCloseButton.click()


def DisableHoveringJavaScriptObjects(browser):
    """Disables the two elements which prevent the script from
       selecting the villages correctly.
    """
    browser.execute_script("document.getElementById('map_mover').outerHTML = ''")
    browser.execute_script("document.getElementById('special_effects_container').outerHTML = ''")
    # for the headless option
    browser.execute_script("document.getElementById('linkContainer').outerHTML = ''")
    browser.execute_script("document.getElementById('footer').outerHTML = ''")
    browser.execute_script("document.getElementById('bottom').outerHTML = ''")


def CenterTheMapOnTargetVillageLocation(browser, villageLocation, locationInputBoxes):
    """Centers the map on the village which is the target of the attack.
       While selecting the village in next step map must
       be centered otherwise the locations of the villages do not correctly
       respond to the images which represent them on the map. If the map
       wouldn't be centered the script wouldn't be able to click on the targeted village.
    """
    try:
        for (locationInputBox, locationCordinateXY) in zip(locationInputBoxes, range(0, 2)):
            locationInputBox.clear()
            locationInputBox.send_keys(villageLocation.split("x")[locationCordinateXY])
            browser.find_element_by_class_name('btn').click()
            time.sleep(0.25)
    except IndexError:
        print('Please check whether village locations specified in barbarianVillageLocations.txt file are correct.')



def LocateTheVillageOnTheMap(browser, villageId):
    """Searches for the village based on the villageId provided in barbarianVillageIdList.txt.
       Then opens the attack form.
    """
    try:
        villagePosition = WebDriverWait(browser, 3).until(
            EC.element_to_be_clickable((By.ID, "map_village_" + villageId))
        )
    except TimeoutException:
        print('Village with id %s could not be located.\n Please check whether the %s and location in barbarianVillageIdList.txt and barbarianVillageLocations.txt are correct.' % villageId)

    villagePosition.click()
    attackButton = browser.find_element_by_id('mp_att')
    attackButton.click()


def CheckIfUserHasSufficientArmyUnits(browser, villageId, villageLocation):
    """Checks whether user poses enough units to perform attack he requsted.
    """
    try:
        browser.find_element(By.CSS_SELECTOR, '.autoHideBox.error')
    except NoSuchElementException:
        return True

    else:
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
    else:
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
    time.sleep(1)   ### This wait is necessary for opera and chrome browser
    unitsObjectInputList = browser.find_elements_by_class_name('unitsInput')
    for (inputObject, unitsQuantity) in zip(unitsObjectInputList, armyUnits):
        inputObject.send_keys(unitsQuantity)
    browser.find_element_by_id("target_attack").click()
    time.sleep(1)                                                                       ##### EDIT
    if CheckIfUserHasSufficientArmyUnits(browser, villageId, villageLocation):
        CheckIfUserAllowsSendingSingleTroops(browser, villageId, villageLocation, userSettings)
    else:
        browser.find_element_by_class_name('popup_box_close').click()


def main():
    userSettings = CreateDictionaryWithData("config.txt")
    barbarianVillageIdList = CreateDictionaryWithData("barbarianVillageIdList.txt")
    barbarianVillageLocations = CreateDictionaryWithData("barbarianVillageLocations.txt")
    armyUnits = CreateDictionaryWithData("attackSettings.txt")
    options = SetWebDriverOptions(userSettings)
    browser = ChooseBrowser(userSettings, options)
    if browser:
        browser.maximize_window()
        if LoginIntoTheGame(userSettings, browser):
            if SelectActiveWorld(browser, userSettings):
                DisableHoveringJavaScriptObjects(browser)
                locationInputBoxes = browser.find_elements_by_class_name("centercoord")
                for (villageLocation, villageId) in zip(barbarianVillageLocations.values(), barbarianVillageIdList.values()):
                    CenterTheMapOnTargetVillageLocation(
                        browser, villageLocation, locationInputBoxes)
                    LocateTheVillageOnTheMap(browser, villageId)
                    FillTheAttackForm(browser, armyUnits.values(),
                                      userSettings, villageLocation, villageId)
        print('\nAll of the operations for this execution of the script has been performed.')
        browser.quit()
    else:
        print('\nAn error occured please check the log displayed in your console.')

if __name__ == '__main__':
    main()
    input('\nPress ENTER to exit the console')
