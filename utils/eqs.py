# 品质系数: QAC
# rank: 破旧, 普通, 神器, 史诗, 独特, 不朽I, 不朽II
# 品质: D, C, B, A, S, SS, SSS
# Ex: 破旧 普通D 普通 C, QAC = 1, 普通 A, QAC = 5, 神器 D, QAC = 13, 神器 A, QAC = 19
# Ex: 史诗 SS, QAC = 37, 史诗 A, QAC = 33, 史诗 C, QAC = 29
# Ex: 独特 B, QAC = 45
# 暴伤(damage): D(70%-75%), C(75%-80%), B(80%-85%), A(85%-90%), S(90%-95%), SS(95%-100%), SSS(100%-105%), 不朽I(105%-110%), 不朽II(110%-115%)
# 暴击(crit): D(11%), C(12%), B(13%), A(14%), S(15%-17%), SS(18%-20%), SSS(21%-23%), 不朽I(24%-26%), 不朽II(27%-29%)

#weapons = [
#    ['新手剑', '一把普通的剑', '破旧', 'attack=10+7(5), (crit=10), lv=1'],
#    ['赤柳血刃', '似乎会给使用者提供生命气息', '神器', 'B: attack=6, B:hp=39, (attack=5, damage=28, armor-addi=14.03), lv=2'],
#    ['冰晶之刃', '剑锋覆盖者冰晶, 碰到的敌人都会被冻住', '神器', 'B: attack=561, D: damage=73, (armor-addi=16.53, armor-addi=26.36, armor-addi=23.08) lv=196'],
#    ['毛毛的爪子', '这? 这也是武器?', '史诗', 'SS: attack=28, B: crit=22, (armor-addi=14.41, armor=11, armor-addi=20.85, attack=15), lv=5'],
#    ['战士长剑', '六级战士使用的长剑', '史诗', 'SS: attack=730, A: armor=404, (damage=28, attack=558, crit=17, armor=222), lv=196'],
#    ['普通长剑', '朴实无华的长剑，有的只有强力的攻击力', '普通', 'D: attack=420, (hp-addi=16.85, damage=16), lv=199'],
#    ['狱岩石太刀', '用狱岩石制作的太刀, 据说拥有让使用者潜力爆发的神秘力量', '史诗', 'C: attack=578, B: crit=22, (hp=1335, armor=369, damage=41, crit=15), lv=197'],
#    ['紫炎波刃剑', '传说中狂战士最喜爱的剑', '史诗', 'B: attack=886, (damage=46, armor-addi=23.4, hp=1390, crit=13), lv=200'],
#    ['大师大冒险家之剑', '大师大冒险家之剑', '独特', 'B: attack=1248, C: hp=8546, (hp=1605, attack=496, damage=36, attack=537, armor-addi=42.95), lv=196'],
#    ['数珠丸恒次', '具体情况不明， 传说为日莲上人所有', '独特', 'D: attack=943+1197(13), (attack=507, crit=21, armor=313, hp=1198, attack-addi=32.33), lv=96'],
#    ['埃苏莱布斯军刃', '', '独特', 'A: attack=1346, C: armor=727, A: block=364, (hp-addi=24.08, armor=276, armor-addi=38.73, attack=655, attack-addi=38.27), lv=197'],
#]

# 新手剑: attack = 50 * QAC + 0.9 * LV
# 普通长剑: attack = 62 * QAC + 0.9 * LV
# 战士长剑: attack = 74 * QAC + 1 * LV, armor = 7 * QAC + 0.9 * LV
# 毛毛的爪子: attack = 76 * QAC + 1.1 * LV, crit (ref to quality)
# 冰晶之刃: attack = 88 * QAC + 1.2 * LV, damage (ref to quality)
# 赤柳血刃: attack = 90 * QAC + 1.2 * LV, hp = 100 * QAC + 0.9 * LV
# 狱岩石太刀: attack = 92 * QAC + 1.2 * LV, crit (ref to quality)
# 紫炎波刃剑: attack = 94 * QAC + 1.4 * LV

# 大师大冒险家之剑: attack = 100 * QAC + 1.8 * LV, hp = 150 * QAC + 1.8 * LV
# 数珠丸恒次: attack = 100 * QAC + 4 * LV
# 埃苏莱布斯军刃: attack = 100 * QAC + 2.1 * LV, armor = 20 * QAC + 1.6 * LV, block = 10 * QAC + 1 * LV
# 无名剑: attack = 100 * QAC + 2.7 * LV, crit (ref to quality) + 2.5 * 21
# 死亡之刃: attack = 100 * QAC + 2 * LV, crit (ref to qulity) + 1.5 * 21, damage (ref to quality) + 1.3 * 21
# 霜龙利刃: attack = 100 * QAC + 1.9 * LV, crit (ref to qulity) + 1.6 * 21, damage (ref to quality) + 1.3 * 21
# 阿加雷斯血色巨剑: attack = 100 * QAC + 1.8 * LV, crit (ref to qulity) + 1.5 * 21, damage (ref to quality) + 1.4 * 21
# 神龙纳格林之刃: attack = 100 * QAC + 2.8 * LV, damage (ref to quality) + 2 * 21
# 六翼天使武刃: attack = 100 * QAC + 2.6 * LV, damage (ref to quality) + 1.2 * 21, armor = 20 * QAC + 1.1 * LV
# 黑色冰虎刃: attack = 100 * QAC + 2 * LV, armor = 20 * QAC + 1.2 * LV, hp = 150 * QAC + 1.1 * LV
# 繁星之剑: attack = 100 * QAC + 1.7 * LV, damage (ref to quality) + 1 * 21, hp = 150 * QAC + 1 * LV
# 心碎瞬间短剑: attack = 100 * QAC + 2 * LV, damage (ref to qulity) + 1.4 * 21, armor = 20 * QAC + 0.9 * LV

