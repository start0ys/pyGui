from tkinter import *
root = Tk()            # tkinter를 이용하기위해서 해야하는 필수조건
root.title("시작")     #  실행이름
root.geometry("640x480+2500+200") # 가로x(소문자)세로+실행x좌표+실행y좌표
root.resizable(False,False)  #창크기(가로,세로) 값 변경불가

Label(root,text="메뉴고르기").pack(side="top")  #side를 통해 위치를 정할수있다
Button(root,text="주문").pack(side="bottom") #side를 통해 위치를 정할수있다


frame_burger = Frame(root, relief = "solid",bd=10) #relief는 테두리 모양,bd는 테두르 크기
frame_burger.pack(side="left",expand=True,fill="both") #fill과 expand로 frame크기를 키운다

Button(frame_burger,text="불고기버거").pack() #frame안에 넣는거이기때문에 root가아닌 frame_buger에 넣는다
Button(frame_burger,text="치즈버거").pack()
Button(frame_burger,text="치킨버거").pack()

frame_drink = LabelFrame(root, text="음료") #frame에 제목넣기
frame_drink.pack(side="right",expand=True,fill="both")
Button(frame_drink,text="콜라").pack()
Button(frame_drink,text="사이다").pack()
Button(frame_drink,text="환타").pack()


root.mainloop()        # tkinter를 이용하기위해서 해야하는 필수조건