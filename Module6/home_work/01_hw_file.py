# Напишите функцию log() принимающую в качестве аргумента строку и дописывающую это строку в конец файла

def log(text, file="log.txt"): #если при использовании функции будет указано 2 аргумента, то запишем в новый, если нет то в тот что указан в функции
    f = open(file, "a", encoding="utf-8")
    f.write("\n" + text)
    f.close()
    pass


log("hello world")  # дописывает "hello world" в конец файла log.txt
log("message", "log01.txt")  # дописывает "message" в конец файла log01.txt
