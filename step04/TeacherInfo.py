class Teacher:
    def __init__(self, name, grade, subject):
        self.t_name = name
        self.t_grade = grade
        self.t_subject = subject
    
    def __str__(self):
        return self.t_name + '선생님은 ' + self.t_grade + ' ' + self.t_subject + '담당입니다.'

    def get_name(self):
        return self.t_name
    
    def get_grade(self):
        return self.t_grade
    
    # def set_grade(self):
    #     new_grade = input("변경할 담당 학년을 입력하세요 : ")
    #     if new_grade == self.t_grade:
    #         print("변경할 필요가 없습니다.")
    #     else:
    #         if new_grade not in ['1학년', '2학년', '3학년']:
    #             print("잘못된 입력값입니다.")
    #         else:
    #             self.t_grade = new_grade
        
    #     return self.t_name + '선생님의 담당 학년이' + self.t_grade +'로 변경 되었습니다.'    


    def set_grade(self):
        new_grade = input("변경할 담당 학년을 입력하세요 : ")
        msg = self.t_name + '선생님의 담당 학년이' + new_grade +'로 변경 되었습니다.'
        if new_grade == self.t_grade:
            print("변경할 필요가 없습니다.")
            msg = '변동 없음'
        else:
            if new_grade not in ['1학년', '2학년', '3학년']:
                
                msg = '잘못된 입력값입니다. 확인 부탁드립니다.'
            else:
                self.t_grade = new_grade

        return msg    