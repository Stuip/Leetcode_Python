"""# 读入三个整数，按每个整数占8个字符的宽度，右对齐输出它们。
nums = input()
nums = nums.split(" ")
for value in nums:
    print("{:>8d}".format(int(value)),end=" ")
"""

"""
读入一个双精度浮点数，保留12位小数，输出这个浮点数。

num = float(input())
print("%.12f" % num)
"""

"""
读入一个字符，一个整数，一个单精度浮点数，一个双精度浮点数，然后按顺序输出它们，
并且要求在他们之间用一个空格分隔。输出浮点数时保留6位小数。

nums = list()
while True:
    num = input()
    nums.append(num)
    if not num:
        break
print("{} {} {:.6f} {:.6f}".format(nums[0],nums[1],float(nums[2]),float(nums[3])))
"""

"""
读入一个双精度浮点数，分别按输出格式“%f”，“%f”保留5位小数，“%e”和“%g”的形式输出这个整数，每次在单独一行上输出。
输入：
    12.3456789
输出：
    12.345679
    12.34568
    1.234568e+001
    12.3457

num = float(input())
print("%f" % num)
print("%.5f" % num)
print("%.6e" % num)
print("%.6g" % num)
"""

"""
甲流并不可怕，在中国，它的死亡率并不是很高。请根据截止2009年12月22日各省报告的甲流确诊数和死亡数，计算甲流在各省的死亡率。
输入：
    输入仅一行，有两个整数，第一个为确诊数，第二个为死亡数。
    10433 60
输出：
    输出仅一行，甲流死亡率，以百分数形式输出，精确到小数点后3位。
    0.575%

nums = input()
nums = [int(value) for value in nums.split()]
num = nums[1] / nums[0]
print("{:.3%}".format(num))
"""

"""
描述：
    利用公式 C = 5 * (F-32) / 9 （其中C表示摄氏温度，F表示华氏温度） 进行计算转化。
输入：
    输入一行，包含一个实数f，表示华氏温度。（f >= -459.67）
    41
输出：
    输出一行，包含一个实数，表示对应的摄氏温度，要求精确到小数点后5位。
    5.00000

F = int(input())
if F >= -459.67:
    C = 5 * (F - 32) / 9

print("%.5f" % C)


n = int(input())
print(2 ** n)
"""


def findOcurrences(text, first, second):
    ans = list()
    text = text.split(" ")
    index = 0
    while index < len(text):
        part = text[index:index+3]
        if len(part) < 3:
            break
        if part[0] == first and part[1] == second:
            ans.append(part[2])
        index += 1
    return ans


text = "alice is a good girl she is a good student"
first = "a"
second = "good"
# ans = findOcurrences(text,first,second)
# print(ans)

def kWeakestRows(mat, k):
    ans = [(sum(mat[i]), i) for i in range(len(mat))]
    ans.sort()
    return [value[1] for value in ans[:k]]


mat = [[1,1,0,0,0],[1,1,1,1,0],[1,0,0,0,0],[1,1,0,0,0],[1,1,1,1,1]]
k = 3
# kWeakestRows(mat,k)


def numUniqueEmails(emails):
    ans = set()
    for email in emails:
        email = email.split("@")
        # print(email)
        if "+" in email[0]:
            index = email[0].index("+")
            email[0] = email[0][:index]
        email[0] = email[0].replace(".","")
        e = email[0] + '@' +email[1]
        ans.add(e)
    return len(ans)


emails = ["test.email+alex@leetcode.com", "test.email@leetcode.com"]
# ans = numUniqueEmails(emails)
# print(ans)