ATTR_0 = {'attack': [0, 0], 'armor': [0, 0], 'hp': [0, 0], 'block': [0, 0], 'damage': [0, 0], 'crit': [0, 0], 'gold': [0]}

def empty_attr(attr):
    attr = {'attack': [0, 0], 'armor': [0, 0], 'hp': [0, 0], 'block': [0, 0], 'damage': [0, 0], 'crit': [0, 0], 'gold': [0]}
    return attr

WP = [{'ID': '001', 'name': '新手剑', 'desc': '一把普通的剑', 'attr': ATTR_0},
      {'ID': '002', 'name': '普通长剑', 'desc': '朴实无华的长剑，有的只有强力的攻击力', 'attr': ATTR_0},
      {'ID': '003', 'name': '战士长剑', 'desc': '六级战士使用的长剑', 'attr': ATTR_0},
      {'ID': '004', 'name': '毛毛的爪子', 'desc': '这? 这也是武器?', 'attr': ATTR_0},
      {'ID': '005', 'name': '冰晶之刃', 'desc': '剑锋覆盖者冰晶, 碰到的敌人都会被冻住', 'attr': ATTR_0},
      {'ID': '006', 'name': '赤柳血刃', 'desc': '似乎会给使用者提供生命气息', 'attr': ATTR_0},
      {'ID': '007', 'name': '狱岩石太刀', 'desc': '用狱岩石制作的太刀, 据说拥有让使用者潜力爆发的神秘力量', 'attr': ATTR_0},
      {'ID': '008', 'name': '紫炎波刃剑', 'desc': '传说中狂战士最喜爱的剑', 'attr': ATTR_0},
      {'ID': '020', 'name': '大师大冒险家之剑', 'desc': '大师大冒险家之剑', 'attr': ATTR_0},
      {'ID': '021', 'name': '数珠丸恒次', 'desc': '具体情况不明， 传说为日莲上人所有', 'attr': ATTR_0},
      {'ID': '022', 'name': '埃苏莱布斯军刃', 'desc': '埃苏莱布斯军刃', 'attr': ATTR_0},
      {'ID': '023', 'name': '无名剑', 'desc': '无名剑', 'attr': ATTR_0},
      {'ID': '024', 'name': '死亡之刃', 'desc': '死亡之刃', 'attr': ATTR_0},
      {'ID': '025', 'name': '霜龙利刃', 'desc': '霜龙利刃', 'attr': ATTR_0},
      {'ID': '026', 'name': '阿加雷斯血色巨剑', 'desc': '阿加雷斯血色巨剑', 'attr': ATTR_0},
      {'ID': '027', 'name': '神龙纳格林之刃', 'desc': '神龙纳格林之刃', 'attr': ATTR_0},
      {'ID': '028', 'name': '六翼天使武刃', 'desc': '六翼天使武刃', 'attr': ATTR_0},
      {'ID': '029', 'name': '黑色冰虎刃', 'desc': '黑色冰虎刃', 'attr': ATTR_0},
      {'ID': '030', 'name': '繁星之剑', 'desc': '繁星之剑', 'attr': ATTR_0},
      {'ID': '031', 'name': '心碎瞬间短剑', 'desc': '心碎瞬间短剑', 'attr': ATTR_0},
      ]

# 新手剑: attack = 50 * QAC + 0.9 * LV
ATTR = empty_attr(ATTR_0)
ATTR['attack'] = [50, 0.9]
WP[0]['attr'] = ATTR

# 普通长剑: attack = 62 * QAC + 0.9 * LV
ATTR = empty_attr(ATTR_0)
ATTR['attack'] = [62, 0.9]
WP[1]['attr'] = ATTR

# 战士长剑: attack = 74 * QAC + 1 * LV, armor = 7 * QAC + 0.9 * LV
ATTR = empty_attr(ATTR_0)
ATTR['attack'] = [74, 1]
ATTR['armor'] = [7, 0.9]
WP[2]['attr'] = ATTR

# 毛毛的爪子: attack = 76 * QAC + 1.1 * LV, crit (ref to quality)
ATTR = empty_attr(ATTR_0)
ATTR['attack'] = [76, 1.1]
ATTR['crit'] = [21, 0] # have this attr if attr['crit'] != 0
WP[3]['attr'] = ATTR

# 冰晶之刃: attack = 88 * QAC + 1.2 * LV, damage (ref to quality)
ATTR = empty_attr(ATTR_0)
ATTR['attack'] = [88, 1.2]
ATTR['damage'] = [21, 0] # have this attr if attr['damage'] != 0
WP[4]['attr'] = ATTR

# 赤柳血刃: attack = 90 * QAC + 1.2 * LV, hp = 100 * QAC + 0.9 * LV
ATTR = empty_attr(ATTR_0)
ATTR['attack'] = [90, 1.2]
ATTR['hp'] = [100, 0.9]
WP[5]['attr'] = ATTR

# 狱岩石太刀: attack = 92 * QAC + 1.2 * LV, crit (ref to quality)
ATTR = empty_attr(ATTR_0)
ATTR['attack'] = [92, 1.2]
ATTR['crit'] = [21, 0]
WP[6]['attr'] = ATTR

