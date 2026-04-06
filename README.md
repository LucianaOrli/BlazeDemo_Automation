 🚀 Projeto BlazeDemo - Automação & Performance (Lux by Or)

 📋 Cenário de Performance 
 * **URL:** https://www.blazedemo.com
* **Critério:** 250 RPS / 90th Percentile < 2s.

 🌟 ***![Performance Test CI](https://github.com/lucianaorli/blazedemo/actions/workflows/main.yml/badge.svg)***

📊 Análise Técnica:
O script foi desenvolvido em **Locust** para atingir a vazão solicitada. 
Resultado: Sob estresse de 250 RPS, o ambiente público apresentou degradação (Timeouts), indicando a necessidade de escalonamento de infraestrutura para satisfazer o critério de aceitação em ambiente produtivo.

🛠️ Como Executar:
1. Funcional: `pytest tests/test_blaze.py --html=evidencias/relatorio.html`
2. Performance: `locust -f tests/test_performance_blaze.py --headless -u 100 -r 25 -t 1m --host https://www.blazedemo.com`
⚡ Execução de Performance 

Para validar o critério de **250 RPS**, utilize os comandos abaixo conforme a estratégia de teste desejada:

1. Teste de Carga (Load Test): Objetivo: Validar a estabilidade do sistema sob carga constante.
   bash
   python3 -m locust -f tests/test_performance_blaze.py --headless -u 100 -r 10 -t 5m --host [https://www.blazedemo.com](https://www.blazedemo.com)

Teste de Pico (Spike Test): Objetivo: Validar a resiliência do sistema a subidas repentinas de tráfego.
bash
python3 -m locust -f tests/test_performance_blaze.py --headless -u 250 -r 50 -t 2m --host [https://www.blazedemo.com](https://www.blazedemo.com)

2. 📊 Análise de Resultados (Evidências Reais):
Após a execução dos testes de estresse, foram observados os seguintes indicadores:
Vazão (RPS): O ambiente sustentou uma média de 170.20 RPS com 100 usuários simultâneos.
Latência Média: Estabilizada em 581ms, demonstrando boa resposta base para requisições individuais.
Picos de Resposta (Max): Foram registradas latências de até 3206ms (3.2 segundos) em momentos de maior concorrência.
Conclusão Técnica: O critério de aceitação (Percentil 90 < 2s) não foi plenamente satisfeito sob a carga máxima de 250 RPS.

A análise de carga via Locust identificou que o 90th percentile excede 2s devido à latência de rede e tempo de processamento do backend do ambiente de demonstração (Blaze Demo). O comportamento foi mapeado e documentado nos relatórios de performance anexos na pasta /reports.

📂 Clique aqui para ver o Relatório de Performance (CSV)

Recomendação de QA: Para ambiente de produção, é imprescindível o escalonamento horizontal e a reserva de recursos dedicada para garantir que o tempo de resposta permaneça dentro do SLA estabelecido pela regra de negócio.
Sob estresse de 250 RPS, o ambiente público apresentou latência elevada e timeouts ocasionais.
Conclusão: O critério de 90th percentile < 2s não foi satisfatório devido às limitações do ambiente compartilhado,  evidenciando a necessidade de escalonamento horizontal e reserva de recursos para garantir a performance em produção.

**CI/CD Pipeline (GitHub Actions)***
***O projeto conta com uma esteira de Integração Contínua (CI) configurada via GitHub Actions, garantindo a qualidade em cada entrega***:

Execução Automatizada: O script de performance (test_performance_blaze.py) é disparado automaticamente a cada push ou pull request.

Relatórios Automáticos: A pipeline gera e armazena os artefatos de execução (HTML e CSV) diretamente na aba Actions do GitHub após cada teste.

Ambiente Padronizado: Execução em ambiente isolado (Ubuntu Latest) com Python 3.9, garantindo a reprodutibilidade dos testes.



