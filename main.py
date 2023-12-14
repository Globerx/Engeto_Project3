"""
projekt_3.py: třetí projekt do Engeto Online Python Akademie

author: Jiri Gloza
email: gloza.jiri@gmail.com
"""

import sys
import bs4 as bs4
import csv as csv
import requests as requests
from Selectionpicker import user_input, get_cities_url
from Scrappingmodule import get_all_data



def main(City, File):
    """
    Hlavní funkce programu
    :return: výsledky hledání
    """
    CitiesLink = user_input(City)
    Citylink = get_cities_url(CitiesLink)

    print(f"stahuji data pro vybrane mesto. Vas vyber > Mesto:{CitiesLink['city']}, URL:{CitiesLink['link']}")
    get_all_data(Citylink, File)
    print("hotovo")
    return Citylink

#if __name__ == "__main__":
    #main(str(sys.argv[1]), str(sys.argv[2]))

main("Praha", "Praha.csv")


