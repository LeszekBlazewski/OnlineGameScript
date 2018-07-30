            ################################################################################
            #                          FIRST STEPS FOR ANY PLATFORM                        #
            #        Everything you need to know about the installation process            #
            ################################################################################

1. Requirements to use the script.

A) Both platforms are supported - Linux and Windows.

B) Installed python - 3.6.6 version recommended with environmental variables set up.
   There are many tutorials floating around the net just type "install python on windows/linux" based on your OS in goggle and follow the guide.
   Remember to download the 3.6.6 version from: https://www.python.org/

2. Supported browsers for this script are :
    1)Firefox
    2)Chrome
    3)Opera

3. Download the driver for the chosen browser and operating system.
  A) After choosing your browser:

    a) Firefox - navigate to https://github.com/mozilla/geckodriver/releases
       From the list choose driver which correctly corespondents to your operation system needs.

    b) Chrome - navigate to https://sites.google.com/a/chromium.org/chromedriver/downloads
       At top of the page there will be a link which will forward you to the download page.
       From the list of files choose the driver which suits your operation system.

    c) Opera - navigate to https://github.com/operasoftware/operachromiumdriver/releases
       From the list choose driver which correctly corespondents to your operation system needs.


            ################################################################################
            #                       Instruction for LINUX users                            #
            ################################################################################

4. Set up the downloaded driver properly.

    A) Step 1.
       Extract the downloaded file by using this command in terminal:

       tar -xvzf nameOfYourDriver

       where nameOfYourDriver is dependent on the browser you have chosen.

       Example for firefox - geckodriver-v0.21.0-linux64.tar.gz, Chrome - chromedriver_linux64.zip etc.

       NOTE EXAMPLE MAY NOT MUCH THE ACTUAL NAME OF THE DRIVER SINCE NEW DRIVERS ARE RELEASED AS THE BROWSERS GET UPDATES.

    B) Step 2.
       Put the extracted driver in directory which is added to the system variable $PATH.

       a) Check your $PATH variable by running this script in terminal:

       echo $PATH

       Option 1:

       If you are able to locate the /usr/bin directory in your terminal than execute this commands:

       sudo chmod +x nameOfYourDriver
       sudo mv nameOfYourDriver /usr/bin/

       Option 2:

       If you are NOT able to see /usr/bin directory in your terminal you have to add it to your system variables.

       You can edit the ~/.bashrc file manually with any text editor and add this line to it : PATH=$PATH:/usr/bin

       or you can simply type this into your terminal and press enter:

       echo "PATH=\$PATH:/usr/bin" >> ~/.bashrc

       After executing the script above the directory /usr/bin should be in the $PATH variable (you can check it with command: echo $PATH)

       *** NOW MOVE ONTO OPTION NUMBER 1 !!! Execute the commands written in that part. ***


            ################################################################################
            #                       Instruction for WINDOWS users                          #
            ################################################################################

4. Set up the downloaded driver properly.

  A) Step 1.
     Extract the downloaded file.










































Now you are good to go !
Proceed and open the README2_HOW_2_USE_THE_SCRIPT_GUIDE.txt where any necessary information about the use of the script is provided.
