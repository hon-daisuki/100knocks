import argparse
import sys

def main():
   parser = argparse.ArgumentParser(description="無限城での試練（argparse編）")
   parser.add_argument('--breath', type=str, help='呼吸法')
   parser.add_argument('--sword', type=str, help='日輪刀の種類')

   args = parser.parse_args()

   if len(sys.argv) == 1:
       print("【始まりの間】呼吸も刀も構えていない…")
   elif args.breath and not args.sword:
       print(f"【呼吸の間】呼吸を構えた: {args.breath}")
   elif args.breath and args.sword:
       print(f"【剣技の間】呼吸: {args.breath}, 日輪刀: {args.sword}")
   else:
       print("【混乱の間】入力が不完全です")

if __name__ == '__main__':
    main()