# 紫炎波刃剑: attack = 94 * QAC + 1.4 * LV
ATTR = empty_attr(ATTR_0)
ATTR['attack'] = [94, 1.4]
WP[7]['attr'] = ATTR

# 大师大冒险家之剑: attack = 100 * QAC + 1.8 * LV, hp = 150 * QAC + 1.8 * LV
ATTR = empty_attr(ATTR_0)
ATTR['attack'] = [100, 1.8]
ATTR['hp'] = [150, 1.8]
WP[8]['attr'] = ATTR

# 数珠丸恒次: attack = 100 * QAC + 4 * LV
ATTR = empty_attr(ATTR_0)
ATTR['attack'] = [100, 4]
WP[9]['attr'] = ATTR

# 埃苏莱布斯军刃: attack = 100 * QAC + 2.1 * LV, armor = 20 * QAC + 1.6 * LV, block = 10 * QAC + 1 * LV
ATTR = empty_attr(ATTR_0)
ATTR['attack'] = [100, 2.1]
ATTR['armor'] = [20, 1.6]
ATTR['block'] = [10, 1]
WP[10]['attr'] = ATTR

# 无名剑: attack = 100 * QAC + 2.7 * LV, crit (ref to quality) + 2.5 * 21
ATTR = empty_attr(ATTR_0)
ATTR['attack'] = [100, 2.7]
ATTR['crit'] = [21, 2.5]
WP[11]['attr'] = ATTR

# 死亡之刃: attack = 100 * QAC + 2 * LV, crit (ref to qulity) + 1.5 * 21, damage (ref to quality) + 1.3 * 21
ATTR = empty_attr(ATTR_0)
ATTR['attack'] = [100, 2]
ATTR['crit'] = [21, 1.5]
ATTR['damage'] = [21, 1.3]
WP[12]['attr'] = ATTR

# 霜龙利刃: attack = 100 * QAC + 1.9 * LV, crit (ref to qulity) + 1.6 * 21, damage (ref to quality) + 1.3 * 21
ATTR = empty_attr(ATTR_0)
ATTR['attack'] = [100, 1.9]
ATTR['crit'] = [21, 1.6]
ATTR['damage'] = [21, 1.3]
WP[13]['attr'] = ATTR

# 阿加雷斯血色巨剑: attack = 100 * QAC + 1.8 * LV, crit (ref to qulity) + 1.5 * 21, damage (ref to quality) + 1.4 * 21
ATTR = empty_attr(ATTR_0)
ATTR['attack'] = [100, 1.8]
ATTR['crit'] = [21, 1.5]
ATTR['damage'] = [21, 1.4]
WP[14]['attr'] = ATTR

# 神龙纳格林之刃: attack = 100 * QAC + 2.8 * LV, damage (ref to quality) + 2 * 21
ATTR = empty_attr(ATTR_0)
ATTR['attack'] = [100, 2.8]
ATTR['damage'] = [21, 2]
WP[15]['attr'] = ATTR

# 六翼天使武刃: attack = 100 * QAC + 2.6 * LV, damage (ref to quality) + 1.2 * 21, armor = 20 * QAC + 1.1 * LV
ATTR = empty_attr(ATTR_0)
ATTR['attack'] = [100, 2.6]
ATTR['armor'] = [20, 1.1]
ATTR['damage'] = [21, 1.2]
WP[16]['attr'] = ATTR

# 黑色冰虎刃: attack = 100 * QAC + 2 * LV, armor = 20 * QAC + 1.2 * LV, hp = 150 * QAC + 1.1 * LV
ATTR = empty_attr(ATTR_0)
ATTR['attack'] = [100, 2]
ATTR['armor'] = [20, 1.2]
ATTR['hp'] = [150, 1.1]
WP[17]['attr'] = ATTR

# 繁星之剑: attack = 100 * QAC + 1.7 * LV, damage (ref to quality) + 1 * 21, hp = 150 * QAC + 1 * LV
ATTR = empty_attr(ATTR_0)
ATTR['attack'] = [100, 1.7]
ATTR['hp'] = [150, 1]
ATTR['damage'] = [21, 1]
WP[18]['attr'] = ATTR

# 心碎瞬间短剑: attack = 100 * QAC + 2 * LV, damage (ref to qulity) + 1.4 * 21, armor = 20 * QAC + 0.9 * LV
ATTR = empty_attr(ATTR_0)
ATTR['attack'] = [100, 2]
ATTR['armor'] = [20, 0.9]
ATTR['damage'] = [21, 1.4]
WP[19]['attr'] = ATTR

#suits = [
#    ['新手铠甲', '普通的衣甲', '破旧', 'armor=10+7(5), (crit=10), lv=1'],
#    ['战士重铠', '六级战士使用的重型铠甲', '神器', 'C: armor=477, D: hp=2776, (hp=1054, armor-addi=18.48, armor-addi=26.87), lv=197'],
#    ['天权轻甲', '舍弃防御性能的轻甲，因为更加轻便, 攻击性能更加突出', '神器', 'B: armor=3， A: hp=10, A: attack=1, (hp-addi=7.1, hp=6, attack=3), lv=1'],
#    ['赤柳血铠', '似乎会给使用者提供生命气息', '神器', 'B: armor=430, C: hp=4115, (hp=1082, armor-addi=22.11, armor=171), lv=196'],
#    ['紫金守护胸甲', '够肉才能输出', '神器', 'D: armor=771, D:hp=2128, (hp=1116, armor-addi=29.18, armor-addi=21.98), lv=199'],
#]

