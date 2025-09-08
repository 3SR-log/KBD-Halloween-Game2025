# app.py
from flask import Flask, render_template, jsonify
import random

app = Flask(__name__)

# このリストはサーバーが起動している間、状態を保持します
words = [
    "キャンディーコーン", "パンプキンパイ", "ホットチョコレート", "焼きマシュマロ",
    "コスプレ", "お墓", "ろうそく", "クモの巣", "棺桶", "ほうき", "大釜",
    "城", "森", "ヴァンパイア", "人狼", "フランケンシュタイン", "魔女",
    "スケルトン", "満月", "呪文"
]

# ここに出たワードを保存する新しいリストを追加します
used_words = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_word')
def get_word():
    if not words:
        return jsonify({"word": "すべてのワードが出ました！", "is_complete": True})

    selected_word = random.choice(words)
    words.remove(selected_word)
    
    # 新しく出たワードをused_wordsリストに追加
    used_words.append(selected_word)

    return jsonify({"word": selected_word, "is_complete": False, "used_words": used_words})
