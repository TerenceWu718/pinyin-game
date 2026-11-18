# -*- coding: utf-8 -*-
"""适合小学 1-2 年级的拼音声调题库。

每条题目字段：
  level   : 1 单韵母与声调 / 2 拼读小能手 / 3 词语小达人
  type    : hanzi_to_pinyin | pinyin_to_hanzi | tone | judge
  prompt  : 题目展示文字（可含 emoji）
  options : 选项列表
  answer  : 正确答案（与 options 中某一项完全相同）
  explain : 答题后的讲解
  speak   : 可选，点小喇叭时朗读的文本
"""

LEVELS = {
    1: "第一关：单韵母和声调",
    2: "第二关：拼读小能手",
    3: "第三关：词语小达人",
}

QUESTIONS = [
    # ---------------- 第一关：单韵母和声调 ----------------
    dict(level=1, type="hanzi_to_pinyin", prompt="🐴 马", options=["mǎ", "mà", "mā", "má"],
         answer="mǎ", explain="“马”读 mǎ，第三声，像下坡又上坡。", speak="马"),
    dict(level=1, type="hanzi_to_pinyin", prompt="👩 妈", options=["mā", "má", "mǎ", "mà"],
         answer="mā", explain="“妈”读 mā，第一声，声音高高平平。", speak="妈"),
    dict(level=1, type="hanzi_to_pinyin", prompt="👨 爸", options=["bà", "bā", "bá", "bǎ"],
         answer="bà", explain="“爸”读 bà，第四声，声音从高降到低。", speak="爸"),
    dict(level=1, type="hanzi_to_pinyin", prompt="🔥 火", options=["huǒ", "huō", "huó", "huò"],
         answer="huǒ", explain="“火”读 huǒ，第三声。", speak="火"),
    dict(level=1, type="hanzi_to_pinyin", prompt="💧 水", options=["shuǐ", "shuī", "shuí", "shuì"],
         answer="shuǐ", explain="“水”读 shuǐ，第三声。", speak="水"),
    dict(level=1, type="hanzi_to_pinyin", prompt="⛰️ 山", options=["shān", "shán", "shǎn", "shàn"],
         answer="shān", explain="“山”读 shān，第一声。", speak="山"),
    dict(level=1, type="pinyin_to_hanzi", prompt="mā（第一声）", options=["妈", "马", "吗", "麻"],
         answer="妈", explain="mā 第一声，是“妈妈”的“妈”。", speak="妈"),
    dict(level=1, type="pinyin_to_hanzi", prompt="mǎ（第三声）", options=["马", "妈", "麻", "骂"],
         answer="马", explain="mǎ 第三声，是“小马”的“马”。", speak="马"),
    dict(level=1, type="pinyin_to_hanzi", prompt="bà（第四声）", options=["爸", "八", "拔", "把"],
         answer="爸", explain="bà 第四声，是“爸爸”的“爸”。", speak="爸"),
    dict(level=1, type="pinyin_to_hanzi", prompt="dà（第四声）", options=["大", "打", "答", "搭"],
         answer="大", explain="dà 第四声，是“大小”的“大”。", speak="大"),
    dict(level=1, type="tone", prompt="👩 妈 mā", options=["第一声（ā）", "第二声（á）", "第三声（ǎ）", "第四声（à）"],
         answer="第一声（ā）", explain="“妈”是 mā，第一声，高高平平。", speak="妈"),
    dict(level=1, type="tone", prompt="🐴 马 mǎ", options=["第一声（ā）", "第二声（á）", "第三声（ǎ）", "第四声（à）"],
         answer="第三声（ǎ）", explain="“马”是 mǎ，第三声，先降后升。", speak="马"),
    dict(level=1, type="tone", prompt="👨 爸 bà", options=["第一声（ā）", "第二声（á）", "第三声（ǎ）", "第四声（à）"],
         answer="第四声（à）", explain="“爸”是 bà，第四声，从高降到低。", speak="爸"),
    dict(level=1, type="tone", prompt="8️⃣ 八 bā", options=["第一声（ā）", "第二声（á）", "第三声（ǎ）", "第四声（à）"],
         answer="第一声（ā）", explain="“八”是 bā，第一声。", speak="八"),
    dict(level=1, type="judge", prompt="🐮 牛 — niú", options=["✅ 拼音正确", "❌ 拼音错误"],
         answer="✅ 拼音正确", explain="“牛”读 niú，第二声，拼音正确。", speak="牛"),
    dict(level=1, type="judge", prompt="🐶 狗 — gǒu", options=["✅ 拼音正确", "❌ 拼音错误"],
         answer="✅ 拼音正确", explain="“狗”读 gǒu，第三声，拼音正确。", speak="狗"),
    dict(level=1, type="judge", prompt="🌸 花 — huà", options=["✅ 拼音正确", "❌ 拼音错误"],
         answer="❌ 拼音错误", explain="“花”读 huā，第一声，不是 huà。", speak="花"),
    dict(level=1, type="judge", prompt="☀️ 太阳 — tài yáng", options=["✅ 拼音正确", "❌ 拼音错误"],
         answer="✅ 拼音正确", explain="“太阳”读 tài yáng，拼音正确。", speak="太阳"),

    # ---------------- 第二关：拼读小能手 ----------------
    dict(level=2, type="hanzi_to_pinyin", prompt="📚 书", options=["shū", "shú", "shǔ", "shù"],
         answer="shū", explain="“书”读 shū，第一声。", speak="书"),
    dict(level=2, type="hanzi_to_pinyin", prompt="✏️ 笔", options=["bǐ", "bī", "bí", "bì"],
         answer="bǐ", explain="“笔”读 bǐ，第三声。", speak="笔"),
    dict(level=2, type="hanzi_to_pinyin", prompt="🚪 门", options=["mén", "mēn", "mèn", "men"],
         answer="mén", explain="“门”读 mén，第二声。", speak="门"),
    dict(level=2, type="hanzi_to_pinyin", prompt="🪟 窗", options=["chuāng", "chuáng", "chuǎng", "chuàng"],
         answer="chuāng", explain="“窗”读 chuāng，第一声。", speak="窗"),
    dict(level=2, type="hanzi_to_pinyin", prompt="🧑‍🎓 学", options=["xué", "xuē", "xuě", "xuè"],
         answer="xué", explain="“学”读 xué，第二声。", speak="学"),
    dict(level=2, type="hanzi_to_pinyin", prompt="🏫 校", options=["xiào", "xiāo", "xiáo", "xiǎo"],
         answer="xiào", explain="“校”读 xiào，第四声。", speak="校"),
    dict(level=2, type="pinyin_to_hanzi", prompt="lǎo shī（老师）", options=["老师", "同学", "学生", "学校"],
         answer="老师", explain="lǎo shī 是“老师”。", speak="老师"),
    dict(level=2, type="pinyin_to_hanzi", prompt="tóng xué（同学）", options=["同学", "老师", "学校", "朋友"],
         answer="同学", explain="tóng xué 是“同学”。", speak="同学"),
    dict(level=2, type="pinyin_to_hanzi", prompt="péng you（朋友）", options=["朋友", "同学", "老师", "家人"],
         answer="朋友", explain="péng you 是“朋友”，“友”读轻声。", speak="朋友"),
    dict(level=2, type="tone", prompt="🧑‍🎓 学 xué", options=["第一声（xuē）", "第二声（xué）", "第三声（xuě）", "第四声（xuè）"],
         answer="第二声（xué）", explain="“学”是 xué，第二声。", speak="学"),
    dict(level=2, type="tone", prompt="✏️ 笔 bǐ", options=["第一声（bī）", "第二声（bí）", "第三声（bǐ）", "第四声（bì）"],
         answer="第三声（bǐ）", explain="“笔”是 bǐ，第三声。", speak="笔"),
    dict(level=2, type="judge", prompt="📖 读书 — dú shū", options=["✅ 拼音正确", "❌ 拼音错误"],
         answer="✅ 拼音正确", explain="“读书”读 dú shū，拼音正确。", speak="读书"),
    dict(level=2, type="judge", prompt="✏️ 铅笔 — qiān bǐ", options=["✅ 拼音正确", "❌ 拼音错误"],
         answer="✅ 拼音正确", explain="“铅笔”读 qiān bǐ，拼音正确。", speak="铅笔"),
    dict(level=2, type="judge", prompt="🍎 苹果 — píng guǒ", options=["✅ 拼音正确", "❌ 拼音错误"],
         answer="✅ 拼音正确", explain="“苹果”读 píng guǒ，拼音正确。", speak="苹果"),

    # ---------------- 第三关：词语小达人 ----------------
    dict(level=3, type="hanzi_to_pinyin", prompt="🍉 西瓜", options=["xī guā", "xí guā", "xǐ guā", "xì guā"],
         answer="xī guā", explain="“西瓜”读 xī guā。", speak="西瓜"),
    dict(level=3, type="hanzi_to_pinyin", prompt="🌞 太阳", options=["tài yáng", "tài yán", "tài yàng", "tái yáng"],
         answer="tài yáng", explain="“太阳”读 tài yáng。", speak="太阳"),
    dict(level=3, type="hanzi_to_pinyin", prompt="🌙 月亮", options=["yuè liang", "yuè liáng", "yuè làng", "yè liang"],
         answer="yuè liang", explain="“月亮”里“亮”读轻声 liang，不标声调。", speak="月亮"),
    dict(level=3, type="hanzi_to_pinyin", prompt="⭐ 星星", options=["xīng xing", "xíng xing", "xǐng xing", "xìng xing"],
         answer="xīng xing", explain="“星星”里第二个“星”读轻声 xing。", speak="星星"),
    dict(level=3, type="hanzi_to_pinyin", prompt="🍊 橘子", options=["jú zi", "jié zi", "jū zi", "jù zi"],
         answer="jú zi", explain="“橘子”读 jú zi，“子”读轻声。", speak="橘子"),
    dict(level=3, type="pinyin_to_hanzi", prompt="xiāng jiāo（香蕉）", options=["香蕉", "苹果", "西瓜", "橘子"],
         answer="香蕉", explain="xiāng jiāo 是“香蕉”。", speak="香蕉"),
    dict(level=3, type="pinyin_to_hanzi", prompt="qiān bǐ（铅笔）", options=["铅笔", "钢笔", "毛笔", "水笔"],
         answer="铅笔", explain="qiān bǐ 是“铅笔”。", speak="铅笔"),
    dict(level=3, type="pinyin_to_hanzi", prompt="xī guā（西瓜）", options=["西瓜", "西爪", "稀瓜", "洗瓜"],
         answer="西瓜", explain="xī guā 是“西瓜”。", speak="西瓜"),
    dict(level=3, type="tone", prompt="🌙 月 yuè", options=["第一声（yuē）", "第二声（yué）", "第三声（yuě）", "第四声（yuè）"],
         answer="第四声（yuè）", explain="“月”是 yuè，第四声。", speak="月"),
    dict(level=3, type="tone", prompt="🌸 花 huā", options=["第一声（huā）", "第二声（huá）", "第三声（huǎ）", "第四声（huà）"],
         answer="第一声（huā）", explain="“花”是 huā，第一声。", speak="花"),
    dict(level=3, type="judge", prompt="🌙 月亮 — yuè liàng", options=["✅ 拼音正确", "❌ 拼音错误"],
         answer="❌ 拼音错误", explain="“亮”在“月亮”里读轻声 liang，不写 liàng。", speak="月亮"),
    dict(level=3, type="judge", prompt="⭐ 星星 — xīng xing", options=["✅ 拼音正确", "❌ 拼音错误"],
         answer="✅ 拼音正确", explain="“星星”读 xīng xing，第二个“星”读轻声。", speak="星星"),
]


def build_quiz(level, count=8):
    """按关卡抽题；level=0 表示混合关卡。"""
    import random

    pool = QUESTIONS if level == 0 else [q for q in QUESTIONS if q["level"] == level]
    picked = random.sample(pool, min(count, len(pool)))
    fixed = []
    for q in picked:
        q = dict(q)
        options = list(q["options"])
        random.shuffle(options)
        q["options"] = options
        fixed.append(q)
    return fixed
