# by LV, Rank
# rank = 1 新手
#price = 180 * (lv)

# rank = 2 普通
# LV(1) = 324, LV(2) = 712, LV(4) = 2068, LV(106051) = 29.31 * 10 ^ 8
#=> price = 324 * lv + (lv-1) * 710.24
# rank = 3 神器
# LV(1) = 600, LV(4) = 2820, LV(128775) = 65.40 * 10 ^ 8
#=> price = 613 * lv + (lv-1) * 781.55
# rank = 4 史诗
# LV(1) = 1000, LV(2) = 1282, LV(3) = 2262, LV(128778) = 84.64 * 10 ^ 8
#=> price = 988 * lv + (lv-1) * 805.64
# rank = 5 独特
# LV(106054) = 70.36 * 10 ^ 8
#=> price = 1533 * lv + (lv -1) * 925.37

def item_valuation(lv, rank):
    V = [[180, 0], [324, 710.24], [613, 781.55], [988, 805.64], [1533, 925.37]]
    price = lv * V[rank - 1][0] + (lv -1 ) * V[rank-1][1]
    return round(price)

if __name__ == '__main__':
    p = item_valuation(100, 5)
    print(f'price={p}')

    x = [1, 2, 3, 4, 5]
    y = x.pop(3)
    print(y, x)