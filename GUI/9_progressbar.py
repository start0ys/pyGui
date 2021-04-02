import tkinter.ttk as ttk # 프로그래스바 를 사용하려면 tkinter.ttk을 import해줘야하고 길기때문에 편의상ttk로 사용하기위해 as처리
from tkinter import *


root = Tk()            # tkinter를 이용하기위해서 해야하는 필수조건
root.title("시작")     #  실행이름
root.geometry("640x480+2500+200") # 가로x(소문자)세로+실행x좌표+실행y좌표
root.resizable(False,False)  #창크기(가로,세로) 값 변경불가

#편의상   프로그래스바의 칸을 칸 , 프로그래스바에서 진행률을 보여주는 초록색을 진행이라 하고 설명하겠다
progressbar = ttk.Progressbar(root, maximum=100, mode ="determinate") 
#maximum은 칸의 크기 즉 100이면 start(10)에서 10ms의 속도로 100까지 차는거라빠르게 차고 1000이면 10ms속도로 1000까지 차는거라 느리게찬다
#모드가 indeterminate면 결정되지않아 진행이 칸에 가득 차지않고 좌우로 계속 움직인다 #
# determinate 하면 진행이 칸의 처음부터 끝까지 가득찬다 stop을해주지않으면 칸의 끝까지 가득차도 다시초기화되어 처음부터 다시찬다
progressbar.start(10) #스타트를 하지않으면 움직이지않는다 10은 10ms로 움직이는걸 의미
progressbar.pack()




def cmd():
    progressbar.stop() # 진행이 멈추는데 칸의 50%까지진행되도 거기서 멈추는게아니라 완전히 멈추기때문에 진행자체가 사라지고 칸만남는다
btn = Button(root, text="버튼", command = cmd)
btn.pack()

root.mainloop()        # tkinter를 이용하기위해서 해야하는 필수조건