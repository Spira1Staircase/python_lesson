#while文(breakなし)
#xの平方根を求める
x = 2
#
rnew = x
#
diff = rnew - x/rnew
if (diff < 0):
    diff = diff
while (diff > 1.0E-6):
    r1 = rnew
    r2 = x/r1
    rnew = (r1 + r2)/2
    print(r1, rnew, r2)
    diff = r1 - r2
    if (diff < 0):
        diff = -diff
