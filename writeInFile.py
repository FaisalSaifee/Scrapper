# Import libraries
import requests
import urllib.request
import time
from bs4 import BeautifulSoup
import csv
import re
import pandas as pd 


def write_in_file(siteUrl):
    finalSiteUrl = "https://www.screener.in" + siteUrl
    print(finalSiteUrl)
    time.sleep(1)
    print("final")
    responseOne = requests.get(finalSiteUrl)
    soupOne = BeautifulSoup(responseOne.text, "html.parser")
    
    success = soupOne.find("div", class_ = "success")
    warning = soupOne.find("div", class_ = "warning")
    text_warning = warning.get_text()
    text = success.get_text()
    total_points = text.count("\n")
    total_points = total_points -2
    warning_total_points = text_warning.count("\n")
    warning_total_points = warning_total_points - 2
    final = finalSiteUrl + "\t" + str(total_points) + "\t" + str(warning_total_points)
    
    #file1 = open("myfile.txt","w") 
    file1 = open("myfile.txt","a+") 
    file1.write("\n") 
    file1.write(final) 
    file1.close() 

#write_in_file("/company/DFMFOODS/")