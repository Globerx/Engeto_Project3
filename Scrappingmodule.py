from bs4 import BeautifulSoup
import requests
from Selectionpicker import user_input, get_citydata, get_citydict, get_url, get_cities_url
import os
import csv


def get_all_data(Citylink, File):
    """
    """
    print(f"Zapisuji data do CSV souboru {File}")
    with open(File, mode="w") as nove_csv:
        i = 0
        PartyDict = {"code": "code", "location": "location", "registered": "registered", "envelopes": "envelopes","valid": "valid", "party": "party", "votes": "votes", "percentage": "percentage"}
        helplink = "https://volby.cz/pls/ps2017nss/ps311?xjazyk=CZ&xkraj=2&xobec=534421&xvyber=2102"
        response = requests.get(helplink)
        soup = BeautifulSoup(response.text, "html.parser")
        parties = soup.find_all("td", {"headers": "t1sa1 t1sb2"})
        parties2 = soup.find_all("td", {"headers": "t2sa1 t2sb2"})
        votes = soup.find_all("td", {"headers": "t1sa2 t1sb3"})
        for party in parties:
            PartyDict.update({f"Party{i}" : party.text })
            i = i + 1
        for party in parties2:
            PartyDict.update({f"Party{i}" : party.text })
            i = i + 1


        zapisovac = csv.DictWriter(nove_csv, delimiter=";", fieldnames=(PartyDict.values()))
        zapisovac.writeheader()
        for City in Citylink:
            if Citylink[City]["city"] == "-":
                break
            SaveLink = Citylink[City]["link"]
            SaveTag = Citylink[City]["tag"]
            SaveCity = Citylink[City]["city"]
            response = requests.get(SaveLink)
            soup = BeautifulSoup(response.text, "html.parser")
            table = soup.find_all("table", {"class": "table"})
            i = 0
            partyvotes = {}
            for wrapper in table[0].find_all("td", {"headers": "sa2"}):
                registered = wrapper.text
            for wrapper in table[0].find_all("td", {"headers": "sa3"}):
                envelopes = wrapper.text
            for wrapper in table[0].find_all("td", {"headers": "sa6"}):
                valid = wrapper.text
            for wrapper in table[0].find_all("td", {"headers": "sa7"}):
                percentage = wrapper.text
            for wrapper in table[1].find_all("td", {"headers": "t1sa2 t1sb3"}):
                votes = wrapper.text
                partyvotes.update({f"Party{i}": votes})
                i = i + 1
            x = i
            for wrapper in table[2].find_all("td", {"headers": "t2sa2 t2sb3"}):
                votes = wrapper.text
                partyvotes.update({f"Party{x}": votes})
                x = x + 1


            zapisovac.writerow({"code": SaveTag, "location": SaveCity, "registered": registered, "envelopes": envelopes,"valid": valid, "percentage": percentage,
                                PartyDict['Party0']: partyvotes['Party0'], PartyDict['Party1']: partyvotes['Party1'], PartyDict['Party2']: partyvotes['Party2'], PartyDict['Party3']: partyvotes['Party3'],
                                PartyDict['Party4']: partyvotes['Party4'], PartyDict['Party5']: partyvotes['Party5'], PartyDict['Party6']: partyvotes['Party6'], PartyDict['Party7']: partyvotes['Party7'],
                                PartyDict['Party8']: partyvotes['Party8'], PartyDict['Party9']: partyvotes['Party9'], PartyDict['Party10']: partyvotes['Party10'], PartyDict['Party11']: partyvotes['Party11'],
                                PartyDict['Party12']: partyvotes['Party12'],
                                PartyDict['Party13']: partyvotes['Party13'], PartyDict['Party14']: partyvotes['Party14'], PartyDict['Party15']:
                                partyvotes['Party15'], PartyDict['Party16']: partyvotes['Party16'],
                                PartyDict['Party17']: partyvotes['Party17'], PartyDict['Party18']: partyvotes['Party18'], PartyDict['Party19']:
                                partyvotes['Party19'], PartyDict['Party20']: partyvotes['Party20'],
                                PartyDict['Party22']: partyvotes['Party21'], PartyDict['Party22']: partyvotes['Party22'], PartyDict['Party23']:
                                partyvotes['Party23'], PartyDict['Party24']: partyvotes['Party24'],
                                PartyDict['Party25']: partyvotes['Party25']})
        print(f"Dokoncen zapis CSV souboru {File}")
