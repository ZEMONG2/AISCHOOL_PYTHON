dct ={}

hakbun = input('학번 입력 => ')
irum = input('이름 입력 => ')
kor = int(input('국어 점수 입력 => '))
eng = int(input('영어 점수 입력 => '))
math = int(input('수학 점수 입력 => '))

dct['학번'] = hakbun
dct['이름'] = irum
dct['국어'] = kor
dct['영어'] = eng
dct['수학'] = math

dct["총점"] = dct['국어'] + dct['영어'] + dct['수학']
dct["평균"] = dct["총점"] / 3

print(dct)

print("\n\t\t\t *** 성적표 ***")
print("===============================================")
print("학번   이름    국어    영어    수학    총점    평균")
print("===============================================")
print("%s    %3s    %3d    %3d    %3d    %3d    %5.2f" %(dct['학번'],dct['이름'],dct['국어'],dct['영어'],dct['수학'],dct['총점'],dct['평균']))



score = int(input('총점을 입력해 주세요: '))

if score >= 90:
    print('수')
else:
    if 80 <= score < 90:
        print('우')
    else:
        if 70<= score <80:
            print("미")
        else:
            if 60<= score <70:
                print("양")
            else:
                print("가")
print("The End....")


count = 1
total = 0

while count <=100:
    total = total + count
    count = count + 1
    if(count == 10):
        break
else:
    print("1부터 100까지의 합은:",total)


message= "Hello"
messages = ["Hello World", "강릉원주대학교 정보기수루공학과"]
numbers = (1,2,3)
polygon = {"triangle":2,"rectangle":1,"line":0}
color = {"red", "green", "blue"}

for item in message:
    print(item)
print("1====================")
for item in messages:
    print(item)
print("2====================")
for item in numbers:
    print(item)
print("3====================")
for item in polygon:
    print(item)
print("4====================")
for item in color:
    print(item)



a = 10
if a>10:
    pass
else:
    print(a)


