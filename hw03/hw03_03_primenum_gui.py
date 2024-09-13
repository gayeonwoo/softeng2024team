import tkinter as tk
from tkinter import messagebox

def is_prime(n:int) -> bool:
    if n<2:
        return False
    for i in range(2,n):
        if n % i == 0:
            return False
    return True

def check_prime():
    try:
        num = int(entry.get())
        if is_prime(num):
            result_label.config(text=f"{num}은 소수입니다.")
        else:
            result_label.config(text=f"{num}은 소수가 아닙니다.")
    except ValueError:
        messagebox.showerror("자연수를 입력하십시오.")

def main():
    root = tk.Tk()
    root.title("소수판별 프로그램")

    label = tk.Label(root, text="숫자를 입력하시오.")
    label.grid(row=0, column=0, pady=20)

    global entry
    entry = tk.Entry(root)
    entry.grid(row=1, column=0, padx=65)

    button = tk.Button(root, text="확인", command=check_prime)
    button.grid(row=2, column=0, pady=20)

    global result_label
    result_label = tk.Label(root, text="")
    result_label.grid(row=3, column=0)

    root.mainloop()

if __name__ == '__main__':
    main()
