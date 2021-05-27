
from StudentInfo import Student

class DataPublic:
    def stu_public():
        with open('students.csv', 'r', encoding = 'utf-8') as f:
            data = f.readline()
        
        print(data)
        print(data.split(','))

        s_info = data.split(',')
        s = Student(s_info[0],s_info[1],s_info[2],s_info[3])
        print(s)

    def stu_public2():
        all_stu = [] 
        
        with open('students.csv', 'r', encoding = 'utf-8') as f:
            data = f.readlines()
        
        for v in data:
            sv = v.split(',')
            all_stu.append(Student(sv[0],sv[1],sv[2],sv[3]))

        return all_stu

    #csv파일로부터 read해서 프로그램 상에서 사용가능한 구조의 데이터 객체로 생성하여 반환(제공)
    def stu_public3():
        all_stu = [] 
        
        with open('students.csv', 'r', encoding = 'utf-8') as f:
            data = f.readlines()
        
        for v in data:
            sv = v.split(',')
            all_stu.append(Student(sv[0],sv[1],sv[2],sv[3]))

        return all_stu
    
    #제공해주는 학생 정보들을 반복문을 통해 출력하는 메소드
    def stu_all_print(all_stu):
        for value in all_stu:
            print(value)     ##__str__ 메소드가 참조 변수값을 단순 출력시에 자동으로 호출 됨


    if __name__ == '__main__':
        #stu_public()
        #stu_public2()

        all = stu_public3()
        stu_all_print(all)