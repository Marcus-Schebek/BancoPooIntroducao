#include <iostream>
#include "Banco.h"

int main (){
    Banco meuBanco;
    meuBanco.ContaEmBanco("Marcus Schebek");

    meuBanco.Deposita(100);
    meuBanco.Saca(30);

    // Verifica e exibe o saldo atual
    float saldoAtual = meuBanco.getSaldo();
    string nome = meuBanco.getNome();
    std::cout << "Saldo atual do banco de " << nome << " : R$ "  << saldoAtual << std::endl;

}