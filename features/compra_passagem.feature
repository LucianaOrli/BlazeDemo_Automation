# language: pt
Funcionalidade: Compra de Passagem Aérea - BlazeDemo
  Como um usuário do portal
  Eu quero pesquisar e comprar uma passagem
  Para validar a integridade do fluxo de vendas.

  Contexto:
    Dado que eu acesso o portal BlazeDemo

  Cenário: 01 - Reserva de voo com sucesso
    Quando eu seleciono a origem "Sao Paolo" e o destino "London"
    E clico no botão de procurar voos
    E escolho o primeiro voo disponível
    E preencho os dados de pagamento com sucesso
    Então o sistema deve exibir a mensagem "Thank you for your purchase today!"
