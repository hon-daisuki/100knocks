# test.py

import random
import sys

def test():
    win_map = {
        "グー": "チョキ",
        "チョキ": "パー",
        "パー": "グー"
    }

    hands = ["グー", "チョキ", "パー"]

    args = sys.argv

    if len(args) != 2:
        print("引数不正です")
        return "引数不正です"

    user_hand = args[1]
    computer_hand = random.choice(hands)

    print(f"あなた：{user_hand}、私：{computer_hand}")

    if computer_hand == win_map[user_hand]:
        print("あなたの勝利です")
    elif user_hand == win_map[computer_hand]:
        print("あなたの負けです")
    else:
        print("あいこです")

if __name__ == "__main__":
    test()
