# Roadmap

A sequência considera dependências, não datas prometidas. Consulte BACKLOG.md e as issues para critérios.

## M0 — Fundação e decisões

- EC-001: Medir VS Code com múltiplos repositórios
- EC-002: Escolher toolkit de interface nativa Rust
- EC-003: Auditar API e formatos do VS Code
- EC-004: Validar integração do GitHub Copilot
- EC-005: Validar integração do Claude Code

## M1 — Editor utilizável

- EC-006: Implementar buffer de texto e histórico de edição
- EC-007: Abrir, salvar e recuperar documentos com segurança
- EC-008: Construir janela, abas e renderização do editor
- EC-009: Adicionar comandos, atalhos e configurações
- EC-010: Importar temas de cores do VS Code
- EC-011: Adicionar realce de sintaxe e gramáticas

## M2 — Muitos repositórios

- EC-012: Implementar catálogo de repositórios e ativação sob demanda
- EC-013: Criar supervisor de tarefas e orçamento de recursos
- EC-014: Implementar árvore virtualizada e watchers seletivos
- EC-015: Adicionar busca de arquivos e conteúdo entre repos
- EC-016: Integrar status e diff por repositório

## M3 — Ferramentas de desenvolvimento

- EC-017: Implementar cliente LSP e supervisor de servidores
- EC-018: Adicionar refatoração, formatação e semantic tokens
- EC-019: Implementar terminal integrado com PTY
- EC-020: Adicionar tarefas e cliente DAP

## M4 — IA e compatibilidade

- EC-021: Criar interface de provedores e painel de IA
- EC-022: Integrar Claude Code ao fluxo de edição
- EC-023: Integrar GitHub Copilot pelo caminho validado
- EC-024: Prototipar host isolado de extensões VS Code
- EC-025: Adicionar instalação de pacotes e temas de ícones
- EC-026: Implementar confiança de workspace e revisão de alterações de IA

## M5 — Qualidade e lançamento

- EC-027: Validar acessibilidade, internacionalização e edição avançada
- EC-028: Criar suíte de regressão e comparar com VS Code
- EC-029: Preparar empacotamento e atualização segura
- EC-030: Publicar guia de uso, migração e critérios de versão 0.1

## Primeiros passos
Executar baseline, auditoria de compatibilidade e provas de Claude/Copilot. Escolher UI com evidências, depois implementar buffer e persistência. Não esperar terminar o editor para descobrir restrições das integrações.
