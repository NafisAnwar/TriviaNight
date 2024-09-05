#Name: Nafis Anwar
#U-Number: U2092-0991
#Description: This is the first module of a trivia program that holds a question class with several attributes, and their accessors, mutators


class Question:
    def __init__(self, prompt, ans1, ans2, ans3, ans4, corr_ans):
        self.prompt = prompt
        self.ans1 = ans1 
        self.ans2 = ans2
        self.ans3 = ans3
        self.ans4 = ans4
        self.corr_ans = corr_ans

    #accessor methods 

    def getprompt(self):
        return self.prompt   
    
    def getans1(self):
        return self.ans1

    def getans2(self):
        return self.ans2
    
    def getans3(self):
        return self.ans3
    
    def getans4(self):
        return self.ans4

    def getcorr_ans(self):
        return self.corr_ans
    
    #mutator methods 
    
    def setprompt(self, p):
        self.prompt = p

    def setans1(self, a1):
        self.ans1 = a1

    def setans2(self, a2):
        self.ans2 = a2

    def setans3(self, a3):
        self.ans3 = a3

    def setans4(self, a4):
        self.ans4 = a4

    def setcorr_ans(self, ca):
        self.corr_ans = ca

    #correct answer checking method 

    def check_answer(self, user_answer):
        return user_answer == self.corr_ans

    def __str__(self):
        return f"{self.prompt}\n1. {self.ans1}\n2. {self.ans2}\n3. {self.ans3}\n4. {self.ans4}\n"




    