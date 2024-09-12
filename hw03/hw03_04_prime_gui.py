import tkinter as tk
import time

def is_prime(num):
    if num>2:
        for i in range(2,num):
            if num%i==0:
                return False
            else:
                continue
        return True
    elif num==2:
        return True
    else:
        return False

def main():

    window=tk.Tk()
    window.title("Print prime")
    window.resizable(width=False, height=False)

    lbl_info=tk.Label(master=window,text="1부터 50까지 숫자 중 소수를 출력합니다.")
    lbl_p=tk.Label(master=window,text=f"{[i for i in range(1,51) if is_prime(i)==True]}")

    lbl_info.grid(row=0,pady=20)
    lbl_p.grid(row=1,pady=20,padx=10)

    window.mainloop()

if __name__ =="__main__":
    main()
