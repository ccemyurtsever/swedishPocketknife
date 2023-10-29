import pyautogui
import time

width, height = pyautogui.size()

try:
    print(f"Main Screen Resolution: {width}x{height}")
    xdef , ydef = width / 1.23  , height / 1.23
    xdefmov , ydefmove = width / 10  , height / 15
    
except ZeroDivisionError:
  print("No resolution found.")
  breakpoint()
except ValueError:
  print("Could not create a screen with this resolution.")
  breakpoint()
except:
  print("An unknown problem has occurred.")
  breakpoint()