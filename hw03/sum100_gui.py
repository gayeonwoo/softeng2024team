import tkinter as tk

def odd_even(num):
    if num%2==0:
        return True
    else:
        return False
    
window=tk.Tk()
window.title("Sum100")
window.resizable(width=False,height=False)

lbl_info=tk.Label(master=window,text="1부터 100까지 짝수의 합을 출력합니다.")
lbl_output=tk.Label(master=window,text=f"{sum([i for i in range(1,101) if odd_even(i)==True])}")

lbl_info.grid(row=0,pady=20,padx=10)
lbl_output.grid(row=1,pady=20)

window.mainloop()