import tkinter.ttk as ttk # 콤보박스를 사용하려면 tkinter.ttk을 import해줘야하고 길기때문에 편의상ttk로 사용하기위해 as처리
from tkinter import *


root = Tk()            # tkinter를 이용하기위해서 해야하는 필수조건
root.title("시작")     #  실행이름
root.geometry("640x480+2500+200") # 가로x(소문자)세로+실행x좌표+실행y좌표
root.resizable(False,False)  #창크기(가로,세로) 값 변경불가

values = [str(i)+ "일"  for i in range(1,32)] # 1일부터 31일까지 
cbb = ttk.Combobox(root,height=5,values=values ,state="readonly")
cbb = ttk.Combobox(root,height=5,values=values ,state="readonly")

#state설정을 추가해서 readonly를 해주지않으면 목록을 수정할수있고 수정값을 출력할수있게된다
#height 의 숫자가 5면 목록이 5개씩 보이고 10이면 10개씩보인다
cbb.pack()
cbb.set("날짜 선택") #최초 목록에는 빈칸인데 빈칸대신 글씨를 추가

def cmd():
    print(cbb.get())
btn = Button(root, text="버튼", command = cmd)
btn.pack()

root.mainloop()        # tkinter를 이용하기위해서 해야하는 필수조건