from tkinter import*
from PIL import Image , ImageTk
import speech_to_text
import action

root=Tk()
root.title("ROBO")
root.geometry("800x800")
root.resizable(False,False)
root.config(bg="#0D384B")

def ask():
    user_val= speech_to_text.speech_to_text()
    bot_val=action.Action(user_val)
    text.insert(END,'User-->'+user_val+"\n")
    if bot_val!=None:
        text.insert(END,"Robo--->"+str(bot_val)+"\n")
    if bot_val=="ok sir":
        root.destroy()


def send():
    send=entry.get()
    bot=action.Action(send)
    text.insert(END,'User-->'+send+"\n")
    if bot!=None:
        text.insert(END,"Robo--->"+str(bot)+"\n")
    if bot=="ok sir":
        root.destroy()


def del_text():
    text.delete('1.0',"end")

fream=LabelFrame(root,padx=100,pady=7,borderwidth=3,relief="raised")
fream.config(bg="#3683A5")
fream.grid(row=0,column=1,padx=55,pady=10)

text_label=Label(fream,text="ROBO",font=("Noto Sans",14,"bold"),bg="#5E6097")
text_label.grid(row=0,column=0,padx=20,pady=10)


image=ImageTk.PhotoImage(Image.open("image/assistant.png"))
image_label=Label(fream,image=image)
image_label.grid(row=1,column=0,pady=10,padx=20)


text=Text(root,font=('courier 10 bold'),bg="#435672")
text.grid(row=2,column=0)
text.place(x=100,y=455,width=500,height=100)

entry=Entry(root,justify=CENTER)
entry.place(x=150,y=570,width=350,height=30)


Button1=Button(root,text="ASK",font=("Noto Sans",10,"bold"),bg="#356696",pady=16,padx=40,borderwidth=3,relief=SOLID,command=ask)
Button1.place(x=100,y=650)

Button2=Button(root,text="SEND",font=("Noto Sans",10,"bold"),bg="#356696",pady=16,padx=40,borderwidth=3,relief=SOLID,command=send)
Button2.place(x=430,y=650)

Button3=Button(root,text="DELETE",font=("Noto Sans",10,"bold"),bg="#356696",pady=16,padx=40,borderwidth=3,relief=SOLID,command=del_text)
Button3.place(x=255,y=650)
root.mainloop()