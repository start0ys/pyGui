import time #time sleep 을 사용하기위해 time 라이브러리를 불러온다
import tkinter.ttk as ttk # 프로그래스바 를 사용하려면 tkinter.ttk을 import해줘야하고 길기때문에 편의상ttk로 사용하기위해 as처리
from tkinter import *


root = Tk()            # tkinter를 이용하기위해서 해야하는 필수조건
root.title("시작")     #  실행이름
root.geometry("640x480+2500+200") # 가로x(소문자)세로+실행x좌표+실행y좌표
root.resizable(False,False)  #창크기(가로,세로) 값 변경불가

#편의상   프로그래스바의 칸을 칸 , 프로그래스바에서 진행률을 보여주는 초록색을 진행이라 하고 설명하겠다
p_var2 = DoubleVar()
progressbar = ttk.Progressbar(root, maximum=100, length=150, mode ="determinate", variable= p_var2) 
#maximum은 칸의 크기 즉 100이면 start(10)에서 10ms의 속도로 100까지 차는거라빠르게 차고 1000이면 10ms속도로 1000까지 차는거라 느리게찬다
#length는 칸의 길이
#모드가 indeterminate면 결정되지않아 진행이 칸에 가득 차지않고 좌우로 계속 움직인다 #
# determinate 하면 진행이 칸의 처음부터 끝까지 가득찬다 stop을해주지않으면 칸의 끝까지 가득차도 다시초기화되어 처음부터 다시찬다
progressbar.pack()


def cmd():
    for i in range(1,101): #1~ 100까지 진행하기위해서 만약 maximum이 100이아니라 1000이면 100까지이기때문에 1/10까지만 진행한다
        time.sleep(0.01) # 0.01초대기
        p_var2.set(i)
#for문안에서 계속 1~100까지를 업데이트를 해줘야 칸에 진행이 되는걸 볼수있고 업데이트가없다면 100까지 다 된 후 set을 해주기때문에 칸이 한번에 차지버린다
        progressbar.update() 

btn = Button(root, text="시작", command = cmd)
btn.pack()

root.mainloop()        # tkinter를 이용하기위해서 해야하는 필수조건