# pip install speechrecognition
import speech_recognition
import os
from farsi import convert

os.system("cls")

r=speech_recognition.Recognizer()

mic=speech_recognition.Microphone()

merge = ""

end = "پایان"

while True :
    with mic as mic_open :
        try:
            r.adjust_for_ambient_noise(mic_open , duration=1)
            print(convert("لطفا صحبت کنید")) 
            audio=r.listen(mic_open)
            my_text=r.recognize_google(audio , language="fa-IR") # en-US
            os.system("cls")
            merge = merge+" "+ my_text
            if my_text == end :
                print("======================")
                print(convert(merge))
                print("======================")
                print(convert("به امید دیدار"))
                input(convert("برای خروج یکی از کلید های کیبرد را فشار دهید"))
                break
            print(convert(merge))
        except speech_recognition.exceptions.RequestError:
            print(convert("لطفا وضعیت شبکه خود را بررسی کنید"))
            input(convert("برای خروج یکی از کلید های کیبرد را فشار دهید"))
            break
        except OSError :
            print(convert("لطفا وضعیت میکروفون خود را بررسی کنید"))
            input(convert("برای خروج یکی از کلید های کیبرد را فشار دهید"))
            break
        except :
            print(convert("برنامه با شکست مواجه شد"))
            input(convert("برای خروج یکی از کلید های کیبرد را فشار دهید"))
            break