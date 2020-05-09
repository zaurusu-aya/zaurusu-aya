import mei
import time
import yaml
import scan
import skill
import julius_test

def say_something():
    julius_test.listen()
    if text == 'ラーメンタイマー' or text == '砂時計':
        skill.ramen()
    elif text == '癒やして':
        skill.care()
    elif text == '計算' or text == '電卓':
        skill.calculation()
    else:
        scan.scanandsay(text)
        
        
    
while True:        
    if __name__ == '__main__':
        say_something()