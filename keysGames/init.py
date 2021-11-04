#  https://www.cnblogs.com/fanghao/p/8453207.html

import pyautogui

# 获取屏幕尺寸
def getPmPx():
    screenWidth, screenHeight = pyautogui.size() # 屏幕尺寸
    return screenWidth,screenHeight
def getMouseLon():
    mouseX, mouseY = pyautogui.position() # 返回当前鼠标位置，注意坐标系统中左上方是(0, 0)
    return mouseX,mouseY

def oClike():
    pyautogui.click(35, 40)

print(getMouseLon())