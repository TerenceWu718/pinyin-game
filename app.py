# -*- coding: utf-8 -*-
"""拼音声调大作战 —— 适合小学 1-2 年级的课堂小游戏。

本地运行：
    pip install -r requirements.txt
    streamlit run app.py

部署：把本项目整个文件夹上传到 GitHub，然后在 https://share.streamlit.io
     选择该仓库的 app.py 即可获得公开链接。
"""

import json
import random
import time

import streamlit as st
import streamlit.components.v1 as components

from questions import LEVELS, build_quiz

st.set_page_config(
    page_title="拼音声调大作战",
    page_icon="🔊",
    layout="centered",
    initial_sidebar_state="collapsed",
)

CUSTOM_CSS = """
<style>
  #MainMenu, footer, header { visibility: hidden; }
  .block-container { padding-top: 1.6rem; padding-bottom: 2rem; max-width: 720px; }
  body { background: linear-gradient(160deg, #fff7ed 0%, #f0f9ff 55%, #faf5ff 100%); }
  .big-title { text-align:center; font-size: 2.2rem; font-weight: 900; color:#ea580c; margin-bottom:.2rem; }
  .subtitle { text-align:center; color:#64748b; font-size:1rem; margin-bottom:1.4rem; }
  .card {
    background:#ffffff; border-radius:20px; padding:1.2rem 1.2rem 1rem;
    box-shadow:0 8px 24px rgba(251,146,60,.18); border:2px solid #fed7aa;
  }
  .q-card {
    background:#ffffff; border-radius:22px; padding:1.4rem 1rem;
    box-shadow:0 10px 30px rgba(56,189,248,.20); border:3px solid #bae6fd;
    text-align:center; margin:.6rem 0 1rem;
  }
  .q-hint { color:#0284c7; font-size:.95rem; font-weight:700; }
  .q-text { font-size:2.4rem; font-weight:900; color:#0f172a; margin:.5rem 0; line-height:1.35; }
  .stButton>button {
    border-radius:14px !important; border:2px solid #fdba74 !important;
    background:#fff7ed !important; color:#9a3412 !important;
    font-size:1.15rem !important; font-weight:800 !important;
    min-height:58px; padding:.4rem .6rem !important;
    transition: transform .08s ease, box-shadow .08s ease;
  }
  .stButton>button:hover:not(:disabled) {
    background:#ffedd5 !important; transform: translateY(-2px);
    box-shadow: 0 6px 14px rgba(249,115,22,.22);
  }
  .stButton>button:disabled { opacity:.55; }
  div[data-testid="stProgress"] > div > div { background: linear-gradient(90deg,#fb923c,#38bdf8); }
  .score-pill {
    display:inline-block; background:#fff; border:2px solid #fde68a; border-radius:999px;
    padding:.35rem .9rem; font-weight:800; color:#b45309; box-shadow:0 3px 10px rgba(251,191,36,.2);
  }
  .star { font-size:2rem; letter-spacing:.2rem; }
  .center { text-align:center; }
</style>
"""

st.markdown(CUSTOM_CSS, unsafe_allow_html=True)

DEFAULTS = {
    "page": "home",          # home | quiz | result
    "name": "",
    "level": 1,
    "questions": [],
    "q_index": 0,
    "score": 0,
    "answered": False,
    "selected": None,
    "last_correct": None,
    "start_time": None,
    "round_id": 0,
    "celebrated": False,
}
for key, value in DEFAULTS.items():
    if key not in st.session_state:
        st.session_state[key] = value


def start_game():
    st.session_state.round_id += 1
    st.session_state.questions = build_quiz(st.session_state.level, count=8)
    st.session_state.q_index = 0
    st.session_state.score = 0
    st.session_state.answered = False
    st.session_state.selected = None
    st.session_state.last_correct = None
    st.session_state.start_time = time.time()
    st.session_state.celebrated = False
    st.session_state.page = "quiz"


def select_answer(option):
    if st.session_state.answered:
        return
    q = st.session_state.questions[st.session_state.q_index]
    st.session_state.answered = True
    st.session_state.selected = option
    st.session_state.last_correct = (option == q["answer"])
    if st.session_state.last_correct:
        st.session_state.score += 1


def next_question():
    st.session_state.q_index += 1
    st.session_state.answered = False
    st.session_state.selected = None
    st.session_state.last_correct = None
    if st.session_state.q_index >= len(st.session_state.questions):
        st.session_state.page = "result"


def go_home():
    st.session_state.page = "home"


def speak_component(text):
    """在页面里放一个朗读按钮，使用浏览器自带的中文语音，无需联网。"""
    safe_text = json.dumps(text, ensure_ascii=False)
    html = f"""
    <div style="text-align:center;margin:.2rem 0 .5rem;">
      <button onclick="speakIt()" style="
        background:#e0f2fe;border:2px solid #7dd3fc;border-radius:999px;
        padding:.45rem 1.1rem;font-size:1rem;font-weight:800;color:#075985;cursor:pointer;">
        🔊 听一听
      </button>
      <div id="msg" style="font-size:.8rem;color:#94a3b8;margin-top:.25rem;"></div>
    </div>
    <script>
      function speakIt() {{
        if (!('speechSynthesis' in window)) {{
          document.getElementById('msg').innerText = '这个浏览器不支持朗读哦';
          return;
        }}
        var u = new SpeechSynthesisUtterance({safe_text});
        u.lang = 'zh-CN';
        u.rate = 0.75;
        u.pitch = 1.1;
        window.speechSynthesis.cancel();
        window.speechSynthesis.speak(u);
        document.getElementById('msg').innerText = '认真听，注意声调～';
      }}
    </script>
    """
    components.html(html, height=86, scrolling=False)


