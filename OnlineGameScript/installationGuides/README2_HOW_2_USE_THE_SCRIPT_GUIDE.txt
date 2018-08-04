            ################################################################################
            #                             Guide to TribalWarsScript.py                     #
            #      Everything you need to know once you are set up and ready to farm!      #
            ################################################################################

*** Everything written here will ONLY work if you completed the guide in README1_INSTALATION_GUIDE.txt file ***

*** DO NOT CHANGE NAME OF THE FILES WITH .txt EXTENSIONS OTHERWISE THE SCRIPT WILL NOT WORK ***

*** FOLLOW THE SYSTEM OF WRITING IN .txt FILES OTHERWISE THE SCRIPT WON'T WORK PROPERLY ***

*** DO NOT INCLUDE SPACE AFTER THE HYPHEN (-) SIGN ***

*** NON OF THE PROVIDED DATA IS COLLECTED, ONCE YOU DOWNLOAD THE FILES FROM GITHUB I DO NOT HAVE ACCESS TO THEM ***

*** REMEMBER TO ALWAYS SAVE YOUR CONFIG.TXT FILE AFTER CHANGES OTHERWISE THE SCRIPT WILL USE OUTDATED DATA ***


            ################################################################################
            #                         Messing around with config.txt.                      #
            ################################################################################


This file stores all of the user data which is needed to properly handle operations performed by the script: logging to site, choosing world etc.

You can check out how sample config file looks like by opening the SampleConfig.txt file.


Username -- Here you enter the username which is used to log in to TribalWars site.
Password -- Password which is used to log in to the game site.
InternetBrowser -- You have 3 options here: firefox, chrome, opera
ActiveWorld -- Number of the world on which the script should work.
LinkToGameWebsite -- Here paste the link from your browser which you use to log in into the game when accessing your account.
AllowSendingOneTroopToTargetVillage -- There are two options yes/no

* ActiveWorld
  For example i am playing on two worlds - World_130 and World_148 ( These are chosen right after you successfully log in to the site ) ( The are displayed as beige buttons)
  You have to specify the number of world on which script should work. If you want to use it on multiple worlds just run the script over and over again with changed config.txt file

* LinkToGameWebsite
  Simply navigate to the site where you log in to the game whenever you want to play.
  When you have got displayed the site where you choose the active world on which you want to play, copy the URL from address bar and paste it in the config.txt file. (NOTE: DO NOT INCLUDE SPACE AFTER HYPHEN - )

*AllowSendingOneTroopToTargetVillage
  There is always a warning whenever you are trying to send 1 troop to village so this options allows or disallows it.


Once you are done with editing your config.txt it's time for extracting information about the targeted villages. Proceed onto the next step.

            ################################################################################
            #                         Data extraction for:                                 #
            #                       - barbarianVillageIdList.txt                           #
            #                       - barbarianVillageLocations.txt                        #
            ################################################################################

This two files ( barbarianVillageIdList.txt and barbarianVillageLocations.txt) contain the information about the targeted villages.
In order to make the script work you have to extract the specific id which reefer to villages where you want to send your troops.

You can check out how sample barbarianVillageIdList and barbarianVillageLocations files look like by opening the Sample files with equivalent names.
I know that it does not look as clear as previous file but you will get it in a sec !
I promise :)

The file barbarianVillageIdList.txt contains 5 digit Id's of the villages where you want to send your attack.
In addition to that barbarianVillageLocations.txt contains the coordinates of the villages where you want to send your attack.

Step 1 Locate the villages where the attacks will be sent - Every barbarian village you are willing to farm can be added to the file.

    A) Get the coordinates of the villages in this format XcoordinatexYcordinate ( note the x in the middle ) - See barbarianVillageLocations.txt for sample looks of the file.

      These are simple the map coordinates which you see on the border of the map. The map is divided into squares and the X and Y coordinates only correspond to one square of the map.

      When you are getting the coordinates you can also gather the id of the map. ( See B step to get it.)

    B) extract the id of the specific village.

    *** FOR EASIER SETUP WATCH THE VIDEO get_the_id_of_the_targeted_village.mp4  ***

    This is the hardest step of the whole configuration.

    No worry tho I will keep it as simple as possible.

    While you are harvesting locations you can also get the id. Here is the step by step guide to do it:

    1. Navigate to the map where you can send attacks from.

    2. Put your mouse cursor on the image of the village which x and y coordinates you already have and right click it.

    3. From the drop down menu chose: Inspect Element.

    4. Once the console is opened you will see a bunch of code - don't worry tho, keep it cool.

    5. After right clicking your mouse on the village don't move the mouse cursor. Just look at the code and check this line: <a id="map" href="/game.php?village=67762&screen=info_village&id=63886&"

    6. As you can see the id which we are looking for is right at the end of the link !

    NOTES:

    *** WHEN EXTRACTING THE ID OF THE VILLAGE PLACE IT IN THE barbarianVillageIdList.txt WITHOUT THE & SIGN ! ***

    *** THIS IS ONLY AN EXAMPLE THE ID WILL NOT MATCH THE VILLAGE YOU ARE INSPECTING ***


LAST BUT NOT LEAST

The id's and locations of the villages have to match each other ! See the example below:

in the barbarianVillageIdList.txt we have

village1-69742

and respectively in barbarianVillageLocations.txt we have

village1-746x846

This coordinates REFER to the id of the SAME village. ( This is basically the same village !!!)
