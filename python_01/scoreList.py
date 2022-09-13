lst = []

hakbun = input('학번 입력 => ')
irum = input('이름 입력 => ')
kor = int(input('국어 점수 입력 => '))
eng = int(input('영어 점수 입력 => '))
math = int(input('수학 점수 입력 => '))

lst.append(hakbun)
lst.append(irum)
lst.append(kor)
lst.append(eng)
lst.append(math)
lst.append(lst[2]+lst[3]+lst[4])
lst.append(lst[5]/3)

print(lst)

print("\n\t\t\t *** 성적표 ***")
print("===============================================")
print("학번   이름    국어    영어    수학    총점    평균")
print("===============================================")
print("%s    %3s    %3d    %3d    %3d    %3d    %5.2f" %(lst[0],lst[1],lst[2],lst[3],lst[4],lst[5],lst[6]))