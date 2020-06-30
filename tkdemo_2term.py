import tkinter as tk

# 計算機能のための変数とイベント用の関数定義

# 二項演算のモデル
# 入力中の数字
currnet_number = 0

# 第一項
first_term = 0
# 第二項
second_term = 0
# 結果
result = 0

def do_plus():
    "＋キーが押されたときの計算動作、第一項の設定と入力中の数字のクリア"
    global currnet_number
    global first_term

    first_term = currnet_number
    currnet_number = 0

def do_eq():
    "イコールキーが押されたときの計算動作、第二項の設定、加算の実施、入力中の数字のクリア"
    global second_term
    global result
    global currnet_number
    second_term = currnet_number
    result = first_term + second_term
    currnet_number = 0

#数字キーの Call Back 関数
def key1():
    key(1)

def key2():
    key(2)

def key3():
    key(3)

def key4():
    key(4)

def key5():
    key(5)

def key6():
    key(6)

def key7():
    key(7)

def key8():
    key(8)

def key9():
    key(9)

def key0():
    key(0)

# 数字キーを一括処理する関数
def key(n):
    global currnet_number
    currnet_number = currnet_number * 10 + n
    show_number(currnet_number)

def clear():
    global currnet_number
    currnet_number = 0
    show_number(currnet_number)

def plus():
    do_plus()
    show_number(currnet_number)

def eq():
    do_eq()
    show_number(result)

def show_number(num):
    e.delete(0,tk.END)
    e.insert(0,str(num))

# tkinter での画面構成
root = tk.TK()
f = tk.Frame(root)
f.grid()

#ウィジェットの作成
b1 = tk.Button(f.text='1', command=key1)
b2 = tk.Button(f.text='2', command=key2)
b3 = tk.Button(f.text='3', command=key3)
b4 = tk.Button(f.text='4', command=key4)
b5 = tk.Button(f.text='5', command=key5)
b6 = tk.Button(f.text='6', command=key6)
b7 = tk.Button(f.text='7', command=key7)
b8 = tk.Button(f.text='8', command=key8)
b9 = tk.Button(f.text='9', command=key9)
b0 = tk.Button(f.text='0', command=key0)
bc = tk.Button(f.text='C', command=clear)
bp = tk.Button(f.text='+', command=plus)
be = tk.Button(f.text='=', command=eq)


# Grid 型ジオメトリマネージャによるウィジェットの割付


b1.grid(row=3,column=0)
b1.grid(row=3,column=1)
b1.grid(row=3,column=2)
b1.grid(row=2,column=0)
b1.grid(row=2,column=1)
b1.grid(row=2,column=2)
b1.grid(row=1,column=0)
b1.grid(row=1,column=1)
b1.grid(row=1,column=2)
b1.grid(row=4,column=0)
b1.grid(row=1,column=3)
b1.grid(row=4,column=3)
b1.grid(row=2,column=3)


#数値を表示するウィジェット
e = tk.Entry(f)
e.grid(row=0,column=0,columnspan=4)
clear()

#ここからGUIがスタート
root.mainloop()