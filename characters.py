# coding=utf8
import random

male = [
    '厚', '炜', '纯', '杰', '海', '瑞', '周', '衡', '维', '茂', '镭', '骋', '峥', '明', '翼',
    '秋', '炼', '银', '前', '子', '澄', '盼', '寅', '向', '艺', '渤', '隽', '禹', '强', '舜',
    '科', '迅', '琛', '瑾', '韵', '捷', '富', '烽', '崴', '耿', '硕', '余', '轩', '庚', '昊',
    '延', '献', '烨', '湛', '炳', '腾', '兵', '璇', '顺', '孟', '力', '曦', '熹', '梁', '通',
    '祺', '卿', '贵', '鹏', '喜', '乐', '若', '皓', '越', '亨', '森', '刚', '庆', '轶', '迎',
    '浩', '豹', '炯', '镇', '琦', '裕', '彬', '冰', '鲁', '标', '祯', '枫', '椒', '盟', '克',
    '牧', '溪', '名', '广', '固', '翊', '肖', '波', '创', '剑', '陈', '欢', '蔚', '新', '昱',
    '月', '俊', '颢', '甫', '钦', '霆', '涵', '梅', '坤', '挺', '乔', '丹', '影', '昌', '程',
    '里', '治', '唯', '量', '洋', '颂', '良', '琨', '韦', '志', '洪', '杨', '潮', '亚', '锋',
    '研', '天', '功', '沙', '勇', '典', '弘', '谦', '能', '众', '耀', '国', '圆', '雄', '严',
    '朗', '岩', '路', '圣', '邦', '旗', '旭', '意', '保', '竹', '鸣', '岑', '虹', '高', '廷',
    '野', '园', '益', '奔', '宾', '山', '钊', '操', '昀', '李', '普', '晔', '耕', '培', '准',
    '旻', '煌', '迁', '宇', '佳', '方', '煜', '康', '夭', '泰', '理', '聪', '忱', '宝', '岚',
    '遥', '一', '定', '胤', '玥', '羽', '盛', '家', '郁', '增', '岳', '鸿', '或', '疆', '卓',
    '逊', '开', '晨', '福', '运', '秦', '青', '湘', '瀚', '韬', '其', '显', '惠', '纬', '桔',
    '光', '卡', '发', '千', '陆', '重', '轮', '根', '楷', '童', '嘉', '奕', '璞', '舒', '展',
    '响', '珍', '峰', '岭', '霄', '斌', '舟', '勃', '万', '沁', '灏', '桢', '帆', '焕', '贺',
    '闻', '红', '干', '州', '豪', '航', '锐', '澎', '涛', '巍', '辰', '栩', '吉', '嵘', '炬',
    '菲', '利', '民', '怡', '飚', '贤', '军', '泳', '垄', '之', '举', '琼', '田', '叶', '瑛',
    '非', '游', '勋', '拓', '翔', '源', '宽', '威', '以', '冠', '申', '澍', '霖', '晋', '雁',
    '晴', '鼎', '震', '文', '哲', '宁', '扬', '琴', '昭', '宏', '希', '晟', '朋', '燕', '熠',
    '津', '继', '河', '歌', '飞', '禄', '淮', '帅', '麒', '松', '虎', '均', '凡', '宪', '立',
    '迪', '会', '朝', '桥', '平', '鉴', '滔', '南', '仲', '静', '龙', '将', '伟', '焱', '勉',
    '友', '亮', '成', '烈', '超', '丽', '信', '总', '咏', '骞', '峻', '钢', '凌', '跃', '时',
    '桐', '尚', '瑜', '升', '添', '见', '舰', '江', '毓', '臣', '列', '逸', '堃', '柯', '蕾',
    '石', '进', '来', '骏', '琳', '晗', '磊', '兴', '竞', '琰', '淳', '垒', '承', '杭', '涌',
    '春', '铭', '悦', '朔', '敬', '水', '珂', '树', '渊', '焘', '岗', '恩', '华', '振', '荣',
    '星', '黎', '君', '芳', '登', '赛', '士', '特', '贝', '璟', '致', '渝', '远', '鹰', '侃',
    '仁', '蛇', '阔', '博', '诚', '征', '淼', '钧', '劲', '双', '实', '彦', '声', '键', '丰',
    '冬', '永', '英', '滨', '灵', '全', '原', '笑', '丁', '业', '柳', '潜', '祥', '嵩', '生',
    '骥', '玎', '绍', '达', '元', '麟', '隆', '柱', '榕', '恺', '锴', '垚', '行', '劫', '洁',
    '风', '俭', '猛', '熙', '冶', '攀', '寒', '魁', '凯', '苏', '浪', '葵', '云', '梦', '起',
    '犇', '义', '辉', '啸', '钰', '昂', '果', '学', '陶', '忠', '金', '菁', '畅', '壮', '善',
    '敏', '曙', '旋', '苗', '仪', '喆', '谊', '胜', '晖', '宣', '韶', '晶', '城', '辛', '伯',
    '默', '融', '照', '罡', '卫', '昆', '队', '争', '安', '靓', '林', '鹤', '驰', '魏', '德',
    '印', '满', '东', '侠', '翀', '杉', '端', '中', '珑', '旦', '武', '先', '晓', '翰', '川',
    '坚', '辑', '启', '战', '润', '冀', '放', '才', '冉', '甲', '易', '栋', '奇', '弛', '轲',
    '羿', '睿', '景', '慧', '品', '楠', '雪', '洲', '赫', '铁', '齐', '尧', '玮', '乾', '铎',
    '微', '群', '多', '煦', '冲', '崇', '锟', '骁', '霞', '章', '弋', '灿', '季', '清', '智',
    '泽', '真', '楚', '营', '革', '舸', '臻', '勤', '思', '钟', '宸', '健', '阳', '日', '歆',
    '潇', '权', '正', '蒙', '礼', '柏', '念', '策', '诺', '恒', '骅', '彪', '锦', '赞', '闯',
    '焰', '萍', '鲲', '屹', '伦', '雨', '京', '和', '笛', '彭', '泓', '胡', '存', '夏', '爽',
    '佩', '毅', '戈', '炎', '昕', '为', '然', '珩', '泉', '璋', '沛', '玉', '斐', '颖', '衍',
    '建', '懿', '世', '幸', '想', '昶', '玺', '可', '言', '韧', '琪', '有', '铮', '桦', '雷',
    '烁', '政', '望', '鑫', '密', '同', '稳', '洵', '心', '欣', '汉', '萌', '宙', '靖', '璐',
    '珉', '奎', '育', '旺', '坦', '纲'
]

