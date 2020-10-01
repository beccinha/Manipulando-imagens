class fracao(object):

    def __init__(self, n, d):
        self.num, self.dem = fracao.reduce(n, d)

    def __add__(self, other):
        Nnum = self.num*other.dem + self.dem*other.num
        Ndem = self.dem*other.dem 
        return fracao(Nnum, Ndem)

    def __sub__(self, other):
        Nnum = self.num*other.dem - self.dem*other.num 
        Ndem = self.dem*other.dem 
        return fracao(Nnum, Ndem)
    
    def __mul__(self, other):
        Nnum = self.num*other.num
        Ndem = self.dem*other.dem  
        return fracao(Nnum, Ndem)

    def __truediv__(self,other):
        Nnum = self.num*other.dem  
        Ndem = self.dem*other.num 
        return fracao(Nnum,Ndem)

    def __pow__(self,other):
        Nnum = self.num**other.num
        Ndem = self.dem**other.num
        return fracao(Nnum, Ndem)

    def __eq__(self, other):
        primeiro = self.num*other.dem 
        segundo = self.dem*other.num 
        return primeiro == segundo

    def maiorQ(self, other):
        primeiro = self.num*other.dem  
        segundo = self.dem*other.num 
        return primeiro > segundo

    def menorQ(self, other):
        primeiro = self.num*other.dem
        segundo = self.dem*other.num 
        return primeiro < segundo

    @staticmethod
    def gcd(a,b):
        while b != 0:
            a,b = b, a%b
        return a 

    @classmethod
    def reduce(cls, n1, n2):
        g = cls.gcd(n1,n2)
        return (n1 // g, n2 // g)
    
    def __str__(self):
        return str(self.num) + '/' +str(self.dem)
    
print(fracao.maiorQ(fracao(1,4), fracao(1,2)))
print(fracao.menorQ(fracao(1,4), fracao(1,2)))