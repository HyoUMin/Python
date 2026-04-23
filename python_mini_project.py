import math as m

print("====== MINI PROJECT ======\n")

# [전역 데이터 저장소]
# 모드 1, 2에서 입력받은 데이터가 저장될 공간
robot_info = {}       # 예: {"에이로봇": 200, "KDT로봇": 100.0}
locations = {}        # 예: {"강남": (10.5, 20.2), "판교": (30.0, 45.5)}

# --- 예외 처리 보조 함수  ---
def is_valid_num(num):

    check_num = num

    if len(check_num) > 0:
        if check_num.count('-') > 1 or check_num.count('.') > 1:
            print("잘못된 형식입니다.\n")
            return None

        else:
            if check_num.startswith('-'):
                check_number = check_num[1:]
            else:
                check_number = check_num

            if check_number.replace('.','').isdigit() and check_number != "":
                num = float(num)
                return num

            else:
                print("잘못된 형식입니다.\n")
                return None

    else:
        print("아무것도 입력되지 않았습니다.\n")
        return None

# --- 모드 1: 로봇 등록 ---
def register_robot():
    while True:
        robot_name = input("로봇 이름을 입력하세요: ")

        if not robot_name:
            print("입력되지 않았습니다. 다시 입력하세요.\n")
            continue

        if robot_name.lower() == 'x':
            print("입력을 종료합니다.\n")
            break
        
        robot_battery = input("로봇의 배터리 용량을 입력하세요(단위: mAh): ")
        
        if not robot_battery:
            print("입력되지 않았습니다. 다시 입력하세요.\n")
            continue

        if robot_battery.lower() == 'x':
            print("입력을 종료합니다.\n")
            break

        if robot_battery.startswith('-'):
            print("음수를 입력하셨습니다.\n")
            continue

        robot_battery = is_valid_num(robot_battery)

        robot_info[robot_name] = robot_battery
    print("등록된 로봇: ", robot_info, '\n')

# --- 모드 2: 장소 등록 ---
def register_location():

    while True:
        loc = input("장소를 입력하세요: ")

        if not loc:
            print("장소가 입력되지 않았습니다.\n")
            continue

        if loc.lower() == 'x':
            print("입력을 종료합니다.\n")
            break
        
        loc_x = input("위치(x 좌표)를 입력하세요: ")
        loc_y = input("위치(y 좌표)를 입력하세요: ")

        if not loc_x and loc_y:
            print("입력되지 않았습니다. 다시 입력하세요.\n")
            continue

        if loc_x.lower() == 'x' or loc_y.lower() == 'x':
            print("입력을 종료합니다.\n")
            break

        loc_x = is_valid_num(loc_x)
        loc_y = is_valid_num(loc_y)

        loc_tuple = loc_x, loc_y
        locations[loc] = loc_tuple

    print("등록된 장소: ", locations, '\n')


# --- 모드 4: 주행 시작 (가변 매개변수 *waypoints 사용) ---
def start_driving(robot ,start_node, end_node, *waypoints):

    total_path = [start_node] + list(waypoints) + [end_node]
    current_battery = robot_info[robot]
    init_current_battery = current_battery
    total_distance = 0

    for i in range(len(total_path) - 1):
        u, v = total_path[i], total_path[i+1]
        print(f"\n[ {u} ] " + "=" * 10 + ">" + f" [ {v} ] 이동 중...")

    for i in range(len(total_path) - 1):

        x1, y1 = locations[total_path[i]]
        x2, y2 = locations[total_path[i + 1]]

        distance = m.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
        total_distance += distance    
    
        consumed = distance * 10
        current_battery -= consumed

        if current_battery < 0:
            print("배터리가 방전되어 목적지에 도착하지 못했습니다.")
            robot_info[robot] = 0
            return
        
    robot_info[robot] = current_battery 

    print("-" * 30)
    print(f"목적지 '{end_node}' 도착 완료!")
    print(f"{robot} 총 주행 거리: {total_distance:.2f}m")
    print(f"{robot} 배터리: {init_current_battery} -> {current_battery:.2f}mAh") 

    print("\n[최종 주행 경로]")
    print("[출발] " + " -> ".join(total_path) + " [도착]")
    
# --- 메인 루프 (Main Menu) ---
def main():
    while True:
        print("\n=== 로봇 주행 시스템 메뉴 ===")
        print("1. 로봇 등록  2. 장소 등록  3. 경로 설정 및 주행  4. 종료")
        print("참고: 주행거리 1m당 배터리 10mAh 소모")

        try:
            choice = int(input("원하는 모드를 선택하세요: "))
        
            match choice:
                    case 1:
                        print("==== 로봇 등록 ====")
                        register_robot()
                    
                    case 2:
                        print("==== 장소 등록 ====")
                        register_location()

                    case 3:
                        print("==== 경로 설정 및 주행 ====")
                        
                        robot = input("주행시킬 로봇을 선택하세요: ")
                        if robot not in robot_info:
                            print("등록되지 않은 로봇입니다. 저장 후 선택하세요.\n")
                            continue
                            
                        start_node = input("출발 장소를 선택하세요: ")
                        if start_node not in locations:
                            print("등록되지 않은 장소입니다. 저장 후 선택하세요.\n")
                            continue

                        end_node = input("도착 장소를 선택하세요: ")

                        if end_node not in locations:
                            print("등록되지 않은 장소입니다. 저장 후 선택하세요.\n")
                            continue

                        waypoints_exist = int(input("경유지를 설정하세요.(1: 설정, 2: 종료): "))

                        waypoints_list = []

                        match waypoints_exist:
                            case 1:
                                waypoints_list = input("경유지를 입력하세요: ").split()
                                for i in waypoints_list:
                                    can_drive = True
                                    
                                    if i not in locations:
                                        print("등록되지 않은 장소입니다. 저장 후 선택하세요.\n")
                                        can_drive = False
                                        continue

                                if not can_drive:
                                    continue

                            case 2:
                                print("경유지 설정을 종료합니다.\n")
                                pass
                            case _:
                                print("잘못된 형식입니다.\n")
                                continue

                        start_driving(robot, start_node, end_node, *waypoints_list)

                    case 4:
                        print("시스템을 종료합니다.\n")
                        break
                    
                    case _:
                        print("잘못된 형식입니다.\n")
                        continue
        except ValueError:
            print("잘못된 형식입니다.\n")

if __name__ == "__main__":
    main()