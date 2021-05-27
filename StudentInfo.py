#한 학생 정보만 보유 가능한 클래스
#학생 수 만큼 객체 생성할 경우 데이터 혼란 방지

class Student:
    def __init__(self, name, grade, gender, subject):
        self.stu_name = name
        self.stu_grade = grade
        self.stu_gender = gender
        self.stu_subject = subject
    
    #멤버 변수들을 모두 결합하여 하나의 문자열로 반환
    #참조 변수명만 출력시에 str이 자동 실행~~??
    def __str__(self):
        return '학생 정보 : ' + self.stu_name + ' ' + self.stu_grade + ' ' + self.stu_gender + ' ' + self.stu_subject 

    # 각 멤버 변수별로 get/setxxx 메소드 보유되어 있다 가정

    # ? grade 1학년, 2학년, 3학년 값에 한해서만 지정
    # 유효성 검증 코드 필수
    def setStuGrade(self, new_grade):
        if new_grade[0] != '1' or '2' or '3':
            print("학년 입력이 올바르지 않습니다.")
        else : 
            self.stu_grade = new_grade


    # gender는 남or여or기타
    # 유효성 검증 코드 필수
    
    def setStuGender(self, new_gender):
        if new_gender == self.stu_gender:
            print("성별 정정 필요 없음")
        else: 
            if new_gender == '남':
                self.stu_gender = new_gender
            elif new_gender == '여':
                self.stu_gender = new_gender