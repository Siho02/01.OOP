# 고객(이름(cust_name), 등급(cust_grade))
# 멤버 변수 : cust_name, cust_grade
# 메소드 : 이름(getCust_name or getCustName) & 등급(getCust_grade or getCustGrade) 리턴

class Customer:
    
    #생성자 - 객체 생성(실 데이터로 생성 = 멤버 변수에 값 할당 = 멤버 변수 초기화)
    def __init__(self, name, grade):
        self.cust_name = name
        self.cust_grade = grade

    def getCustName(self):
        return self.cust_name
