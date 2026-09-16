# Conferência de cobertura do VS Code

## Conclusão

As 30 issues originais descreviam uma fundação/MVP. Elas não cobriam paridade completa.
O planejamento agora possui **98 tarefas**, incluindo 68 complementos de paridade.

## Referência congelada

- Release estável consultada: [VS Code 1.137.0](https://github.com/microsoft/vscode/releases/tag/1.137.0).
- Código: [645f29cc3176500b4b5762ba887cf2a7f0ffdf2c](https://github.com/microsoft/vscode/tree/645f29cc3176500b4b5762ba887cf2a7f0ffdf2c).
- Documentação consultada: [81d76c22e9a4f5c63733c38e4ccedaf8c9f051bf](https://github.com/microsoft/vscode-docs/tree/81d76c22e9a4f5c63733c38e4ccedaf8c9f051bf).
- Main anteriormente inspecionado: 29d5c1ecf1086c8ba833108afa45a766f6cc9f0b; não confundir com a release estável.
- Conferência: 2026-09-15. Serviços e docs online podem mudar; paridade é avaliada por versão.

## O que foi conferido

Árvore completa da API GitHub, com truncated=false; classificação manual de todos os diretórios imediatos de workbench/editor/sessions contrib; leitura de 96 manifestos de extensões built-in e de vscode.d.ts; consulta a editorOptions.ts, extensionsRegistry.ts, product.json e documentação oficial.
Foram extraídos 736 registros de responsabilidade:

- 100 de workbench
- 59 de editor
- 29 de sessions
- 107 de platform
- 95 de service
- 96 de builtin
- 15 de api-namespace
- 179 de proposed-api
- 56 de manifest-contribution

A extração não substitui a leitura semântica de todos os métodos. A issue EC-032 exige inventário por AST/registry de cada comando, setting e contrato público; EC-092 exige testes diferenciais; EC-098 bloqueia a declaração de paridade enquanto houver gaps.

## Lacunas corrigidas no planejamento

Edição avançada e navegação; layout multiwindow; Settings UI/context keys; perfis/sync; arquivos virtuais/histórico; built-ins e linguagens; Git/merge; tasks/debug/terminal completos; testes/cobertura; notebooks/Jupyter; webviews/custom editors; APIs e ciclo de vida de extensões; autenticação; SSH/WSL/containers/túneis/web; agentes/MCP/voz; acessibilidade; CLI/rede/políticas; diagnósticos; atualização e homologação.

## O que permanece incerto

- Viabilidade de executar cada extensão original, especialmente APIs propostas e dependências nativas.
- Acesso/licenciamento/autenticação de serviços Microsoft, GitHub, Anthropic e demais provedores.
- Toolkit de interface e custo de um motor web para webviews.
- Economia real de memória com funcionalidade equivalente.
- Recursos de documentação/main posteriores à release: catalogar como delta, não assumir que existem no baseline.

## Critério de completude

A matriz rastreia entradas estruturais; **não significa 100% do VS Code implementado ou especificado método a método**.
Nada dependente de fornecedor deve sumir do checklist: vira integração aprovada, equivalente documentado ou impedimento aberto.
Não declarar paridade completa enquanto existir requisito planejado, parcial, bloqueado ou sem teste no contrato vigente.

Veja [checklist de execução](EXECUTION-CHECKLIST.md), [backlog](PARITY-BACKLOG.md), [matriz](PARITY-MATRIX.md) e [dados verificáveis](planning/parity-plan.json).
