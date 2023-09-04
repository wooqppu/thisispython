import pyautogui
import time
import pyperclip

날씨=["울산 날씨", "서울 날씨", "부산 날씨", "강릉 날씨"]

addr_x = 1348
addr_y = 231

start_x = 1116
start_y = 207

end_x = 1547
end_y = 646

for 지역날씨 in 날씨:
    pyautogui.moveTo(1348, 231, 0.2)
    pyautogui.click()
    time.sleep(1)

    pyperclip.copy(지역날씨)
    pyautogui.hotkey("ctrl", "v")
    time.sleep(0.7)
    pyautogui.write(["enter"])

    time.sleep(1)

    저장경로 = 지역날씨 + ".png"
    pyautogui.screenshot(저장경로, region=(start_x, start_y, end_x-start_x, end_y-start_y))


# pop install pillow
# 1116 207 시작  1547 646 종료

#start_x = 1116
#start_y = 207
#end_x = 1547
#end_y = 646

#pyautogui.screenshot(r'울산날씨.png', region=(start_x, start_y, end_x-start_x, end_y-start_y))

