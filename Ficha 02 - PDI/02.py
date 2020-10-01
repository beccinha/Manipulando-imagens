class PortaLogica: 

    def __init__(self, n):
        self.label = n
        self.output = None 
    
    def getLabel(self):
        return self.label
    
    def getOutput(self):
        self.output = self.performGateLogic()
        return self.output

class PortaUni(PortaLogica):
    
    def __init__(self, n):
        PortaLogica.__init__(self,n)

        self.pin = None 
    
    def getPin(self):
        if self.pin == None:
            return int(input("Digite a entrada do Pino para a porta " + self.getLabel() + "---->"))
        else:
            return self.pin.getFrom().getOutput()
    
    def setNextPin(self, source):
        if self.pin == None:
            self.pin = source 
        else : 
            print("Erro: Não há pino livre")

class PortaBin(PortaLogica):
    def __init__(self, n):
        PortaLogica.__init__(self,n)

        self.pinA = None
        self.pinB = None

    def getPinA(self):
        if self.pinA == None:
            return int(input("Digite a entrada do Pino A para a porta " + self.getLabel() + "--->"))
        else:
            return self.pinA.getFrom().getOutput()

    def getPinB(self):
        if self.pinB == None:
            return int(input("Digite a entrada do Pino B para a porta " + self.getLabel() + "--->"))
        else: 
            return self.pinB.getFrom().getOutput()
    
    def setNextPin(self, source):
        if self.pinA == None:
            self.pinA = source
        else:
            if self.pinB == None:
                self.pinB = source
            else:
                print("Erro: Não há pino livre")

class Connector:

    def __init__(self, fgate, tgate):
        self.fromgate = fgate
        self.togate = tgate

        tgate.setNextPin(self)

    def getFrom(self):
        return self.fromgate

    def getTo(self):
        return self.togate 

class PortaNand(PortaBin):

    def __init__(self, n):
        PortaBin.__init__(self,n)
    
    def performGateLogic(self):

        a = self.getPinA()
        b = self.getPinB()
        if a==1 and b==1:
            return 0
        else:
            return 1

class PortaNor(PortaBin):

    def __init__(self, n):
        PortaBin.__init__(self,n)
    
    def performGateLogic(self):

        a = self.getPinA()
        b = self.getPinB()
        if a==1 or b==1:
            return 0
        else: 
            return 1

class PortaNot(PortaUni):

    def __init__(self,n):
        PortaUni.__init__(self,n)
    
    def performGateLogic(self):
        a = self.getPin()
        if a==1:
            return 0
        else:
            return 1

class PortaXor(PortaBin):
    
    def __init__(self,n):
        PortaBin.__init__(self,n)
    
    def performGateLogic(self):
        a = self.getPinA()
        b = self.getPinB()
        if a == b:
            return 0
        else:
            return 1

class PortaXnor(PortaBin):

    def __init__(self, n):
        PortaBin.__init__(self,n)
    
    def performGateLogic(self):

        a = self.getPinA()
        b = self.getPinB()
        if a==b:
            return 1
        else: 
            return 0

def main():
    g1 = PortaNand("Nand")
    g2 = PortaNot("Not")
    g3 = PortaNor("Nor")
    g5 = PortaXor("Xor")
    g6 = PortaXnor("Xnor")

    c1 = Connector(g1,g3)
    c2 = Connector(g3,g5)
    c3 = Connector(g1,g6)
    print(c1.getTo().getOutput())

main()