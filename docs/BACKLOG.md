# Backlog detalhado

IDs EC são estáveis; números de issues são vinculados em GITHUB-ISSUES.md.

## EC-001 — Medir VS Code com múltiplos repositórios

Marco: M0 — Fundação e decisões. Área: Pesquisa.

Criar cenários sintéticos com 1, 10 e 50 repositórios e comparar configuração sem extensões e configuração de uso real.

**Aceite:** Registrar hardware, versões, RAM da árvore de processos, CPU ociosa, startup frio/quente e latência de abertura; publicar resultados reproduzíveis sem caminhos ou código privado.

**Dependências:** Nenhuma.

## EC-002 — Escolher toolkit de interface nativa Rust

Marco: M0 — Fundação e decisões. Área: Arquitetura.

Comparar candidatos por protótipos mínimos; não assumir que Rust garante menor consumo.

**Aceite:** Documentar ADR com Windows, IME, acessibilidade, texto Unicode, DPI, renderização e licenças; medir memória e latência; escolher um toolkit.

**Dependências:** EC-001.

## EC-003 — Auditar API e formatos do VS Code

Marco: M0 — Fundação e decisões. Área: Compatibilidade.

Mapear comandos, configurações, temas, snippets e APIs necessárias às extensões prioritárias usando uma revisão fixa do upstream.

**Aceite:** Publicar matriz planejado/implementado/verificado/parcial/bloqueado; separar API estável e proposta; registrar origem e licença de qualquer código reutilizado. Impedimentos não removem requisitos da meta de paridade.

**Dependências:** Nenhuma.

## EC-004 — Validar integração do GitHub Copilot

Marco: M0 — Fundação e decisões. Área: IA.

Investigar interfaces oficialmente disponíveis, autenticação e diferenças entre autocomplete, chat e agente para editor próprio.

**Aceite:** Entregar PoC mínima ou relatório de impedimento com fontes; não usar endpoints privados nem prometer portabilidade de assinatura; decidir integração antes de depender dela.

**Dependências:** EC-003.

## EC-005 — Validar integração do Claude Code

Marco: M0 — Fundação e decisões. Área: IA.

Verificar CLI e interfaces documentadas para sessão, contexto, streaming, cancelamento e diffs.

**Aceite:** Demonstrar fluxo autorizado em ambiente de teste; documentar login, cobrança, limitações e alternativa pelo terminal; não embutir credenciais.

**Dependências:** EC-003.

## EC-006 — Implementar buffer de texto e histórico de edição

Marco: M1 — Editor utilizável. Área: Core.

Construir núcleo independente da UI com estrutura adequada a documentos grandes.

**Aceite:** Cobrir Unicode, CRLF/LF, seleção, edição agrupada, undo/redo e limites de memória; comparar desempenho em arquivos de tamanhos distintos.

**Dependências:** EC-002.

## EC-007 — Abrir, salvar e recuperar documentos com segurança

Marco: M1 — Editor utilizável. Área: Arquivos.

Implementar I/O de documentos, codificações e recuperação de sessão.

**Aceite:** Tratar gravação atômica quando suportada, conflito externo, falha de disco, arquivo somente leitura, BOM e recuperação após encerramento; nunca perder conteúdo silenciosamente.

**Dependências:** EC-006.

## EC-008 — Construir janela, abas e renderização do editor

Marco: M1 — Editor utilizável. Área: UI.

Criar shell nativo com painel de arquivos, abas e área de texto virtualizada.

**Aceite:** Abrir e editar arquivo real; implementar rolagem, cursor, seleção, clipboard, IME, zoom, DPI e navegação por teclado; UI não bloqueia durante I/O.

**Dependências:** EC-002, EC-006, EC-007.

## EC-009 — Adicionar comandos, atalhos e configurações

Marco: M1 — Editor utilizável. Área: UI.

Criar registro de comandos, paleta e configuração por usuário/workspace.

**Aceite:** Permitir remapeamento, precedência de configurações e diagnóstico de JSON inválido; documentar subconjunto importável de keybindings/settings do VS Code.

**Dependências:** EC-008, EC-003.

## EC-010 — Importar temas de cores do VS Code

Marco: M1 — Editor utilizável. Área: Temas.

Interpretar cores da interface, tokenColors e semanticTokenColors com fallbacks explícitos.

**Aceite:** Carregar fixtures redistribuíveis; mapear cores e precedência, includes e erros; publicar diferenças de fidelidade; trocar tema sem reiniciar.

**Dependências:** EC-003, EC-008.

