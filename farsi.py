#pip install arabic-reshaper
#pip install python-bidi
import arabic_reshaper
from bidi.algorithm import get_display

def convert (text) :
    reshap = arabic_reshaper.reshape(text)
    rtl = get_display(reshap)
    return rtl

