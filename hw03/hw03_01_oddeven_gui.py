import tkinter as tk
from tkinter import messagebox

def is_even(n):
    return n%2==0

def check_even():
    try:
        num = int(entry.get())
        if is_even(num):
            result = f"{num}은 짝수입니다."
        else:
            result = f"{num}은 홀수입니다."

        result_label.config(text=result)
    except ValueError:
        messagebox.showerror("자연수를 입력하세요.")

def main():
    root = tk.Tk()
    root.title("홀수 짝수")

    label = tk.Label(root, text="숫자를 입력하시오.")
    label.grid(row=0, column=0)

    global entry
    entry = tk.Entry(root)
    entry.grid(row=1, column=0)

    button = tk.Button(root, text="입력", command=check_even)
    button.grid(row=2, column=0)

    global result_label
    result_label = tk.Label(root, text="")
    result_label.grid(row=3, column=0)

    root.mainloop()


if __name__ == '__main__':
    main()