import requests

response = requests.get("https://coinmarketcap.com/").content

splitted_response = response.split("<span>")

for text in splitted_response:
    if text.startwith("$"):
        for text2 in text.split("</span"):
            if text2.startwith("$") and text2[0].isdigit():
                print(text)