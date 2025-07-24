import sys

def main():
    # コマンドライン引数の数をチェック（スクリプト名も含まれているため、最低1つはある）
    if len(sys.argv) < 2:
        print("エラー: 数字を引数として1つ入力してください（例: python script.py 0）")
        return

    # 引数を数値として取得（例外処理付き）
    try:
        arg = int(sys.argv[1])
    except ValueError:
        print("エラー: 数値を入力してください")
        return

    # 条件分岐して出力
    if arg == 0:
        print("0が入力されました")
    elif arg == 1:
        print("1が入力されました")
    elif arg == 2:
        print("2が入力されました")
    elif arg == 3:
        print("3が入力されました")
    else:
        print("0〜3の範囲で入力してください")

if __name__ == "__main__":
    main()
