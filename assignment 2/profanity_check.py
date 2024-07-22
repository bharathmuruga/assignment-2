import requests

def user_input():
    return input("Enter the sentence: ")

def profanity(user_sentence):
    url = "https://www.purgomalum.com/service/containsprofanity"

    params = {
        "text": user_sentence
    }

    response = requests.get(url, params=params)
    response.raise_for_status()

    return response.text == "true"

def display(is_profanity):
    if is_profanity:
        print("Bad word detected!")
    else:
        print("No bad word found")

user_sentence = user_input()
is_profanity = profanity(user_sentence)
display(is_profanity)
