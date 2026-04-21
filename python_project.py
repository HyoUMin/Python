# [전역 데이터 저장소]
# 모드 1, 2에서 입력받은 데이터가 저장될 공간
robot_info = {}       # 예: {"name": "알파로봇", "battery": 100.0}
locations = {}        # 예: {"강남": (10.5, 20.2), "판교": (30.0, 45.5)}

# --- 예외 처리 보조 함수  ---
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

# --- 모드 1: 로봇 등록 ---
def register_robot():
    """
    힌트:
    1. input()으로 이름과 초기 배터리 입력받기
    2. 배터리 입력이 숫자인지 is_valid_num으로 검증
    3. robot_info 딕셔너리에 저장
    """
    pass

# --- 모드 2: 장소 등록 ---
def register_location():
    """
    힌트:
    1. 장소 이름, x좌표, y좌표 입력받기
    2. 좌표가 숫자인지 검증
    3. (x, y)를 튜플로 묶어서 locations[장소이름] = 튜플 형태로 저장
    """
    pass

# --- 모드 3: 경로 설정 (가변 매개변수 활용) ---
def set_path():
    """
    힌트:
    1. 출발지, 도착지 이름을 입력받고 locations에 존재하는지 확인
    2. 경유지들은 공백으로 구분해서 한꺼번에 입력받은 후 리스트로 변환
    3. 주행 함수(mode 4)를 호출할 때 *리스트 형태로 가변 매개변수를 전달
    """
    pass

# --- 모드 4: 주행 시작 (가변 매개변수 *waypoints 사용) ---
def start_driving(start_node, end_node, *waypoints):
    """
    힌트:
    1. start_node, *waypoints, end_node를 순서대로 합친 '전체 경로 리스트' 생성
    2. 반복문을 사용하여 (현재 지점 -> 다음 지점) 좌표를 튜플에서 가져옴
    3. 사칙연산: 피타고라스 정리를 사용하여 지점 간 거리 계산
    4. 배터리 계산: (계산된 거리 / 10) * 5 만큼 현재 배터리 차감
    5. 조건문: 차감 후 배터리가 0 이하인지 매 순간 체크 -> 0 이하면 break 및 정지 메시지
    6. 모든 경로 통과 시 최종 배터리 잔량 출력
    """
    pass

# --- 메인 루프 (Main Menu) ---
def main():
    while True:
        print("\n=== 자율주행 시스템 메뉴 ===")
        print("1. 로봇 등록  2. 장소 등록  3. 경로 설정 및 주행  4. 종료")
        choice = input("원하는 모드를 선택하세요: ")
        
        # 힌트: choice 값에 따라 위에서 만든 함수들을 조건문(if-elif)으로 호출
        # 잘못된 모드 번호 입력 시 예외 메시지 출력
        pass

if __name__ == "__main__":
    main()