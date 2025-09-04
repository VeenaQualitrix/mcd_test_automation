# python-behave-appium
BDD test project writen in python using the appium-python-client and behave to implement behavior driven development.
Allure is added for reporting.

###  PreRequisites 


# Install:

pip install -r requirements.txt


# Execute - command :

pytest -m <tagName> --plateform=<platform_name> 

For web : pytest -m McdRegression --platform=web
For Android : pytest -m McdRegression --platform=android
For iOS : pytest -m McdRegression --platform=ios


* Valid Plateform Names - web,android,ios 
* file should place under src\builds*
**--consecutive_failure_abort**- default is True , False -to  disable execution abortion
**--consecutive_failure_count** -default is 5, if consecutive_failure_abort is true then execution abort after 5 consequitive failure
**--screenShotToggle** -- default is False - to add All Screen shot for passed Test cases too (before and after every action)


# Report:


allure generate

allure serve

allure open

# Docker Setup

docker run -p 9000:9000 -it -v  D:\Qualitrix\Indee\Indee_App_Automation:/home appautomation:1 /bin/bash 
cd /home
pip install -r requirements.txt
touch /root/.Xauthority 
Xvfb :99 -screen 0 1024x768x24 & export DISPLAY=:99  


# References:
appium-python-client: https://pypi.org/project/Appium-Python-Client/

behave: https://behave.readthedocs.io/en/latest/

allure: https://allurereport.org/docs/behave/

Android Studio has been used to emulate device