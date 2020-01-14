import os, json


def mergeAllExercisesData():
    data = readJsonsInDirectory("./allExercises")
    for key in data:
        directory = "./final_data/allExercises/"
        if not os.path.exists(directory):
            os.makedirs(directory)
        saveJson(directory+key+".json", data[key])


def mergeExercisesLevelData():
    data = readJsonsInDirectory("./ExercisesLevel")
    for key in data:
        directory = "./final_data/ExercisesLevel/"
        if not os.path.exists(directory):
            os.makedirs(directory)
        saveJson(directory+key+".json", data[key])


def mergeExercisesMechanicsData():
    data = readJsonsInDirectory("./ExercisesMechanics")
    for key in data:
        directory = "./final_data/ExercisesMechanics/"
        if not os.path.exists(directory):
            os.makedirs(directory)
        saveJson(directory+key+".json", data[key])


def mergeExercisesTypeData():
    data = readJsonsInDirectory("./ExercisesType")
    for key in data:
        directory = "./final_data/ExercisesType/"
        if not os.path.exists(directory):
            os.makedirs(directory)
        saveJson(directory+key+".json", data[key])


def readJsonsInDirectory(directory):
    retval = {}
    for root, dirs, files in os.walk(directory):
        for name in files:
            key_name = os.path.basename(root)
            if not key_name in retval:
                retval[key_name] = []
            file_content = readJson(os.path.join(root,name))
            for cont in file_content:
                retval[key_name].append(cont)
    return retval 



def readJson(file_path_name):
    with open(file_path_name, "r") as infile:
        return json.load(infile)


def saveJson(save_path_name, data):
    with open(save_path_name, 'w') as outfile:
        json.dump(data, outfile)



mergeAllExercisesData()
mergeExercisesLevelData()
mergeExercisesMechanicsData()
mergeExercisesTypeData()