female = [
    '灵', '照', '语', '汝', '俏', '蕾', '女', '文', '思', '均', '榕', '晶', '仙', '梓', '珠',
    '蔚', '徽', '韫', '娆', '玥', '恩', '贤', '玄', '肖', '雁', '玉', '蒙', '跃', '诺', '珏',
    '曾', '蔓', '雅', '密', '原', '扬', '俪', '诚', '昀', '苑', '亚', '一', '颜', '意', '华',
    '情', '媚', '嵩', '瓤', '弛', '裕', '琼', '芹', '烟', '彩', '缨', '纨', '忻', '姬', '彬',
    '书', '夏', '皓', '良', '懿', '亭', '嫣', '雪', '翊', '胤', '珑', '蕊', '侃', '双', '笑',
    '秦', '荃', '允', '辰', '巍', '燕', '奕', '渊', '芳', '潇', '愉', '希', '旗', '倩', '葳',
    '娴', '素', '丛', '郁', '溪', '汀', '楚', '星', '霞', '夕', '蓓', '牧', '纬', '熠', '励',
    '衍', '萍', '茉', '苇', '卿', '芙', '蝶', '展', '澄', '蓝', '盈', '飒', '萌', '昭', '盼',
    '珂', '贝', '寒', '融', '策', '砚', '美', '斐', '齐', '俞', '筠', '琛', '香', '靓', '沫',
    '昱', '秀', '顺', '枝', '杭', '贞', '晔', '箐', '业', '妤', '微', '西', '卫', '旖', '音',
    '畅', '骁', '予', '森', '珩', '耀', '旎', '频', '钧', '馨', '伊', '单', '珊', '辛', '痴',
    '晖', '尔', '爱', '佳', '艾', '诗', '芄', '焕', '盛', '婕', '君', '矫', '来', '欢', '尧',
    '馥', '幼', '润', '飚', '利', '鸿', '爽', '叶', '菊', '宛', '雯', '台', '杏', '蓉', '申',
    '韶', '沛', '泓', '轶', '苗', '游', '闪', '凝', '琳', '鑫', '妙', '舒', '俐', '天', '黛',
    '斌', '妃', '妲', '宾', '谨', '竹', '朦', '冬', '征', '甜', '恺', '飘', '翎', '娥', '前',
    '益', '含', '婵', '凛', '茹', '霏', '洲', '芮', '苑', '霁', '晏', '嫒', '露', '朔', '程',
    '衡', '恋', '醒', '易', '引', '珉', '月', '萃', '米', '松', '枫', '韵', '鹭', '苹', '立',
    '璧', '钦', '娇', '沙', '帆', '丰', '闻', '滢', '烨', '琪', '媛', '旋', '若', '玢', '葡',
    '满', '群', '朝', '桑', '彤', '玎', '净', '烁', '葵', '桔', '凤', '苏', '晓', '清', '童',
    '桦', '姝', '妍', '南', '梦', '泳', '淳', '瑕', '拉', '冶', '实', '格', '礼', '默', '璇',
    '喆', '柯', '智', '翼', '兰', '陶', '维', '娉', '樱', '钰', '林', '寅', '端', '娓', '嫚',
    '蕙', '熹', '瑾', '紫', '悦', '依', '明', '贺', '培', '栩', '韦', '昂', '越', '遥', '尉',
    '荣', '娟', '平', '郦', '知', '言', '冠', '新', '眉', '渝', '熙', '谦', '咏', '海', '晰',
    '心', '望', '莲', '芬', '源', '弘', '妮', '佩', '典', '沁', '垚', '震', '璐', '春', '如',
    '莎', '丹', '祯', '嫱', '尤', '缘', '幸', '花', '琬', '品', '田', '臻', '岑', '睿', '小',
    '菡', '捷', '茵', '筱', '凡', '岳', '碧', '璟', '琴', '菁', '怡', '非', '苓', '茜', '欣',
    '聪', '乐', '川', '桐', '洋', '余', '娅', '珺', '营', '霭', '恒', '洵', '洺', '迪', '颢',
    '菱', '曦', '蔷', '凌', '白', '郡', '总', '簧', '驰', '泉', '岩', '优', '菲', '季', '飞',
    '粼', '湘', '豫', '椒', '恬', '禾', '绮', '军', '芊', '锦', '姣', '念', '祥', '淑', '风',
    '冰', '玫', '秋', '京', '杉', '铃', '舟', '暖', '柔', '艺', '锐', '映', '正', '麟', '鹂',
    '千', '方', '盟', '庆', '茂', '颖', '攀', '灿', '绚', '雄', '煦', '璜', '吉', '喻', '晨',
    '萱', '璞', '朋', '颉', '蝴', '鸽', '妹', '慈', '艳', '皎', '迅', '霜', '滨', '延', '云',
    '雨', '容', '涓', '迎', '涵', '慕', '玮', '岚', '果', '漫', '真', '屏', '霓', '瀛', '肠',
    '芸', '昕', '虹', '城', '琦', '珍', '巧', '楠', '瑗', '铭', '玲', '丽', '艳', '静', '歆',
    '也', '敏', '宝', '慧', '晗', '英', '翀', '颐', '嘉', '霖', '乔', '裙', '杨', '纯', '筝',
    '浩', '朵', '成', '吟', '黎', '汇', '鹃', '为', '霄', '嵘', '麒', '丁', '祺', '勉', '婧',
    '晴', '羽', '龙', '好', '或', '桥', '严', '园', '然', '想', '琚', '芯', '荟', '影', '洁',
    '桃', '蕴', '琰', '津', '莺', '姿', '莹', '野', '鸥', '枚', '斯', '荔', '唯', '笛', '喜',
    '婉', '钥', '溢', '元', '仪', '宜', '赞', '姗', '堃', '金', '安', '宁', '惟', '永', '毓',
    '劼', '颇', '珣', '忠', '多', '逸', '圆', '魏', '茗', '敬', '桂', '薇', '咪', '荷', '惠',
    '子', '炜', '赉', '翠', '曼', '莉', '囡', '亮', '瑜', '梅', '连', '行', '红', '颍', '澜',
    '毅', '联', '令', '蜜', '忆', '娜', '芝', '胜', '航', '国', '柳', '漪', '育', '弦', '信',
    '旻', '尚', '俭', '忱', '可', '殷', '环', '瑛', '卉', '谊', '隽', '青', '婷', '瑶', '桢',
    '学', '焱', '赫'
]

# femaleNames = femaleNames1 | femaleNames2 | femaleNames3
# print(femaleNames)

# testName = femaleNamesTest[random.randint(0, len(
#     femaleNamesTest))] + femaleNamesTest[random.randint(
#         0, len(femaleNamesTest))]

if __name__ == '__main__':
    testName = female[random.randint(0, len(female))] + female[random.randint(0, len(female))]
    print("Your name is: %s" % (testName))