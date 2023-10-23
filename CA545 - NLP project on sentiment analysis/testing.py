import speech_recognition as sr

r = sr.Recognizer()

# with sr.AudioFile('data/sample_female_call_recording.wav') as source:
#     audio = r.listen(source)
#     try:
#         text = r.recognize_google(audio)
#         print('Working on ...')
#         print(text)
#     except:
#         print('Error: Try again.')

max_iter = 5
index = 0
fptr = open('read.txt', 'w')

while index < max_iter:
    # Using the system's default microphone as the source
    with sr.Microphone(device_index=1) as source:
        print()
        print('Say Something ...')
        audio = r.listen(source, timeout=3)
        r.adjust_for_ambient_noise(source, duration=5)

        try:
            text = r.recognize_google(audio)
            print(text)
            fptr.write(text + '\n')
        except:
            print('ERROR: Try again.')

        index = index + 1

fptr.close()
