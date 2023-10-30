from Banco import Banco

meuBanco = Banco("Marcus Schebek")

meuBanco.Deposita(300)
meuBanco.Saca(149.99)

saldoAtual = meuBanco.GetSaldo()
nome = meuBanco.GetName()
print(f"Saldo Atual do {nome} : R$ {saldoAtual}")