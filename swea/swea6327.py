def squr(s):
    for i in s:
        print('square({}) => {}' .format(int(i), int(i)*int(i)))
n = input()
x = n.split(", ")
squr(x)