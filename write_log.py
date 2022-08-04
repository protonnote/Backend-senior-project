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

def read_log(code):
    filename = 'user_database.json'
    listObj = []
    try :
        if path.isfile(filename) is False:
            raise Exception("File not found")

        # # Read JSON file
        with open(filename) as fp:
            listObj = json.load(fp)
        
        for i in range(len(listObj)):
            if int(listObj[i]['Code']) == code :
                return True, listObj[i]['Name']

        # return True, len(listObj)

    except Exception as e :
        print(e)
        return False,"None"