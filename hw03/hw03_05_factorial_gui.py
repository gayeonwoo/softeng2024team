import tkinter as tk

def factorial(num):
    if num>1:
        return num*factorial(num-1)
    elif num==1:
        return 1
    
def run():
    num=ent_num.get()
    if len(str(round(float(num))))==len(num) and int(num)>0:
        lbl_output["text"]=f"{factorial(int(num))}"
        lbl_b["text"]=""
    else:
        lbl_b["text"]="*자연수를 입력하세요."
        lbl_output["text"]=""

def main():
    window=tk.Tk()
    window.title("Factorial")
    window.resizable(width=False,height=False)

    global lbl_b
    lbl_b=tk.Label(master=window)

    frame=tk.Frame(master=window)

    global ent_num
    ent_num=tk.Entry(master=frame,width=5)
    
    lbl_f=tk.Label(master=frame,text="!")
    btn_convert=tk.Button(master=frame,
                          text="=",
                          command=run)
    global lbl_output
    lbl_output=tk.Label(master=frame)

    lbl_b.grid(row=0,padx=10)
    frame.grid(row=1,padx=10,pady=20)
    ent_num.grid(row=0,column=0)
    lbl_f.grid(row=0,column=1)
    btn_convert.grid(row=0,column=2)
    lbl_output.grid(row=0,column=3)

    window.mainloop()

if __name__=="__main__":
    main()
