import argparse
import random

def main():
    parser = argparse.ArgumentParser(
        description="無惨と鳴女に同時に勝たないと、地獄行き。ジャンケンで勝負せよ。\n"
                    "引数 kata に 'グー'、'チョキ'、'パー' のいずれかを指定すること。"
    )
    parser.add_argument('--kata', required=True, help="自分の手。グー・チョキ・パーのいずれか")

    args = parser.parse_args()
    player = args.kata

    valid = ['グー', 'チョキ', 'パー']
    if player not in valid:
        print("不正な入力です。グー、チョキ、パーのいずれかを指定してください。")
        return

    muzan = random.choice(valid)
    nakime = random.choice(valid)

    def judge(me, opponent):
        if me == opponent:
            return 'draw'
        if (me == 'グー' and opponent == 'チョキ') or \
           (me == 'チョキ' and opponent == 'パー') or \
           (me == 'パー' and opponent == 'グー'):
            return 'win'
        return 'lose'

    result_muzan = judge(player, muzan)
    result_nakime = judge(player, nakime)

    print(f"あなた: {player}")
    print(f"無惨: {muzan}")
    print(f"鳴女: {nakime}")
    print("――――――――――")

    if result_muzan == 'win' and result_nakime == 'win':
        print(" 無惨と鳴女、両者を圧倒！お前が最強の剣士だ！")
    else:
        print(" 無惨と鳴女の呪いが襲いかかる… 修行して出直せ。")

if __name__ == '__main__':
    main()
