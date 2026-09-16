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

## Expansão para paridade funcional

M0–M5 são a fundação. P0–P6 agrupam 68 tarefas adicionais, chegando a 98 tarefas técnicas. Consulte [checklist de execução](EXECUTION-CHECKLIST.md), [backlog de paridade](PARITY-BACKLOG.md) e [índice de issues](GITHUB-ISSUES.md). Os marcos não substituem a ordem de dependências. A versão 0.1 é um marco intermediário.

## Marcos de paridade

### P0 — Contrato, inventário e auditoria de paridade

EC-[031 / #31](https://github.com/joaogabriel15/editor-code/issues/31) · EC-[032 / #38](https://github.com/joaogabriel15/editor-code/issues/38) · EC-[072 / #62](https://github.com/joaogabriel15/editor-code/issues/62) · EC-[095 / #46](https://github.com/joaogabriel15/editor-code/issues/46) · EC-[098 / #98](https://github.com/joaogabriel15/editor-code/issues/98)

### P1 — Experiência completa do editor

EC-[033 / #39](https://github.com/joaogabriel15/editor-code/issues/39) · EC-[034 / #47](https://github.com/joaogabriel15/editor-code/issues/47) · EC-[035 / #32](https://github.com/joaogabriel15/editor-code/issues/32) · EC-[036 / #33](https://github.com/joaogabriel15/editor-code/issues/33) · EC-[037 / #40](https://github.com/joaogabriel15/editor-code/issues/40) · EC-[038 / #41](https://github.com/joaogabriel15/editor-code/issues/41) · EC-[039 / #34](https://github.com/joaogabriel15/editor-code/issues/34) · EC-[040 / #48](https://github.com/joaogabriel15/editor-code/issues/48) · EC-[041 / #55](https://github.com/joaogabriel15/editor-code/issues/55) · EC-[043 / #35](https://github.com/joaogabriel15/editor-code/issues/35) · EC-[044 / #42](https://github.com/joaogabriel15/editor-code/issues/42) · EC-[046 / #37](https://github.com/joaogabriel15/editor-code/issues/37) · EC-[047 / #43](https://github.com/joaogabriel15/editor-code/issues/43) · EC-[096 / #80](https://github.com/joaogabriel15/editor-code/issues/80)

### P4 — Desenvolvimento remoto e web

EC-[042 / #66](https://github.com/joaogabriel15/editor-code/issues/66) · EC-[074 / #63](https://github.com/joaogabriel15/editor-code/issues/63) · EC-[075 / #75](https://github.com/joaogabriel15/editor-code/issues/75) · EC-[076 / #76](https://github.com/joaogabriel15/editor-code/issues/76) · EC-[077 / #77](https://github.com/joaogabriel15/editor-code/issues/77) · EC-[078 / #84](https://github.com/joaogabriel15/editor-code/issues/84) · EC-[079 / #78](https://github.com/joaogabriel15/editor-code/issues/78)

### P6 — Plataformas, qualidade e distribuição

EC-[045 / #36](https://github.com/joaogabriel15/editor-code/issues/36) · EC-[086 / #93](https://github.com/joaogabriel15/editor-code/issues/93) · EC-[087 / #54](https://github.com/joaogabriel15/editor-code/issues/54) · EC-[088 / #79](https://github.com/joaogabriel15/editor-code/issues/79) · EC-[089 / #86](https://github.com/joaogabriel15/editor-code/issues/86) · EC-[090 / #64](https://github.com/joaogabriel15/editor-code/issues/64) · EC-[091 / #94](https://github.com/joaogabriel15/editor-code/issues/94) · EC-[092 / #95](https://github.com/joaogabriel15/editor-code/issues/95) · EC-[093 / #65](https://github.com/joaogabriel15/editor-code/issues/65) · EC-[094 / #96](https://github.com/joaogabriel15/editor-code/issues/96)

### P2 — Linguagens, Git e ferramentas

EC-[048 / #49](https://github.com/joaogabriel15/editor-code/issues/49) · EC-[049 / #56](https://github.com/joaogabriel15/editor-code/issues/56) · EC-[050 / #67](https://github.com/joaogabriel15/editor-code/issues/67) · EC-[051 / #68](https://github.com/joaogabriel15/editor-code/issues/68) · EC-[052 / #81](https://github.com/joaogabriel15/editor-code/issues/81) · EC-[053 / #44](https://github.com/joaogabriel15/editor-code/issues/44) · EC-[054 / #45](https://github.com/joaogabriel15/editor-code/issues/45) · EC-[055 / #57](https://github.com/joaogabriel15/editor-code/issues/57) · EC-[056 / #69](https://github.com/joaogabriel15/editor-code/issues/69) · EC-[057 / #50](https://github.com/joaogabriel15/editor-code/issues/50) · EC-[058 / #82](https://github.com/joaogabriel15/editor-code/issues/82) · EC-[073 / #74](https://github.com/joaogabriel15/editor-code/issues/74) · EC-[080 / #88](https://github.com/joaogabriel15/editor-code/issues/88) · EC-[097 / #97](https://github.com/joaogabriel15/editor-code/issues/97)

### P3 — Notebooks e compatibilidade de extensões

EC-[059 / #51](https://github.com/joaogabriel15/editor-code/issues/51) · EC-[060 / #70](https://github.com/joaogabriel15/editor-code/issues/70) · EC-[061 / #71](https://github.com/joaogabriel15/editor-code/issues/71) · EC-[062 / #52](https://github.com/joaogabriel15/editor-code/issues/52) · EC-[063 / #53](https://github.com/joaogabriel15/editor-code/issues/53) · EC-[064 / #58](https://github.com/joaogabriel15/editor-code/issues/58) · EC-[065 / #59](https://github.com/joaogabriel15/editor-code/issues/59) · EC-[066 / #72](https://github.com/joaogabriel15/editor-code/issues/72) · EC-[067 / #87](https://github.com/joaogabriel15/editor-code/issues/87) · EC-[068 / #60](https://github.com/joaogabriel15/editor-code/issues/60) · EC-[069 / #61](https://github.com/joaogabriel15/editor-code/issues/61) · EC-[070 / #73](https://github.com/joaogabriel15/editor-code/issues/73) · EC-[071 / #83](https://github.com/joaogabriel15/editor-code/issues/83)

### P5 — IA, agentes e automações

EC-[081 / #85](https://github.com/joaogabriel15/editor-code/issues/85) · EC-[082 / #89](https://github.com/joaogabriel15/editor-code/issues/89) · EC-[083 / #90](https://github.com/joaogabriel15/editor-code/issues/90) · EC-[084 / #91](https://github.com/joaogabriel15/editor-code/issues/91) · EC-[085 / #92](https://github.com/joaogabriel15/editor-code/issues/92)
