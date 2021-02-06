import requests
from joke.jokes import *
import random


def respond(data):
    if data[0:2] != "!!":
        return "I'm sorry! I don't recongize that command! Type '!! help' for possible options"
    text = data[2:]

    words = text.split()
    if words[0] == "about":
        return "My name is butler-bot! I'm a bot designed by my master Rami to suite everyone's needs!"
    elif words[0] == "help":
        return "Oh dear! I'm sorry you're having trouble. I'll try as best I can to help you. These are the commands I recognize: !! about | !! help | !! funtranslate | !! chuck | !! dance"
    elif words[0] == "funtranslate":
        term = ""
        for word in words[2:]:
            term = term + "%" + word
        r = requests.get(
            "http://api.funtranslations.com/translate/shakespeare?text="
            + str(words[1])
            + str(term)
        )
        try:
            translation = r.json()["contents"]["translated"]
        except (KeyError):
            return (
                "Sorry! funtranslate API has reached its rate limit. Try again later!"
            )
        transwords = translation.split("%")
        final = ""
        for t in transwords:
            final = final + t + " "
        return final
    elif words[0] == "chuck":
        return chucknorris()
    elif words[0] == "dance":
        return "*dances uncontrollably*\n...well sir/madam, I'm sorry you had to see that, but it was my best attempt."
    else:
        return "I'm sorry! I don't recongize that command! Type '!! help' for possible options"
