x = 1
y = -2

if x > 0:
    if y > 0:
        print("第一象限")
    else:
        print("第四象限")
else:
    if y > 0:
        print("第二象限")
    else:
        print("第三象限")

        # ------------------上公交车
money = int(input("请输入公交卡余额:"))
sit = int(input("请输入座位剩余:"))
if money > 2:
    print("可以上公交车")
    if sit > 0:
        print("可以坐到位子上")
    else:
        print("没有位子了")
else:
    print("余额不足")