# 新手铠甲: armor = 20 * QAC + 0 * LV
# 战士重铠: armor = 30 * QAC + 0.8 * LV, hp = 90 * QAC + 0.4 * LV
# 天权轻甲: armoa = 25 * QAC + 0.7 * LV, hp = 80 * QAC + 0.2 * LV, attack = 7 * QAC + 1 * LV
# 赤柳血铠: armor = 30 * QAC + 0.8 * LV, hp = 100 * QAC + 0.4 * LV
# 紫金守护胸甲 armor = 36 * QAC + 1 * LV, hp = 110 * QAC + 0.5 * LV
# 哈皮毛毛连身衣: armor = 30 * QAC + 0.9 * LV, hp = 90 * QAC + 0.4 * LV, attack = 6 * QAC + 0.8 * LV

# 剑豪盔甲: armor = 50 * QAC + 2.1 * LV, hp = 160 * QAC + 2.6 * LV
# 肃清者戎衣: hp = 160 * QAC + 1.8 * LV, attack = 16 * QAC + 2.5 * LV, block = 10 * QAC + 1.3 * LV
# 红月的夜行衣: armor = 50 * QAC + 1.2 * LV, hp = 160 * QAC + 1.7 * LV, attack = 16 * QAC + 1.2 * LV
# 隐武士铠甲: armor = 50 * QAC + 1.3 * LV, hp = 160 * QAC + 1.9 * LV, attack = 16 * QAC + 0.9 * LV
# 芬萨里尔追踪者: armor = 50 * QAC + 1.1 * LV, damage (ref to quality) + 1.6 * 21, attack = 16 * QAC + 1.8 * LV
# 黑镇月: armor = 50 * QAC + 2.6 * LV, hp = 160 * QAC + 2.1 * LV
# 破坏者H-018: armor = 50 * QAC + 1.6 * LV, hp = 160 * QAC + 1.6 * LV, damage (ref to quality) + 1.6 * 21
# 心花乱坠长袍: armor = 50 * QAC + 1.8 * LV, hp = 160 * QAC + 1.4 * LV, attack = 16 * QAC + 1.5 * LV
# 法夜: armor = 50 * QAC + 1.2 * LV, hp = 160 * QAC + 0.6 * LV, damage (ref to quality) + 2.1 * 21
ARMOR = [{'ID': '101', 'name': '新手铠甲', 'desc': '普通的衣甲', 'attr': ATTR_0},
      {'ID': '102', 'name': '战士重铠', 'desc': '六级战士使用的重型铠甲', 'attr': ATTR_0},
      {'ID': '103', 'name': '天权轻甲', 'desc': '舍弃防御性能的轻甲，因为更加轻便, 攻击性能更加突出', 'attr': ATTR_0},
      {'ID': '104', 'name': '赤柳血铠', 'desc': '似乎会给使用者提供生命气息', 'attr': ATTR_0},
      {'ID': '105', 'name': '紫金守护胸甲', 'desc': '够肉才能输出', 'attr': ATTR_0},
      {'ID': '106', 'name': '哈皮毛毛连身衣', 'desc': '哈皮毛毛连身衣', 'attr': ATTR_0},
      {'ID': '120', 'name': '剑豪盔甲', 'desc': '剑豪盔甲', 'attr': ATTR_0},
      {'ID': '121', 'name': '肃清者戎衣', 'desc': '肃清者戎衣', 'attr': ATTR_0},
      {'ID': '122', 'name': '红月的夜行衣', 'desc': '红月的夜行衣', 'attr': ATTR_0},
      {'ID': '123', 'name': '隐武士铠甲', 'desc': '隐武士铠甲', 'attr': ATTR_0},
      {'ID': '124', 'name': '芬萨里尔追踪者', 'desc': '芬萨里尔追踪者', 'attr': ATTR_0},
      {'ID': '125', 'name': '黑镇月', 'desc': '黑镇月', 'attr': ATTR_0},
      {'ID': '126', 'name': '破坏者H-018', 'desc': '破坏者H-018', 'attr': ATTR_0},
      {'ID': '127', 'name': '心花乱坠长袍', 'desc': '心花乱坠长袍', 'attr': ATTR_0},
      {'ID': '128', 'name': '法夜', 'desc': '法夜', 'attr': ATTR_0},
      ]

# 新手铠甲: armor = 20 * QAC + 0 * LV
ATTR = empty_attr(ATTR_0)
ATTR['armor'] = [20, 0]
ARMOR[0]['attr'] = ATTR

# 战士重铠: armor = 30 * QAC + 0.8 * LV, hp = 90 * QAC + 0.4 * LV
ATTR = empty_attr(ATTR_0)
ATTR['armor'] = [30, 0.8]
ATTR['hp'] = [90, 0.4]
ARMOR[1]['attr'] = ATTR

# 天权轻甲: armoa = 25 * QAC + 0.7 * LV, hp = 80 * QAC + 0.2 * LV, attack = 7 * QAC + 1 * LV
ATTR = empty_attr(ATTR_0)
ATTR['armor'] = [25, 0.7]
ATTR['hp'] = [80, 0.2]
ATTR['attack'] = [7, 1]
ARMOR[2]['attr'] = ATTR

# 赤柳血铠: armor = 30 * QAC + 0.8 * LV, hp = 100 * QAC + 0.4 * LV
ATTR = empty_attr(ATTR_0)
ATTR['armor'] = [30, 0.8]
ATTR['hp'] = [100, 0.4]
ARMOR[3]['attr'] = ATTR

