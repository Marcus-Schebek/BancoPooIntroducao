#include <iostream>
#include <string>
#include "Banco.h"
using namespace std;

void Banco::ContaEmBanco(string nome){
    this->saldo = 0;
    this->name = nome;
}

void Banco::Deposita(float valor){
    if(valor > 0){
        this->saldo += valor;
    } else {
        std::cout << "O valor do depósito deve ser maior que zero." << std::endl;
    }
}

void Banco::Saca(float valor){
    if (valor > 0 && valor <= saldo) {
        this->saldo -= valor;
    } else if (valor <= 0) {
        std::cout << "O valor do saque deve ser maior que zero." << std::endl;
    } else {
        std::cout << "Saldo insuficiente para o saque." << std::endl;
    }
}

float Banco::getSaldo() {
    return this->saldo;
}

string Banco::getNome(){
    return this->name;
}