## EC-011 — Adicionar realce de sintaxe e gramáticas

Marco: M1 — Editor utilizável. Área: Temas.

Escolher estratégia de parsing e compatibilidade com scopes TextMate.

**Aceite:** Realçar linguagens iniciais com atualização incremental; validar comentários, strings e Unicode; documentar relação com tokenColors e licenças das gramáticas.

**Dependências:** EC-006, EC-010.

## EC-012 — Implementar catálogo de repositórios e ativação sob demanda

Marco: M2 — Muitos repositórios. Área: Workspace.

Separar repositórios cadastrados dos serviços efetivamente ativos.

**Aceite:** Modelar estados inativo/ativo/suspenso; abrir vários roots, persistir seleção e impedir inicialização de LSP/Git/watchers em todos os repos por padrão.

**Dependências:** EC-007, EC-009.

## EC-013 — Criar supervisor de tarefas e orçamento de recursos

Marco: M2 — Muitos repositórios. Área: Performance.

Centralizar filas, concorrência, cancelamento e ciclo de vida de processos.

**Aceite:** Aplicar backpressure, prioridades e limites configuráveis; encerrar processos filhos corretamente; expor consumo por serviço e evitar tarefas duplicadas.

**Dependências:** EC-012.

## EC-014 — Implementar árvore virtualizada e watchers seletivos

Marco: M2 — Muitos repositórios. Área: Arquivos.

Monitorar apenas raízes necessárias com exclusões e tratamento de eventos em lote.

**Aceite:** Respeitar ignores configurados; tratar symlinks, junctions, renames e tempestades de eventos; medir escala sem varreduras contínuas.

**Dependências:** EC-012, EC-013.

## EC-015 — Adicionar busca de arquivos e conteúdo entre repos

Marco: M2 — Muitos repositórios. Área: Busca.

Implementar busca incremental e cancelável com limites de resultados.

**Aceite:** Respeitar ignores, encoding e escopo escolhido; tratar binários e arquivos grandes; publicar benchmarks de 1/10/50 repos.

**Dependências:** EC-013, EC-014.

## EC-016 — Integrar status e diff por repositório

Marco: M2 — Muitos repositórios. Área: Git.

Executar operações Git isoladas por repo e sob demanda.

**Aceite:** Mostrar status/diff, branch e erros; lidar com worktrees e submódulos; cancelamento e limites de concorrência; operações destrutivas exigem ação explícita.

**Dependências:** EC-012, EC-013, EC-008.

## EC-017 — Implementar cliente LSP e supervisor de servidores

Marco: M3 — Ferramentas de desenvolvimento. Área: Linguagens.

Integrar Language Server Protocol com processos iniciados sob demanda.

**Aceite:** Validar initialize/shutdown, sincronização versionada, UTF-16/negociação de posição, diagnóstico, completion, hover e definição; tratar crash e timeout.

**Dependências:** EC-006, EC-012, EC-013.

## EC-018 — Adicionar refatoração, formatação e semantic tokens

Marco: M3 — Ferramentas de desenvolvimento. Área: Linguagens.

Expandir LSP para edição assistida e coloração semântica.

**Aceite:** Validar workspace edits entre arquivos, preview, versões divergentes, rename, code actions e formatting; manter undo e precedência das cores.

**Dependências:** EC-017, EC-010.

## EC-019 — Implementar terminal integrado com PTY

Marco: M3 — Ferramentas de desenvolvimento. Área: Terminal.

Oferecer sessões por repositório, começando por Windows/ConPTY.

**Aceite:** Validar resize, ANSI, Unicode, clipboard, saída intensa e encerramento; não interpolar comandos com caminhos de forma insegura.

**Dependências:** EC-008, EC-012, EC-013.

## EC-020 — Adicionar tarefas e cliente DAP

Marco: M3 — Ferramentas de desenvolvimento. Área: Debug.

Implementar execução de tarefas e depuração por protocolo.

**Aceite:** Suportar launch, breakpoints, stepping e variáveis em adaptador de teste; documentar subconjunto de tasks.json/launch.json e exigir confiança antes de executar configuração do repo.

**Dependências:** EC-019, EC-009, EC-013.

## EC-021 — Criar interface de provedores e painel de IA

Marco: M4 — IA e compatibilidade. Área: IA.

Definir contratos de sessão, contexto, streaming, cancelamento e uso de ferramentas.

**Aceite:** Implementar provedor simulado; seleção explícita de arquivos, limites de contexto, redaction de logs e armazenamento seguro de credenciais; rede e ferramentas requerem autorização apropriada.

