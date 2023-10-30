class Banco:
    def __init__(self, name):
        self._saldo = 0;
        self._name = name;

    def Deposita(self, valor):
        if valor > 0:
            self._saldo += valor;
    def Saca(self, valor):
        if valor > 0 and valor < self._saldo:
            self._saldo -= valor;
        elif valor > self._saldo:
            print("Saldo insuficiente")
        else:
            print("Valor deve ser maior que R$ 0.00")
    def GetSaldo(self):
        return self._saldo
    def GetName(self):
        return self._name

    