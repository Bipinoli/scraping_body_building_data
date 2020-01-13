from bs4 import BeautifulSoup
import requests
import json


def scrapePage(url, save_file_name):
    data = requests.get(url)
    soup = BeautifulSoup(data.text, 'html.parser')
    contents = soup.find_all(class_="ExResult-row")
    retval = []
    for content in contents:
        retval.append(extractDetails(content))
    with open(save_file_name, 'w') as outfile:
        json.dump(retval, outfile)


def extractDetails(content):
    image = content.find_all("img")[0]["data-src"]
    name = content.find_all(class_="ExResult-resultsHeading")[0].get_text().strip()
    targeted_muscle = content.find_all(class_="ExResult-muscleTargeted")[0].find_all("a")[0].get_text().strip()
    equipment_used = content.find_all(class_="ExResult-equipmentType")[0].find_all("a")[0].get_text().strip()
    avg_rating = content.find_all(class_="ExRating-badge")[0].get_text().strip()
    details_page = content.find_all(class_="ExResult-resultsHeading")[0].find_all("a")[0].get_text().strip()
    return {
        name: name,
        image: image,
        targeted_muscle: targeted_muscle,
        equipment_used: equipment_used,
        avg_rating: avg_rating,
        details_page: details_page
    }


def scrapeAllExercises():
    totalPages = 206
    for pageNum in range(1, totalPages+1):
        url = "https://www.bodybuilding.com/exercises/finder/"+ str(pageNum) + "/?undefined"
        save_file_name = "allExercises_pageNum_" + str(pageNum) + ".json"
        scrapePage(url, save_file_name)



scrapeAllExercises()