**Dependências:** EC-004, EC-005, EC-008, EC-013.

## EC-022 — Integrar Claude Code ao fluxo de edição

Marco: M4 — IA e compatibilidade. Área: IA.

Implementar a abordagem aprovada na prova de viabilidade.

**Aceite:** Validar sessão, contexto selecionado, cancelamento e revisão de diff; manter caminho via terminal quando necessário; testar sem publicar credenciais ou conteúdo privado.

**Dependências:** EC-005, EC-019, EC-021.

## EC-023 — Integrar GitHub Copilot pelo caminho validado

Marco: M4 — IA e compatibilidade. Área: IA.

Implementar apenas recursos aprovados na prova de viabilidade, com status explícito por capacidade.

**Aceite:** Testar autenticação, expiração, erros, sugestão/chat conforme suporte; documentar restrições; marcar bloqueado com evidências se não houver caminho suportado.

**Dependências:** EC-004, EC-021.

## EC-024 — Prototipar host isolado de extensões VS Code

Marco: M4 — IA e compatibilidade. Área: Compatibilidade.

Avaliar processo Node separado e ponte RPC para subconjunto explícito da API vscode.

**Aceite:** Executar extensão de teste própria com comandos/documentos/configuração; crash não derruba editor; não chamar isolamento de processo de sandbox; definir modelo de permissões e incompatibilidades.

**Dependências:** EC-003, EC-009, EC-013.

## EC-025 — Adicionar instalação de pacotes e temas de ícones

Marco: M4 — IA e compatibilidade. Área: Compatibilidade.

Criar fluxo local VSIX e, somente após validação de termos, catálogo compatível.

**Aceite:** Validar paths contra zip slip, tamanho e integridade; separar temas declarativos de código executável; importar ícones com fallback; não pressupor acesso ao Marketplace Microsoft.

**Dependências:** EC-010, EC-024.

## EC-026 — Implementar confiança de workspace e revisão de alterações de IA

Marco: M4 — IA e compatibilidade. Área: Segurança.

Controlar execução de comandos, servidores, extensões e aplicação de edições.

**Aceite:** Em workspace não confiável não executar código automaticamente; pré-visualizar alterações, detectar conflito de versão, suportar rejeição/undo e logs sem segredos.

**Dependências:** EC-007, EC-021, EC-024.

## EC-027 — Validar acessibilidade, internacionalização e edição avançada

Marco: M5 — Qualidade e lançamento. Área: Qualidade.

Completar comportamento de editor para uso diário.

**Aceite:** Testar teclado, leitor de tela, contraste, IME, Unicode/graphemes, multicursor, busca/substituição, folding e arquivos grandes; registrar limitações conhecidas.

**Dependências:** EC-008, EC-009, EC-011, EC-018.

## EC-028 — Criar suíte de regressão e comparar com VS Code

Marco: M5 — Qualidade e lançamento. Área: Performance.

Reutilizar cenários da baseline para medir o editor completo.

**Aceite:** Publicar RAM total incluindo filhos, CPU ociosa, p50/p95 de edição/busca/startup; definir limites baseados em dados; impedir alegações de ganho sem resultados reproduzíveis.

**Dependências:** EC-001, EC-015, EC-017, EC-024, EC-027.

## EC-029 — Preparar empacotamento e atualização segura

Marco: M5 — Qualidade e lançamento. Área: Release.

Criar artefatos Windows primeiro e validar portabilidade em Linux/macOS.

**Aceite:** Produzir build reproduzível com checksums, inventário/licenças de dependências, instalação/desinstalação e estratégia de assinatura/rollback; não publicar release estável sem QA.

**Dependências:** EC-026, EC-027, EC-028.

## EC-030 — Publicar guia de uso, migração e critérios de versão 0.1

Marco: M5 — Qualidade e lançamento. Área: Documentação.

Consolidar onboarding, atalhos, temas, multi-repo e suporte real de IA/extensões.

**Aceite:** Guia deve refletir recursos implementados; checklist de release com limitações, métricas e instalação em máquina limpa; fechar roadmap somente com evidência.

**Dependências:** EC-022, EC-023, EC-025, EC-029.

## Complemento obrigatório

Este arquivo mantém as 30 tarefas iniciais da fundação. A meta ampliada está em [PARITY-BACKLOG.md](PARITY-BACKLOG.md). Nenhum limite inicial de subconjunto elimina o restante do contrato de paridade.
