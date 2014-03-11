class math:
    #recursive factorial
    def recurFactorial(self, n):
        return self.recurFactorial(n-1) * n;
    
    #non recursive factorial
    def factorial(self, n):
        factorial = 0;
        if n.isdigit():
            for i in range(1, n+1):
                factorial *= i;
            return factorial;
        else:
            raise Exception("Number supplied to factorial function is not a digit");
            return None;
                
        