# Visão

Editor Code deve permitir trabalhar em muitos repositórios sem manter toda a infraestrutura de cada projeto em execução.

## Primeira versão
Windows, edição confiável, navegação por teclado, busca, temas, catálogo multi-root, Git, terminal e suporte inicial por LSP. Integrações de IA entram após provas de viabilidade.

## Meta depois da fundação
Paridade funcional verificável com VS Code 1.137.0: edição e workbench completos, linguagens, Git, terminal/debug/testes, notebooks, APIs de extensões, webviews, perfis/sync, remoto/web, IA/agentes, acessibilidade e distribuição. Compatibilidade parcial é uma etapa, não o escopo final.

## Dependências e evidências
Marketplace, serviços de conta/sync/remoto e extensões de terceiros dependem de interfaces e direitos verificáveis. Permanecem no checklist como integrações ou impedimentos, nunca exclusões silenciosas. Nenhuma compatibilidade completa ou economia de memória está comprovada. Veja PARITY-AUDIT.md e ADR 0002.

## Princípios
Integridade do documento; resposta rápida; cancelamento; serviços sob demanda; configuração explícita; nenhuma execução automática de código não confiável.
