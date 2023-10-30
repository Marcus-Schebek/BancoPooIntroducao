public class Banco {
    private String name;
    private float saldo;
    
    
    public void ContaEmBanco(String name){
        this.saldo = 0;
        this.name = name;
    }
    public void Deposita(float valor){
        if(valor > 0){
            this.saldo = saldo + valor;
        } else {
            System.out.println("O valor depositado deve ser maior que R$ 0.00");
        }
    }
    public void Saca(float valor){
        if(valor > 0 && valor < this.saldo){
            this.saldo = saldo - valor;
        } else if(valor > this.saldo){
            System.out.println("Saldo insuficiente");
        } else{
            System.out.println("O valor a ser sacado deve ser maior que R$ 0.00");
        }
    }
    public float GetSaldo(){
        return saldo;
    }
    public String GetName(){
        return name;
    }
    
}