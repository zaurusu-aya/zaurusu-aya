import time
import random
import mei

def ramen():
    text = 'タイマーを3分にセットしました。'
    mei.jtalk_normal(text)
    time.sleep(180)
    text = '3分経ちましたよ。ラーメンを食べる時間です！'
    mei.jtalk_normal(text)
    
def care():
    i = random.randint(0, 1)
    if i == 1:
        text = '疲れているのですか？たまには休息を取ることが必要ですよ。'
        mei.jtalk_normal(text)
    elif i == 0:
        text = 'そんなときははラーメンを食べると元気が出ますよ。ラーメンタイマーをセットしますね。'
        mei.jtalk_normal(text)
        time.sleep(5)
        ramen()

def calculation():
    text = 'はい。計算しますよ。'
    mei.jtalk_normal(text)
    k = input('計算:')
    k = k.split('たす')
    