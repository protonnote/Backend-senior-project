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
    try:
        return _extracted_from_read_log_5(filename, code)
            # return True, len(listObj)

    except Exception as e :
        print(e)
        return False,"None"


# TODO Rename this here and in `read_log`
def _extracted_from_read_log_5(filename, code):
    if path.isfile(filename) is False:
        raise Exception("File not found")

    # # Read JSON file
    with open(filename) as fp:
        listObj = json.load(fp)

    re_bool = False
    re_name = "None"

    for i in range(len(listObj)):
        if int(listObj[i]['Code']) == code :
            re_bool = True
            re_name = listObj[i]['Code']


    return re_bool, re_name