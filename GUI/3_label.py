from tkinter import *

root = Tk()            # tkinter를 이용하기위해서 해야하는 필수조건
root.title("시작")     #  실행이름
root.geometry("640x480+2500+200") # 가로x(소문자)세로+실행x좌표+실행y좌표
root.resizable(False,False)  #창크기(가로,세로) 값 변경불가

label1 = Label(root,text="꼭꼭숨어라")   # 글자 label 추가 (버튼이아닌 고정된 label)
label1.pack() #label추가시 필수조건

photo = PhotoImage(file ="Game/내공.png")  # 그림1추가
change_photo = PhotoImage(file = "Game/프로젝트캐릭터.png") #바뀌는 그림2추가
label2 = Label(root, image=photo) #그림1불러오기
label2.pack() 

def change_img(): #버튼 누를시 함수 실행
    label1.config(text = "걸렸다") #label1의 글자 변경
    #그림 변경시 그림2추가를 함수안에서 하고 config로 변경해도된다 그치만 함수내에서 변수 선언시 밖에서 사용하려면 global로 전역변수로사용해야한다
    #예시(위의 change_photo를 선언안해주어도 그림이 바뀜)
    #global change_photo
    #change_photo = PhotoImage(file = "Game/프로젝트캐릭터.png") #바뀌는 그림2를 여기서추가
    
    label2.config(image = change_photo) #label2의 그림을 그림2로 변경
    

btn = Button(root, text="공뒤에 정신이가 숨어있어요", command=change_img) 
btn.pack()



root.mainloop()        # tkinter를 이용하기위해서 해야하는 필수조건