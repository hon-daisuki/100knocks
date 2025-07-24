import argparse
import sys

def main():
    parser = argparse.ArgumentParser(description='引数の数に応じてメッセージを表示します')
    parser.add_argument('--arg1', type=str, help='1つ目の引数')
    parser.add_argument('--arg2', type=str, help='2つ目の引数')

    args = parser.parse_args()

    # sys.argvを使って-hのみのときも対応
    if len(sys.argv) == 1:
        print("引数がありません")
    elif args.arg1 and not args.arg2:
        print(f"引数1つを受け取りました: arg1 = {args.arg1}")
    elif args.arg1 and args.arg2:
        print(f"引数2つを受け取りました: arg1 = {args.arg1}, arg2 = {args.arg2}")
    else:
        print("想定外の使い方です")

if __name__ == '__main__':
    main()
