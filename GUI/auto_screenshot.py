import time
from PIL import ImageGrab

time.sleep(5)   #프로그램을 실행하고 5초간 사용자가 준비하는시간

for i in range (1,11): #10개이미지 저장
    img=ImageGrab.grab() # 현재 스크린 이미지를 가져옴
    img.save("image{}.png".format(i)) #파일로저장
    time.sleep(2) # 2초간격으로 이미지가져오기