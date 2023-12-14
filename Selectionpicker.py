import os
import bs4 as bs4
import csv as csv
import requests as requests

def get_url(url):
    """
    Funkce načte url a vrátí jej jako soup
    :param url: url adresa
    :return: soup
    """
    response = requests.get(url)
    soup = bs4.BeautifulSoup(response.text, "html.parser")
    return soup

def get_citydict(soup):
    """
    Funkce vytvoří tabulku ze soup a prevede ji do slovníku
    :param soup: soup
    :return: tabulka
    """
    table = soup.find_all("table", {"class": "table"})
    citydict = {}
    i = 1
    for row in table:
        names = row.find_all("tr")

        for name in names:
            if name.select("td:nth-of-type("+str(2)+")", text=True) == []:
                continue

            webpages = name.find_all("a", href=True)
            for webpage in webpages:

                link = (webpage.get("href"))

            if name.text.split("\n")[1] == []:
                print("test")
                continue
            citydict.update({f"result{i}": {"tag": name.text.split("\n")[1],
                                            "city": name.text.split("\n")[2],
                                            "link": link}})
            i += 1

    return citydict

def get_citydata(citydict, cityname):
    """
    Funkce vypíše výsledky hledání
    :param citydict: slovník s výsledky
    :param cityname: název města
    :return: výsledky hledání
    """

    userselection = {}
    found = False

    for key, value in citydict.items():
        if value["city"] == cityname:
            userselection["link"] = (f'https://volby.cz/pls/ps2017nss/{value["link"]}')
            userselection["city"] = (f"{value['city']}")
            userselection["tag"] = (f"Tag: {value['tag']}")
            found = True
            break

    if found == False:
        print("Město nenalezeno")

    return userselection



def user_input(Cityname):
    """
    Funkce načte vstup od uživatele
    :param Cityname: název města
    :return: vstup od uživatele a výsledky hledání
    """

    Link = get_citydata(get_citydict(get_url('https://volby.cz/pls/ps2017nss/ps3?xjazyk=CZ')), Cityname)
    return Link

def get_cities_url(Citylink):
    """
    Funkce vytvoří tabulku ze soup a prevede ji do slovníku
    :param soup: soup
    :return: tabulka
    """
    response = requests.get(Citylink["link"])
    soup = bs4.BeautifulSoup(response.text, "html.parser")
    table = soup.find_all("table", {"class": "table"})
    citiesdict = {}
    i = 1

    for row in table:
        rows = row.find_all("tr")

        for row in rows:
            if row.select("td:nth-of-type(" + str(2) + ")", text=True) == []:
                continue

            webpages = row.find_all("a", href=True)
            for webpage in webpages:
                if ("vyber") not in webpage.get("href"):
                    continue
                link = (webpage.get("href"))

            citiesdict.update({f"result{i}": {"tag": row.text.split("\n")[1],
                                            "city": row.text.split("\n")[2],
                                            "link": f'https://volby.cz/pls/ps2017nss/{link}'}})
            i += 1

    return citiesdict










