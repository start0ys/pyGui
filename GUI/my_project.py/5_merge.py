import os
import tkinter.ttk as ttk # 프로그래스바 를 사용하려면 tkinter.ttk을 import해줘야하고 길기때문에 편의상ttk로 사용하기위해 as처리
import tkinter.messagebox as msg 
from tkinter.filedialog import *
from tkinter import *
from PIL import Image


root = Tk()            # tkinter를 이용하기위해서 해야하는 필수조건
root.title("시작")     #  실행이름
root.geometry("480x540+2500+200") # 가로x(소문자)세로+실행x좌표+실행y좌표   
root.resizable(False,False)  #창크기(가로,세로) 값 변경불가

#파일 추가 선택삭제 버튼
frame0=Frame(root,padx=5)
def add_file():
 
    select_file=askopenfilenames(title="추가되는 이미지 고르기",\
        filetype=(("PNG 파일","*.png"),("모든 파일","*.*")),\
        initialdir="C:/Users/Administrator/Desktop/파이썬/") #파일열기 대화상장의 초기 경로 설정
    for select_files in select_file: ##############여러개 한번에 올리기######################
        listbox.insert(END,str(select_files)) #변수를 위에서 부터 리스트에 삽입
def del_file():
    for select_del in reversed(listbox.curselection()):    ##########여러개 한번에 지우기 ##########
        #위에서 부터 지우면 위에가 지워지자마자 바로밑에 인덱스가 올라와서 순서 안맞는다 그래서 뒤에서부터지운다
        listbox.delete(select_del) #리스에서 선택한것을 삭제

Button(frame0,text="파일추가",padx=25,pady=5,command=add_file).pack(side="left")  
Button(frame0,text="선택삭제",padx=25,pady=5,command=del_file).pack(side="right")
frame0.pack(side="top",expand=True,fill="both") 


#선택한 파일이 보이는곳(listbox,scrollbar)
frame1=Frame(root,padx=5,pady=5)

scroll=Scrollbar(frame1)
scroll.pack(side="right",fill="y")
listbox=Listbox(frame1,selectmode="extended",height=15,yscrollcommand=scroll.set)
listbox.pack(side="left",expand=True,fill="both")
scroll.config(command=listbox.yview)
frame1.pack(expand=True,fill="both")


#저장경로 가 보이는 곳(entry,button)
frame2=LabelFrame(root,text="저장경로",padx=5,pady=5)
def find():
    save_file=askdirectory() #저장 할 위치의 경로를 가져온다
    if save_file == "": #취소를눌렀을때 (아무것도 누르지않았을때) 저장경로를 그대로 납둔다
        return
    find_file.delete(0,END) #경로를 가져오기전에 기존 경로를 삭제하고 삽입해준다
    find_file.insert(0,save_file) #가져온 경로를 Entry에삽입해준다
find_file=Entry(frame2)
find_file.pack(side="left",expand="True",fill="x",padx=3,ipady=3)
Button(frame2,text="찾아보기",padx=10,pady=2,command=find).pack(side="right",padx=3)
frame2.pack(expand=True,fill="both")


#옵션이 보이는 곳 (label,combobox)
frame3=LabelFrame(root,text="옵션",padx=5,pady=5)

#가로넓이

Label(frame3,text="가로넓이").pack(side="left",padx=5)
val_1=["원본유지",1024,800,640]
cbb1=ttk.Combobox(frame3,width=10,value=val_1 ,state="readonly")
cbb1.pack(side="left",padx=5)
cbb1.current(0)      


#간격
val_2=["없음","좁게","보통","넓게"]
Label(frame3,text="간격").pack(side="left",padx=5)
cbb2=ttk.Combobox(frame3,width=10,value=val_2 ,state="readonly")
cbb2.pack(side="left",padx=5)
cbb2.current(0)


#포맷
val_3=["PNG","JPG","BMP"]
Label(frame3,text="포맷").pack(side="left",padx=5)
cbb3=ttk.Combobox(frame3,width=10,value=val_3 ,state="readonly")
cbb3.pack(side="left",padx=5)
cbb3.current(0)

frame3.pack(fill="both")


#진행상황 (progressbar)
frame4=LabelFrame(root,text="진행상황",padx=5)
ttk.Progressbar(frame4).pack(expand="True",fill="x")
frame4.pack(expand=True,fill="both")


#시작 삭제
frame5=Frame(root,padx=5,pady=5)
def merge_image(): #사진을 합치는 함수
    images=[Image.open(a) for a in listbox.get(0,END)] #리스트박스의 이미지들을 이미지형태로 전부가져오기
    #이미지들이 합치게 될 공간(스케치북)만들기
    widths = [a.size[0] for a in images]  #가져온 이미지들의 가로크기 저장
    heights = [a.size[1] for a in images] #가져온 이미지들의 세로크기 저장
    width = max(widths) # 스케치북의 가로크기는 가져온이미지들중 가장 큰 가로크기
    height = sum (heights) #스케치북의 세로크기는 가져온이미지들의 세로이미지들의 합
    
    sketchbook = Image.new("RGB",(width , height), (255,255,255) ) #배경이 하얀색이고 구한크기의 스케치북만들기
    y_offset = 0 #이미지들이 저장될 Y위치좌표
    for merge_img in images:
        sketchbook.paste(merge_img, (0,y_offset)) #스케치북에 이미지들을 가져와 (0,y_offset)좌표에 붙이기
        y_offset += merge_img.size[1] #가져온 이미지의 세로크기만큼 y좌표 변경
    
    path = os.path.join(find_file.get(), "merge_photo.png") # 저장경로를 불러와 저장될 이미지의 이름과 함께 경로저장
    sketchbook.save(path)  #스케치북을 경로에 저장
    msg.showinfo("작업종료","이미지 합치기 작업이 완료되었습니다") #작업완료 메세지알림


def start():
    #시작을 누르면 각 옵션들의 값을 가져와야한다

    if listbox.size() == 0: #리스트박스에 아무런 이미지파일이 없을 때
        msg.showwarning("시작불가","이미지를 골라주세요")

    if listbox.size() != 0: #리스트 박스에 사진은 골랐지만 경로를 설정하지않았을떄
        if len(find_file.get()) ==0 : 
            msg.showwarning("시작불가","저장경로를 설정해주세요")
    #사진파일도 있고 경로를 설정을 했을때 옵션값을 print해서 실험하기
    if listbox.size() != 0 and len(find_file.get()) !=0:
        merge_image()



Button(frame5,text="닫기",padx=25,pady=5,command=root.quit).pack(side="right",padx=10)
Button(frame5,text="시작",padx=25,pady=5,command=start).pack(side="right")
frame5.pack(side="bottom",expand=True,fill="both")

root.mainloop()        # tkinter를 이용하기위해서 해야하는 필수조건