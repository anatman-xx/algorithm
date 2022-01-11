import random
import matplotlib.pyplot as plt


def monte_carlo_flip_coin(n):
    def flip_coin():
        """
        抛硬币
        :return: 0 -> 正面
                 1 -> 反面
        """
        return random.randint(0, 1)

    tail_prob_val_list = list()
    tail_results = 0
    for i in range(n):
        tail_results += flip_coin()
        tail_prob_val = tail_results / (i + 1)
        tail_prob_val_list.append(tail_prob_val)

    # 绘图
    plt.axhline(y=0.5, color='r', linestyle='-')
    plt.title('flip coin tail probability')
    plt.xlabel('iterations') # 迭代次数
    plt.ylabel('probability') # 概率
    plt.plot(tail_prob_val_list)
    plt.show()


if __name__ == '__main__':
    monte_carlo_flip_coin(5000)
