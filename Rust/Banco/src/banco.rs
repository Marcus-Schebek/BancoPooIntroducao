pub struct Banco {
    saldo: f32,
    name: String,
}


impl Banco{
    pub fn conta_em_banco(nome: &str) -> Banco {
        Banco {
            saldo: 0.0,
            name: nome.to_string(),
        }
    }
    pub fn depositar(&mut self, valor: f32){
        if valor > 0.0{
            self.saldo += valor;
            println!("Depositado {} reais.", valor);
        } else{
            println!("O valor depositado deve ser maior que 0");
        }
    }
    pub fn sacar(&mut self, valor: f32){
        if valor > 0.0 && valor <= self.saldo {
            self.saldo -= valor;
            println!("Sacado {} reais.", valor);
        } else if valor <= 0.0 {
            println!("O valor do saque deve ser maior que zero.");
        } else {
            println!("Saldo insuficiente para o saque.");
        }
    }
    pub fn get_saldo(&mut self) -> f32 {
        self.saldo
    }
    
    pub fn get_name(&mut self) -> &String {
        &self.name
    }
}