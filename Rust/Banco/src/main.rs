mod banco;

use banco::Banco;

fn main(){
    let mut meu_banco = Banco::conta_em_banco("Marcus Schebek");
    meu_banco.depositar(300.0);
    meu_banco.sacar(150.0);

    let saldo_atual = meu_banco.get_saldo();
    let nome = meu_banco.get_name();

    println!("Saldo atual do {}: R$ {}", nome, saldo_atual);

}