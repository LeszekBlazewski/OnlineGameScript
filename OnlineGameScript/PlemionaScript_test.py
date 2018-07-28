"""File name: PlemionaScript_test.py
   Author: Leszek Błażewski
   Description: Script used to test all possible outputs
   of the PlemionaScript.py
"""

import PlemionaScript as ps
import unittest


class TestBrowser(unittest.TestCase):
    """Contains tests which refere to browser settings and options."""

    def setUp(self):
        self._userSettings = {'InternetBrowser': 'Firefox',
                              'Username': 'ValidUserName', 'Password': 'ValidPassword'}
        self._options = ps.SetWebDriverOptions()
        self._browser = ps.ChooseBrowser(self._userSettings, self._options)

    def test_SettingWebDriverOptionsToheadless(self):
        options = ps.SetWebDriverOptions()
        assert options.arguments[0] == '-headless'

    def test_ChooseFirefoxBrowser(self):
        browser = ps.ChooseBrowser(self._userSettings, self._options)
        assert browser.capabilities['browserName'] == 'firefox'
        browser.quit()

    def test_LoggingToGameSiteWithValidData(self):
        assert ps.LoginIntoTheGame(self._userSettings, self._browser)

    def test_LoggingToGameSiteWithInvalidData(self):
        # Enter invalid username into the dictionary in order to test the result.
        self._userSettings['Username'] = 'InvalidLogin'
        assert not ps.LoginIntoTheGame(self._userSettings, self._browser)

    def tearDown(self):
        self._browser.quit()


class TestUtilities(unittest.TestCase):
    """Contains test which refere to other functions used by the browser within PlemionaScript.py"""

    def test_CreateDictionaryWithData(self):
        userSettings = ps.CreateDictionaryWithData("config.txt")
        assert isinstance(userSettings, dict)
