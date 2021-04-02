from tkinter import *
root = Tk()            # tkinter를 이용하기위해서 해야하는 필수조건
root.title("시작")     #  실행이름
root.geometry("640x480+2500+200") # 가로x(소문자)세로+실행x좌표+실행y좌표
root.resizable(False,False)  #창크기(가로,세로) 값 변경불가



frame= Frame(root) #리스트박스는 frame넣어서 관리하는게 편하다
frame.pack()

scroll=Scrollbar(frame)
scroll.pack(side="right",fill="y") #fill로 y방향으로 꽉 채우기

listbox = Listbox(frame, selectmode="extended",height =10,yscrollcommand=scroll.set)
#yscrollcommand를하고 set을 해주지않으면 scroll은 아무 기능을 하지않는다 
#yscrollcommand로 리스트박스와 scroll을 매핑해준다(서로가서로를 매핑)-매핑1
for date in range(1,32):
    listbox.insert(END , str(date)+"일")
listbox.pack(side="left")

scroll.config(command=listbox.yview) #스크로바도 리스트와 매핑해준다 (서로가서로를 매핑)-매핑2
#매핑1과 매핑2를 둘다해주지않고 한개씩만했을떄 매핑1만하고 매핑2를하지않으면 리스트박스에서 내리거나 올리면 스크롤도 내려가거나 올라가지만
#스크롤을 올리거나 내리면 리스트박스는 반응하지않는다 반대로 매핑2만하게된다면 스트롤을 내리거나올리면 리스트박스도 내려가거나 올라가지만
#리스트박스를 올리거나 내리면 스크롤은 반응하지않는다

root.mainloop()        # tkinter를 이용하기위해서 해야하는 필수조건