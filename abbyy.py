import requests
import datetime 
import os

# Receive an authentication token from Abbyy Lingvo and 
# store it in the variable `auth`. The token is used to
# consume endpoints.
URL_AUTH = "url_here"
KEY = "key_here" 
headers_auth = {"Authorization": "Basic " + KEY}
auth = requests.post(URL_AUTH, headers=headers_auth)

# Endpoints  
# Миникарточка для краткого перевода слов или фраз
URL_MINICARD = "end_point_here"
# NOT USING RIGHT NOW. Словарьный перевод слов или фраз
URL_DICT = "another_end_point"
# NOT USING RIGHT NOW. Словоформы для слова
URL_DICT = "another_end_point"

# Create a file to store vocabulary
# The file is named after the date
# If the file already exists, then append to it.
filename = str(datetime.date.today()) 
if os.path.isfile(filename):
    fout = open(filename, 'a', encoding='utf-8')
else:
    fout = open(filename, 'w+', encoding='utf-8')

if auth.status_code == 200:
    token = auth.text
    while True:
        word = input("Введите слово для перевода: ")
        if word != "done":
            headers_abbyy= {
                    "Authorization": "Bearer " + token
            }
            params_minicard = {
                    "text": word,
                    "srcLang": 1049,
                    "dstLang": 1033 
            }
            # NOT USING RIGHT NOW.
            params_dict = {
                    "text": word,
                    "srcLang": 1049,
                    "dstLang": 1033,
                    "isCaseSensitive": False
            }
            # NOT CURRENTLY USING 
            params_wordforms = {
                    "text": word,
                    "lang": 1049
            }
            card = requests.get(URL_MINICARD, headers=headers_abbyy, params=params_minicard )
            res_card = card.json()
            short_translation = res_card["Translation"]["Translation"]

            try:
                print("Значение", short_translation)
                print(word, ":", short_translation, file=fout) 
            except:
                print("Слова не найдёна")
        else:
            break
else:
    print("Ошибка: auth не равно 200")

fout.close()
