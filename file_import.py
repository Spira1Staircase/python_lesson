import os

#Working Directori表示
print(os.getcwd())
f = open('日本語ファイル.txt', 'w')
f.write('日本語¥n 日本語¥n 日本語¥n')
f.close()

f = open('日本語ファイル.txt', 'r')
s = f.read()
f.close()
print(s)
