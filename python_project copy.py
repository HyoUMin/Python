

# 힌트: 
#     1. 입력받은 문자열에서 소수점('.')을 한 번만 제거해본 후 .isdigit()인지 확인
#     2. 음수('-') 처리가 필요하다면 첫 글자도 확인
#     3. 유효하면 float로 변환하여 반환, 아니면 None 반환 (조건문 활용)

def is_valid_num(num):
    check_num = num
    if len(check_num) > 0:
        if check_num.count('-') > 1 or check_num.count('.') > 1:
            print("잘못된 형식입니다.")
        else:
            if check_num.startswith('-'):
                check_num = check_num.lstrip('-')

                if check_num.replace('.','').isdigit():
                    num = float(num)
                else:
                    num = None
                    print("잘못된 형식입니다.")

            else:
                if check_num.replace('.','').isdigit():
                    num = float(num)
                else:
                    num = None
                    print("잘못된 형식입니다.")
    else:
        print("아무것도 입력되지 않았습니다.")





# try:
#     num = float(input())

# except:
#     print('예외가 발생했습니다.')
