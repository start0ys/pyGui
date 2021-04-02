import tkinter.ttk as ttk # 프로그래스바 를 사용하려면 tkinter.ttk을 import해줘야하고 길기때문에 편의상ttk로 사용하기위해 as처리
from tkinter import *

root = Tk()            # tkinter를 이용하기위해서 해야하는 필수조건
root.title("시작")     #  실행이름
root.geometry("640x480+2500+200") # 가로x(소문자)세로+실행x좌표+실행y좌표
root.resizable(False,False)  #창크기(가로,세로) 값 변경불가
#파일 추가 선택삭제 버튼
frame0=Frame(root)
Button(frame0,text="파일추가").pack(side="left")
Button(frame0,text="선택삭제").pack(side="right")
frame0.pack(side="top",fill="x")
#선택한 파일이 보이는곳(listbox,scrollbar)
frame1=Frame(root)
listbox=Listbox(frame1)
listbox.pack(side="left",expand="True",fill="both")
scroll=Scrollbar(frame1)
scroll.pack(side="right")
frame1.pack(fill="x")
#저장경로 가 보이는 곳(entry,button)
frame2=LabelFrame(root,text="저장경로")
Entry(frame2).pack(side="left",expand="True",fill="x")
Button(frame2,text="찾아보기").pack(side="right")
frame2.pack(fill="x")
#옵션이 보이는 곳 (label,combobox)
frame3=LabelFrame(root,text="옵션")
#가로넓이
frame3_1=Frame(frame3)
Label(frame3_1,text="가로넓이").pack(side="left")
ttk.Combobox(frame3_1).pack(side="right")
frame3_1.pack(side="left")
#포맷
frame3_3=Frame(frame3)
Label(frame3_3,text="포맷").pack(side="left")
ttk.Combobox(frame3_3).pack(side="right")
frame3_3.pack(side="right")
#간격
frame3_2=Frame(frame3)
Label(frame3_2,text="간격").pack(side="left")
ttk.Combobox(frame3_2).pack(side="right")
frame3_2.pack()
frame3.pack(fill="x")
#진행상황 (progressbar)
frame4=LabelFrame(root,text="진행상황")
ttk.Progressbar(frame4).pack(expand="True",fill="x")
frame4.pack(fill="x")
#시작 삭제
frame5=Frame(root)
Button(frame5,text="닫기").pack(side="right")
Button(frame5,text="시작").pack(side="right")
frame5.pack(side="bottom",fill="x")
root.mainloop()        # tkinter를 이용하기위해서 해야하는 필수조건