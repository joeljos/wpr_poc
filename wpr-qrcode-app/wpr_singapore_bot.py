import os
import requests
import json
import re
import appconfig
import display_html
from requests_toolbelt.multipart.encoder import MultipartEncoder
from werkzeug.utils import secure_filename


bot_email, bot_name = None, None

bearer = appconfig.bearer # BOT'S ACCESS TOKEN

roomids = appconfig.roomids

headers = {
    "Accept": "application/json",
    "Content-Type": "application/json; charset=utf-8",
    "Authorization": "Bearer " + bearer
}

UPLOAD_FOLDER = appconfig.UPLOAD_FOLDER

def send_spark_post(url, data):
    result = requests.post(url, json.dumps(data), headers=headers)
    return result

def runme(request):
    arguments = []
    arguments.append(request.form["machineid"])
    arguments.append(request.form["descr"])
    arguments.append(request.form["ccoid"])
    f = None
    try:
        f = request.files['image']
    except Exception as e:
        print("Exception raised!!",e)
    if(arguments[1] != "" and arguments[2] != ""):
        descr = "An issue '"+arguments[1]+"' with '"+arguments[0]+"' has been reported by '"+arguments[2]+"'."
    elif(arguments[1] != "" and arguments[2] == "") :
        descr = "An issue '"+arguments[1]+"' with '"+arguments[0]+"' has been reported."
    elif(arguments[1] == "" and arguments[2] != "") :
        descr = "An issue with '"+arguments[0]+"' has been reported by '"+arguments[2]+"'."  
    else:
        descr = "An issue with '"+arguments[0]+"' has been reported."
    count = 0
    while(True):
        if (f):
            print("****",f)
            filename = secure_filename(f.filename)
            filepath = os.path.join(UPLOAD_FOLDER, filename)
            f.save(filepath)
            m = MultipartEncoder({'roomId': roomids[arguments[0]],
                        'text': "",
                        "markdown": descr,
                        'files': (filename, open(filepath, 'rb'),
                        'image/jpg')})
            result = requests.post('https://api.ciscospark.com/v1/messages', data=m,
                        headers={'Authorization': 'Bearer '+ bearer,
                        'Content-Type': m.content_type})
        else:
            result = send_spark_post("https://api.ciscospark.com/v1/messages",
                                    {
                                        "roomId": roomids[arguments[0]],
                                        "markdown": descr
                                    }
                                    )
        if(result.status_code == 200 or count == 100):
            os.remove(filepath)
            break
        count = count + 1
    return display_html(count,arguments[0])


