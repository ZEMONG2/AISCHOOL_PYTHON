fp = open("text.txt", "rt", encoding="utf-8")

while True:
    line = fp.readline()
    if line == "":
        break
    print(line.strip())

fp.close()


# lines = fp.readlines() #개행문자를 기준으로 리스트 형식으로 출력
#
# for line in lines:
#     print(line, end="")