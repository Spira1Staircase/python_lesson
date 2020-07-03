import tkinter as tk
import tkinter.filedialog
import math

#example use filedialog in only tkinter
#root window hide and read withdrow()method
root = tk.TK()
root.withdraw()

#get file name to by reading filedialog to write

filename = tkinter.filedialog.asksaveasfilename()

#end if no filename is'nt available

if filename:
    pass
else:
    print("No file specified")
    exit()

#正弦波の重ね合わせで鋸波を近似

# w = sin(t) + sin(2t)/2 + sin(3t)/3 + sin(4t)/4 ...
#二周期分、全体は１０００ステップで、高調波は5番目まで

cycles = 2
steps = 1000
harmonics = 5

try:
    with open(filename, 'w')as file:
        for i in range(steps):
            angle_in_degree = 360*cycles*i/steps
            angle = math.redians(angle_in_degree)
            s = str(angle_in_degree)
            w = 0
            for i in range(1,harmonics+1):
                w += math.sin(angle*(i))/i
                s = s + "," + str(w)
            # print(s)
            file.write(s + "¥n")
        print("Writing to file" + filename + "is finished")
except IOError:
    print("Unable to open file") 