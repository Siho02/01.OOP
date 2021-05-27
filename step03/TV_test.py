from TVInfo import TV

class Test:
    #list에 tv객체들 저장하여 제공
    def tv_info_public():
        tv_all = [TV('television1', 'LG'), TV('television2', 'Samsung')]
        return tv_all
    


    #이미 list내에 저장된 tv객체들의 tv이름만 출력
    def tv_info_output(datas):
        for data in datas :
            print(data.getName())


    if __name__ == '__main__':
        #STEP02 - 데이터 받아서 활용하는 메소드 호출
        all = tv_info_public()
        tv_info_output(all)
        #객체를 생성하여 변수(tv)에 주소값 대입

    #    tv = TV('난 TV', 'LG')
    #    print(tv)   ##__str__ 자동 호출 >> 객체를 참조하는 변수(객체명 또는 객체라고 표현)
    #    print(TV('television', 'Samsung'))
    