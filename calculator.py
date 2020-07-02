class Dentaku():
    def __init__(self):
        self.first_term = 0
        self.second_term = 0
        self.result = 0
        self_operation = "+"
    
    def do_opelation(self):
        if self.opelation == "+":
            self.result = self.first_term + self.second_term
        else self.opelation == "-":
            self.result = self.first_term - self.second_term

dentaku = Dentaku()
while True:
    f = int(input("First term"))
    dentaku.first_term = f
    o = input("Oeration")
    dentaku.opration = o
    s = int(input("Second term "))
    dentaku.do_operation()
    r = dentaku.result
    print("Result", r)
