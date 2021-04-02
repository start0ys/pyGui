toon = ["신의탑","캐슬","광장"] #월요일 웹툰 신의탑, 수요일 웹툰 캐슬, 토요일 웹툰 광장
week =["월요일","수요일","토요일"]

print(list(zip(toon,week))) #리스트안에 같은 위치에 있는 변수들을 묶어준다

toonweek = [("신의탑","월요일"),("캐슬","수요일"),("광장","토요일")] 

print(list(zip(*toonweek))) #리스트 안에 묶여진 리스트를 나눠준다.

toon2 , week2 = zip(*toonweek)

print(toon2)
print(week2)
