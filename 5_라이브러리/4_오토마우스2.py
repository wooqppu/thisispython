import pyautogui
import time
import pyperclip

pyautogui.moveTo(1348, 231, 0.1)
pyautogui.click()
time.sleep(0.3)

pyperclip.copy("울산 날씨")
pyautogui.hotkey("ctrl", "v")

pyautogui.write(["enter"])
time.sleep(1)

# pop install pillow
# 1116 207 시작  1547 646 종료

start_x = 1116
start_y = 207

end_x = 1547
end_y = 646

pyautogui.screenshot(r'울산날씨.png', region=(start_x, start_y, end_x-start_x, end_y-start_y))

