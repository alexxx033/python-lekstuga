# We will work as follows:
#
# Connect Python to our web browser and access the website (Expedia in our example here).
# Choose the ticket type based on our preference(round trip, one way, etc.).
# Select the departure country.
# Select the arrival country(if round trip).
# Select departure and return dates.
# Compile all available flights in a structured format(for those who love to do some exploratory data analysis!).
# Connect to your email.
# Send the best rate for the current hour.


# Selenium (for accessing websites and automation testing)

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Pandas (we will mainly just used Pandas for structuring our data):

import pandas as pd

# Time and date-time (for using delays and returning current time

import time
import datetime

# We need those for connecting to our email and sending our message

import smtplib
from email.mime.multipart import MIMEMultipart

# This will open an empty browser telling you that this browser is being controlled by automated test software

browser = webdriver.Chrome(executable_path='.\chromedriver\chromedriver.exe')

# store the tags and ids for the three different ticket types
# Setting ticket types paths
ekonomi_ticket = "//li[@id="e"]"
premium_ekonomi_ticket = "//li[@id="p"]"
business_ticket = "//li[@id="b"]"
first_ticket = "//li[@id="f"]"
multi_ticket = "//li[@id="m"]"

# Then I define a function to choose a ticket type


def ticket_chooser(ticket):
    try:
        ticket_type = browser.find_element_by_xpath(ticket)
        ticket_type.click()
    except Exception as e:
        pass

# Below I define a function to choose the departure country


def dep_country_chooser(dep_country):
    fly_from = browser.find_element_by_xpath("//input[@id=""]")
    time.sleep(1)
    fly_from.clear()
    time.sleep(1.5)
    fly_from.send_keys("  " + dep_country)
    time.sleep(1.5)
    first_item = browser.find_element_by_xpath("//a[@id=""]")
    time.sleep(1.5)
    first_item.click()
