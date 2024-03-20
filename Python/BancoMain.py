import streamlit as st
from Banco import Banco

def main():
    st.title("Banco App")
    
    # Verifica se o estado da sessão já tem um Hash 'bancos'. Se não, cria um.
    if 'bancos' not in st.session_state:
        st.session_state['bancos'] = {}
    
    nome = st.text_input("Digite o nome do titular da conta", "Marcus Schebek")
    
    # Se o nome não estiver no HashMap, crie um novo banco para a pessoa
    if nome not in st.session_state['bancos']:
        st.session_state['bancos'][nome] = Banco(nome)
    
    deposito = st.number_input("Digite o valor do depósito", min_value=0.0, step=0.01)
    if st.button('Depositar'):
        st.session_state['bancos'][nome].Deposita(deposito)
    
    saque = st.number_input("Digite o valor do saque", min_value=0.0, step=0.01)
    if st.button('Sacar'):
        st.session_state['bancos'][nome].Saca(saque)
    
    # Cria uma tabela com o nome de cada pessoa e seu saldo
    data = {nome: f"R$ {banco.GetSaldo():.2f}" for nome, banco in st.session_state['bancos'].items()}
    st.table(data)

if __name__ == "__main__":
    main()