# 紫金守护胸甲 armor = 36 * QAC + 1 * LV, hp = 110 * QAC + 0.5 * LV
ATTR = empty_attr(ATTR_0)
ATTR['armor'] = [36, 1]
ATTR['hp'] = [110, 0.5]
ARMOR[4]['attr'] = ATTR

# 哈皮毛毛连身衣: armor = 30 * QAC + 0.9 * LV, hp = 90 * QAC + 0.4 * LV, attack = 6 * QAC + 0.8 * LV
ATTR = empty_attr(ATTR_0)
ATTR['armor'] = [30, 0.9]
ATTR['hp'] = [90, 0.4]
ATTR['attack'] = [6, 0.8]
ARMOR[5]['attr'] = ATTR

# 剑豪盔甲: armor = 50 * QAC + 2.1 * LV, hp = 160 * QAC + 2.6 * LV
ATTR = empty_attr(ATTR_0)
ATTR['armor'] = [50, 2.1]
ATTR['hp'] = [160, 2.6]
ARMOR[6]['attr'] = ATTR

# 肃清者戎衣: hp = 160 * QAC + 1.8 * LV, attack = 16 * QAC + 2.5 * LV, block = 10 * QAC + 1.3 * LV
ATTR = empty_attr(ATTR_0)
ATTR['attack'] = [16, 2.5]
ATTR['hp'] = [160, 1.8]
ATTR['block'] = [10, 1.3]
ARMOR[7]['attr'] = ATTR

# 红月的夜行衣: armor = 50 * QAC + 1.2 * LV, hp = 160 * QAC + 1.7 * LV, attack = 16 * QAC + 1.2 * LV
ATTR = empty_attr(ATTR_0)
ATTR['armor'] = [50, 1.2]
ATTR['hp'] = [160, 1.7]
ATTR['attack'] = [16, 1.2]
ARMOR[8]['attr'] = ATTR

# 隐武士铠甲: armor = 50 * QAC + 1.3 * LV, hp = 160 * QAC + 1.9 * LV, attack = 16 * QAC + 0.9 * LV
ATTR = empty_attr(ATTR_0)
ATTR['armor'] = [50, 1.3]
ATTR['hp'] = [160, 1.9]
ATTR['attack'] = [16, 0.9]
ARMOR[9]['attr'] = ATTR

# 芬萨里尔追踪者: armor = 50 * QAC + 1.1 * LV, damage (ref to quality) + 1.6 * 21, attack = 16 * QAC + 1.8 * LV
ATTR = empty_attr(ATTR_0)
ATTR['armor'] = [50, 1.1]
ATTR['attack'] = [16, 1.8]
ATTR['damage'] = [21, 1.6]
ARMOR[10]['attr'] = ATTR

# 黑镇月: armor = 50 * QAC + 2.6 * LV, hp = 160 * QAC + 2.1 * LV
ATTR = empty_attr(ATTR_0)
ATTR['armor'] = [50, 2.6]
ATTR['hp'] = [160, 2.1]
ARMOR[11]['attr'] = ATTR

# 破坏者H-018: armor = 50 * QAC + 1.6 * LV, hp = 160 * QAC + 1.6 * LV, damage (ref to quality) + 1.6 * 21
ATTR = empty_attr(ATTR_0)
ATTR['armor'] = [50, 1.6]
ATTR['hp'] = [160, 1.6]
ATTR['damage'] = [21, 1.6]
ARMOR[12]['attr'] = ATTR

# 心花乱坠长袍: armor = 50 * QAC + 1.8 * LV, hp = 160 * QAC + 1.4 * LV, attack = 16 * QAC + 1.5 * LV
ATTR = empty_attr(ATTR_0)
ATTR['armor'] = [50, 1.8]
ATTR['hp'] = [160, 1.4]
ATTR['attack'] = [16, 1.5]
ARMOR[13]['attr'] = ATTR

# 法夜: armor = 50 * QAC + 1.2 * LV, hp = 160 * QAC + 0.6 * LV, damage (ref to quality) + 2.1 * 21
ATTR = empty_attr(ATTR_0)
ATTR['armor'] = [50, 1.2]
ATTR['hp'] = [160, 0.6]
ATTR['damage'] = [21, 2.1]
ARMOR[14]['attr'] = ATTR

#necks = [
#    ['新手项链', '一条普通的项链', '破旧', 'attack=10+7(5), (crit=10), lv=1'],
#    ['十字军项链', '十字军佩戴的项链', '史诗', 'C: amor=5, B: hp=19, SS: block=3, (hp=12, crit=9, hp=12, block=3), lv=2'],
#    ['冰龙凝雪', '冰龙凝雪', '普通', 'A: damage=33, B: crit=6, S: hp=28, (hp=7, attack=8), lv=5'],
#    ['银魄之眼', '银魄之眼', '普通', 'A: crit=14, B: hp=1003, C: attack=164, (crit=8,, crit=8), lv=199'],
#]

# 新手项链: damage (ref to quality)
# 冰龙凝雪: damage (ref to quality), crit (ref to quality), hp = 90 * QAC + 0.5 * LV
# 银魄之眼: crit (ref to quality), hp = 60 * QAC + 0.5 * LV, attack = 5 * QAC + 0.5 * LV
# 十字军项链: armor = 15 * QAC + 0.5 * LV, hp = 60 * QAC + 0.5 * LV, block = 0.9 * QAC + 1 * LV

