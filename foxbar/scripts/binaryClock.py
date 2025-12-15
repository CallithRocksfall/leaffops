import datetime
import json


def encodeBinaryString(binaryString):
    return binaryString.replace(
        "0", "<span color='#729b79'>" + "" + "</span>\n"
    ).replace("1", "<span color='#729b79'>" + "" + "</span>\n")


def addDivider():
    return "<span color='#489ca5'>" + "" + "</span>\n"


now = datetime.datetime.now()
hour = int(now.strftime("%H"))
minute = int(now.strftime("%M"))
hourBin = "{0:06b}".format(hour)
minuteBin = "{0:06b}".format(minute)

result = encodeBinaryString(hourBin) + addDivider() + encodeBinaryString(minuteBin)[:-1]

print(json.dumps({"text": result}))
