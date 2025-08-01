import sys

def main():
    
    args = sys.argv[1:]


    if len(args) == 0:
        print("【無限城の石畳】何も手にしていない。")
    elif len(args) == 1:
       print(f"【鬼の間】一つ目の武器を構えた: {args[0]}")
    elif len(args) == 2:
       print(f"【闇の通路】二つの武器を構えた: {args[0]}, {args[1]}")
    elif len(args) == 3:
       print(f"【玉座の間】三つの力を解放した: {args[0]}, {args[1]}, {args[2]}")
    else:
       print("【錯乱の間】持ち物が多すぎる！力を制御できない…")

if __name__ == "__main__":
    main()
