import random
from urllib import request
import requests as r
def icq(phone):
    try:
        url = 'https://u.icq.net/api/v70/rapi/auth/sendCode'
        payload = {
    "reqId": "39475-1649148569",
    "params": {
    "phone": phone,
    "language": "ru-RU",
    "route": "sms",
    "devId": "ic1rtwz1s1Hj1O0r",
    "application": "icq"
    }
}
        a = r.post(url, json=payload)
        print(a.text)
    except Exception as e:
        print(e)

icq("79811687383")




def generatePassword():
    letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    smallLetters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    mail = ""
    password = ""
    name = ""
    lastName = ""
    for i in range(10):
        temp = random.randint(1, 3)
        if temp == 1:
            password += random.choice(letters)
        elif temp == 2:
            password += random.choice(smallLetters)
        else:
            password += str(random.choice(numbers))
    lastName = mail = name = password
    return [name, lastName, mail, password]