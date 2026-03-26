# language: pt
Funcionalidade: Compra de Passagem Aérea - BlazeDemo
  Como um viajante do portal
  Eu quero pesquisar voos entre as cidades permitidas
  Para validar o fluxo de compra com 4 passageiros.

  Contexto:
    Dado que eu acesso o portal BlazeDemo

  @regressivo @missao_israel
  Cenário: 01 - Reserva de voo Paris para Londres (Grupo 4 Passageiros)
    Quando eu seleciono a origem "Paris" e o destino "London"
    E clico no botão de procurar voos
    E escolho o primeiro voo disponível
    E preencho os dados para "Luciana - Grupo 4 Israel"
    Então o sistema deve exibir "Thank you for your purchase today!"
