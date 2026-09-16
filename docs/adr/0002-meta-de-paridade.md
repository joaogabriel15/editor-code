# ADR 0002 — Ampliar a meta para paridade funcional verificável

Status: aceita por instrução do usuário em 2026-09-15.

## Contexto
O usuário pediu conferência cuidadosa e inclusão de tudo necessário para funcionar como VS Code, sem limitar o planejamento ao MVP.

## Decisão
Manter implementação nova em Rust. Ampliar a meta para o conjunto funcional do baseline VS Code 1.137.0, incluindo notebooks, remoto, cliente web e APIs de extensões. Os marcos M0–M5 continuam como fundação; P0–P6 detalham a paridade. A versão 0.1 não significa paridade completa.

## Consequências
Compatibilidade parcial é uma etapa, não a definição final do escopo. Features dependentes de fornecedor ficam como impedimentos abertos até solução ou decisão explícita do usuário. Igualdade de marca/endpoints proprietários não é presumida. Nenhum ganho de desempenho é aceito sem comparação equivalente.

## Validação
EC-032 inventaria contratos; EC-092 compara comportamento; EC-094 homologa extensões reais; EC-098 revisa o conjunto. Qualquer diferença intencional de comportamento precisa constar no contrato, incluindo ativação de serviços sob demanda.
