import random
import time
from dis import code_info

coin_sides =["앞면", "뒷면"]
user_wins = 0
computer_wins = 0
round_played = 0

print("동전 던지기 게임이 시작되었습니다.")
while True:
    print(f"==========ROUND{round_played}==========")
    print("==========현재 전적==========")
    print(f"사용자 : {user_wins}, 컴퓨터 : {computer_wins}")
    break


    user_guess = input("앞면과 뒷면 중 하나를 선택해주세요. (그만하려면 '종료' 입력 :")
    if user_guess == "종료":
        print("==========게임 종료==========")
        print(f"최종 전적: 사용자{user_wins}승, 컴퓨터{computer_wins}")
        print("==========================")
        break

    if user_guess not in coin_sides:
        print("앞면, 뒷면 또는 종료 중 하나를 정확히 입력해 주세요.")
        continue

    print("\n동전을 던집니다...!")
    time.sleep(2)

    coin_result = random.choice(code_sides)

    print(f"\n동전은{coin_result}이(가) 나왔습니다!")

    if user_guess == coin_result:
        print("예측 성공! 맞추셧습니다. \n")
        user_wins += 1

    else:
        print("예측 실패... 실패했습니다.\n")
        computer_wins += 1

    round_plays += 1

    if user_wins == 5:
        print(f"축하합니다! 시용자가{user_wins}승으로 게임에서 승리했습니다.")
    elif:
        print(f"아쉽네요... 컴퓨터가{computer_wins}승으로 게임에서 승리했습니다.")
        break

