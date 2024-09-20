def main():
    try:
        dan=int(input("구구단을 생성할 자연수를 입력해 주세요. >>"))
        with open("hw04/gugudan.html","w")as f:
            f.write("<html>")
            for i in range(1,10):
                f.write(f"{dan}x{i}={dan*i}<br>")
            f.write("</html>")
    except ValueError:
        print("자연수를 입력하세요.")

if __name__=="__main__":
    main()