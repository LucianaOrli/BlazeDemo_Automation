# 🚀 Projeto BlazeDemo - Automação & Performance (Lux by Or)

## 📋 Cenário de Performance (Questão 3)
* **URL:** https://www.blazedemo.com
* **Critério:** 250 RPS / 90th Percentile < 2s.

### 📊 Análise Técnica:
O script foi desenvolvido em **Locust** para atingir a vazão solicitada. 
* **Resultado:** Sob estresse de 250 RPS, o ambiente público apresentou degradação (Timeouts), indicando a necessidade de escalonamento de infraestrutura para satisfazer o critério de aceitação em ambiente produtivo.

## 🛠️ Como Executar:
1. Funcional: `pytest tests/test_blaze.py --html=evidencias/relatorio.html`
2. Performance: `locust -f tests/test_performance_blaze.py --headless -u 100 -r 25 -t 1m --host https://www.blazedemo.com`
### ⚡ Execução de Performance (Questão 3)

Para validar o critério de **250 RPS**, utilize os comandos abaixo conforme a estratégia de teste desejada:

1. **Teste de Carga (Load Test):** *Objetivo: Validar a estabilidade do sistema sob carga constante.*
   ```bash
   locust -f tests/test_performance_blaze.py --headless -u 100 -r 10 -t 5m --host [https://www.blazedemo.com](https://www.blazedemo.com)
  2. **Teste de Pico** (Spike Test): Objetivo: Validar a resiliência do sistema a subidas repentinas de tráfego.
    locust -f tests/test_performance_blaze.py --headless -u 250 -r 50 -t 2m --host [https://www.blazedemo.com](https://www.blazedemo.com)
Análise de Resultados:
Sob estresse de 250 RPS, o ambiente público apresentou latência elevada e timeouts ocasionais.
Conclusão: O critério de 90th percentile < 2s não foi satisfatório devido às limitações do ambiente compartilhado (infraestrutura pública), evidenciando a necessidade de escalonamento horizontal e reserva de recursos para garantir a performance em produção.
