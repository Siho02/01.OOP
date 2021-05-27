
# >python BookShop.py

# Customer / Book 클래스를 사용해서 정보 저장(메모리에 생성) 및 활용
# Customer 객체 생성 -> getCustName() 호출해서 고객 이름 출력

# 모듈 적용

from CustomerInfo import Customer
from BookInfo import Book
#ctrl + 마우스 클릭 -> 해당 모듈로 이동 

class BookShopAdmin:
   

    # self 라는 키워드는 클래스 내에 멤버 변수 선언 및 호출 시에 사용
    # 멤버 변수를 사용하는 메소드들도 parameter or argument or 인수 or 인자

    # BookShopAdmin에는 멤버 변수가 없음 따라서 self 불필요
    # 객체 생성 후에만 self 키워드가 유효한 기능 따라서 객체 생성 없이 메소드만 호출시에는 self parameter 미선언!
    def cust_create() : 
        #c1은 로컬변수, 메소드 실행 시에 생성되었다가 메소드 종료되며 메모리에서 삭제
        #시스템 자원의 한계로 메모리 관리를 자체적으로 함
        c1 = Customer('Amy', 'VVIP')
        return c1

    def book_create():
        b1 = Book('Python basic', '종원')
        return b1

    print("dd")


    # >python BookShopAdmin.py 명령어로 실행시 최초로 자동 실행되는 로직 코드
    # !!!!!암기!!!!! 
    if __name__ == '__main__':
        # 생성된 객체의 주소값을 보유하고 있는 c1값을 그대로 받아서 출력 따라서 메모리 위치 출력
       print(cust_create())

       #생성된 객체가 저장된 시스템의 메모리의 이름을 c1이라는 새로운 변수에 대입
       c1 = cust_create()

       #c1 보유한 주소번지에 저장된 객체의 getCustName() 이라는 고객 이름을 반환하는 메소드의 결과값 받고 출력
       print(c1.getCustName())

    print(8)

