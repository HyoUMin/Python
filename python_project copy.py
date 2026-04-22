

# # 힌트: 
# #     1. 입력받은 문자열에서 소수점('.')을 한 번만 제거해본 후 .isdigit()인지 확인
# #     2. 음수('-') 처리가 필요하다면 첫 글자도 확인
# #     3. 유효하면 float로 변환하여 반환, 아니면 None 반환 (조건문 활용)

# def is_valid_num(num):
#     check_num = num
#     if len(check_num) > 0:
#         if check_num.count('-') > 1 or check_num.count('.') > 1:
#             print("잘못된 형식입니다.")
#         else:
#             if check_num.startswith('-'):
#                 check_num = check_num.lstrip('-')

#                 if check_num.replace('.','').isdigit():
#                     num = float(num)
#                 else:
#                     num = None
#                     print("잘못된 형식입니다.")

#             else:
#                 if check_num.replace('.','').isdigit():
#                     num = float(num)
#                 else:
#                     num = None
#                     print("잘못된 형식입니다.")
#     else:
#         print("아무것도 입력되지 않았습니다.")



# # try:
# #     num = float(input())

# # except:
# #     print('예외가 발생했습니다.')



robot_info = {}       # 예: {"name": "알파로봇", "battery": 100.0}
locations = {}        # 예: {"강남": (10.5, 20.2), "판교": (30.0, 45.5)}

def is_valid_num(num):

    check_num = num

    if len(check_num) > 0:
        if check_num.count('-') > 1 or check_num.count('.') > 1:
            print("잘못된 형식입니다.")
            return None

        else:
            if check_num.startswith('-'):
                check_num = check_num[1:]

                if check_num.replace('.','').isdigit():
                    num = float(num)
                    return num

                else:
                    print("잘못된 형식입니다.")
                    return None

            else:
                if check_num.replace('.','').isdigit():
                    num = float(num)
                    return num

                else:
                    print("잘못된 형식입니다.")
                    return None

    else:
        print("아무것도 입력되지 않았습니다.")
        return None
    
    
#  힌트:
#     1. input()으로 이름과 초기 배터리 입력받기
#     2. 배터리 입력이 숫자인지 is_valid_num으로 검증
#     3. robot_info 딕셔너리에 저장

def register_robot():
    while True:
        robot_name = input("로봇 이름을 입력하세요: ")

        if not robot_name:
            print("입력되지 않았습니다. 다시 입력하세요.")
            continue

        if robot_name.lower() == 'x':
            print("계산을 종료합니다.")
            break
        
        robot_battery = input("로봇의 배터리 용량을 입력하세요: ")
        
        if not robot_battery:
            print("입력되지 않았습니다. 다시 입력하세요.")
            continue

        if robot_battery.lower() == 'x':
            print("계산을 종료합니다.")
            break

        if robot_battery.startswith('-'):
            print("음수를 입력하셨습니다.")
            continue

        robot_battery = is_valid_num(robot_battery)

        robot_info[robot_name] = robot_battery

register_robot()
print(robot_info)


# --- 모드 2: 장소 등록 ---
def register_location():
    # 힌트:
    # 1. 장소 이름, x좌표, y좌표 입력받기
    # 2. 좌표가 숫자인지 검증
    # 3. (x, y)를 튜플로 묶어서 locations[장소이름] = 튜플 형태로 저장
    pass


