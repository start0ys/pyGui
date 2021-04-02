from tkinter import *


root = Tk()            # tkinter를 이용하기위해서 해야하는 필수조건
root.title("시작")     #  실행이름
root.geometry("640x480+2500+200") # 가로x(소문자)세로+실행x좌표+실행y좌표
root.resizable(False,False)  #창크기(가로,세로) 값 변경불가
mn =Menu(root) #메뉴만들기

def cmd():
    print("반갑습니다")

mn_menu = Menu(mn, tearoff = 0) #첫번째 메뉴추가
#첫번째 메뉴안에 메뉴들을 추가
mn_menu.add_command(label = "안녕하세요", command=cmd)
mn_menu.add_command(label = "시작입니다")
mn_menu.add_separator() # -------경계선
mn_menu.add_command(label = "게임만들기")
mn_menu.add_command(label = "GUI프로그래밍")

mn.add_cascade(label="메뉴공부",menu=mn_menu)  #첫번째 메뉴를 추가하기위한 필수조건

mn_menu2 = Menu(mn, tearoff = 0) #두번째 메뉴 추가
#두번째 메뉴안에 메뉴들을 추가
mn_menu2.add_command(label = "매일매일 새로운 시작") 
mn_menu2.add_command(label = "새로운 공부")
mn_menu2.add_command(label = "시작", state="disable") #비활성화

mn.add_cascade(label="메뉴공부2",menu=mn_menu2) #두번째 메뉴를 추가하기위한 필수조건

# radio버튼을 이용해 한개만 선탁 가능한 메뉴만들기

mn_rdbtn = Menu(mn, tearoff = 0)
mn_rdbtn.add_radiobutton(label = "하나만")
mn_rdbtn.add_radiobutton(label = "가능")
mn_rdbtn.add_radiobutton(label = "하지롱")
mn.add_cascade(label="라디오버튼",menu=mn_rdbtn)

# check버튼을 이용해 한개만 선탁 가능한 메뉴만들기

mn_ckbtn = Menu(mn, tearoff = 0)
mn_ckbtn.add_checkbutton(label = "여러개상관없이")
mn_ckbtn.add_checkbutton(label = "선택되었다가")
mn_ckbtn.add_checkbutton(label = "해제 가능 하지롱")
mn.add_cascade(label="체크버튼",menu=mn_ckbtn)

#메뉴안에 메뉴들 추가없이 하나만 이용하려면 cascade를이용해 바로 사용가능
mn.add_cascade(label = "창닫기",command = root.quit) #창닫기 메뉴를 누르면 프로그램 종료

root.config(menu=mn) #메뉴만들기 필수조건
root.mainloop()        # tkinter를 이용하기위해서 해야하는 필수조건