class FourCal1:
    def __init__(self, num1, num2):
        self.first = num1 # 초기화
        self.second = num2
    def add(self):
        self.result = self.first + self.second
    def div(self):
        self.result = self.first / self.second

class MoreFourCal1(FourCal1):
    def mul(self):
        self.result = self.first * self.second
    def sub(self):
        self.result = self.first - self.second
    def div(self): # 재정의 
        if self.second == 0:
            self.result = 0
        else:
            self.result = self.first / self.second

PI = 3.141592

def sum1(num1, num2):
    result = num1 + num2
    return result


dddd = MoreFourCal1(100, 20)

a = 10