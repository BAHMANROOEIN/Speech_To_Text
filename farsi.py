#pip install arabic-reshaper
#pip install python-bidi
import arabic_reshaper
from bidi.algorithm import get_display

def farsi (name) :
    reshap = arabic_reshaper.reshape(name)
    rtl = get_display(reshap)
    return rtl
print(farsi("سلام"))
print(farsi("خوبی"))