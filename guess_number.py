import random

def play_game():
    target_number = random.randint(1, 100) 
    guess_count = 0 
    print("欢迎来到猜数字游戏！")
    print("我已经想好了一个 1 到 100 之间的数字，你猜猜看？")
    while True:
        try:
            # 获取用户输入，并转换为整数
            user_guess = int(input("请输入你猜的数字: "))
            guess_count += 1
            if user_guess < target_number:
                print("小了！再往大猜猜。")
            elif user_guess > target_number:
                print(" 大了！再往小猜猜。")
            else:
                print(f"恭喜你，猜对啦！答案就是 {target_number}。")
                print(f"你一共猜了 {guess_count} 次。")
                break 
        except ValueError:
            print("输入无效，请输入一个整数数字！")
if __name__ == "__main__":
    play_game()