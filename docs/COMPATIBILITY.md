# Compatibilidade e meta final

**Nenhuma capacidade de editor está implementada no bootstrap.** Todos os grupos abaixo estão planejados.

| Grupo | Meta / tarefas de referência |
| --- | --- |
| Editor, interface, atalhos e settings | EC-033–046 |
| Temas, ícones, sintaxe e built-ins | EC-047–051 |
| Markdown, mídia, Git e diff/merge | EC-052–054 |
| Tarefas, debugger, terminal e testes | EC-055–058 |
| Notebooks/Jupyter e custom editors | EC-059–061 |
| Webviews, host e APIs de extensões | EC-062–072 |
| Comentários e colaboração | EC-073 |
| SSH, WSL, containers, túneis e web | EC-074–080 |
| Chat, sugestões, agentes, MCP e voz | EC-081–086 |
| Acessibilidade, plataformas, rede e distribuição | EC-087–091 |
| Conformidade, segurança, fornecedores e ecossistema | EC-092–098 |

## Níveis de evidência

- **Planejado:** issue e critérios existem.
- **Implementado:** código existe, ainda sem homologação completa.
- **Verificado:** testes/evidências do contrato passaram nas plataformas declaradas.
- **Parcial:** algum fluxo funciona, diferenças documentadas.
- **Bloqueado:** impedimento técnico ou de fornecedor com evidência.

## Distinções obrigatórias

Extensão Claude/Copilot original, CLI integrada e integração nativa são capacidades diferentes; validar cada uma.
API com mesma assinatura não garante mesma semântica.
Tema importado não implica execução da extensão que o distribui.
Backend alternativo de sync/remoto não implica acesso aos serviços Microsoft.
API proposta exige versão explícita e teste do consumidor.
Extensões externas têm versões, plataformas, licenças e backends próprios.

Veja [matriz](PARITY-MATRIX.md), [homologação planejada](PARITY-BACKLOG.md#ec-094) e [checklist](EXECUTION-CHECKLIST.md).
