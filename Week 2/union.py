# Enter your code here. Read input from STDIN. Print output to STDOUT
eng_num = input()
eng = set(input().split(" "))
fr_num = input()
fr = input().split(" ")
uni = eng.union(fr)
print(len(uni))
