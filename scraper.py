from bs4 import BeautifulSoup
import requests
import json
import os


def scrapePage(url, save_file_name):
    data = requests.get(url)
    soup = BeautifulSoup(data.text, 'html.parser')
    contents = soup.find_all(class_="ExResult-row")
    retval = []
    for content in contents:
        retval.append(extractDetails(content))
    with open(save_file_name, 'w') as outfile:
        json.dump(retval, outfile)
    if soup.find_all(class_="ExLoadMore-btn"):
        return {"moreContents": True}
    return {"moreContents": False}


def extractDetails(content):
    image = content.find_all("img")[0]["data-src"]
    name = content.find_all(class_="ExResult-resultsHeading")[0].get_text().strip()
    targeted_muscle = content.find_all(class_="ExResult-muscleTargeted")[0].find_all("a")[0].get_text().strip()
    equipment_used = content.find_all(class_="ExResult-equipmentType")[0].find_all("a")[0].get_text().strip()
    avg_rating = content.find_all(class_="ExRating-badge")[0].get_text().strip()
    details_page = content.find_all(class_="ExResult-resultsHeading")[0].find_all("a")[0].get_text().strip()
    return {
        "name": name,
        "image": image,
        "targeted_muscle": targeted_muscle,
        "equipment_used": equipment_used,
        "avg_rating": avg_rating,
        "details_page": details_page
    }


def scrapeAllExercises():
    totalPages = 206
    for pageNum in range(1, totalPages+1):
        url = "https://www.bodybuilding.com/exercises/finder/"+ str(pageNum) + "/?undefined"
        save_file_name = "./allExercises/allExercises_pageNum_" + str(pageNum) + ".json"
        scrapePage(url, save_file_name)



def scrapeAllExercisesBasedOnType():
    types = [
        "cardio",
        "olympic-weightlifting",
        "plyometrics",
        "powerlifting",
        "strength",
        "stretching",
        "strongman"
    ]
    for typ in types:
        pageNum = 1
        while True:
            url = "https://www.bodybuilding.com/exercises/finder/"+ str(pageNum) +"/?exercise-type=" + typ
            save_directory = "./ExercisesType/" + typ + "/"
            if not os.path.exists(save_directory):
                os.makedirs(save_directory)
            save_file_name = save_directory + str(pageNum) + ".json"
            pageNum += 1
            if not scrapePage(url, save_file_name)["moreContents"]:
                break




def scrapeAllExercisesBasedOnLevel():
    levels = [
        "beginner",
        "intermediate",
        "expert"
    ]
    for level in levels:
        pageNum = 1
        while True:
            url = "https://www.bodybuilding.com/exercises/finder/"+ str(pageNum) +"/?level=" + level + "&cacheBust=1"
            save_directory = "./ExercisesLevel/" + level + "/"
            if not os.path.exists(save_directory):
                os.makedirs(save_directory)
            save_file_name = save_directory + str(pageNum) + ".json"
            pageNum += 1
            if not scrapePage(url, save_file_name)["moreContents"]:
                break
    

def scrapeAllExercisesBasedOnMechanicsType():
    mechanics_type = [
        "compound",
        "isolation",
        "not-available"
    ]
    for mechanics in mechanics_type:
        pageNum = 1
        while True:
            url = "https://www.bodybuilding.com/exercises/finder/"+ str(pageNum) +"/?mechanics-type=" + mechanics + "&cacheBust=1"
            save_directory = "./ExercisesMechanics/" + mechanics + "/"
            if not os.path.exists(save_directory):
                os.makedirs(save_directory)
            save_file_name = save_directory + str(pageNum) + ".json"
            pageNum += 1
            if not scrapePage(url, save_file_name)["moreContents"]:
                break



# scrapeAllExercisesBasedOnMechanicsType()

# data = scrapePage("https://www.bodybuilding.com/exercises/finder/3/?exercise-type=cardio", "dont.json")
# print(data["moreContents"])