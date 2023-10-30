public class BancoMain {
    public static void main(String[] args) {
        // Cria um novo cofrinho
        Banco meuBanco = new Banco();
        meuBanco.ContaEmBanco("Marcus Schebek");

        // Realiza operações de depósito e saque
        meuBanco.Deposita(100);
        meuBanco.Saca(30);

        // Verifica e exibe o saldo atual
        System.out.println("Saldo atual do Banco de " + meuBanco.GetName() + ": R$ "  + meuBanco.GetSaldo());
    }
}