# 伟大单身成员的项链: damage (refer to quality) + 1.1 * 21, block = 1 * QAC + 1.3 * LV, hp = 110 * QAC + 1 * LV
# 十字旅团降魔项链: attack = 12 * QAC + 0.7 * LV, hp = 110 * QAC + 0.8 * LV, armor = 25 * QAC + 0.9 * LV
# 进阶黑暗龙王项链: damage (refer to quality) + 1 * 21, crit (ref to quality) + 0.5 * 21, hp = 110 * QAC + 0.8 * LV
# 魔族之翼展: damage (refer to quality) + 1.6 * 21, crit (ref to quality) + 1.6 * 21
# 金色钥匙项链: hp = 110 * QAC + 0.6 * LV, damage (refer to quality) + 0.8 * 21, crit (refer to quality) + 0.5 * 21, gold * 1.3
# 蓝色冰心骑士团项链: hp = 110 * QAC + 1.2 * LV, damage (refer to quality) + 1.6 * 21
# 死神项链: hp = 110 * QAC + 0.8 * LV, damage (refer to quality) + 0.9 * 21, attack = 12 * QAC + 0.8 * LV
# 失落之心毛毛项圈: hp = 110 * QAC + 1 * LV, damage (refer to quality) + 0.9 * 21, armor = 25 * QAC + 0.9 * LV
# 强欲: damage (refer to quality) + 2.2 * 21
NECKLACE = [{'ID': '201', 'name': '新手项链', 'desc': '一条普通的项链', 'attr': ATTR_0},
      {'ID': '202', 'name': '冰龙凝雪', 'desc': '冰龙凝雪', 'attr': ATTR_0},
      {'ID': '203', 'name': '银魄之眼', 'desc': '银魄之眼', 'attr': ATTR_0},
      {'ID': '204', 'name': '十字军项链', 'desc': '十字军佩戴的项链', 'attr': ATTR_0},
      {'ID': '220', 'name': '伟大单身成员的项链', 'desc': '伟大单身成员的项链', 'attr': ATTR_0},
      {'ID': '221', 'name': '十字旅团降魔项链', 'desc': '十字旅团降魔项链', 'attr': ATTR_0},
      {'ID': '222', 'name': '进阶黑暗龙王项链', 'desc': '进阶黑暗龙王项链', 'attr': ATTR_0},
      {'ID': '223', 'name': '魔族之翼展', 'desc': '魔族之翼展', 'attr': ATTR_0},
      {'ID': '224', 'name': '金色钥匙项链', 'desc': '金色钥匙项链', 'attr': ATTR_0},
      {'ID': '225', 'name': '蓝色冰心骑士团项链', 'desc': '蓝色冰心骑士团项链', 'attr': ATTR_0},
      {'ID': '226', 'name': '死神项链', 'desc': '死神项链', 'attr': ATTR_0},
      {'ID': '227', 'name': '失落之心毛毛项圈', 'desc': '失落之心毛毛项圈', 'attr': ATTR_0},
      {'ID': '228', 'name': '强欲', 'desc': '强欲', 'attr': ATTR_0},
      ]

# 新手项链: damage (ref to quality)
ATTR = empty_attr(ATTR_0)
ATTR['damage'] = [21, 0]
NECKLACE[0]['attr'] = ATTR

# 冰龙凝雪: damage (ref to quality), crit (ref to quality), hp = 90 * QAC + 0.5 * LV
ATTR = empty_attr(ATTR_0)
ATTR['damage'] = [21, 0]
ATTR['crit'] = [21, 0]
ATTR['hp'] = [90, 0.5]
NECKLACE[1]['attr'] = ATTR

# 银魄之眼: crit (ref to quality), hp = 60 * QAC + 0.5 * LV, attack = 5 * QAC + 0.5 * LV
ATTR = empty_attr(ATTR_0)
ATTR['crit'] = [21, 0]
ATTR['hp'] = [60, 0.5]
ATTR['attack'] = [5, 0.5]
NECKLACE[2]['attr'] = ATTR

# 十字军项链: armor = 15 * QAC + 0.5 * LV, hp = 60 * QAC + 0.5 * LV, block = 0.9 * QAC + 1 * LV
ATTR = empty_attr(ATTR_0)
ATTR['armor'] = [15, 0.5]
ATTR['hp'] = [60, 0.5]
ATTR['block'] = [0.9, 1]
NECKLACE[3]['attr'] = ATTR

# 伟大单身成员的项链: damage (refer to quality) + 1.1 * 21, block = 1 * QAC + 1.3 * LV, hp = 110 * QAC + 1 * LV
ATTR = empty_attr(ATTR_0)
ATTR['damage'] = [21, 1.1]
ATTR['hp'] = [110, 1]
ATTR['block'] = [1, 1.3]
NECKLACE[4]['attr'] = ATTR

# 十字旅团降魔项链: attack = 12 * QAC + 0.7 * LV, hp = 110 * QAC + 0.8 * LV, armor = 25 * QAC + 0.9 * LV
ATTR = empty_attr(ATTR_0)
ATTR['attack'] = [12, 0.7]
ATTR['hp'] = [110, 0.8]
ATTR['armor'] = [25, 0.9]
NECKLACE[5]['attr'] = ATTR

# 进阶黑暗龙王项链: damage (refer to quality) + 1 * 21, crit (ref to quality) + 0.5 * 21, hp = 110 * QAC + 0.8 * LV
ATTR = empty_attr(ATTR_0)
ATTR['damage'] = [21, 1]
ATTR['crit'] = [21, 0.5]
ATTR['hp'] = [110, 0.8]
NECKLACE[6]['attr'] = ATTR

