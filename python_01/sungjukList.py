from sungjukClass import Sungjuk

def f_menu():
    print("*** 메뉴 ***")
    print("1. 성적정보 입력")
    print("2. 성적정보 출력")
    print("3. 성적정보 조회")
    print("4. 성적정보 수정")
    print("5. 성적정보 삭제")
    print("6. 프로그램 종료")

# 성적정보 입력
def f_input(f_students):
    obj = Sungjuk()
    obj.input_sungjuk()
    obj.process_sungjuk()

    f_students.append(obj)
    print("\n성적정보 입력 성공!!\n")


# 성적정보 출력
def f_output(f_students):
    total_avg = 0


    print("\n\t\t\t\t\t *** 성적표 ***")
    print("===============================================================")
    print(" 학번     이름     국어     영어     수학     총점     평균     등급")
    print("===============================================================")
    for f_student in f_students:  # for 변수 in 컨테이너 객체
        total_avg += f_student.avg
        f_student.output_sungjuk()

    print("===============================================================")
    print("총학생 수 = %s, 전체 평균 = %s" % (len(f_students), total_avg / len(f_students)))
    print()


# 성적정보 조회
def search(f_students):
    a = input("조회할 학번을 입력하세요 : ")
    for f_student in f_students:
        if a == f_student.hakbun:
            print("\n\t\t\t\t\t *** 성적표 ***")
            print("===============================================================")
            print(" 학번     이름     국어     영어     수학     총점     평균     등급")
            print("===============================================================")
            f_student.output_sungjuk()
            print("===============================================================")
            print()
            break
    else:
        print("조회할 학번 %s가 없습니다." % a)

# # 성적정보 수정
def edit(f_students):
    a = input("수정할 학번을 입력하세요 :")
    for data in f_students:
        if a == data["hakbun"]:
            data["kor"] = int(input("국어점수를 입력하세요 : "))
            data["eng"] = int(input("영어점수를 입력하세요 : "))
            data["math"] = int(input("수학점수를 입력하세요 : "))

            data["tot"] = data["kor"] + data["eng"] + data["math"]
            data["avg"] = data["tot"] / 3

            if data["avg"] >= 90:
                data["grade"] = "수"
            elif 80 <= data["avg"] < 90:
                data["grade"] = "우"
            elif 70 <= data["avg"] < 80:
                data["grade"] = "미"
            elif 60 <= data["avg"] < 70:
                data["grade"] = "양"
            else:
                data["grade"] = "가"
            print("학번 %s 성적정보 수정 성공!!!" % a)
            break
    else:
        print("수정할 학번 %s가 없습니다." % a)

# # 성적정보 삭제
def delete(f_students):
    a = input("삭제할 학번을 입력하세요 : ")
    for data in f_students:
        if a == data["hakbun"]:
            f_students.remove(data)
            print("학번 %s 성적정보 삭제 성공!!" % a)
            break
    else:
        print("삭제할 학번 %s가 없습니다." % a)


if __name__ == "__main__":
    students = []

    while True:
        f_menu()
        menu = int(input("\n메뉴를 선택하세요 : "))
        if menu == 1:
            f_input(students)
        elif menu == 2:
            f_output(students)
        elif menu == 3:
            search(students)
        elif menu == 4:
            edit(students)
        elif menu == 5:
            delete(students)
        elif menu == 6:
            print("\n프로그램 종료...")
            break
        else:
            print("\n메뉴를 다시 입력하세요!\n")