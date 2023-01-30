import json
from os import path


def save_log(dic):
    filename = 'prediction_log.json'
    listObj = []
    try :
        if path.isfile(filename) is False:
            raise Exception("File not found")

            # # Read JSON file
        with open(filename) as fp:
            listObj = json.load(fp)
        
        listObj.append(dic)
            
        with open(filename, 'w') as json_file:
            json.dump(listObj, json_file, 
                                indent=4,  
                                separators=(',',': '))
        return True
    except Exception as e :
        print(e)
        return False

def read_log(pin_code):
    filename = 'user_database.json'
    listObj = []
    re_bool = False
    re_name = "None"

    with open(filename) as fp:
        listObj = json.load(fp)

    # print(listObj)

    for i in listObj:
        if i['Pin'] == pin_code :
            re_bool = True
            re_name = i['Name']

    return re_bool, re_name

