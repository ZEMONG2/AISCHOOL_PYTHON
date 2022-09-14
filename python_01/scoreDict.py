lists=[]
cnt = 0

while True:
    dct = {}

    hakbun = input('학번 입력 => ')
    if hakbun == "exit":
        break
    irum = input('이름 입력 => ')
    kor = int(input('국어 점수 입력 => '))
    eng = int(input('영어 점수 입력 => '))
    math = int(input('수학 점수 입력 => '))

    dct['hakbun'] = hakbun
    dct['irum'] = irum
    dct['kor'] = kor
    dct['eng'] = eng
    dct['math'] = math

    dct["total"] = dct['kor'] + dct['eng'] + dct['math']
    dct["avg"] = dct["total"] / 3



    if dct["avg"] >= 90:
        dct["grade"] = '수'
    else:
        if 80 <= dct["avg"] < 90:
            dct["grade"]='우'
        else:
            if 70<= dct["avg"] <80:
                dct["grade"]='미'
            else:
                if 60<= dct["avg"] <70:
                    dct["grade"]='양'
                else:
                    dct["grade"]='가'
    lists.append(dct)
    cnt += 1


print("\n\t\t\t *** 성적표 ***")
print("===============================================")
print("학번   이름    국어    영어    수학    총점    평균    등급")
print("===============================================")
for list in lists:
    print("%s    %3s    %3d    %3d    %3d    %3d    %5.2f   %s" %(list['hakbun'],list['irum'],list['kor'],list['eng'],list['math'],list['total'],list['avg'],list["grade"]))


# count = 1
# total = 0
#
# while count <=100:
#     total = total + count
#     count = count + 1
#     if(count == 10):
#         break
# else:
#     print("1부터 100까지의 합은:",total)
#
#
# message= "Hello"
# messages = ["Hello World", "강릉원주대학교 정보기수루공학과"]
# numbers = (1,2,3)
# polygon = {"triangle":2,"rectangle":1,"line":0}
# color = {"red", "green", "blue"}
#
# for item in message:
#     print(item)
# print("1====================")
# for item in messages:
#     print(item)
# print("2====================")
# for item in numbers:
#     print(item)
# print("3====================")
# for item in polygon:
#     print(item)
# print("4====================")
# for item in color:
#     print(item)
#
#
#
# a = 10
# if a>10:
#     pass
# else:
#     print(a)
#
#
