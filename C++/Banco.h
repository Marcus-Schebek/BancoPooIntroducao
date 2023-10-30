#ifndef BANCO_H
#define BANCO_H
using namespace std;
class Banco{
    public:
        void ContaEmBanco(string nome);
        void Deposita(float valor);
        void Saca(float valor);
        float getSaldo();
        string getNome();
    private:
        float saldo;
        string name;
};

#endif 