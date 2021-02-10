import pyttsx3
import speech_recognition as sr 
import datetime
import wikipedia 
import webbrowser
import os
import smtplib
import sys 
import pyjokes
import randfacts

engine = pyttsx3.init('sapi5')  #windows API for accepting voice(sapi5) inbuilt in windows
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        print("Good Morning! smith")
        speak("Good Morning smith")

    elif hour>=12 and hour<18:
        print("Good Afternoon! smith")
        speak("Good Afternoon smith")   

    else:
        print("Good Evening! smith")
        speak("Good Evening smith")  

    print("I am your Medical AI Voice Assistant. I can suggest home remedies for your medical problems but if the problems are severe please consider contacting a doctor or a medical professional. Please tell me how may I help you")
    speak("I am your Medical AI Voice Assistant. I can suggest home remedies for your medical problems but if the problems are severe please consider contacting a doctor or a medical professional. Please tell me how may I help you")       

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1 # seconds of pause before a sentence is deemed as comoplete for eg: 1 sec
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n") #f string for real time change as per the values

    except Exception as e:
        # print(e)  
      
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('smithdabreo24@gmail.com', 'google@smith777')
    server.sendmail('smithdabreo24@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            print("Searching Wikipedia...")
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'common cold' in query:
            print("For pacifying common cold you can use peppermint as a home remedy. Peppermint leaves are well known for their healing properties. Menthol in peppermint soothes the throat and acts as a decongestant, helping to break down mucus. You can benefit by drinking peppermint tea or by inhaling peppermint vapors from a steam bath. for more info about your medical issue use the wikipedia feature ")
            speak("For pacifying common cold you can use peppermint as a home remedy. Peppermint leaves are well known for their healing properties. Menthol in peppermint soothes the throat and acts as a decongestant, helping to break down mucus. You can benefit by drinking peppermint tea or by inhaling peppermint vapors from a steam bath. for more info about your medical issue use the wikipedia feature ")


        elif 'cough' in query:
            print("For pacifying common cold you can use peppermint as a home remedy. Peppermint leaves are well known for their healing properties. Menthol in peppermint soothes the throat and acts as a decongestant, helping to break down mucus. You can benefit by drinking peppermint tea or by inhaling peppermint vapors from a steam bath. for more info about your medical issue use the wikipedia feature ")
            speak("For pacifying cough you can use peppermint as a home remedy. Peppermint leaves are well known for their healing properties. Menthol in peppermint soothes the throat and acts as a decongestant, helping to break down mucus. You can benefit by drinking peppermint tea or by inhaling peppermint vapors from a steam bath. for more info about your medical issue use the wikipedia feature ")

        elif 'hair loss' in query:
            print("You can make coconut milk at home by grinding the grated coconut and squeezing out its juice (milk). This is a natural, surefire home remedy to prevent hair loss. also avoid using hot or warm water for hair wash as it increases hair loss.for more info about your medical issue use the wikipedia feature ")
            speak("You can make coconut milk at home by grinding the grated coconut and squeezing out its juice (milk). This is a natural, surefire home remedy to prevent hair loss. also avoid using hot or warm water for hair wash as it increases hair loss.for more info about your medical issue use the wikipedia feature ")

        elif 'headache' in query:
            print("for soothing pain, Massage  peppermint oil onto your temples, the back of your jaw, and forehead. You will feel a cooling sensation upon applying it. Breathe deeply, and if possible, find a quiet place to relax and sip some cool water.")
            speak("for soothing pain, Massage  peppermint oil onto your temples, the back of your jaw, and forehead. You will feel a cooling sensation upon applying it. Breathe deeply, and if possible, find a quiet place to relax and sip some cool water.")

        elif 'body pain' in query:
            print("A mustard oil massage is a great way to fight persistent body aches. This oil contains a compound called allyl isothiocyanate, which helps in reducing the pain caused by inflammation in the body. ")
            speak("A mustard oil massage is a great way to fight persistent body aches. This oil contains a compound called allyl isothiocyanate, which helps in reducing the pain caused by inflammation in the body.  ")

        elif 'stop bleeding' in query:
            print("Applying ice to a wound will constrict the blood vessels, allowing a clot to form more quickly and stop the bleeding. The best way to do this is to wrap ice in a clean, dry cloth and place it on the wound. If the beeding doesnt stop please counsult a doctor")
            speak("Applying ice to a wound will constrict the blood vessels, allowing a clot to form more quickly and stop the bleeding. The best way to do this is to wrap ice in a clean, dry cloth and place it on the wound. if the bleeding doesnt stop please consult a doctor")

        elif 'minor burn' in query:
            print("For a minor burn, soak the burned area in milk for 15 minutes or so. You may also apply a cloth soaked in milk to the area. Repeat every few hours to relieve pain. Be sure to wash out the cloth after use, as it will sour quickly.")
            speak("For a minor burn, soak the burned area in milk for 15 minutes or so. You may also apply a cloth soaked in milk to the area. Repeat every few hours to relieve pain. Be sure to wash out the cloth after use, as it will sour quickly.")

        elif 'diarrhoea' in query:
            print("Look for yogurt with live cultures. These cultures are friendly bacteria that can go in and line your intestines, providing you with protection from the bad germs and bacterias. If you've already got diarrhea, yogurt can help produce lactic acid in your intestines, which can kill off the nasty bacteria and get you feeling better, faster.")
            speak("Look for yogurt with live cultures. These cultures are friendly bacteria that can go in and line your intestines, providing you with protection from the bad germs and bacterias. If you've already got diarrhea, yogurt can help produce lactic acid in your intestines, which can kill off the nasty bacteria and get you feeling better, faster.")

        elif 'hiccups' in query:
            print("to get rid of hiccups Hold your nose and close your mouth. the way you would when you're ready to jump in a pool. for as long as you can or until you sense that the hiccups are gone.")
            speak("to get rid of hiccups Hold your nose and close your mouth. the way you would when you're ready to jump in a pool. for as long as you can or until you sense that the hiccups are gone.")

        elif 'insomnia' in query:
            print("keep a strict sleep-wake schedule, even on weekends. If you can't sleep one night, get up at your usual time the next morning and don't take any naps. If you nap, you'll have more trouble getting to sleep the next night, thereby compounding your insomnia. It's best to let yourself get good and sleepy so that it will be easier to get to sleep the next night.")
            speak("keep a strict sleep-wake schedule, even on weekends. If you can't sleep one night, get up at your usual time the next morning and don't take any naps. If you nap, you'll have more trouble getting to sleep the next night, thereby compounding your insomnia. It's best to let yourself get good and sleepy so that it will be easier to get to sleep the next night.")

        elif 'poor apetite' in query:
            print("Ginger helps stimulate a tired appetite, both through its medicinal properties and its refreshing taste. Try nibbling on gingersnaps or sipping ginger ale made with real ginger. Ginger tea is also a way to start the day off on an appetizing note.")
            speak("Ginger helps stimulate a tired appetite, both through its medicinal properties and its refreshing taste. Try nibbling on gingersnaps or sipping ginger ale made with real ginger. Ginger tea is also a way to start the day off on an appetizing note.")

        elif 'remove face tan' in query:
            print("for removing tan naturally, Mash a portion of papaya into pulp and mix in a bowl with a tablespoon of honey. Mix well and apply the paste directly on your face. Leave it on for about 30 minutes and rinse off with lukewarm water. ")
            speak("for removing tan naturally, Mash a portion of papaya into pulp and mix in a bowl with a tablespoon of honey. Mix well and apply the paste directly on your face. Leave it on for about 30 minutes and rinse off with lukewarm water.")

        elif 'acne' in query:
            print("get rid of acne by Using a clean finger or cotton pad, rub a little honey into pimples. Otherwise, add honey to a face or body mask. you can even mix honey with aloe vera for better results")
            speak("get rid of acne by Using a clean finger or cotton pad, rub a little honey into pimples. Otherwise, add honey to a face or body mask. you can even mix honey with aloe vera for better results")


        elif 'open health line' in query:
            speak("Sure sir")
            webbrowser.open("https://www.healthline.com/")

        elif 'buy medicine' in query:
            speak("okay just a sec")
            webbrowser.open("https://www.netmeds.com/")


        elif 'open youtube' in query:
            speak("Sure sir")
            webbrowser.open("https://www.youtube.com/")

        elif 'open google' in query:
            speak("Sure sir")
            webbrowser.open("google.com")
        
        elif 'twitter ' in query:
            speak("Sure sir")
            webbrowser.open("twitter.com")

        elif 'open stack overflow' in query:
            speak("Sure sir")
            webbrowser.open("stackoverflow.com")

        elif 'shopping' in query:
            speak("Sure sir")
            webbrowser.open("amazon.in") 
                
        elif 'play music' in query:
            speak("playing music")
            music_dir = 'C:\\Users\\SMIT\\Desktop\\Ai Assistant\\Music'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            speak("opening vs code ")
            codePath = "C:\\Users\\SMIT\\AppData\\Local\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'write something' in query:
            speak("okay here you go ")
            codePath = "C:\\WINDOWS\\system32\\notepad.exe"
            os.startfile(codePath)

        elif 'email' in query:
            try:
                print("What should I say?")
                speak("What should I say?")
                content = takeCommand()
                to = "8382.smith.beit@gmail.com"    
                sendEmail(to, content)
                print("email has been sent")
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry sir, I am not able to send this email")  

        elif 'joke'in query:
            speak("okay, here comes the joke ")
            joke = pyjokes.get_joke()
            print (joke)
            speak(joke)

        elif 'fact'in query:
            speak("okay a random fact coming your way ")
            fact = randfacts.getFact()
            print (fact)
            speak(fact)
            

        elif 'exit' in query:
            print("okay, bye have a nice day! ")
            speak("okay, bye have a nice day ")
            sys.exit()
        
            