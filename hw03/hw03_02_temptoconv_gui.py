import tkinter as tk
from tkinter import messagebox

def f2c(temp_f:float)->float:
    return(temp_f - 32) * 5 / 9

def c2f(temp_c:float)->float:
    return (temp_c * 9/5) + 32

def f2c_temp():
    try:
        temp_f = float(f_entry.get())
        temp_c = f2c(temp_f)
        c_entry.delete(0, tk.END)
        c_entry.insert(0, f"{temp_c:.1f}")
    except ValueError:
        c_entry.delete(0, tk.END)
        c_entry.insert(0, "바르게 입력해주세요.")

def c2f_temp():
    try:
        temp_c = float(c_entry.get())
        temp_f = c2f(temp_c)
        f_entry.delete(0, tk.END)
        f_entry.insert(0, f"{temp_f:.1f}")
    except ValueError:
        f_entry.delete(0, tk.END)
        f_entry.insert(0, "바르게 입력해주세요.")

def main():
    root = tk.Tk()
    root.title("온도변환 프로그램")

    f_label = tk.Label(root, text="화씨(℉)")
    f_label.grid(row=0, column=0, pady=20)

    global f_entry
    f_entry = tk.Entry(root)
    f_entry.grid(row=0, column=1)

    f_to_c_button = tk.Button(root, text="화씨 -> 섭씨 변환", command=f2c_temp)
    f_to_c_button.grid(row=0, column=2)

    c_label = tk.Label(root, text="섭씨(℃)")
    c_label.grid(row=1, column=0, pady=20)

    global c_entry
    c_entry = tk.Entry(root)
    c_entry.grid(row=1, column=1)

    f_to_c_button = tk.Button(root, text="섭씨 -> 화씨 변환", command=c2f_temp)
    f_to_c_button.grid(row=1, column=2)



    root.mainloop()



if __name__ == '__main__':
    main()
