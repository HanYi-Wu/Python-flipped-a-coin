import random
import matplotlib.pyplot as plt
import matplotlib

matplotlib.rcParams['font.family'] = 'SimHei'
plt.rcParams['toolbar'] = 'None'


def randomNumber():
    counts = int(input('请输入抛硬币的次数：'))
    print('开始实验......')
    i = 0
    heads = 0
    tails = 0
    while i < counts:
        num = random.randint(1, 10)
        if counts < 100:
            if num % 2:
                heads += 1
                if i != counts - 1:
                    print('正面', end=', ')
                else:
                    print('正面')
            else:
                tails += 1
                if i != counts - 1:
                    print('反面', end=', ')
                else:
                    print('反面')
            i += 1
        else:
            if num % 2:
                heads += 1
            else:
                tails += 1
            i += 1
    print('一共模拟了', str(counts), '次抛硬币，结果如下：', end='\n')
    print('正面：', str(heads), '次')
    print('反面：', str(tails), '次')
    fan = round((tails / counts * 100), 2)
    zheng = round((heads / counts * 100), 2)
    print('反面的概率为：', str(fan), '%')
    print('正面的概率为：', str(zheng), '%')
    print('计算方式：正或反出现的次数除以所有次数')
    a = input('按下ENTER查看饼图')
    fig, ax = plt.subplots()
    data = [int(fan), int(zheng)]
    labels = [('反面：' + str(tails)), ("正面：" + str(heads))]
    ax.pie(data, labels=labels, autopct='%1.1f%%')
    ax.set_title("随机事件课程实验饼图")
    plt.show()


if __name__ == '__main__':
    print('随机事件计算')
    print('制作：吴Hen')
    while True:
        randomNumber()
