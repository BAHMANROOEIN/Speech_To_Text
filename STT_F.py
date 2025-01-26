import speech_recognition 
import os
import time
from farsi import convert

os.system("cls")

r=speech_recognition.Recognizer()

file=speech_recognition.AudioFile("sound/test.wav")

try:
    time_min = int(input("min: "))
except ValueError:
    print("===========================================================")
    print(convert("لطفا مقدار دقیقه را به صورت عدد وارد کنید."))
    print("===========================================================")
    input(convert("برای خروج یکی از کلید های کیبرد را فشار دهید"))
    exit()
try:
    time_sec = int(input("sec: "))
except ValueError:
    print("===========================================================")
    print(convert("لطفا مقدار ثانیه را به صورت عدد وارد کنید."))
    print("===========================================================")
    input(convert("برای خروج یکی از کلید های کیبرد را فشار دهید"))
    exit()

os.system("cls")
total_time = (time_min*59) + time_sec
print(str(total_time)+ " s ")
merge = ""
offs = 0

try:
    while offs <= total_time: # 100 s
        with file as file_open :
            r.adjust_for_ambient_noise(file_open , duration=1)
            audio=r.record(file_open , offset=offs , duration=20)  #20  40 60 80 100
            try:
                print(convert("در حال تبدیل صدا به متن ..."))
                my_text=r.recognize_google(audio , language="fa-IR") 
                os.system("cls")
                merge = merge + " " + my_text
                print("===========================================================")
                print(convert(merge))
                print("===========================================================")
                offs = offs + 20
                if offs <= total_time :
                    print(str(offs) + " s " + "/ " +str(total_time) + " s ")
                else:
                    print(convert("عملیات با موفقیت انجام شد"))
                    print("===========================================================")
                    input(convert("برای خروج یکی از کلید های کیبرد را فشار دهید"))
            except speech_recognition.exceptions.UnknownValueError :
                os.system("cls")
                print(convert("در حال تلاش مجدد ..."))
                time.sleep(1)
                os.system("cls")
                print("===========================================================")
                print(convert(merge))
                print("===========================================================")
                offs = offs + 20
                if offs <= total_time :
                    print(str(offs) + " s " + "/ " +str(total_time) + " s ")
                else:
                    print(convert("عملیات با موفقیت انجام شد"))
                    print("===========================================================")
                    input(convert("برای خروج یکی از کلید های کیبرد را فشار دهید"))
            except speech_recognition.exceptions.RequestError :
                os.system("cls")
                print(convert("متن ذخیره شده"))
                print("===========================================================")
                print(convert(merge))
                print("===========================================================")
                print(convert("لطفا وضعیت شبکه را بررسی کنید"))
                print("===========================================================")
                print(convert("در حال تلاش مجدد..."))
                print("===========================================================")
                time.sleep(2)
            except :
                print(convert("برنامه با خطا مواجه شد."))
                print("===========================================================")
                input(convert("برای خروج یکی از کلید های کیبرد را فشار دهید"))
                break
except FileNotFoundError :
    os.system("cls")
    print("===========================================================")
    print(convert("فایل یافت نشد."))
    print("===========================================================")
    input(convert("برای خروج یکی از کلید های کیبرد را فشار دهید"))
    exit()
except ValueError :
    os.system("cls")
    print("===========================================================")
    print(convert("این فرمت صدا پشتیبانی نمی شود ."))
    print("===========================================================")
    input(convert("برای خروج یکی از کلید های کیبرد را فشار دهید"))
    exit()
except PermissionError :
    os.system("cls")
    print("===========================================================")
    print(convert("لطفا مسیر فایل را بررسی کنید."))
    print("===========================================================")
    input(convert("برای خروج یکی از کلید های کیبرد را فشار دهید"))
    exit()
except:
    print(convert("برنامه با خطا مواجه شد."))
    print("===========================================================")
    input(convert("برای خروج یکی از کلید های کیبرد را فشار دهید"))
    exit()

