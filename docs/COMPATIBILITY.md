# Matriz de compatibilidade

Todos os itens estão **não implementados** neste bootstrap.

| Capacidade | Estratégia prevista | Condição de aceite |
| --- | --- | --- |
| Temas de cores | Adaptar colors/tokenColors/semanticTokenColors | Fixtures e comparação visual |
| Ícones | Mapear manifesto e recursos | Fallback e validação de assets |
| Settings/atalhos | Subconjunto documentado | Precedência e diagnóstico |
| Gramáticas/snippets | Seleção de estratégia | Licenças e testes de sintaxe |
| LSP/DAP | Clientes próprios | Testes de protocolo e falhas |
| Claude Code | CLI/interface documentada | PoC com autenticação válida |
| Copilot | Interface oficialmente disponível | PoC por capacidade e condições de uso |
| Extensões VS Code | Host separado e RPC parcial | Suite de conformidade por API |
| Webviews/APIs propostas | Avaliação posterior | Decisão explícita de custo/escopo |
| Marketplace | Não presumido | Verificação de termos e distribuição |

Não confundir importar um tema com executar uma extensão. Não confundir disponibilidade de SDK com acesso a todos os recursos ou portabilidade de uma assinatura.

Fontes iniciais:
- https://code.visualstudio.com/api/advanced-topics/extension-host
- https://code.visualstudio.com/api/extension-capabilities/theming
- https://code.claude.com/docs/en/ide-integrations
- https://docs.github.com/en/copilot/get-started/quickstart-for-using-github-copilot-in-your-ide
