import pyautogui
#to find the size of the laptop screen / coordinates
# wh = pyautogui.size()
# print(wh)
# print(wh[0])
# print(wh.width)

#pyautogui.position() - this function for exact position of the mouse
for i in range(10):
    pyautogui.move(100,0, duration=0.25) #right
    pyautogui.move(0, 100, duration=0.25) #down
    pyautogui.move(-100,0,duration=0.25)#left
    pyautogui.move(0, -100, duration=0.25)#up

auto = pyautogui.position() #current position of the mouse
print(auto)
p = pyautogui.position()
print(p)
# pyautogui.click(71,375, button='left')
py = pyautogui.click(10,5)
print(py)
#coordinates for windows key Point(x=71, y=667)