def f():
    line = str(input("Etner string: "))

    for i in range(0, int(len(line)/2)+1):
        if (line[i] == 'п' or line[i] == "П"):
            line = line[0:i] + '*' + line[i+1:]

    print(f"Sting: {line}")
f()    