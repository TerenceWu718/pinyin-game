# 拼音声调大作战

一个用 Python + Streamlit 做的小学低年级（1-2 年级）拼音声调课堂游戏。
学生点开网页链接就能玩，不需要安装 Python；支持电脑和手机浏览器。

## 功能

- 三个关卡：单韵母和声调 / 拼读小能手 / 词语小达人，外加混合挑战
- 四种题型：看汉字选拼音、看拼音选汉字、选声调、判断对错
- 点“🔊 听一听”可用浏览器内置的中文语音朗读（无需联网）
- 即时讲解、星星评分、成绩单、最高分可自行记录
-  colourful 大按钮界面，适合课堂投屏或学生平板

## 本地运行

```bash
pip install -r requirements.txt
streamlit run app.py
```

浏览器会自动打开 `http://localhost:8501`。

## 发布成别人也能打开的网页（免费）

### 方式 A：Streamlit Community Cloud（推荐）

1. 在 GitHub 新建一个仓库，把本文件夹里的所有文件上传（包括 `app.py`、`questions.py`、`requirements.txt` 和 `.streamlit/config.toml`）。
2. 打开 https://share.streamlit.io ，用 GitHub 账号登录。
3. 点 **New app**，选择刚才的仓库、分支 `main`、主文件 `app.py`。
4. 点 **Deploy**，等 1-2 分钟，就会得到一个类似
   `https://your-name-pinyin-game.streamlit.app` 的公开链接。
5. 把这个链接发给学生或同事，他们用浏览器打开即可玩。

> 代码更新后，只要 `git push`，网页会自动更新。

### 方式 B：Hugging Face Spaces

1. 在 https://huggingface.co/new-space 新建 Space，SDK 选 **Streamlit**。
2. 上传本文件夹所有文件。
3. 构建完成后 Space 页面就是公开链接。

## 文件说明

- `app.py` —— 游戏页面与交互逻辑
- `questions.py` —— 题库（可自行增删题目）
- `requirements.txt` —— Python 依赖
- `.streamlit/config.toml` —— 主题配色

## 修改题库

打开 `questions.py`，按现有格式新增 `dict(...)` 即可。
字段说明见文件顶部注释。每关默认随机抽 8 题，可在 `app.py` 的 `build_quiz(..., count=8)` 修改题量。
