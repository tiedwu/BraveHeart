# 品质系数: QAC
# rank: 破旧, 普通, 神器, 史诗, 独特, 不朽I, 不朽II
# 品质: D, C, B, A, S, SS, SSS
# Ex: 破旧 普通D 普通 C, QAC = 1, 普通 A, QAC = 5, 神器 D, QAC = 13, 神器 A, QAC = 19
# Ex: 史诗 SS, QAC = 37, 史诗 A, QAC = 33, 史诗 C, QAC = 29
# Ex: 独特 B, QAC = 45
# 暴伤(damage): D(70%-75%), C(75%-80%), B(80%-85%), A(85%-90%), S(90%-95%), SS(95%-100%), SSS(100%-105%), 不朽I(105%-110%), 不朽II(110%-115%)
# 暴击(crit): D(11%), C(12%), B(13%), A(14%), S(15%-17%), SS(18%-20%), SSS(21%-23%), 不朽I(24%-26%), 不朽II(27%-29%)
# 生命指环: hp = 20 * QAC + 15.2 * LV
# 十字军项链: armor = 5 * QAC + 1.16 * LV, hp = 19 * QAC + 4.86 * LV, block = 3 * 5 + ?
# 天权軽甲: armoa = 3 * QAC + 0.81 * LV, hp = 10 * QAC + 8.33 * LV, attack = 1 * QAC + 0.93 * LV
# 毛毛的爪子: attack = 28 * QAC + 1.72 * LV, crit (ref to quality)
# 战士重铠: armor = 11 * QAC + 1.59 * LV, hp = 55 * QAC + 10.47 * LV
# 冰晶之刃: attack = 10 * QAC + V * LV, damage (ref to quality)
# 银魄之眼: crit (ref to quality), hp = 20 * QAC + 4.94 * LV, attack = 10 * QAC + 0.74 * LV
# 战士长剑: attack = 10 * QAC + 1.84 * LV, armor = 3 * QAC + 1.56 * LV
# 冰龙凝雪: damage (ref to quality), crit (ref to quality), hp = 28 * QAC + 5.43 * LV
# 毛毛指环: hp = 10 * QAC + 15.04 * LV, attack = 5 * QAC + 0.13 * LV, crit (ref to quality)
# 赤柳血刃: attack = 6 * QAC + 1.56 * LV, hp = 39 * QAC + 13.09 * LV
# 赤柳血铠: armor = 10 * QAC + 1.33 * LV, hp = 20 * QAC + 19.47 * LV
# 普通长剑: attack = 20 * QAC + 2.02 * LV
# 狱岩石太刀: attack = 15 * QAC + 0.73 * LV, crit (ref to quality)
# 紫炎波刃剑: attack = 17 * QAC + 1.8 * LV
# 大师大冒险家之剑: attack = 20 * QAC + 1.78 * LV, hp = 20 * QAC + 39.22 * LV
# 数珠丸恒次: attack = 20 * QAC + 1.29 * LV

weapons = [
    ['新手剑', '一把普通的剑', '破旧', 'attack=10+7(5), (crit=10), lv=1'],
    ['赤柳血刃', '似乎会给使用者提供生命气息', '神器', 'B: attack=6, B:hp=39, (attack=5, damage=28, armor-addi=14.03), lv=2'],
    ['冰晶之刃', '剑锋覆盖者冰晶, 碰到的敌人都会被冻住', '神器', 'B: attack=561, D: damage=73, (armor-addi=16.53, armor-addi=26.36, armor-addi=23.08) lv=196'],
    ['毛毛的爪子', '这? 这也是武器?', '史诗', 'SS: attack=28, B: crit=22, (armor-addi=14.41, armor=11, armor-addi=20.85, attack=15), lv=5'],
    ['战士长剑', '六级战士使用的长剑', '史诗', 'SS: attack=730, A: armor=404, (damage=28, attack=558, crit=17, armor=222), lv=196'],
    ['普通长剑', '朴实无华的长剑，有的只有强力的攻击力', '普通', 'D: attack=420, (hp-addi=16.85, damage=16), lv=199'],
    ['狱岩石太刀', '用狱岩石制作的太刀, 据说拥有让使用者潜力爆发的神秘力量', '史诗', 'C: attack=578, B: crit=22, (hp=1335, armor=369, damage=41, crit=15), lv=197'],
    ['紫炎波刃剑', '传说中狂战士最喜爱的剑', '史诗', 'B: attack=886, (damage=46, armor-addi=23.4, hp=1390, crit=13), lv=200'],
    ['大师大冒险家之剑', '大师大冒险家之剑', '独特', 'B: attack=1248, C: hp=8546, (hp=1605, attack=496, damage=36, attack=537, armor-addi=42.95), lv=196'],
    ['数珠丸恒次', '具体情况不明， 传说为日莲上人所有', 'D: attack=943+1197(13), (attack=507, crit=21, armor=313, hp=1198, attack-addi=32.33), lv=96'],
]

suits = [
    ['新手铠甲', '普通的衣甲', '破旧', 'armor=10+7(5), (crit=10), lv=1'],
    ['战士重铠', '六级战士使用的重型铠甲', '神器', 'C: armor=477, D: hp=2776, (hp=1054, armor-addi=18.48, armor-addi=26.87), lv=197'],
    ['天权轻甲', '舍弃防御性能的轻甲，因为更加轻便, 攻击性能更加突出', '神器', 'B: armor=3， A: hp=10, A: attack=1, (hp-addi=7.1, hp=6, attack=3), lv=1'],
    ['赤柳血铠', '似乎会给使用者提供生命气息', '神器', 'B: armor=430, C: hp=4115, (hp=1082, armor-addi=22.11, armor=171), lv=196'],
]

necks = [
    ['新手项链', '一个普通的项链', '破旧', 'attack=10+7(5), (crit=10), lv=1'],
    ['十字军项链', '十字军佩戴的项链', '史诗', 'C: amor=5, B: hp=19, SS: block=3, (hp=12, crit=9, hp=12, block=3), lv=2'],
    ['冰龙凝雪', '冰龙凝雪', '普通', 'A: damage=33, B: crit=6, S: hp=28, (hp=7, attack=8), lv=5'],
    ['银魄之眼', '银魄之眼', '普通', 'A: crit=14, B: hp=1003, C: attack=164, (crit=8,, crit=8), lv=199'],

]

rings = [
[
    ['新手指环', '一个普通的指环', '破旧', 'hp=20+7(5), (crit=10), lv=1'],
    ['生名指环', '据说拥有增强佩戴者体质的神秘功效', '普通', 'A: hp=35, (hp=10, attack=4), lv=3'],
    ['御魂之戒', '出来吧， 卡赞！吸纳所有彷徨的灵魂！--鬼剑士约翰', '普通', 'C: hp=8, B: attack=1, (crit=6, armor=1), lv=1'],
    ['毛毛指环', '喵喵戒指', '史诗', 'C: hp=3267, C: attack=169, D: crit=14%, (crt=16, armor=271, attack=423, hp=1146), lv=198'],

]




