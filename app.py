# app.py
from flask import Flask, render_template, jsonify
import random

app = Flask(__name__)

words = [
    "キャンディーコーン", "パンプキンパイ", "ホットチョコレート", "焼きマシュマロ",
    "コスプレ", "お墓", "ろうそく", "クモの巣", "棺桶", "ほうき", "大釜",
    "城", "森", "ヴァンパイア", "人狼", "フランケンシュタイン", "魔女",
    "スケルトン", "満月", "呪文"
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_word')
def get_word():
    if not words:
        return jsonify({"word": "すべてのワードが出ました！", "is_complete": True})
    
    selected_word = random.choice(words)
    words.remove(selected_word)
    
    return jsonify({"word": selected_word, "is_complete": False})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
