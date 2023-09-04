# pip install googletrans==4.0.0-rc1

import googletrans

translator = googletrans.Translator();

str1="행복하세요"
result1 = translator.translate(str1, dest='en', src='auto')
print("행복하세요 : ", result1.text)

str2="good luck to you"
result2 = translator.translate(str2, dest='ko', src='en')
print(f"good luck to you : {result2.text}")