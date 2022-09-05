import random

chart = "0123456789ABCDEFHIJKLMNOPQRSTUVWXYZ*#()@%=abcdefghijklmnopqrstuvxyz"
pass_lenght = int(input("Hur långt lösen vill du ha?: "))
password = "".join(random.sample(chart, pass_lenght))
print("Detta är din genererade lösen: %s" % password)
