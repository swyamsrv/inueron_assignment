"""## QUESTION 1
class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    @classmethod
    def get_input(self):
        while True:
            try:
                a = float(input("Value of a-"))
                b = float(input("Value of b-"))
                c = float(input("Value of c-"))
                return self(a, b, c)
            except:
                continue

class Calculation(Triangle):

    def __init__(self, *args):
        Triangle.__init__(self, *args)

    def get_area(self):
        self.s = (self.a + self.b + self.c) / 2
        self.area = (self.s * (self.s - self.a) * (self.s - self.b) * (self.s - self.c)) ** 0.5
        print(self.area)

ans = Calculation.get_input()
ans.get_area()
"""

"""## QUESTION 1_1

def word(words, n):
    temp = []
    for w in words:
        if len(w) >= n:
            temp.append(w)
    return temp

string = input("Enter the string->")
words = string.split(" ")
n = int(input('Enter the number->'))
print(word(words, n))
"""

## QUESTION_2_1

"""def word_map(word):
    temp = []
    for w in word:
        temp.append(len(w))

    return temp

string = input("Enter the string->")
words = string.split(" ")
print(word_map(words))

"""

## QUESTION 2_2
"""
def clarify(lis):
    vow = ['a', 'e', 'i', 'o', 'u']
    if lis in vow:
        return True
    else:
        return False

string = input()
print(clarify(string))"""