# 魔族之翼展: damage (refer to quality) + 1.6 * 21, crit (ref to quality) + 1.6 * 21
ATTR = empty_attr(ATTR_0)
ATTR['damage'] = [21, 1.6]
ATTR['crit'] = [21, 1.6]
NECKLACE[7]['attr'] = ATTR

# 金色钥匙项链: hp = 110 * QAC + 0.6 * LV, damage (refer to quality) + 0.8 * 21, crit (refer to quality) + 0.5 * 21, gold * 1.3
ATTR = empty_attr(ATTR_0)
ATTR['hp'] = [110, 0.6]
ATTR['damage'] = [21, 0.8]
ATTR['crit'] = [21, 0.5]
ATTR['gold'] = [1.3]
NECKLACE[8]['attr'] = ATTR

# 蓝色冰心骑士团项链: hp = 110 * QAC + 1.2 * LV, damage (refer to quality) + 1.6 * 21
ATTR = empty_attr(ATTR_0)
ATTR['hp'] = [110, 1.2]
ATTR['damage'] = [21, 1.6]
NECKLACE[9]['attr'] = ATTR

# 死神项链: hp = 110 * QAC + 0.8 * LV, damage (refer to quality) + 0.9 * 21, attack = 12 * QAC + 0.8 * LV
ATTR = empty_attr(ATTR_0)
ATTR['hp'] = [110, 0.8]
ATTR['damage'] = [21, 0.9]
ATTR['attack'] = [12, 0.8]
NECKLACE[10]['attr'] = ATTR

# 失落之心毛毛项圈: hp = 110 * QAC + 1 * LV, damage (refer to quality) + 0.9 * 21, armor = 25 * QAC + 0.9 * LV
ATTR = empty_attr(ATTR_0)
ATTR['hp'] = [110, 1]
ATTR['damage'] = [21, 0.9]
ATTR['armor'] = [25, 0.9]
NECKLACE[11]['attr'] = ATTR

# 强欲: damage (refer to quality) + 2.2 * 21
ATTR = empty_attr(ATTR_0)
ATTR['damage'] = [21, 2.2]
NECKLACE[12]['attr'] = ATTR

#rings = [
#    ['新手指环', '一个普通的指环', '破旧', 'hp=20+7(5), (crit=10), lv=1'],
#    ['生名指环', '据说拥有增强佩戴者体质的神秘功效', '普通', 'A: hp=35, (hp=10, attack=4), lv=3'],
#    ['御魂之戒', '出来吧， 卡赞！吸纳所有彷徨的灵魂！--鬼剑士约翰', '普通', 'C: hp=8, B: attack=1, (crit=6, armor=1), lv=1'],
#    ['毛毛指环', '喵喵戒指', '史诗', 'C: hp=3267, C: attack=169, D: crit=14%, (crt=16, armor=271, attack=423, hp=1146), lv=198'],
#]

# 新手指环: hp = 20 * QAC + 0.1 * LV
# 毛毛指环: hp = 570 * QAC + 0.4 * LV, attack = 8 * QAC + 0.5 * LV, crit (ref to quality)
# 生命指环: hp = 250 * QAC + 0.5 * LV
# 御魂之戒: hp = 1340 * QAC + 0.4 * LV, attack = 16 * QAC + 0.4 * LV

# 真毛毛指环: damage (ref to quality) + 1.2 * 21, crit (ref to damage) + 0.5 * 21, attack = 50 * QAC + 1 * LV
# 死神名片戒指: damage (ref t0 quality) + 1 * 21, crit (ref to damage) + 0.6 * 21, hp = 1800 * QAC + 0.9 * LV
# 素盏鸣尊的意志: damage (ref to quality) + 1.6 * 21, attack = 50 * QAC + 1.2 * LV
# 月夜见尊的意志: damage (ref to quality) + 1.5 * 21, hp = 1800 * QAC + 1.2 * LV
# 黑龙传说指环: hp = 1800 * QAC + 0.8 * LV, damage (ref to quality) + 1.2 * 21, crit (ref to quality) + 0.5 * 21
# 小小心戒指: attack = 50 * QAC + 0.7 * LV, hp = 1800 * QAC + 0.8 * LV, damage (ref to quality) + 1 * 21, crit (ref to quality) + 0.5 * 21
# 金色幸运戒指: hp = 1800 * QAC + 0.7 * LV, damage (ref to quality) + 0.9 * 21, crit (ref to quality) + 0.5 * 21, gold * 1.3
# 绿光森林戒指: hp = 1800 * QAC + 2.5 * LV, damage (ref to quality) + 0.8 * 21
# 混沌: damage (ref to quality) + 2.2 * 21
RING = [{'ID': '301', 'name': '新手指环', 'desc': '一个普通的指环', 'attr': ATTR_0},
      {'ID': '302', 'name': '毛毛指环', 'desc': '喵喵戒指', 'attr': ATTR_0},
      {'ID': '303', 'name': '生命指环', 'desc': '据说拥有增强佩戴者体质的神秘功效', 'attr': ATTR_0},
      {'ID': '304', 'name': '御魂之戒', 'desc': '出来吧， 卡赞！吸纳所有彷徨的灵魂！--鬼剑士约翰', 'attr': ATTR_0},
      {'ID': '320', 'name': '真毛毛指环', 'desc': '真毛毛指环', 'attr': ATTR_0},
      {'ID': '321', 'name': '死神名片戒指', 'desc': '死神名片戒指', 'attr': ATTR_0},
      {'ID': '322', 'name': '素盏鸣尊的意志', 'desc': '素盏鸣尊的意志', 'attr': ATTR_0},
      {'ID': '323', 'name': '月夜见尊的意志', 'desc': '月夜见尊的意志', 'attr': ATTR_0},
      {'ID': '324', 'name': '黑龙传说指环', 'desc': '黑龙传说指环', 'attr': ATTR_0},
      {'ID': '325', 'name': '小小心戒指', 'desc': '小小心戒指', 'attr': ATTR_0},
      {'ID': '326', 'name': '金色幸运戒指', 'desc': '金色幸运戒指', 'attr': ATTR_0},
      {'ID': '327', 'name': '绿光森林戒指', 'desc': '绿光森林戒指', 'attr': ATTR_0},
      {'ID': '328', 'name': '混沌', 'desc': '混沌', 'attr': ATTR_0},
      ]

