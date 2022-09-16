class Person:
    def __init__(self, hakbun, irum):
        self._hakbun = hakbun
        self._irum = irum
        print("객체 생성")
    # def setHakbun(self, hakbun) :
    #     self._hakbun = hakbun
    #     print("학번 변경")
    # def setIrum(self, irum):
    #     self._irum = irum
    #     print("이름 변경")
    def printData(self):
        print("학번 :", self._hakbun, "이름 :", self._irum)
    def __del__(self):
        print("객체 소멸",self._hakbun)


if __name__ == "__main__":
    obj = Person("A001","이기자")
    # obj.setHakbun("A001")
    # obj.setIrum("이기자")
    obj.printData()
    obj = Person("A002", "이기자")
    obj.printData()