# ---------------------------------------------------------------- 首页
if st.session_state.page == "home":
    st.markdown('<div class="big-title">🔊 拼音声调大作战</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle">边玩边学拼音，一起拿下四声小怪兽！</div>', unsafe_allow_html=True)

    with st.container():
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.session_state.name = st.text_input(
            "你的名字（写在成绩单上）",
            value=st.session_state.name,
            placeholder="例如：小雨",
            max_chars=12,
        )
        level_options = [1, 2, 3, 0]
        st.session_state.level = st.radio(
            "选择关卡",
            options=level_options,
            format_func=lambda x: "🌈 混合挑战（全部题目）" if x == 0 else LEVELS[x],
            horizontal=True,
            index=level_options.index(st.session_state.level),
        )
        st.caption("每关 8 题，答错也没关系，看完讲解继续闯关！")
        st.markdown('</div>', unsafe_allow_html=True)

    st.write("")
    _, col, _ = st.columns([1, 2, 1])
    with col:
        st.button("🚀 开始闯关", on_click=start_game, use_container_width=True)

    st.markdown(
        """
        <div class="center" style="color:#94a3b8;font-size:.85rem;margin-top:1.2rem;">
          💡 小提示：点“🔊 听一听”可以听汉字读音（需要浏览器支持中文语音）
        </div>
        """,
        unsafe_allow_html=True,
    )

# ---------------------------------------------------------------- 答题
elif st.session_state.page == "quiz":
    questions = st.session_state.questions
    idx = st.session_state.q_index
    q = questions[idx]
    total = len(questions)

    left, right = st.columns([3, 1])
    with left:
        st.markdown(f'<span class="score-pill">⭐ 得分 {st.session_state.score} / {total}</span>', unsafe_allow_html=True)
    with right:
        st.markdown(f'<div style="text-align:right;color:#64748b;font-weight:700;">第 {idx + 1} / {total} 题</div>', unsafe_allow_html=True)
    st.progress((idx + (1 if st.session_state.answered else 0)) / total)

    type_hints = {
        "hanzi_to_pinyin": "选出正确的拼音",
        "pinyin_to_hanzi": "选出正确的汉字",
        "tone": "选出正确的声调",
        "judge": "判断拼音对不对",
    }
    st.markdown(
        f"""
        <div class="q-card">
          <div class="q-hint">{type_hints.get(q['type'], '请选择')}</div>
          <div class="q-text">{q['prompt']}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    if q.get("speak"):
        speak_component(q["speak"])

    options = q["options"]
    rid = st.session_state.round_id
    opt_key = lambda i: f"opt_{rid}_{idx}_{i}"

    if len(options) == 4:
        c1, c2 = st.columns(2)
        cols = [c1, c2, c1, c2]
        for i, opt in enumerate(options):
            with cols[i]:
                st.button(
                    opt,
                    key=opt_key(i),
                    on_click=select_answer,
                    args=(opt,),
                    disabled=st.session_state.answered,
                    use_container_width=True,
                )
    else:
        c1, c2 = st.columns(2)
        for i, opt in enumerate(options):
            with (c1 if i == 0 else c2):
                st.button(
                    opt,
                    key=opt_key(i),
                    on_click=select_answer,
                    args=(opt,),
                    disabled=st.session_state.answered,
                    use_container_width=True,
                )

    if st.session_state.answered:
        st.write("")
        if st.session_state.last_correct:
            st.success(f"🎉 答对啦！{q['explain']}")
        else:
            st.error(
                f"差一点点～ 正确答案是：**{q['answer']}**。{q['explain']}"
            )
        is_last = idx == total - 1
        st.button(
            "🏁 查看成绩" if is_last else "下一题 →",
            key=f"next_{rid}_{idx}",
            on_click=next_question,
            use_container_width=True,
        )

# ---------------------------------------------------------------- 成绩
elif st.session_state.page == "result":
    total = len(st.session_state.questions)
    score = st.session_state.score
    rate = score / total if total else 0
    stars = 3 if rate >= 0.9 else 2 if rate >= 0.7 else 1
    star_str = "⭐" * stars + "☆" * (3 - stars)
    seconds = int(time.time() - (st.session_state.start_time or time.time()))
    who = st.session_state.name.strip() or "小朋友"

    if rate >= 0.8 and not st.session_state.celebrated:
        st.balloons()
        st.session_state.celebrated = True

    st.markdown('<div class="big-title">🏆 闯关完成！</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="subtitle">{who} 的成绩单</div>', unsafe_allow_html=True)

    st.markdown(
        f"""
        <div class="q-card">
          <div class="star">{star_str}</div>
          <div style="font-size:2rem;font-weight:900;color:#0f172a;">{score} / {total} 题答对</div>
          <div style="color:#64748b;margin-top:.4rem;">用时 {seconds} 秒 · 正确率 {int(rate * 100)}%</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    if rate == 1:
        msg = "太厉害啦！四声小怪兽全被你打败了！"
    elif rate >= 0.7:
        msg = "表现很棒！再玩一次就更熟练啦！"
    else:
        msg = "勇敢闯关就是进步！多听几遍，再试一次吧！"
    st.markdown(f'<div class="center" style="font-size:1.1rem;color:#c2410c;font-weight:800;margin:.8rem 0;">{msg}</div>', unsafe_allow_html=True)

    c1, c2 = st.columns(2)
    with c1:
        st.button("🔁 再玩一次", on_click=start_game, use_container_width=True)
    with c2:
        st.button("🎚️ 换一关", on_click=go_home, use_container_width=True)

    st.info("把这个网页的链接发给同学，他们也能一起玩！", icon="🔗")
