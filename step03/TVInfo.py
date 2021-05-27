# TV데이터를 표현하는 클래스

class TV:
    def __init__(self, name, company_name ):
        self.name = name
        self.company_name = company_name
    
    def __str__(self):
        return '제품 모델명 : ' + self.name + ', ' + '제조사 : ' + self.company_name

    def getName(self):
        print("모델명을 반환합니다.")
        return self.name
    
    def setName(self):
        new_name = input("새 모델명을 입력 : ")
        self.name = new_name