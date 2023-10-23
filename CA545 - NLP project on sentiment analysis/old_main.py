# OLDER CODE THAT WE IMPLEMENTED

import nltk

# # This will open a GUI window where we can manually download nltk library files etc.
# nltk.download()

# # Manually installing some more library modules
# nltk.download('punkt')
# nltk.download('averaged_perceptron_tagger')
# nltk.download('brown')

from textblob import TextBlob as blob

tb = blob('Hey! We won. All we need to do now is win the next game, and we will be the champions of this season.')
print(tb)

# To read the user manual
print(help(tb))

# Prints the tags in the sentence
print(tb.tags)

# Prints the noun phrases in the sentence
print(tb.noun_phrases)

# Prints the sentiment of the sentence
print(tb.sentiment)

# Doing this for another sentence
tb = blob('I love you Andrea. You know I will always protect you, no matter what.')
print(tb.sentiment)

import speech_recognition as sr

r = sr.Recognizer()

max_iter = 5
index = 0

# # Prints the list of all available microphones on the system
# print(sr.Microphone.list_microphone_names())

while index < max_iter:
    # Using the system's default microphone as the source
    with sr.Microphone(device_index=1) as source:
        print()
        print('Say Something ...')
        audio = r.listen(source, timeout=3)
        r.adjust_for_ambient_noise(source, duration=5)
        # r.energy_threshold()

        try:
            text = r.recognize_google(audio)
            tb = blob(text)
            print(text)
            print('The polarity of the sentence is', tb.sentiment.polarity,
                  'and the subjectivity of the sentence is', tb.sentiment.subjectivity)
        except:
            print('ERROR: Try again.')

        index = index + 1