# 新手指环: hp = 20 * QAC + 0.1 * LV
ATTR = empty_attr(ATTR_0)
ATTR['hp'] = [20, 0.1]
RING[0]['attr'] = ATTR

# 毛毛指环: hp = 570 * QAC + 0.4 * LV, attack = 8 * QAC + 0.5 * LV, crit (ref to quality)
ATTR = empty_attr(ATTR_0)
ATTR['hp'] = [570, 0.4]
ATTR['attack'] = [8, 0.5]
ATTR['crit'] = [21, 0]
RING[1]['attr'] = ATTR

# 生命指环: hp = 250 * QAC + 0.5 * LV
ATTR = empty_attr(ATTR_0)
ATTR['hp'] = [200, 0.5]
RING[2]['attr'] = ATTR

# 御魂之戒: hp = 1340 * QAC + 0.4 * LV, attack = 16 * QAC + 0.4 * LV
ATTR = empty_attr(ATTR_0)
ATTR['hp'] = [1340, 0.4]
ATTR['attack'] = [16, 0.4]
RING[3]['attr'] = ATTR

# 真毛毛指环: damage (ref to quality) + 1.2 * 21, crit (ref to damage) + 0.5 * 21, attack = 50 * QAC + 1 * LV
ATTR = empty_attr(ATTR_0)
ATTR['damage'] = [21, 1.2]
ATTR['crit'] = [21, 0.5]
ATTR['attack'] = [50, 1]
RING[4]['attr'] = ATTR

# 死神名片戒指: damage (ref t0 quality) + 1 * 21, crit (ref to damage) + 0.6 * 21, hp = 1800 * QAC + 0.9 * LV
ATTR = empty_attr(ATTR_0)
ATTR['damage'] = [21, 1]
ATTR['crit'] = [21, 0.6]
ATTR['hp'] = [1800, 0.9]
RING[5]['attr'] = ATTR

# 素盏鸣尊的意志: damage (ref to quality) + 1.6 * 21, attack = 50 * QAC + 1.2 * LV
ATTR = empty_attr(ATTR_0)
ATTR['damage'] = [21, 1.6]
ATTR['attack'] = [50, 1.2]
RING[6]['attr'] = ATTR

# 月夜见尊的意志: damage (ref to quality) + 1.5 * 21, hp = 1800 * QAC + 1.2 * LV
ATTR = empty_attr(ATTR_0)
ATTR['damage'] = [21, 1.5]
ATTR['hp'] = [1800, 1.2]
RING[7]['attr'] = ATTR

# 黑龙传说指环: hp = 1800 * QAC + 0.8 * LV, damage (ref to quality) + 1.2 * 21, crit (ref to quality) + 0.5 * 21
ATTR = empty_attr(ATTR_0)
ATTR['damage'] = [21, 1.2]
ATTR['crit'] = [21, 0.5]
ATTR['hp'] = [1800, 0.8]
RING[8]['attr'] = ATTR

# 小小心戒指: attack = 50 * QAC + 0.7 * LV, hp = 1800 * QAC + 0.8 * LV, damage (ref to quality) + 1 * 21, crit (ref to quality) + 0.5 * 21
ATTR = empty_attr(ATTR_0)
ATTR['attack'] = [50, 0.7]
ATTR['damage'] = [21, 1]
ATTR['crit'] = [21, 0.5]
ATTR['hp'] = [1800, 0.8]
RING[9]['attr'] = ATTR

# 金色幸运戒指: hp = 1800 * QAC + 0.7 * LV, damage (ref to quality) + 0.9 * 21, crit (ref to quality) + 0.5 * 21, gold * 1.3
ATTR = empty_attr(ATTR_0)
ATTR['gold'] = [1.3]
ATTR['damage'] = [21, 0.9]
ATTR['crit'] = [21, 0.5]
ATTR['hp'] = [1800, 0.7]
RING[10]['attr'] = ATTR

# 绿光森林戒指: hp = 1800 * QAC + 2.5 * LV, damage (ref to quality) + 0.8 * 21
ATTR = empty_attr(ATTR_0)
ATTR['damage'] = [21, 0.8]
ATTR['hp'] = [1800, 2.5]
RING[11]['attr'] = ATTR

# 混沌: damage (ref to quality) + 2.2 * 21
ATTR = empty_attr(ATTR_0)
ATTR['damage'] = [21, 2.2]
RING[12]['attr'] = ATTR

EQ = {'weapon': WP, 'armor': ARMOR, 'necklace': NECKLACE, 'ring': RING}

# write into json
import json

with open('eq.json', "w", encoding='utf-8') as f:
	json.dump(EQ, f, indent=4, ensure_ascii=False)


