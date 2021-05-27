from TeacherInfo import Teacher

class TeacherTest:
    
    def teacher_public():
        teacher_info_list = []

        with open('teacher.csv', 'r', encoding = 'utf-8') as f:
            datas = f.readlines()
        
        for data in datas :
            lst = data.split(',')
            teacher_info_list.append(Teacher(lst[0],lst[1],lst[2]))
            
        return teacher_info_list

    if __name__ == '__main__':
        all_teacher = teacher_public()
        print(all_teacher[1].get_name())
        print(all_teacher[1].get_grade())
        print(all_teacher[1].set_grade())
