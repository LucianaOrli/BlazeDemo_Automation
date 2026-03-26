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
