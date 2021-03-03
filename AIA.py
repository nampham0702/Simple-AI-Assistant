import speech_recognition
import pyttsx3
from datetime import date, datetime
aia_record = speech_recognition.Recognizer()
aia_sound = pyttsx3.init()
aia_process = ""
while True:
    with speech_recognition.Microphone() as mic:
        print("AIA: I'm listening")
        audio = aia_record.listen(mic)
    print("AIA:...")
    try:
        you = aia_record.recognize_google(audio)
    except:
        you == ""
    print ("You: " +you)
    if you == "":
        aia_process = " I can't hear you, please try again!"
    elif  "hello" in you:
        aia_process =  "Hello Nam"
    elif "today" in you:
        today = date.today()
        aia_process = today.strftime("%B %d, %Y")
    elif "time" in you:
        now = datetime.now()
        aia_process =  now.strftime("%H hours %M minutes %S seconds")
    elif "rock band" in you:
        aia_process = "Aerosmith"
    elif "bye" in you:
        aia_process = "bye nam"
        print("AIA: " + aia_process)
        aia_sound.say(aia_process)
        aia_sound.runAndWait()
        break
    else:
        aia_process="Sorry, i don't understand."
    print("AIA: " +aia_process)
    aia_sound.say(aia_process)
    aia_sound.runAndWait()
