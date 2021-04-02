import os  #########################################################################
from tkinter import *
root = Tk()            # tkinter를 이용하기위해서 해야하는 필수조건
root.title("제목 없음 - Windows 메모장")     #  실행이름
root.geometry("640x480+2500+200") # 가로x(소문자)세로+실행x좌표+실행y좌표
root.resizable(True,True)  #없어도 크기조정 가능

mn = Menu(root) #메뉴 만들기
mn1=Menu(mn, tearoff=0) #메뉴 1만들기
#메뉴1에 메뉴들 추가

file="mynote.txt"

def write(): #글 저장 함수 만들기
    with open(file,"w",encoding="utf8") as w: #mynote.txt를 만들기
        w.write(txt.get("1.0",END))#txt에 내용을 처음부터 끝까지 mynote.txt에 작성하기
def read():
    if os.path.isfile(file):#파일이 있으면 True 없으면 False    
        with open(file,"r",encoding="utf8") as r: #mynot.txt를 불러오기
            txt.delete("1.0",END) #불러오기전에 txt내용들 다 지우기
            txt.insert(END,r.read()) #불러온 내용을 txt에 삽입하기
        
mn1.add_command(label="열기(O)",command=read) #열기란 메뉴를 누르면 read함수 불러오기
mn1.add_command(label="저장(S)",command=write) #저장이란 메뉴를 누르면 write함수 불러오기
mn1.add_separator()
mn1.add_command(label="끝내기(X)",command=root.quit)#끝내기란 메뉴를 누르면 창을 종료하기
mn.add_cascade(label="파일(F)", menu=mn1) #메뉴에 메뉴1추가하기
#메뉴에 추가하기
mn.add_cascade(label="편집(E)") 
mn.add_cascade(label="서식(O)")
mn.add_cascade(label="보기(V)")
mn.add_cascade(label="도움말(H)")
#frame만들기
frame=Frame(root)
frame.pack(expand="True",fill="both")#frame을 화면에 꽉차게 하기
scroll=Scrollbar(frame)#frame안에 스크롤만들기
scroll.pack(side="right",fill="y") #스크롤을 y축방향(세로)로 꽉차게하기

txt=Text(frame,yscrollcommand=scroll.set)#frame안에 텍스트만들고 스크롤과 매칭
txt.pack(side="left",expand="True",fill="both") #txt를 화면에 꽉차게 하기

scroll.config(command=txt.yview)#스크롤을 txt와 매칭
root.config(menu=mn)
root.mainloop()        # tkinter를 이용하기위해서 해야하는 필수조건