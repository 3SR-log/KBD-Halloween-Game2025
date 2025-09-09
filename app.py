# app.py
from flask import Flask, render_template, jsonify, session
import random

app = Flask(__name__)
# 秘密鍵を設定します。
# 実際にはより複雑な鍵を使用してください。
app.secret_key = 'your_secret_key' 

# 元のワードリストはグローバルな定数として保持
INITIAL_WORDS = [
    "キャンディーコーン", "パンプキンパイ", "ホットチョコレート", "焼きマシュマロ",
    "コスプレ", "お墓", "ろうそく", "クモの巣", "棺桶", "ほうき", "大釜",
    "城", "森", "ヴァンパイア", "人狼", "フランケンシュタイン", "魔女",
    "スケルトン", "満月", "呪文"
]

@app.route('/')
def index():
    # ページにアクセスしたときにビンゴの状態をリセット
    session.pop('words', None)
    session.pop('used_words', None)
    return render_template('index.html')

@app.route('/get_word')
def get_word():
    # セッションにリストがなければ、初期化
    if 'words' not in session:
        session['words'] = INITIAL_WORDS[:]
        session['used_words'] = []

    words = session['words']
    used_words = session['used_words']

    if not words:
        return jsonify({"word": "すべてのワードが出ました！", "is_complete": True})

    selected_word = random.choice(words)
    words.remove(selected_word)
    used_words.append(selected_word)

    # セッションのリストを更新
    session['words'] = words
    session['used_words'] = used_words

    return jsonify({"word": selected_word, "is_complete": False, "used_words": used_words})
