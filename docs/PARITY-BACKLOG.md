# Backlog de paridade detalhado

Complementa as 30 tarefas de fundação; não declara recursos implementados.

<a id="ec-031"></a>
## EC-031 — Definir contrato de paridade e versão de referência

[Issue #31](https://github.com/joaogabriel15/editor-code/issues/31)

**Área:** Governança · **Marco:** P0 — Contrato, inventário e auditoria de paridade · **Estado:** planejado

Transformar a meta de igualdade com VS Code em requisitos verificáveis por plataforma e capacidade.

### Checklist de entrega

- [ ] Fixar VS Code 1.137.0 e SHA 645f29cc3176500b4b5762ba887cf2a7f0ffdf2c; registrar separadamente recursos de main e documentação posterior.
- [ ] Classificar cada capacidade como nativa, compatibilidade de extensão ou dependência de serviço; manter impedimentos visíveis sem chamá-los de equivalência.
- [ ] Definir evidências para estados planejado, implementado, verificado, parcial e bloqueado; não fechar paridade global com exclusões silenciosas.

### Como executar e comprovar

1. Reproduzir o fluxo correspondente no VS Code de referência e registrar comportamento esperado.
2. Criar fixture mínima, definir contratos e detalhar casos negativos antes da implementação.
3. Implementar incrementalmente sem bloquear a UI nem executar conteúdo não confiável.
4. Comparar resultado/eventos/estado com a referência; anexar testes, captura ou benchmark.
5. Atualizar matriz de gaps e documentação; marcar concluído apenas com evidências.

**Dependências:** [#3](https://github.com/joaogabriel15/editor-code/issues/3).

**Fontes:** [referência 1](https://code.visualstudio.com/docs) · [referência 2](https://code.visualstudio.com/api)

<a id="ec-032"></a>
## EC-032 — Inventariar comandos, configurações, APIs e contribuições sem lacunas

[Issue #38](https://github.com/joaogabriel15/editor-code/issues/38)

**Área:** Governança · **Marco:** P0 — Contrato, inventário e auditoria de paridade · **Estado:** planejado

Expandir a auditoria estrutural para cada contrato público e comportamento registrado.

### Checklist de entrega

- [ ] Gerar inventário por AST/registries de comandos, settings, defaults, context keys, activation events, contribution points e símbolos de vscode.d.ts.
- [ ] Mapear cada entrada a issue, caso de teste e versão; separar APIs propostas/internas das estáveis.
- [ ] Falhar a validação em entradas sem classificação e publicar delta ao atualizar upstream; extração textual preliminar não prova cobertura semântica.

### Como executar e comprovar

1. Reproduzir o fluxo correspondente no VS Code de referência e registrar comportamento esperado.
2. Criar fixture mínima, definir contratos e detalhar casos negativos antes da implementação.
3. Implementar incrementalmente sem bloquear a UI nem executar conteúdo não confiável.
4. Comparar resultado/eventos/estado com a referência; anexar testes, captura ou benchmark.
5. Atualizar matriz de gaps e documentação; marcar concluído apenas com evidências.

**Dependências:** [EC-031](./PARITY-BACKLOG.md#ec-031).

**Fontes:** [referência 1](https://code.visualstudio.com/api/references/vscode-api) · [referência 2](https://github.com/microsoft/vscode-docs/blob/81d76c22e9a4f5c63733c38e4ccedaf8c9f051bf/api/references/contribution-points.md) · [referência 3](https://github.com/microsoft/vscode-docs/blob/81d76c22e9a4f5c63733c38e4ccedaf8c9f051bf/api/references/activation-events.md)

<a id="ec-033"></a>
## EC-033 — Completar layout, grupos de editores e múltiplas janelas

[Issue #39](https://github.com/joaogabriel15/editor-code/issues/39)

**Área:** Workbench · **Marco:** P1 — Experiência completa do editor · **Estado:** planejado

Reproduzir composição e persistência da área de trabalho.

### Checklist de entrega

- [ ] Implementar split/grid, abas preview/pinned/sticky, reordenação, arrastar entre grupos/janelas e restauração de sessão.
- [ ] Permitir mover painéis/views, sidebar secundária, status/activity bar, menus, command center, Zen e fullscreen.
- [ ] Validar monitores/DPI distintos, foco, teclado, edições não salvas e estado de janelas auxiliares.

### Como executar e comprovar

1. Reproduzir o fluxo correspondente no VS Code de referência e registrar comportamento esperado.
2. Criar fixture mínima, definir contratos e detalhar casos negativos antes da implementação.
3. Implementar incrementalmente sem bloquear a UI nem executar conteúdo não confiável.
4. Comparar resultado/eventos/estado com a referência; anexar testes, captura ou benchmark.
5. Atualizar matriz de gaps e documentação; marcar concluído apenas com evidências.

**Dependências:** [#8](https://github.com/joaogabriel15/editor-code/issues/8), [EC-031](./PARITY-BACKLOG.md#ec-031).

**Fontes:** [referência 1](https://github.com/microsoft/vscode-docs/blob/81d76c22e9a4f5c63733c38e4ccedaf8c9f051bf/docs/configure/custom-layout.md)

<a id="ec-034"></a>
## EC-034 — Completar navegação, Quick Open, breadcrumbs e Outline

[Issue #47](https://github.com/joaogabriel15/editor-code/issues/47)

**Área:** Workbench · **Marco:** P1 — Experiência completa do editor · **Estado:** planejado

Unificar navegação local e entre símbolos/arquivos.

### Checklist de entrega

- [ ] Quick Open com prefixos e histórico, go-to line/symbol, navegação back/forward e reabrir aba fechada.
- [ ] Breadcrumbs e Outline com filtros, ordenação, seleção sincronizada e cancelamento.
- [ ] Go-to/peek references, definition/implementation/type e hierarquias de chamadas/tipos com histórico e múltiplos resultados.

### Como executar e comprovar

1. Reproduzir o fluxo correspondente no VS Code de referência e registrar comportamento esperado.
2. Criar fixture mínima, definir contratos e detalhar casos negativos antes da implementação.
3. Implementar incrementalmente sem bloquear a UI nem executar conteúdo não confiável.
4. Comparar resultado/eventos/estado com a referência; anexar testes, captura ou benchmark.
5. Atualizar matriz de gaps e documentação; marcar concluído apenas com evidências.

**Dependências:** [#9](https://github.com/joaogabriel15/editor-code/issues/9), [#17](https://github.com/joaogabriel15/editor-code/issues/17), [EC-033](./PARITY-BACKLOG.md#ec-033).

**Fontes:** [referência 1](https://github.com/microsoft/vscode-docs/blob/81d76c22e9a4f5c63733c38e4ccedaf8c9f051bf/docs/editing/editingevolved.md)

<a id="ec-035"></a>
## EC-035 — Completar comandos de edição, seleção e multicursor

[Issue #32](https://github.com/joaogabriel15/editor-code/issues/32)

**Área:** Editor · **Marco:** P1 — Experiência completa do editor · **Estado:** planejado

Implementar operações cotidianas além do buffer básico.

### Checklist de entrega

- [ ] Multicursor, seleção retangular, próxima/todas ocorrências, smart select, seleção ancorada e undo de cursor.
- [ ] Mover/copiar/juntar/ordenar linhas, case transforms, comentários, indent/outdent, transposição e operações de palavra/subpalavra.
- [ ] Auto closing/surround pairs, linked editing, drag/drop e paste providers, clipboard multiseleção e undo agrupado; validar Unicode/IME.

### Como executar e comprovar

1. Reproduzir o fluxo correspondente no VS Code de referência e registrar comportamento esperado.
2. Criar fixture mínima, definir contratos e detalhar casos negativos antes da implementação.
3. Implementar incrementalmente sem bloquear a UI nem executar conteúdo não confiável.
4. Comparar resultado/eventos/estado com a referência; anexar testes, captura ou benchmark.
5. Atualizar matriz de gaps e documentação; marcar concluído apenas com evidências.

**Dependências:** [#6](https://github.com/joaogabriel15/editor-code/issues/6), [#8](https://github.com/joaogabriel15/editor-code/issues/8).

**Fontes:** [referência 1](https://github.com/microsoft/vscode-docs/blob/81d76c22e9a4f5c63733c38e4ccedaf8c9f051bf/docs/editing/codebasics.md)

<a id="ec-036"></a>
## EC-036 — Completar renderização, minimap, folding e decorações

[Issue #33](https://github.com/joaogabriel15/editor-code/issues/33)

**Área:** Editor · **Marco:** P1 — Experiência completa do editor · **Estado:** planejado

Cobrir comportamento visual e interação do editor de texto.

### Checklist de entrega

- [ ] Minimap, overview ruler, glyph margin, line numbers, bracket guides/colorization, sticky scroll, code folding e regiões.
- [ ] Word wrap, font ligatures/zoom, whitespace/control chars, Unicode suspeito, inlay/inline decorations, view zones e scroll sincronizado.
- [ ] Validar fontes fallback, graphemes, RTL/bidi, linhas longas, GPU fallback e minimap em arquivos grandes sem bloquear edição.

### Como executar e comprovar

1. Reproduzir o fluxo correspondente no VS Code de referência e registrar comportamento esperado.
2. Criar fixture mínima, definir contratos e detalhar casos negativos antes da implementação.
3. Implementar incrementalmente sem bloquear a UI nem executar conteúdo não confiável.
4. Comparar resultado/eventos/estado com a referência; anexar testes, captura ou benchmark.
5. Atualizar matriz de gaps e documentação; marcar concluído apenas com evidências.

**Dependências:** [#8](https://github.com/joaogabriel15/editor-code/issues/8), [#11](https://github.com/joaogabriel15/editor-code/issues/11).

**Fontes:** [referência 1](https://github.com/microsoft/vscode-docs/blob/81d76c22e9a4f5c63733c38e4ccedaf8c9f051bf/docs/editing/codebasics.md)

<a id="ec-037"></a>
## EC-037 — Implementar snippets e configurações de linguagem completas

[Issue #40](https://github.com/joaogabriel15/editor-code/issues/40)

**Área:** Editor · **Marco:** P1 — Experiência completa do editor · **Estado:** planejado

Reproduzir snippets do usuário, projeto e extensões.

### Checklist de entrega

- [ ] Tabstops, placeholders aninhados, variáveis, escolhas, regex transforms, escapes e seleção substituída.
- [ ] Snippets por linguagem e globais, prefix completion, file templates e inserção pela paleta.
- [ ] Carregar language-configuration.json com comments, brackets, folding markers, indentation e onEnter; testar cancelamento e undo.

### Como executar e comprovar

1. Reproduzir o fluxo correspondente no VS Code de referência e registrar comportamento esperado.
2. Criar fixture mínima, definir contratos e detalhar casos negativos antes da implementação.
3. Implementar incrementalmente sem bloquear a UI nem executar conteúdo não confiável.
4. Comparar resultado/eventos/estado com a referência; anexar testes, captura ou benchmark.
5. Atualizar matriz de gaps e documentação; marcar concluído apenas com evidências.

**Dependências:** [#11](https://github.com/joaogabriel15/editor-code/issues/11), [EC-035](./PARITY-BACKLOG.md#ec-035).

**Fontes:** [referência 1](https://github.com/microsoft/vscode-docs/blob/81d76c22e9a4f5c63733c38e4ccedaf8c9f051bf/docs/editing/userdefinedsnippets.md) · [referência 2](https://github.com/microsoft/vscode-docs/blob/81d76c22e9a4f5c63733c38e4ccedaf8c9f051bf/api/language-extensions/language-configuration-guide.md)

<a id="ec-038"></a>
## EC-038 — Completar busca, substituição e Search Editor

[Issue #41](https://github.com/joaogabriel15/editor-code/issues/41)

**Área:** Editor · **Marco:** P1 — Experiência completa do editor · **Estado:** planejado

Paridade dos fluxos de pesquisa no documento e workspace.

### Checklist de entrega

- [ ] Regex, case, whole word, seleção, preserve case, grupos de substituição e preview antes de substituir vários arquivos.
- [ ] Includes/excludes/globs, ignores, symlinks, resultado parcial/cancelamento, encodings e arquivos não salvos.
- [ ] Search Editor persistente com contexto, rerun, navegação e integração com providers remotos/virtuais.

### Como executar e comprovar

1. Reproduzir o fluxo correspondente no VS Code de referência e registrar comportamento esperado.
2. Criar fixture mínima, definir contratos e detalhar casos negativos antes da implementação.
3. Implementar incrementalmente sem bloquear a UI nem executar conteúdo não confiável.
4. Comparar resultado/eventos/estado com a referência; anexar testes, captura ou benchmark.
5. Atualizar matriz de gaps e documentação; marcar concluído apenas com evidências.

**Dependências:** [#15](https://github.com/joaogabriel15/editor-code/issues/15), [EC-035](./PARITY-BACKLOG.md#ec-035).

**Fontes:** [referência 1](https://github.com/microsoft/vscode-docs/blob/81d76c22e9a4f5c63733c38e4ccedaf8c9f051bf/docs/editing/codebasics.md) · [referência 2](https://github.com/microsoft/vscode-docs/blob/81d76c22e9a4f5c63733c38e4ccedaf8c9f051bf/docs/editor/glob-patterns.md)

<a id="ec-039"></a>
## EC-039 — Completar Settings UI, JSONC, escopos e variáveis

[Issue #34](https://github.com/joaogabriel15/editor-code/issues/34)

**Área:** Workbench · **Marco:** P1 — Experiência completa do editor · **Estado:** planejado

Preservar a semântica das configurações em todos os escopos.

### Checklist de entrega

- [ ] UI pesquisável com defaults, alterações, reset e schemas; JSONC com comentários e diagnóstico preservados.
- [ ] Precedência default/user/profile/remote/workspace/folder/language e política; aplicar mudanças dinamicamente onde suportado.
- [ ] Resolver variáveis de configuração/input/command/environment com autorização; importar .code-workspace e validar multi-root.

### Como executar e comprovar

1. Reproduzir o fluxo correspondente no VS Code de referência e registrar comportamento esperado.
2. Criar fixture mínima, definir contratos e detalhar casos negativos antes da implementação.
3. Implementar incrementalmente sem bloquear a UI nem executar conteúdo não confiável.
4. Comparar resultado/eventos/estado com a referência; anexar testes, captura ou benchmark.
5. Atualizar matriz de gaps e documentação; marcar concluído apenas com evidências.

**Dependências:** [#9](https://github.com/joaogabriel15/editor-code/issues/9), [#12](https://github.com/joaogabriel15/editor-code/issues/12).

**Fontes:** [referência 1](https://github.com/microsoft/vscode-docs/blob/81d76c22e9a4f5c63733c38e4ccedaf8c9f051bf/docs/configure/settings.md) · [referência 2](https://github.com/microsoft/vscode-docs/blob/81d76c22e9a4f5c63733c38e4ccedaf8c9f051bf/docs/reference/variables-reference.md)

<a id="ec-040"></a>
## EC-040 — Completar keybindings, context keys, menus e comandos

[Issue #48](https://github.com/joaogabriel15/editor-code/issues/48)

**Área:** Workbench · **Marco:** P1 — Experiência completa do editor · **Estado:** planejado

Reproduzir roteamento de comandos e condições de habilitação.

### Checklist de entrega

- [ ] Chords, layouts de teclado, scan codes, remapeamento e resolução de conflitos; editor visual e gravação de atalhos.
- [ ] Avaliar when clauses, context keys e enablement; menus/submenus e ordenação de grupos.
- [ ] Enumerar comandos/default bindings por plataforma e comparar execução, foco e argumentos com baseline.

### Como executar e comprovar

1. Reproduzir o fluxo correspondente no VS Code de referência e registrar comportamento esperado.
2. Criar fixture mínima, definir contratos e detalhar casos negativos antes da implementação.
3. Implementar incrementalmente sem bloquear a UI nem executar conteúdo não confiável.
4. Comparar resultado/eventos/estado com a referência; anexar testes, captura ou benchmark.
5. Atualizar matriz de gaps e documentação; marcar concluído apenas com evidências.

**Dependências:** [#9](https://github.com/joaogabriel15/editor-code/issues/9), [EC-033](./PARITY-BACKLOG.md#ec-033).

**Fontes:** [referência 1](https://github.com/microsoft/vscode-docs/blob/81d76c22e9a4f5c63733c38e4ccedaf8c9f051bf/docs/configure/keybindings.md) · [referência 2](https://github.com/microsoft/vscode-docs/blob/81d76c22e9a4f5c63733c38e4ccedaf8c9f051bf/api/references/when-clause-contexts.md)

<a id="ec-041"></a>
## EC-041 — Implementar perfis e migração de configuração

[Issue #55](https://github.com/joaogabriel15/editor-code/issues/55)

**Área:** Workbench · **Marco:** P1 — Experiência completa do editor · **Estado:** planejado

Perfis persistentes e transportáveis de editor.

### Checklist de entrega

- [ ] Criar/copiar/exportar/importar perfis com settings, snippets, keybindings, UI e extensões; perfil temporário.
- [ ] Associar perfil a workspace, alternar sem contaminar estado e resolver importação conflitante.
- [ ] Migração do VS Code com preview, backup e relatório de itens incompatíveis; não copiar tokens nem executar extensão ao importar.

### Como executar e comprovar

1. Reproduzir o fluxo correspondente no VS Code de referência e registrar comportamento esperado.
2. Criar fixture mínima, definir contratos e detalhar casos negativos antes da implementação.
3. Implementar incrementalmente sem bloquear a UI nem executar conteúdo não confiável.
4. Comparar resultado/eventos/estado com a referência; anexar testes, captura ou benchmark.
5. Atualizar matriz de gaps e documentação; marcar concluído apenas com evidências.

**Dependências:** [EC-039](./PARITY-BACKLOG.md#ec-039), [EC-040](./PARITY-BACKLOG.md#ec-040).

**Fontes:** [referência 1](https://github.com/microsoft/vscode-docs/blob/81d76c22e9a4f5c63733c38e4ccedaf8c9f051bf/docs/configure/profiles.md)

<a id="ec-042"></a>
## EC-042 — Implementar sincronização de configurações e conflitos

[Issue #66](https://github.com/joaogabriel15/editor-code/issues/66)

**Área:** Serviços · **Marco:** P4 — Desenvolvimento remoto e web · **Estado:** planejado

Equivalência funcional de Settings Sync com backend explicitamente escolhido.

### Checklist de entrega

- [ ] Sincronizar settings, atalhos, snippets, perfis, extensões e estado suportado; conflitos, merge e rollback.
- [ ] Suportar offline, versionamento, múltiplos dispositivos, opt-in e exclusão dos dados sincronizados.
- [ ] Validar disponibilidade/termos do backend; não pressupor acesso ao serviço Microsoft; declarar incompatibilidade de conta como impedimento.

### Como executar e comprovar

1. Reproduzir o fluxo correspondente no VS Code de referência e registrar comportamento esperado.
2. Criar fixture mínima, definir contratos e detalhar casos negativos antes da implementação.
3. Implementar incrementalmente sem bloquear a UI nem executar conteúdo não confiável.
4. Comparar resultado/eventos/estado com a referência; anexar testes, captura ou benchmark.
5. Atualizar matriz de gaps e documentação; marcar concluído apenas com evidências.

**Dependências:** [EC-041](./PARITY-BACKLOG.md#ec-041), [EC-031](./PARITY-BACKLOG.md#ec-031).

**Fontes:** [referência 1](https://github.com/microsoft/vscode-docs/blob/81d76c22e9a4f5c63733c38e4ccedaf8c9f051bf/docs/configure/settings-sync.md)

<a id="ec-043"></a>
## EC-043 — Completar Explorer e operações de arquivos

[Issue #35](https://github.com/joaogabriel15/editor-code/issues/35)

**Área:** Workbench · **Marco:** P1 — Experiência completa do editor · **Estado:** planejado

Cobrir toda a interação com diretórios e arquivos.

### Checklist de entrega

- [ ] Criar/renomear/copiar/mover/deletar com trash quando disponível, drag/drop entre roots e desfazer seguro.
- [ ] Compact folders, nesting, sorting, reveal, excludes, decorations, links e Open With.
- [ ] Testar case-only rename, UNC, symlinks/junctions, permissões, path length, arquivo externo alterado e operações em lote.

### Como executar e comprovar

1. Reproduzir o fluxo correspondente no VS Code de referência e registrar comportamento esperado.
2. Criar fixture mínima, definir contratos e detalhar casos negativos antes da implementação.
3. Implementar incrementalmente sem bloquear a UI nem executar conteúdo não confiável.
4. Comparar resultado/eventos/estado com a referência; anexar testes, captura ou benchmark.
5. Atualizar matriz de gaps e documentação; marcar concluído apenas com evidências.

**Dependências:** [#14](https://github.com/joaogabriel15/editor-code/issues/14), [#7](https://github.com/joaogabriel15/editor-code/issues/7).

**Fontes:** [referência 1](https://github.com/microsoft/vscode-docs/blob/81d76c22e9a4f5c63733c38e4ccedaf8c9f051bf/docs/editing/workspaces/workspaces.md)

<a id="ec-044"></a>
## EC-044 — Completar autosave, Hot Exit, Timeline e histórico local

[Issue #42](https://github.com/joaogabriel15/editor-code/issues/42)

**Área:** Editor · **Marco:** P1 — Experiência completa do editor · **Estado:** planejado

Evitar perda de trabalho em todos os tipos de documento.

### Checklist de entrega

- [ ] Autosave por atraso/foco/janela, dirty state, backup de untitled e restauração após crash.
- [ ] Histórico local com diff/restauração, limites de retenção, exclusões e integração Timeline.
- [ ] Cobrir falha durante save, conflitos externos, vários editores do mesmo URI e migração de sessão; nunca descartar alterações silenciosamente.

### Como executar e comprovar

1. Reproduzir o fluxo correspondente no VS Code de referência e registrar comportamento esperado.
2. Criar fixture mínima, definir contratos e detalhar casos negativos antes da implementação.
3. Implementar incrementalmente sem bloquear a UI nem executar conteúdo não confiável.
4. Comparar resultado/eventos/estado com a referência; anexar testes, captura ou benchmark.
5. Atualizar matriz de gaps e documentação; marcar concluído apenas com evidências.

**Dependências:** [#7](https://github.com/joaogabriel15/editor-code/issues/7), [EC-043](./PARITY-BACKLOG.md#ec-043).

**Fontes:** [referência 1](https://github.com/microsoft/vscode-docs/blob/81d76c22e9a4f5c63733c38e4ccedaf8c9f051bf/docs/editing/codebasics.md)

<a id="ec-045"></a>
## EC-045 — Implementar filesystem virtual e identidade de URI

[Issue #36](https://github.com/joaogabriel15/editor-code/issues/36)

**Área:** Plataforma · **Marco:** P6 — Plataformas, qualidade e distribuição · **Estado:** planejado

Permitir arquivos locais, virtuais e remotos pelo mesmo contrato.

### Checklist de entrega

- [ ] Providers stat/read/write/readDirectory/watch e capabilities readonly/case-sensitive; identidade canônica de URI.
- [ ] Documentos virtuais por content provider, dirty/save/revert e eventos versionados.
- [ ] Testar custom schemes, percent encoding, Windows/Unix/UNC e provider indisponível; impedir confusão entre roots e traversal.

### Como executar e comprovar

1. Reproduzir o fluxo correspondente no VS Code de referência e registrar comportamento esperado.
2. Criar fixture mínima, definir contratos e detalhar casos negativos antes da implementação.
3. Implementar incrementalmente sem bloquear a UI nem executar conteúdo não confiável.
4. Comparar resultado/eventos/estado com a referência; anexar testes, captura ou benchmark.
5. Atualizar matriz de gaps e documentação; marcar concluído apenas com evidências.

**Dependências:** [#7](https://github.com/joaogabriel15/editor-code/issues/7), [#12](https://github.com/joaogabriel15/editor-code/issues/12).

**Fontes:** [referência 1](https://github.com/microsoft/vscode-docs/blob/81d76c22e9a4f5c63733c38e4ccedaf8c9f051bf/api/extension-guides/virtual-documents.md) · [referência 2](https://github.com/microsoft/vscode-docs/blob/81d76c22e9a4f5c63733c38e4ccedaf8c9f051bf/api/extension-guides/virtual-workspaces.md)

<a id="ec-046"></a>
## EC-046 — Completar Problems, Output, notificações e progresso

[Issue #37](https://github.com/joaogabriel15/editor-code/issues/37)

**Área:** Workbench · **Marco:** P1 — Experiência completa do editor · **Estado:** planejado

Construir feedback operacional e diagnósticos integrados.

### Checklist de entrega

- [ ] Problems com source/code/severity, filtros, navegação, ações e relação com arquivo/símbolo.
- [ ] Output/log channels com ANSI/links, níveis, rotação, busca e limite de memória.
- [ ] Notification center, modal/nonmodal actions, progress cancelável, status bar e Quick Input com acessibilidade.

### Como executar e comprovar

1. Reproduzir o fluxo correspondente no VS Code de referência e registrar comportamento esperado.
2. Criar fixture mínima, definir contratos e detalhar casos negativos antes da implementação.
3. Implementar incrementalmente sem bloquear a UI nem executar conteúdo não confiável.
4. Comparar resultado/eventos/estado com a referência; anexar testes, captura ou benchmark.
5. Atualizar matriz de gaps e documentação; marcar concluído apenas com evidências.

**Dependências:** [#8](https://github.com/joaogabriel15/editor-code/issues/8), [#17](https://github.com/joaogabriel15/editor-code/issues/17).

**Fontes:** [referência 1](https://github.com/microsoft/vscode-docs/blob/81d76c22e9a4f5c63733c38e4ccedaf8c9f051bf/api/extension-capabilities/common-capabilities.md)

<a id="ec-047"></a>
## EC-047 — Validar fidelidade completa de temas e ícones

[Issue #43](https://github.com/joaogabriel15/editor-code/issues/43)

**Área:** Temas · **Marco:** P1 — Experiência completa do editor · **Estado:** planejado

Ampliar importação básica para conformidade visual.

### Checklist de entrega

- [ ] Cobrir includes, defaults light/dark/high contrast, color references, token scopes/prioridade e semantic selectors.
- [ ] Temas de ícones de arquivo/produto, icon fonts, custom colors, overrides por tema/linguagem e OS theme changes.
- [ ] Golden screenshots e testes de scopes com temas redistribuíveis; rastrear cada token ignorado e garantir contraste acessível.

### Como executar e comprovar

1. Reproduzir o fluxo correspondente no VS Code de referência e registrar comportamento esperado.
2. Criar fixture mínima, definir contratos e detalhar casos negativos antes da implementação.
3. Implementar incrementalmente sem bloquear a UI nem executar conteúdo não confiável.
4. Comparar resultado/eventos/estado com a referência; anexar testes, captura ou benchmark.
5. Atualizar matriz de gaps e documentação; marcar concluído apenas com evidências.

**Dependências:** [#10](https://github.com/joaogabriel15/editor-code/issues/10), [#11](https://github.com/joaogabriel15/editor-code/issues/11), [#25](https://github.com/joaogabriel15/editor-code/issues/25), [EC-036](./PARITY-BACKLOG.md#ec-036).

**Fontes:** [referência 1](https://github.com/microsoft/vscode-docs/blob/81d76c22e9a4f5c63733c38e4ccedaf8c9f051bf/api/references/theme-color.md) · [referência 2](https://github.com/microsoft/vscode-docs/blob/81d76c22e9a4f5c63733c38e4ccedaf8c9f051bf/api/extension-capabilities/theming.md)

<a id="ec-048"></a>
## EC-048 — Cobrir todas as linguagens e extensões distribuídas com Code OSS

[Issue #49](https://github.com/joaogabriel15/editor-code/issues/49)

**Área:** Linguagens · **Marco:** P2 — Linguagens, Git e ferramentas · **Estado:** planejado

Transformar cada manifesto built-in em contrato de suporte explícito.

### Checklist de entrega

- [ ] Inventariar todos os manifestos do SHA fixado, seus idiomas, snippets, configurações, comandos e pontos de contribuição.
- [ ] Implementar ou adaptar gramáticas e recursos de cada pacote com licenças e fixtures por linguagem.
- [ ] Distinguir coloração de language server completo; nenhum pacote desaparece do escopo sem decisão registrada; testes internos não contam como recurso de usuário.

### Como executar e comprovar

1. Reproduzir o fluxo correspondente no VS Code de referência e registrar comportamento esperado.
2. Criar fixture mínima, definir contratos e detalhar casos negativos antes da implementação.
3. Implementar incrementalmente sem bloquear a UI nem executar conteúdo não confiável.
4. Comparar resultado/eventos/estado com a referência; anexar testes, captura ou benchmark.
5. Atualizar matriz de gaps e documentação; marcar concluído apenas com evidências.

**Dependências:** [#3](https://github.com/joaogabriel15/editor-code/issues/3), [#11](https://github.com/joaogabriel15/editor-code/issues/11), [EC-037](./PARITY-BACKLOG.md#ec-037), [EC-031](./PARITY-BACKLOG.md#ec-031).

**Fontes:** [referência 1](https://github.com/microsoft/vscode-docs/blob/81d76c22e9a4f5c63733c38e4ccedaf8c9f051bf/docs/languages/overview.md)

<a id="ec-049"></a>
## EC-049 — Completar IntelliSense e navegação semântica

[Issue #56](https://github.com/joaogabriel15/editor-code/issues/56)

**Área:** Linguagens · **Marco:** P2 — Linguagens, Git e ferramentas · **Estado:** planejado

Cobrir recursos de linguagem expostos pelo VS Code.

### Checklist de entrega

- [ ] Completion resolve/sort/filter/commit chars, signature help, hover Markdown, links e colors/color picker.
- [ ] CodeLens, inlay hints, semantic tokens full/delta/range, linked editing, highlights, folding/selection ranges e hierarquias.
- [ ] Rename, source actions, organize imports, formatting on type/save/paste e diagnostics com WorkspaceEdit versionado; cancelamento e posições UTF-16 corretos.

### Como executar e comprovar

1. Reproduzir o fluxo correspondente no VS Code de referência e registrar comportamento esperado.
2. Criar fixture mínima, definir contratos e detalhar casos negativos antes da implementação.
3. Implementar incrementalmente sem bloquear a UI nem executar conteúdo não confiável.
4. Comparar resultado/eventos/estado com a referência; anexar testes, captura ou benchmark.
5. Atualizar matriz de gaps e documentação; marcar concluído apenas com evidências.

**Dependências:** [#17](https://github.com/joaogabriel15/editor-code/issues/17), [#18](https://github.com/joaogabriel15/editor-code/issues/18), [EC-034](./PARITY-BACKLOG.md#ec-034).

**Fontes:** [referência 1](https://github.com/microsoft/vscode-docs/blob/81d76c22e9a4f5c63733c38e4ccedaf8c9f051bf/api/language-extensions/programmatic-language-features.md)

<a id="ec-050"></a>
## EC-050 — Implementar paridade JavaScript e TypeScript

[Issue #67](https://github.com/joaogabriel15/editor-code/issues/67)

**Área:** Linguagens · **Marco:** P2 — Linguagens, Git e ferramentas · **Estado:** planejado

Garantir recursos de JS/TS que não são resolvidos apenas por LSP genérico.

### Checklist de entrega

- [ ] Projetos jsconfig/tsconfig, múltiplas versões do TS, inferred projects e seleção de SDK por workspace.
- [ ] Auto imports, refactorings, rename/import updates, inlay hints, diagnóstico e plugins TypeScript.
- [ ] Testar monorepo/project references/JSX/TSX, type acquisition e crash; downloads e plugins dependem de confiança.

### Como executar e comprovar

1. Reproduzir o fluxo correspondente no VS Code de referência e registrar comportamento esperado.
2. Criar fixture mínima, definir contratos e detalhar casos negativos antes da implementação.
3. Implementar incrementalmente sem bloquear a UI nem executar conteúdo não confiável.
4. Comparar resultado/eventos/estado com a referência; anexar testes, captura ou benchmark.
5. Atualizar matriz de gaps e documentação; marcar concluído apenas com evidências.

**Dependências:** [EC-048](./PARITY-BACKLOG.md#ec-048), [EC-049](./PARITY-BACKLOG.md#ec-049).

**Fontes:** [referência 1](https://github.com/microsoft/vscode-docs/blob/81d76c22e9a4f5c63733c38e4ccedaf8c9f051bf/docs/languages/typescript.md) · [referência 2](https://github.com/microsoft/vscode-docs/blob/81d76c22e9a4f5c63733c38e4ccedaf8c9f051bf/docs/languages/javascript.md)

<a id="ec-051"></a>
## EC-051 — Implementar HTML, CSS, JSON, Emmet e schemas

[Issue #68](https://github.com/joaogabriel15/editor-code/issues/68)

**Área:** Linguagens · **Marco:** P2 — Linguagens, Git e ferramentas · **Estado:** planejado

Cobrir recursos web e de configuração distribuídos no produto.

### Checklist de entrega

- [ ] HTML/CSS/SCSS/LESS: completions, validation, color previews, linked tags e custom data.
- [ ] JSON/JSONC: schemas locais/remotos, associação de arquivos, cache offline, diagnóstico e completion.
- [ ] Emmet expansions, wrapping, mappings e snippets; tratar PHP e demais language-features built-ins conforme inventário.

### Como executar e comprovar

1. Reproduzir o fluxo correspondente no VS Code de referência e registrar comportamento esperado.
2. Criar fixture mínima, definir contratos e detalhar casos negativos antes da implementação.
3. Implementar incrementalmente sem bloquear a UI nem executar conteúdo não confiável.
4. Comparar resultado/eventos/estado com a referência; anexar testes, captura ou benchmark.
5. Atualizar matriz de gaps e documentação; marcar concluído apenas com evidências.

**Dependências:** [EC-048](./PARITY-BACKLOG.md#ec-048), [EC-049](./PARITY-BACKLOG.md#ec-049).

**Fontes:** [referência 1](https://github.com/microsoft/vscode-docs/blob/81d76c22e9a4f5c63733c38e4ccedaf8c9f051bf/docs/languages/html.md) · [referência 2](https://github.com/microsoft/vscode-docs/blob/81d76c22e9a4f5c63733c38e4ccedaf8c9f051bf/docs/languages/css.md) · [referência 3](https://github.com/microsoft/vscode-docs/blob/81d76c22e9a4f5c63733c38e4ccedaf8c9f051bf/docs/languages/json.md) · [referência 4](https://github.com/microsoft/vscode-docs/blob/81d76c22e9a4f5c63733c38e4ccedaf8c9f051bf/docs/languages/emmet.md)

<a id="ec-052"></a>
## EC-052 — Completar Markdown, mídia e previews

[Issue #81](https://github.com/joaogabriel15/editor-code/issues/81)

**Área:** Linguagens · **Marco:** P2 — Linguagens, Git e ferramentas · **Estado:** planejado

Renderizar e editar conteúdo além de texto puro.

### Checklist de entrega

- [ ] Markdown preview sincronizado/locked, links, imagens, outline, edição de links e extensão de parser/estilos.
- [ ] Math e Mermaid conforme baseline/licença; previews de imagens, SVG, áudio/vídeo com controles e fallback.
- [ ] Restringir scripts/URIs/recursos remotos e conteúdo ativo; testar preview em workspace não confiável, export e arquivos grandes.

### Como executar e comprovar

1. Reproduzir o fluxo correspondente no VS Code de referência e registrar comportamento esperado.
2. Criar fixture mínima, definir contratos e detalhar casos negativos antes da implementação.
3. Implementar incrementalmente sem bloquear a UI nem executar conteúdo não confiável.
4. Comparar resultado/eventos/estado com a referência; anexar testes, captura ou benchmark.
5. Atualizar matriz de gaps e documentação; marcar concluído apenas com evidências.

**Dependências:** [EC-048](./PARITY-BACKLOG.md#ec-048), [EC-061](./PARITY-BACKLOG.md#ec-061), [EC-062](./PARITY-BACKLOG.md#ec-062).

**Fontes:** [referência 1](https://github.com/microsoft/vscode-docs/blob/81d76c22e9a4f5c63733c38e4ccedaf8c9f051bf/docs/languages/markdown.md)

<a id="ec-053"></a>
## EC-053 — Completar Git, branches, remotes e histórico

[Issue #44](https://github.com/joaogabriel15/editor-code/issues/44)

**Área:** SCM · **Marco:** P2 — Linguagens, Git e ferramentas · **Estado:** planejado

Ir além de status/diff para o fluxo completo de versionamento.

### Checklist de entrega

- [ ] Stage/unstage por arquivo/hunk/linha, commit/amend, mensagens e hooks com progresso/erros.
- [ ] Clone/init, fetch/pull/push/sync, branches/tags, stash, worktrees, submodules e múltiplos remotes.
- [ ] Histórico/graph/blame, autenticação e assinatura suportadas; confirmar descartes/resets e testar conflitos, arquivos binários e repo grande.

### Como executar e comprovar

1. Reproduzir o fluxo correspondente no VS Code de referência e registrar comportamento esperado.
2. Criar fixture mínima, definir contratos e detalhar casos negativos antes da implementação.
3. Implementar incrementalmente sem bloquear a UI nem executar conteúdo não confiável.
4. Comparar resultado/eventos/estado com a referência; anexar testes, captura ou benchmark.
5. Atualizar matriz de gaps e documentação; marcar concluído apenas com evidências.

**Dependências:** [#16](https://github.com/joaogabriel15/editor-code/issues/16), [EC-043](./PARITY-BACKLOG.md#ec-043).

**Fontes:** [referência 1](https://github.com/microsoft/vscode-docs/blob/81d76c22e9a4f5c63733c38e4ccedaf8c9f051bf/docs/sourcecontrol/overview.md) · [referência 2](https://github.com/microsoft/vscode-docs/blob/81d76c22e9a4f5c63733c38e4ccedaf8c9f051bf/docs/sourcecontrol/branches-worktrees.md)

<a id="ec-054"></a>
## EC-054 — Completar diff, multidiff e editor de merge

[Issue #45](https://github.com/joaogabriel15/editor-code/issues/45)

**Área:** SCM · **Marco:** P2 — Linguagens, Git e ferramentas · **Estado:** planejado

Comparação e resolução de alterações em documentos.

### Checklist de entrega

- [ ] Diff inline/side-by-side, mudanças intra-linha, whitespace, linhas movidas, navegação e inclusão/exclusão de hunks.
- [ ] Merge de três vias com base/current/incoming/result, conflitos e aceitação parcial segura.
- [ ] Multidiff e documentos virtuais/readonly, undo e integração com Git/IA; binários e arquivos grandes têm fallback explícito.

### Como executar e comprovar

1. Reproduzir o fluxo correspondente no VS Code de referência e registrar comportamento esperado.
2. Criar fixture mínima, definir contratos e detalhar casos negativos antes da implementação.
3. Implementar incrementalmente sem bloquear a UI nem executar conteúdo não confiável.
4. Comparar resultado/eventos/estado com a referência; anexar testes, captura ou benchmark.
5. Atualizar matriz de gaps e documentação; marcar concluído apenas com evidências.

**Dependências:** [#16](https://github.com/joaogabriel15/editor-code/issues/16), [EC-035](./PARITY-BACKLOG.md#ec-035).

**Fontes:** [referência 1](https://github.com/microsoft/vscode-docs/blob/81d76c22e9a4f5c63733c38e4ccedaf8c9f051bf/docs/sourcecontrol/merge-conflicts.md)

<a id="ec-055"></a>
## EC-055 — Completar Tasks, problem matchers e automação de build

[Issue #57](https://github.com/joaogabriel15/editor-code/issues/57)

**Área:** Ferramentas · **Marco:** P2 — Linguagens, Git e ferramentas · **Estado:** planejado

Implementar tasks.json e providers de tarefas.

### Checklist de entrega

- [ ] Shell/process tasks, detected tasks, groups/defaults, dependencies sequenciais/paralelas, inputs e variáveis.
- [ ] Problem matchers multiline/background, reveal/presentation, terminais compartilhados/dedicados e cancelamento de árvore de processos.
- [ ] Providers npm/gulp/grunt/jake ou equivalentes do inventário; escopos OS/multi-root/remote e confiança antes de execução.

### Como executar e comprovar

1. Reproduzir o fluxo correspondente no VS Code de referência e registrar comportamento esperado.
2. Criar fixture mínima, definir contratos e detalhar casos negativos antes da implementação.
3. Implementar incrementalmente sem bloquear a UI nem executar conteúdo não confiável.
4. Comparar resultado/eventos/estado com a referência; anexar testes, captura ou benchmark.
5. Atualizar matriz de gaps e documentação; marcar concluído apenas com evidências.

**Dependências:** [#20](https://github.com/joaogabriel15/editor-code/issues/20), [EC-039](./PARITY-BACKLOG.md#ec-039), [EC-057](./PARITY-BACKLOG.md#ec-057).

**Fontes:** [referência 1](https://github.com/microsoft/vscode-docs/blob/81d76c22e9a4f5c63733c38e4ccedaf8c9f051bf/docs/debugtest/tasks.md) · [referência 2](https://github.com/microsoft/vscode-docs/blob/81d76c22e9a4f5c63733c38e4ccedaf8c9f051bf/docs/reference/tasks-appendix.md)

<a id="ec-056"></a>
## EC-056 — Completar depuração DAP e launch.json

[Issue #69](https://github.com/joaogabriel15/editor-code/issues/69)

**Área:** Ferramentas · **Marco:** P2 — Linguagens, Git e ferramentas · **Estado:** planejado

Paridade de UI e protocolo de debug por capabilities.

### Checklist de entrega

- [ ] Launch/attach/compound, conditional/function/data breakpoints, logpoints, exception filters e session lifecycle.
- [ ] Threads/call stack/scopes/watch, REPL, evaluate, source mapping, disassembly/memory quando suportado pelo adaptador.
- [ ] Pre/post tasks, serverReadyAction, child/multitarget sessions, remote attach e debug console; teste com Node e adaptador controlado.

### Como executar e comprovar

1. Reproduzir o fluxo correspondente no VS Code de referência e registrar comportamento esperado.
2. Criar fixture mínima, definir contratos e detalhar casos negativos antes da implementação.
3. Implementar incrementalmente sem bloquear a UI nem executar conteúdo não confiável.
4. Comparar resultado/eventos/estado com a referência; anexar testes, captura ou benchmark.
5. Atualizar matriz de gaps e documentação; marcar concluído apenas com evidências.

**Dependências:** [#20](https://github.com/joaogabriel15/editor-code/issues/20), [EC-049](./PARITY-BACKLOG.md#ec-049).

**Fontes:** [referência 1](https://github.com/microsoft/vscode-docs/blob/81d76c22e9a4f5c63733c38e4ccedaf8c9f051bf/docs/debugtest/debugging.md) · [referência 2](https://github.com/microsoft/vscode-docs/blob/81d76c22e9a4f5c63733c38e4ccedaf8c9f051bf/docs/debugtest/debugging-configuration.md)

<a id="ec-057"></a>
## EC-057 — Completar terminal, shell integration e persistência

[Issue #50](https://github.com/joaogabriel15/editor-code/issues/50)

**Área:** Ferramentas · **Marco:** P2 — Linguagens, Git e ferramentas · **Estado:** planejado

Terminal com a experiência completa esperada.

### Checklist de entrega

- [ ] Profiles por OS, split/tabs/editor terminal, persistência/reconexão, env collections, cwd e terminal externo.
- [ ] Shell integration: command navigation/history/decorations, links, quick fixes, sugestões e command detection.
- [ ] Busca, seleção, keybinding routing, bells/accessibility, imagens quando suportadas, fluxo intenso e terminal remoto; não executar sequências recebidas como comandos.

### Como executar e comprovar

1. Reproduzir o fluxo correspondente no VS Code de referência e registrar comportamento esperado.
2. Criar fixture mínima, definir contratos e detalhar casos negativos antes da implementação.
3. Implementar incrementalmente sem bloquear a UI nem executar conteúdo não confiável.
4. Comparar resultado/eventos/estado com a referência; anexar testes, captura ou benchmark.
5. Atualizar matriz de gaps e documentação; marcar concluído apenas com evidências.

**Dependências:** [#19](https://github.com/joaogabriel15/editor-code/issues/19), [EC-033](./PARITY-BACKLOG.md#ec-033).

**Fontes:** [referência 1](https://github.com/microsoft/vscode-docs/blob/81d76c22e9a4f5c63733c38e4ccedaf8c9f051bf/docs/terminal/advanced.md) · [referência 2](https://github.com/microsoft/vscode-docs/blob/81d76c22e9a4f5c63733c38e4ccedaf8c9f051bf/docs/terminal/shell-integration.md)

<a id="ec-058"></a>
## EC-058 — Implementar Test Explorer, execução e cobertura

[Issue #82](https://github.com/joaogabriel15/editor-code/issues/82)

**Área:** Ferramentas · **Marco:** P2 — Linguagens, Git e ferramentas · **Estado:** planejado

Integração de testes para usuários e extensões.

### Checklist de entrega

- [ ] Discovery hierárquico/lazy, run/debug profiles, tags, seleção e continuous run.
- [ ] Resultados, failure diffs, source locations, output, histórico e navegação; cancelar execuções.
- [ ] API de test controllers e coverage por arquivo/linha/branch; validar provider próprio e extensão real autorizada.

### Como executar e comprovar

1. Reproduzir o fluxo correspondente no VS Code de referência e registrar comportamento esperado.
2. Criar fixture mínima, definir contratos e detalhar casos negativos antes da implementação.
3. Implementar incrementalmente sem bloquear a UI nem executar conteúdo não confiável.
4. Comparar resultado/eventos/estado com a referência; anexar testes, captura ou benchmark.
5. Atualizar matriz de gaps e documentação; marcar concluído apenas com evidências.

**Dependências:** [#17](https://github.com/joaogabriel15/editor-code/issues/17), [EC-056](./PARITY-BACKLOG.md#ec-056), [EC-046](./PARITY-BACKLOG.md#ec-046).

**Fontes:** [referência 1](https://github.com/microsoft/vscode-docs/blob/81d76c22e9a4f5c63733c38e4ccedaf8c9f051bf/docs/debugtest/testing.md) · [referência 2](https://github.com/microsoft/vscode-docs/blob/81d76c22e9a4f5c63733c38e4ccedaf8c9f051bf/api/extension-guides/testing.md)

<a id="ec-059"></a>
## EC-059 — Implementar editor de notebooks e serialização

[Issue #51](https://github.com/joaogabriel15/editor-code/issues/51)

**Área:** Notebooks · **Marco:** P3 — Notebooks e compatibilidade de extensões · **Estado:** planejado

Documentos com células de código e Markdown.

### Checklist de entrega

- [ ] Cell insert/delete/move/join/split, seleção, folding, clipboard, undo e busca entre células.
- [ ] NotebookData/serializer preservando metadados e outputs, transient fields, save/revert/backup e dirty state.
- [ ] Diff de notebooks, múltiplos editores do mesmo documento e grandes notebooks; round-trip ipynb sem perda.

### Como executar e comprovar

1. Reproduzir o fluxo correspondente no VS Code de referência e registrar comportamento esperado.
2. Criar fixture mínima, definir contratos e detalhar casos negativos antes da implementação.
3. Implementar incrementalmente sem bloquear a UI nem executar conteúdo não confiável.
4. Comparar resultado/eventos/estado com a referência; anexar testes, captura ou benchmark.
5. Atualizar matriz de gaps e documentação; marcar concluído apenas com evidências.

**Dependências:** [#6](https://github.com/joaogabriel15/editor-code/issues/6), [EC-045](./PARITY-BACKLOG.md#ec-045), [EC-033](./PARITY-BACKLOG.md#ec-033).

**Fontes:** [referência 1](https://github.com/microsoft/vscode-docs/blob/81d76c22e9a4f5c63733c38e4ccedaf8c9f051bf/api/extension-guides/notebook.md)

<a id="ec-060"></a>
## EC-060 — Implementar kernels, outputs e integração Jupyter

[Issue #70](https://github.com/joaogabriel15/editor-code/issues/70)

**Área:** Notebooks · **Marco:** P3 — Notebooks e compatibilidade de extensões · **Estado:** planejado

Execução de notebooks e janela interativa.

### Checklist de entrega

- [ ] Controllers/kernels, seleção, execução/cancelamento/restart, ordem/estado, variables e depuração quando suportada.
- [ ] MIME renderers, streaming, imagens/HTML/widgets, renderer messaging e limites de memória/segurança.
- [ ] Kernel local/remoto Jupyter e interactive/REPL window por integração documentada; fixtures e teste de reconexão sem executar notebook não confiável.

### Como executar e comprovar

1. Reproduzir o fluxo correspondente no VS Code de referência e registrar comportamento esperado.
2. Criar fixture mínima, definir contratos e detalhar casos negativos antes da implementação.
3. Implementar incrementalmente sem bloquear a UI nem executar conteúdo não confiável.
4. Comparar resultado/eventos/estado com a referência; anexar testes, captura ou benchmark.
5. Atualizar matriz de gaps e documentação; marcar concluído apenas com evidências.

**Dependências:** [EC-059](./PARITY-BACKLOG.md#ec-059), [EC-062](./PARITY-BACKLOG.md#ec-062), [EC-049](./PARITY-BACKLOG.md#ec-049).

**Fontes:** [referência 1](https://github.com/microsoft/vscode-docs/blob/81d76c22e9a4f5c63733c38e4ccedaf8c9f051bf/docs/datascience/jupyter-notebooks.md) · [referência 2](https://github.com/microsoft/vscode-docs/blob/81d76c22e9a4f5c63733c38e4ccedaf8c9f051bf/api/extension-guides/notebook.md)

<a id="ec-061"></a>
## EC-061 — Implementar Custom Editors e resolvedores Open With

[Issue #71](https://github.com/joaogabriel15/editor-code/issues/71)

**Área:** Extensões · **Marco:** P3 — Notebooks e compatibilidade de extensões · **Estado:** planejado

Extensões devem poder editar documentos textuais ou binários.

### Checklist de entrega

- [ ] CustomTextEditorProvider/CustomEditorProvider, seleção por prioridade/glob e Open With.
- [ ] Save/saveAs/revert/backup, edits/undo/redo, múltiplas views, readonly e hot exit.
- [ ] Round-trip de binário com provider de teste; validar crash do editor customizado sem perda de conteúdo.

### Como executar e comprovar

1. Reproduzir o fluxo correspondente no VS Code de referência e registrar comportamento esperado.
2. Criar fixture mínima, definir contratos e detalhar casos negativos antes da implementação.
3. Implementar incrementalmente sem bloquear a UI nem executar conteúdo não confiável.
4. Comparar resultado/eventos/estado com a referência; anexar testes, captura ou benchmark.
5. Atualizar matriz de gaps e documentação; marcar concluído apenas com evidências.

**Dependências:** [EC-045](./PARITY-BACKLOG.md#ec-045), [EC-064](./PARITY-BACKLOG.md#ec-064).

**Fontes:** [referência 1](https://github.com/microsoft/vscode-docs/blob/81d76c22e9a4f5c63733c38e4ccedaf8c9f051bf/api/extension-guides/custom-editors.md)

<a id="ec-062"></a>
## EC-062 — Implementar webviews compatíveis com isolamento

[Issue #52](https://github.com/joaogabriel15/editor-code/issues/52)

**Área:** Extensões · **Marco:** P3 — Notebooks e compatibilidade de extensões · **Estado:** planejado

Dar suporte aos painéis HTML usados por muitas extensões.

### Checklist de entrega

- [ ] WebviewPanel/WebviewView, lifecycle, serializer, retainContext, postMessage, state e asWebviewUri.
- [ ] CSP, localResourceRoots, isolamento de origens, permissões de rede, links e restrição de navegação.
- [ ] Theming, acessibilidade, find, clipboard e remote resources; medir custo do motor web e testar extensões prioritárias sem comprometer UI nativa.

### Como executar e comprovar

1. Reproduzir o fluxo correspondente no VS Code de referência e registrar comportamento esperado.
2. Criar fixture mínima, definir contratos e detalhar casos negativos antes da implementação.
3. Implementar incrementalmente sem bloquear a UI nem executar conteúdo não confiável.
4. Comparar resultado/eventos/estado com a referência; anexar testes, captura ou benchmark.
5. Atualizar matriz de gaps e documentação; marcar concluído apenas com evidências.

**Dependências:** [#24](https://github.com/joaogabriel15/editor-code/issues/24), [EC-033](./PARITY-BACKLOG.md#ec-033).

**Fontes:** [referência 1](https://github.com/microsoft/vscode-docs/blob/81d76c22e9a4f5c63733c38e4ccedaf8c9f051bf/api/extension-guides/webview.md)

<a id="ec-063"></a>
## EC-063 — Completar host de extensões, resolução e ciclo de vida

[Issue #53](https://github.com/joaogabriel15/editor-code/issues/53)

**Área:** Extensões · **Marco:** P3 — Notebooks e compatibilidade de extensões · **Estado:** planejado

Evoluir PoC para runtime compatível.

### Checklist de entrega

- [ ] Manifest engine/platform, main/browser, dependências/packs, extensionKind, activation events e deactivate/dispose.
- [ ] RPC versionado, marshalling URI/Range/Date/binary/errors, cancelamento e ordenação de eventos.
- [ ] Node/ESM/CJS e módulos nativos por plataforma; restart/bisect/profiling; incompatibilidades claras sem mocks silenciosos.

### Como executar e comprovar

1. Reproduzir o fluxo correspondente no VS Code de referência e registrar comportamento esperado.
2. Criar fixture mínima, definir contratos e detalhar casos negativos antes da implementação.
3. Implementar incrementalmente sem bloquear a UI nem executar conteúdo não confiável.
4. Comparar resultado/eventos/estado com a referência; anexar testes, captura ou benchmark.
5. Atualizar matriz de gaps e documentação; marcar concluído apenas com evidências.

**Dependências:** [#24](https://github.com/joaogabriel15/editor-code/issues/24), [EC-032](./PARITY-BACKLOG.md#ec-032).

**Fontes:** [referência 1](https://github.com/microsoft/vscode-docs/blob/81d76c22e9a4f5c63733c38e4ccedaf8c9f051bf/api/advanced-topics/extension-host.md) · [referência 2](https://github.com/microsoft/vscode-docs/blob/81d76c22e9a4f5c63733c38e4ccedaf8c9f051bf/api/references/extension-manifest.md)

<a id="ec-064"></a>
## EC-064 — Implementar API de documentos, workspace e edições

[Issue #58](https://github.com/joaogabriel15/editor-code/issues/58)

**Área:** Extensões · **Marco:** P3 — Notebooks e compatibilidade de extensões · **Estado:** planejado

Contrato de workspace e objetos básicos da API vscode.

### Checklist de entrega

- [ ] Document/TextEditor/Selection/Range/URI, eventos de abrir/alterar/salvar/fechar e lifecycle correto.
- [ ] WorkspaceEdit text/file/notebook, file operations will/did, findFiles, watchers, configuration e folders.
- [ ] Document selectors, readonly/virtual workspace, failure handling e undo; suite diferencial com extensões de fixture.

### Como executar e comprovar

1. Reproduzir o fluxo correspondente no VS Code de referência e registrar comportamento esperado.
2. Criar fixture mínima, definir contratos e detalhar casos negativos antes da implementação.
3. Implementar incrementalmente sem bloquear a UI nem executar conteúdo não confiável.
4. Comparar resultado/eventos/estado com a referência; anexar testes, captura ou benchmark.
5. Atualizar matriz de gaps e documentação; marcar concluído apenas com evidências.

**Dependências:** [EC-063](./PARITY-BACKLOG.md#ec-063), [EC-045](./PARITY-BACKLOG.md#ec-045), [#6](https://github.com/joaogabriel15/editor-code/issues/6).

**Fontes:** [referência 1](https://code.visualstudio.com/api/references/vscode-api)

<a id="ec-065"></a>
## EC-065 — Implementar API de janela, TreeView e UX extensível

[Issue #59](https://github.com/joaogabriel15/editor-code/issues/59)

**Área:** Extensões · **Marco:** P3 — Notebooks e compatibilidade de extensões · **Estado:** planejado

Superfícies de UI acessíveis a extensões.

### Checklist de entrega

- [ ] TreeDataProvider/TreeView: reveal, seleção, drag/drop, lazy children, icons e views welcome.
- [ ] QuickPick/InputBox, dialogs, notifications, progress, status bar, tabs/tabGroups e editor decorations.
- [ ] Menu/command enablement, lifecycle/dispose e eventos; testar foco e navegação de teclado com extensão fixture.

### Como executar e comprovar

1. Reproduzir o fluxo correspondente no VS Code de referência e registrar comportamento esperado.
2. Criar fixture mínima, definir contratos e detalhar casos negativos antes da implementação.
3. Implementar incrementalmente sem bloquear a UI nem executar conteúdo não confiável.
4. Comparar resultado/eventos/estado com a referência; anexar testes, captura ou benchmark.
5. Atualizar matriz de gaps e documentação; marcar concluído apenas com evidências.

**Dependências:** [EC-063](./PARITY-BACKLOG.md#ec-063), [EC-033](./PARITY-BACKLOG.md#ec-033), [EC-040](./PARITY-BACKLOG.md#ec-040), [EC-046](./PARITY-BACKLOG.md#ec-046).

**Fontes:** [referência 1](https://github.com/microsoft/vscode-docs/blob/81d76c22e9a4f5c63733c38e4ccedaf8c9f051bf/api/extension-guides/tree-view.md) · [referência 2](https://github.com/microsoft/vscode-docs/blob/81d76c22e9a4f5c63733c38e4ccedaf8c9f051bf/api/extension-capabilities/extending-workbench.md)

<a id="ec-066"></a>
## EC-066 — Implementar API de providers de linguagem

[Issue #72](https://github.com/joaogabriel15/editor-code/issues/72)

**Área:** Extensões · **Marco:** P3 — Notebooks e compatibilidade de extensões · **Estado:** planejado

Registrar providers de linguagem diretamente sem exigir LSP.

### Checklist de entrega

- [ ] Cobrir todos os registros/exportações do namespace languages do baseline e seus tipos.
- [ ] Ordenação por selector, múltiplos providers, resolve/lazy, cancelamento e retorno parcial.
- [ ] Testar providers de completion, semantic tokens, formatting, refactor, inlay/code lens e inline completion; não confundir assinatura com semântica.

### Como executar e comprovar

1. Reproduzir o fluxo correspondente no VS Code de referência e registrar comportamento esperado.
2. Criar fixture mínima, definir contratos e detalhar casos negativos antes da implementação.
3. Implementar incrementalmente sem bloquear a UI nem executar conteúdo não confiável.
4. Comparar resultado/eventos/estado com a referência; anexar testes, captura ou benchmark.
5. Atualizar matriz de gaps e documentação; marcar concluído apenas com evidências.

**Dependências:** [EC-063](./PARITY-BACKLOG.md#ec-063), [EC-049](./PARITY-BACKLOG.md#ec-049).

**Fontes:** [referência 1](https://github.com/microsoft/vscode-docs/blob/81d76c22e9a4f5c63733c38e4ccedaf8c9f051bf/api/language-extensions/programmatic-language-features.md)

<a id="ec-067"></a>
## EC-067 — Implementar APIs de tarefas, debug, SCM, testes e notebooks

[Issue #87](https://github.com/joaogabriel15/editor-code/issues/87)

**Área:** Extensões · **Marco:** P3 — Notebooks e compatibilidade de extensões · **Estado:** planejado

Expor serviços especializados ao runtime de extensões.

### Checklist de entrega

- [ ] TaskProvider, DebugAdapter/Configuration providers e SourceControl/ResourceGroup com comportamento completo do baseline.
- [ ] Test controllers/profiles/coverage e NotebookSerializer/Controller/Renderer com lifecycle e cancelamento.
- [ ] Conformance fixtures por namespace; registrar toda API sem implementação como lacuna, sem retornar sucesso falso.

### Como executar e comprovar

1. Reproduzir o fluxo correspondente no VS Code de referência e registrar comportamento esperado.
2. Criar fixture mínima, definir contratos e detalhar casos negativos antes da implementação.
3. Implementar incrementalmente sem bloquear a UI nem executar conteúdo não confiável.
4. Comparar resultado/eventos/estado com a referência; anexar testes, captura ou benchmark.
5. Atualizar matriz de gaps e documentação; marcar concluído apenas com evidências.

**Dependências:** [EC-063](./PARITY-BACKLOG.md#ec-063), [EC-055](./PARITY-BACKLOG.md#ec-055), [EC-056](./PARITY-BACKLOG.md#ec-056), [EC-058](./PARITY-BACKLOG.md#ec-058), [EC-059](./PARITY-BACKLOG.md#ec-059).

**Fontes:** [referência 1](https://code.visualstudio.com/api/references/vscode-api)

<a id="ec-068"></a>
## EC-068 — Implementar autenticação, SecretStorage e ambiente

[Issue #60](https://github.com/joaogabriel15/editor-code/issues/60)

**Área:** Extensões · **Marco:** P3 — Notebooks e compatibilidade de extensões · **Estado:** planejado

Sessões e ambiente de execução compatíveis.

### Checklist de entrega

- [ ] AuthenticationProvider/session change/getSession, consentimento de scopes e contas múltiplas.
- [ ] SecretStorage no cofre do OS, Memento/global/workspace storage, URI handlers e external URI resolution.
- [ ] env/l10n/clipboard/openExternal, proxy/telemetry flags; expiração/revogação e ausência de vazamento em logs/sync.

### Como executar e comprovar

1. Reproduzir o fluxo correspondente no VS Code de referência e registrar comportamento esperado.
2. Criar fixture mínima, definir contratos e detalhar casos negativos antes da implementação.
3. Implementar incrementalmente sem bloquear a UI nem executar conteúdo não confiável.
4. Comparar resultado/eventos/estado com a referência; anexar testes, captura ou benchmark.
5. Atualizar matriz de gaps e documentação; marcar concluído apenas com evidências.

**Dependências:** [EC-063](./PARITY-BACKLOG.md#ec-063), [#26](https://github.com/joaogabriel15/editor-code/issues/26).

**Fontes:** [referência 1](https://code.visualstudio.com/api/references/vscode-api)

<a id="ec-069"></a>
## EC-069 — Completar contribution points e activation events

[Issue #61](https://github.com/joaogabriel15/editor-code/issues/61)

**Área:** Extensões · **Marco:** P3 — Notebooks e compatibilidade de extensões · **Estado:** planejado

Interpretar contribuições declarativas do package.json.

### Checklist de entrega

- [ ] Cobrir cada contribution point estável e activation event do inventário com schema/defaults/erros.
- [ ] Incluir menus/views/themes/grammars/languages/debug/tasks/notebooks/auth/chat e contribuições compostas.
- [ ] Autoactivation, when contexts, localization de manifesto e reload; distinguir propostas/deprecadas e manter testes por entrada.

### Como executar e comprovar

1. Reproduzir o fluxo correspondente no VS Code de referência e registrar comportamento esperado.
2. Criar fixture mínima, definir contratos e detalhar casos negativos antes da implementação.
3. Implementar incrementalmente sem bloquear a UI nem executar conteúdo não confiável.
4. Comparar resultado/eventos/estado com a referência; anexar testes, captura ou benchmark.
5. Atualizar matriz de gaps e documentação; marcar concluído apenas com evidências.

**Dependências:** [EC-032](./PARITY-BACKLOG.md#ec-032), [EC-063](./PARITY-BACKLOG.md#ec-063), [EC-040](./PARITY-BACKLOG.md#ec-040), [EC-047](./PARITY-BACKLOG.md#ec-047).

**Fontes:** [referência 1](https://github.com/microsoft/vscode-docs/blob/81d76c22e9a4f5c63733c38e4ccedaf8c9f051bf/api/references/contribution-points.md) · [referência 2](https://github.com/microsoft/vscode-docs/blob/81d76c22e9a4f5c63733c38e4ccedaf8c9f051bf/api/references/activation-events.md)

<a id="ec-070"></a>
## EC-070 — Completar gerenciamento, catálogo e atualização de extensões

[Issue #73](https://github.com/joaogabriel15/editor-code/issues/73)

**Área:** Extensões · **Marco:** P3 — Notebooks e compatibilidade de extensões · **Estado:** planejado

Experiência de instalar e manter extensões.

### Checklist de entrega

- [ ] Busca/filtros/detalhes, install/uninstall/enable/disable por profile/workspace, pin/pre-release/rollback e dependencies/packs.
- [ ] VSIX local/offline, assinaturas/integridade, compatibilidade OS/arch/engine, cache e atualizações controladas.
- [ ] Validar catálogo e termos; não reutilizar Marketplace sem autorização; recommendations/unwanted e workspace trust explicados.

### Como executar e comprovar

1. Reproduzir o fluxo correspondente no VS Code de referência e registrar comportamento esperado.
2. Criar fixture mínima, definir contratos e detalhar casos negativos antes da implementação.
3. Implementar incrementalmente sem bloquear a UI nem executar conteúdo não confiável.
4. Comparar resultado/eventos/estado com a referência; anexar testes, captura ou benchmark.
5. Atualizar matriz de gaps e documentação; marcar concluído apenas com evidências.

**Dependências:** [#25](https://github.com/joaogabriel15/editor-code/issues/25), [EC-063](./PARITY-BACKLOG.md#ec-063), [EC-068](./PARITY-BACKLOG.md#ec-068).

**Fontes:** [referência 1](https://github.com/microsoft/vscode-docs/blob/81d76c22e9a4f5c63733c38e4ccedaf8c9f051bf/docs/configure/extensions/extension-marketplace.md)

<a id="ec-071"></a>
## EC-071 — Implementar desenvolvimento e depuração de extensões

[Issue #83](https://github.com/joaogabriel15/editor-code/issues/83)

**Área:** Extensões · **Marco:** P3 — Notebooks e compatibilidade de extensões · **Estado:** planejado

Permitir criar e testar extensões no próprio editor.

### Checklist de entrega

- [ ] Extension Development Host, extensionDevelopmentPath/test paths, reload e debugger breakpoints.
- [ ] Ferramentas para inspecionar contexts/tokens/themes, logs/profiling e execução de suite de API.
- [ ] Pacote fixture executa no baseline e no Editor Code; produzir relatório de diferenças por chamada.

### Como executar e comprovar

1. Reproduzir o fluxo correspondente no VS Code de referência e registrar comportamento esperado.
2. Criar fixture mínima, definir contratos e detalhar casos negativos antes da implementação.
3. Implementar incrementalmente sem bloquear a UI nem executar conteúdo não confiável.
4. Comparar resultado/eventos/estado com a referência; anexar testes, captura ou benchmark.
5. Atualizar matriz de gaps e documentação; marcar concluído apenas com evidências.

**Dependências:** [EC-063](./PARITY-BACKLOG.md#ec-063), [EC-056](./PARITY-BACKLOG.md#ec-056), [EC-069](./PARITY-BACKLOG.md#ec-069).

**Fontes:** [referência 1](https://github.com/microsoft/vscode-docs/blob/81d76c22e9a4f5c63733c38e4ccedaf8c9f051bf/api/get-started/your-first-extension.md) · [referência 2](https://github.com/microsoft/vscode-docs/blob/81d76c22e9a4f5c63733c38e4ccedaf8c9f051bf/api/working-with-extensions/testing-extension.md)

<a id="ec-072"></a>
## EC-072 — Controlar APIs propostas e evolução do upstream

[Issue #62](https://github.com/joaogabriel15/editor-code/issues/62)

**Área:** Governança · **Marco:** P0 — Contrato, inventário e auditoria de paridade · **Estado:** planejado

Não perder recursos usados por extensões modernas.

### Checklist de entrega

- [ ] Inventariar todos os vscode.proposed.*.d.ts com revisão e clientes consumidores.
- [ ] Habilitação explícita por versão/extensão; adapter ou impedimento para cada proposta necessária.
- [ ] Upgrade comparado com release notes e testes; APIs propostas não recebem garantia de estabilidade.

### Como executar e comprovar

1. Reproduzir o fluxo correspondente no VS Code de referência e registrar comportamento esperado.
2. Criar fixture mínima, definir contratos e detalhar casos negativos antes da implementação.
3. Implementar incrementalmente sem bloquear a UI nem executar conteúdo não confiável.
4. Comparar resultado/eventos/estado com a referência; anexar testes, captura ou benchmark.
5. Atualizar matriz de gaps e documentação; marcar concluído apenas com evidências.

**Dependências:** [EC-032](./PARITY-BACKLOG.md#ec-032), [EC-063](./PARITY-BACKLOG.md#ec-063).

**Fontes:** [referência 1](https://github.com/microsoft/vscode-docs/blob/81d76c22e9a4f5c63733c38e4ccedaf8c9f051bf/api/advanced-topics/using-proposed-api.md)

<a id="ec-073"></a>
## EC-073 — Implementar comentários, revisão e compartilhamento

[Issue #74](https://github.com/joaogabriel15/editor-code/issues/74)

**Área:** SCM · **Marco:** P2 — Linguagens, Git e ferramentas · **Estado:** planejado

APIs e UI usadas em revisão de código.

### Checklist de entrega

- [ ] Comment controllers/threads/ranges, reply/edit/delete/resolve, reactions quando suportadas e navegação.
- [ ] Comentários em diff, arquivos virtuais, badges/painel e ações de provider.
- [ ] Share providers e links com consentimento; integrar PR/issue via provider documentado sem publicar conteúdo automaticamente.

### Como executar e comprovar

1. Reproduzir o fluxo correspondente no VS Code de referência e registrar comportamento esperado.
2. Criar fixture mínima, definir contratos e detalhar casos negativos antes da implementação.
3. Implementar incrementalmente sem bloquear a UI nem executar conteúdo não confiável.
4. Comparar resultado/eventos/estado com a referência; anexar testes, captura ou benchmark.
5. Atualizar matriz de gaps e documentação; marcar concluído apenas com evidências.

**Dependências:** [EC-065](./PARITY-BACKLOG.md#ec-065), [EC-054](./PARITY-BACKLOG.md#ec-054).

**Fontes:** [referência 1](https://code.visualstudio.com/api/references/vscode-api) · [referência 2](https://github.com/microsoft/vscode-docs/blob/81d76c22e9a4f5c63733c38e4ccedaf8c9f051bf/docs/sourcecontrol/github.md)

<a id="ec-074"></a>
## EC-074 — Criar servidor remoto próprio e RPC resiliente

[Issue #63](https://github.com/joaogabriel15/editor-code/issues/63)

**Área:** Remoto · **Marco:** P4 — Desenvolvimento remoto e web · **Estado:** planejado

Base para separar interface local e serviços remotos.

### Checklist de entrega

- [ ] Handshake/version/capabilities, autenticação, transporte seguro e multiplexação de arquivos/terminal/LSP/extensões.
- [ ] ExtensionKind local/remote/web, URI mapping, reconexão, cancelamento e backpressure.
- [ ] Instalação/upgrade/cleanup do servidor próprio; não redistribuir servidor Microsoft sem direito; testes de rede lenta e queda.

### Como executar e comprovar

1. Reproduzir o fluxo correspondente no VS Code de referência e registrar comportamento esperado.
2. Criar fixture mínima, definir contratos e detalhar casos negativos antes da implementação.
3. Implementar incrementalmente sem bloquear a UI nem executar conteúdo não confiável.
4. Comparar resultado/eventos/estado com a referência; anexar testes, captura ou benchmark.
5. Atualizar matriz de gaps e documentação; marcar concluído apenas com evidências.

**Dependências:** [EC-045](./PARITY-BACKLOG.md#ec-045), [EC-063](./PARITY-BACKLOG.md#ec-063), [#13](https://github.com/joaogabriel15/editor-code/issues/13).

**Fontes:** [referência 1](https://github.com/microsoft/vscode-docs/blob/81d76c22e9a4f5c63733c38e4ccedaf8c9f051bf/docs/remote/remote-overview.md)

<a id="ec-075"></a>
## EC-075 — Implementar desenvolvimento por SSH

[Issue #75](https://github.com/joaogabriel15/editor-code/issues/75)

**Área:** Remoto · **Marco:** P4 — Desenvolvimento remoto e web · **Estado:** planejado

Abrir pastas e executar ferramentas em hosts SSH.

### Checklist de entrega

- [ ] SSH config, keys/agent/jump hosts e fingerprint verification; instalação e diagnóstico do servidor.
- [ ] Abrir workspace remoto, terminal, Git, debug, port forwarding e extensões remotas.
- [ ] Reconexão, host offline, múltiplos hosts/OS suportados, proxy e caminhos com espaços; sem copiar segredos.

### Como executar e comprovar

1. Reproduzir o fluxo correspondente no VS Code de referência e registrar comportamento esperado.
2. Criar fixture mínima, definir contratos e detalhar casos negativos antes da implementação.
3. Implementar incrementalmente sem bloquear a UI nem executar conteúdo não confiável.
4. Comparar resultado/eventos/estado com a referência; anexar testes, captura ou benchmark.
5. Atualizar matriz de gaps e documentação; marcar concluído apenas com evidências.

**Dependências:** [EC-074](./PARITY-BACKLOG.md#ec-074), [EC-068](./PARITY-BACKLOG.md#ec-068).

**Fontes:** [referência 1](https://github.com/microsoft/vscode-docs/blob/81d76c22e9a4f5c63733c38e4ccedaf8c9f051bf/docs/remote/ssh.md)

<a id="ec-076"></a>
## EC-076 — Implementar integração WSL

[Issue #76](https://github.com/joaogabriel15/editor-code/issues/76)

**Área:** Remoto · **Marco:** P4 — Desenvolvimento remoto e web · **Estado:** planejado

Experiência Windows com workspace e ferramentas no Linux.

### Checklist de entrega

- [ ] Descobrir distribuições, abrir folder e iniciar servidor na distribuição escolhida.
- [ ] URI/path mapping Windows/Linux/UNC, terminal, Git/LSP/debug e permissões.
- [ ] Testar WSL reiniciado, distros múltiplas, filesystems diferentes, clipboard e encerramento limpo.

### Como executar e comprovar

1. Reproduzir o fluxo correspondente no VS Code de referência e registrar comportamento esperado.
2. Criar fixture mínima, definir contratos e detalhar casos negativos antes da implementação.
3. Implementar incrementalmente sem bloquear a UI nem executar conteúdo não confiável.
4. Comparar resultado/eventos/estado com a referência; anexar testes, captura ou benchmark.
5. Atualizar matriz de gaps e documentação; marcar concluído apenas com evidências.

**Dependências:** [EC-074](./PARITY-BACKLOG.md#ec-074), [EC-057](./PARITY-BACKLOG.md#ec-057).

**Fontes:** [referência 1](https://github.com/microsoft/vscode-docs/blob/81d76c22e9a4f5c63733c38e4ccedaf8c9f051bf/docs/remote/wsl.md)

<a id="ec-077"></a>
## EC-077 — Implementar Dev Containers e lifecycle

[Issue #77](https://github.com/joaogabriel15/editor-code/issues/77)

**Área:** Remoto · **Marco:** P4 — Desenvolvimento remoto e web · **Estado:** planejado

Desenvolver em contêineres conforme configuração do projeto.

### Checklist de entrega

- [ ] Ler devcontainer.json, build/image/compose, features, mounts/users/env e lifecycle commands com confiança.
- [ ] Reopen/rebuild/attach e persistência, extensões/ports/tasks no container.
- [ ] Validar motores locais/remotos, rebuild falho e limpeza; cumprir especificação e licença da implementação utilizada.

### Como executar e comprovar

1. Reproduzir o fluxo correspondente no VS Code de referência e registrar comportamento esperado.
2. Criar fixture mínima, definir contratos e detalhar casos negativos antes da implementação.
3. Implementar incrementalmente sem bloquear a UI nem executar conteúdo não confiável.
4. Comparar resultado/eventos/estado com a referência; anexar testes, captura ou benchmark.
5. Atualizar matriz de gaps e documentação; marcar concluído apenas com evidências.

**Dependências:** [EC-074](./PARITY-BACKLOG.md#ec-074), [EC-055](./PARITY-BACKLOG.md#ec-055).

**Fontes:** [referência 1](https://github.com/microsoft/vscode-docs/blob/81d76c22e9a4f5c63733c38e4ccedaf8c9f051bf/docs/devcontainers/containers.md)

<a id="ec-078"></a>
## EC-078 — Implementar portas, túneis e cloud workspaces

[Issue #84](https://github.com/joaogabriel15/editor-code/issues/84)

**Área:** Remoto · **Marco:** P4 — Desenvolvimento remoto e web · **Estado:** planejado

Cobrir acesso remoto sem assumir serviços proprietários.

### Checklist de entrega

- [ ] Forwarding manual/automático, labels/protocols/visibility e autorização antes de exposição pública.
- [ ] Resolver túneis e cloud workspace providers por interface documentada, com reconexão e gestão de sessões.
- [ ] Avaliar Codespaces/Remote Tunnels separadamente; fornecer equivalência própria ou registrar bloqueio de serviço com impacto de paridade.

### Como executar e comprovar

1. Reproduzir o fluxo correspondente no VS Code de referência e registrar comportamento esperado.
2. Criar fixture mínima, definir contratos e detalhar casos negativos antes da implementação.
3. Implementar incrementalmente sem bloquear a UI nem executar conteúdo não confiável.
4. Comparar resultado/eventos/estado com a referência; anexar testes, captura ou benchmark.
5. Atualizar matriz de gaps e documentação; marcar concluído apenas com evidências.

**Dependências:** [EC-074](./PARITY-BACKLOG.md#ec-074), [EC-075](./PARITY-BACKLOG.md#ec-075).

**Fontes:** [referência 1](https://github.com/microsoft/vscode-docs/blob/81d76c22e9a4f5c63733c38e4ccedaf8c9f051bf/docs/debugtest/port-forwarding.md) · [referência 2](https://github.com/microsoft/vscode-docs/blob/81d76c22e9a4f5c63733c38e4ccedaf8c9f051bf/docs/remote/tunnels.md) · [referência 3](https://github.com/microsoft/vscode-docs/blob/81d76c22e9a4f5c63733c38e4ccedaf8c9f051bf/docs/remote/codespaces.md)

<a id="ec-079"></a>
## EC-079 — Planejar e implementar cliente web e extensões web

[Issue #78](https://github.com/joaogabriel15/editor-code/issues/78)

**Área:** Remoto · **Marco:** P4 — Desenvolvimento remoto e web · **Estado:** planejado

Incluir o cenário VS Code for the Web no contrato.

### Checklist de entrega

- [ ] ADR de frontend web/WASM e separação de capabilities do desktop; protótipo de edição e persistência.
- [ ] WebWorker extension host/browser entrypoint, filesystem browser e remote compute sem presumir Node local.
- [ ] Teste offline/reconnect, browser permissions e diferença desktop/web documentada; orçamento de memória separado.

### Como executar e comprovar

1. Reproduzir o fluxo correspondente no VS Code de referência e registrar comportamento esperado.
2. Criar fixture mínima, definir contratos e detalhar casos negativos antes da implementação.
3. Implementar incrementalmente sem bloquear a UI nem executar conteúdo não confiável.
4. Comparar resultado/eventos/estado com a referência; anexar testes, captura ou benchmark.
5. Atualizar matriz de gaps e documentação; marcar concluído apenas com evidências.

**Dependências:** [EC-063](./PARITY-BACKLOG.md#ec-063), [EC-074](./PARITY-BACKLOG.md#ec-074), [EC-031](./PARITY-BACKLOG.md#ec-031).

**Fontes:** [referência 1](https://github.com/microsoft/vscode-docs/blob/81d76c22e9a4f5c63733c38e4ccedaf8c9f051bf/docs/remote/vscode-web.md) · [referência 2](https://github.com/microsoft/vscode-docs/blob/81d76c22e9a4f5c63733c38e4ccedaf8c9f051bf/api/extension-guides/web-extensions.md)

<a id="ec-080"></a>
## EC-080 — Implementar navegador integrado e ferramentas de preview

[Issue #88](https://github.com/joaogabriel15/editor-code/issues/88)

**Área:** Ferramentas · **Marco:** P2 — Linguagens, Git e ferramentas · **Estado:** planejado

Navegação de aplicações locais integrada ao desenvolvimento.

### Checklist de entrega

- [ ] URL bar, history, back/forward/reload, devtools e isolamento por sessão quando suportados.
- [ ] Preview local com portas remotas, links e visualização em painéis; no mínimo equivalência dos fluxos do baseline.
- [ ] Acesso por agentes requer permissões específicas; proteger credenciais/cookies e impedir navegação automática não autorizada.

### Como executar e comprovar

1. Reproduzir o fluxo correspondente no VS Code de referência e registrar comportamento esperado.
2. Criar fixture mínima, definir contratos e detalhar casos negativos antes da implementação.
3. Implementar incrementalmente sem bloquear a UI nem executar conteúdo não confiável.
4. Comparar resultado/eventos/estado com a referência; anexar testes, captura ou benchmark.
5. Atualizar matriz de gaps e documentação; marcar concluído apenas com evidências.

**Dependências:** [EC-062](./PARITY-BACKLOG.md#ec-062), [EC-078](./PARITY-BACKLOG.md#ec-078).

**Fontes:** [referência 1](https://github.com/microsoft/vscode-docs/blob/81d76c22e9a4f5c63733c38e4ccedaf8c9f051bf/docs/debugtest/integrated-browser.md)

<a id="ec-081"></a>
## EC-081 — Completar chat, inline chat e sugestões de IA

[Issue #85](https://github.com/joaogabriel15/editor-code/issues/85)

**Área:** IA · **Marco:** P5 — IA, agentes e automações · **Estado:** planejado

Mapear a UX de IA por capacidades, não apenas um painel de texto.

### Checklist de entrega

- [ ] Streaming/cancel/retry, histórico, seleção de modelos/providers, contexto por arquivo/seleção/imagem e referências.
- [ ] Inline chat, quick chat, ghost text, next-edit suggestions e aceitação parcial conforme suporte real do provider.
- [ ] Ask/edit/agent e smart actions com custos/erros/limites; testar conflitos e nunca simular capacidade indisponível.

### Como executar e comprovar

1. Reproduzir o fluxo correspondente no VS Code de referência e registrar comportamento esperado.
2. Criar fixture mínima, definir contratos e detalhar casos negativos antes da implementação.
3. Implementar incrementalmente sem bloquear a UI nem executar conteúdo não confiável.
4. Comparar resultado/eventos/estado com a referência; anexar testes, captura ou benchmark.
5. Atualizar matriz de gaps e documentação; marcar concluído apenas com evidências.

**Dependências:** [#21](https://github.com/joaogabriel15/editor-code/issues/21), [#22](https://github.com/joaogabriel15/editor-code/issues/22), [#23](https://github.com/joaogabriel15/editor-code/issues/23), [EC-066](./PARITY-BACKLOG.md#ec-066).

**Fontes:** [referência 1](https://github.com/microsoft/vscode-docs/blob/81d76c22e9a4f5c63733c38e4ccedaf8c9f051bf/docs/chat/chat-overview.md) · [referência 2](https://github.com/microsoft/vscode-docs/blob/81d76c22e9a4f5c63733c38e4ccedaf8c9f051bf/docs/chat/inline-chat.md) · [referência 3](https://github.com/microsoft/vscode-docs/blob/81d76c22e9a4f5c63733c38e4ccedaf8c9f051bf/docs/editing/ai-powered-suggestions.md)

<a id="ec-082"></a>
## EC-082 — Implementar sessões persistentes de agentes e worktrees

[Issue #89](https://github.com/joaogabriel15/editor-code/issues/89)

**Área:** IA · **Marco:** P5 — IA, agentes e automações · **Estado:** planejado

Orquestrar sessões locais, background e remotas.

### Checklist de entrega

- [ ] Sessões persistentes, retomar/forkar/handoff quando suportados, diff/review e aplicação de commits entre worktrees.
- [ ] Janela de agentes, lista/status/filtros, artifacts, subagentes e isolamento de contexto por workspace.
- [ ] Agendamentos/automations com cancelamento e política de notificações; servidores/harnesses anunciados por capabilities e recuperação de crash.

### Como executar e comprovar

1. Reproduzir o fluxo correspondente no VS Code de referência e registrar comportamento esperado.
2. Criar fixture mínima, definir contratos e detalhar casos negativos antes da implementação.
3. Implementar incrementalmente sem bloquear a UI nem executar conteúdo não confiável.
4. Comparar resultado/eventos/estado com a referência; anexar testes, captura ou benchmark.
5. Atualizar matriz de gaps e documentação; marcar concluído apenas com evidências.

**Dependências:** [EC-081](./PARITY-BACKLOG.md#ec-081), [EC-053](./PARITY-BACKLOG.md#ec-053), [EC-074](./PARITY-BACKLOG.md#ec-074).

**Fontes:** [referência 1](https://github.com/microsoft/vscode-docs/blob/81d76c22e9a4f5c63733c38e4ccedaf8c9f051bf/docs/agents/overview.md)

<a id="ec-083"></a>
## EC-083 — Implementar instruções, prompts, skills, hooks e agentes customizados

[Issue #90](https://github.com/joaogabriel15/editor-code/issues/90)

**Área:** IA · **Marco:** P5 — IA, agentes e automações · **Estado:** planejado

Customização de agentes compatível com formatos do baseline.

### Checklist de entrega

- [ ] Descoberta, escopo e precedência de arquivos de instrução/prompt/agent/skill, com seleção contextual.
- [ ] Hooks/tool sets/plugins versionados e editor/validação de configuração.
- [ ] Conteúdo do repo não concede permissões; explicitar origem e consentimento de execução, erros e diagnóstico de conflitos.

### Como executar e comprovar

1. Reproduzir o fluxo correspondente no VS Code de referência e registrar comportamento esperado.
2. Criar fixture mínima, definir contratos e detalhar casos negativos antes da implementação.
3. Implementar incrementalmente sem bloquear a UI nem executar conteúdo não confiável.
4. Comparar resultado/eventos/estado com a referência; anexar testes, captura ou benchmark.
5. Atualizar matriz de gaps e documentação; marcar concluído apenas com evidências.

**Dependências:** [EC-081](./PARITY-BACKLOG.md#ec-081), [#26](https://github.com/joaogabriel15/editor-code/issues/26).

**Fontes:** [referência 1](https://github.com/microsoft/vscode-docs/blob/81d76c22e9a4f5c63733c38e4ccedaf8c9f051bf/docs/agent-customization/custom-instructions.md) · [referência 2](https://github.com/microsoft/vscode-docs/blob/81d76c22e9a4f5c63733c38e4ccedaf8c9f051bf/docs/agent-customization/agent-skills.md) · [referência 3](https://github.com/microsoft/vscode-docs/blob/81d76c22e9a4f5c63733c38e4ccedaf8c9f051bf/docs/agent-customization/hooks.md)

<a id="ec-084"></a>
## EC-084 — Implementar MCP e APIs de ferramentas/modelos de linguagem

[Issue #91](https://github.com/joaogabriel15/editor-code/issues/91)

**Área:** IA · **Marco:** P5 — IA, agentes e automações · **Estado:** planejado

Extensibilidade de IA e servidores MCP.

### Checklist de entrega

- [ ] Transporte/configuração, autenticação, discovery, tools/resources/prompts e lifecycle com cancelamento.
- [ ] API chat/lm, participants/tools/providers e contribution points; schema validation e streaming de resultados.
- [ ] Trust/approvals, limites de payload, logging sanitizado e reconnect; testes com servidor local fixture sem acesso externo.

### Como executar e comprovar

1. Reproduzir o fluxo correspondente no VS Code de referência e registrar comportamento esperado.
2. Criar fixture mínima, definir contratos e detalhar casos negativos antes da implementação.
3. Implementar incrementalmente sem bloquear a UI nem executar conteúdo não confiável.
4. Comparar resultado/eventos/estado com a referência; anexar testes, captura ou benchmark.
5. Atualizar matriz de gaps e documentação; marcar concluído apenas com evidências.

**Dependências:** [EC-068](./PARITY-BACKLOG.md#ec-068), [EC-081](./PARITY-BACKLOG.md#ec-081), [EC-069](./PARITY-BACKLOG.md#ec-069).

**Fontes:** [referência 1](https://github.com/microsoft/vscode-docs/blob/81d76c22e9a4f5c63733c38e4ccedaf8c9f051bf/docs/agent-customization/mcp-servers.md) · [referência 2](https://github.com/microsoft/vscode-docs/blob/81d76c22e9a4f5c63733c38e4ccedaf8c9f051bf/api/extension-guides/ai/ai-extensibility-overview.md)

<a id="ec-085"></a>
## EC-085 — Completar permissões de agentes, revisão e rollback

[Issue #92](https://github.com/joaogabriel15/editor-code/issues/92)

**Área:** IA · **Marco:** P5 — IA, agentes e automações · **Estado:** planejado

Controlar ações de ferramentas e mudanças feitas por agentes.

### Checklist de entrega

- [ ] Permissões por ação/sessão/workspace, execução terminal/rede/arquivos e prevenção de escapes de diretório.
- [ ] Preview/reject/accept parcial, checkpoints, undo e conflito com edição humana em paralelo.
- [ ] Auditar ferramentas e contexto enviado sem segredos; prompt injection não altera autoridade; validar cancelamento no meio de operações.

### Como executar e comprovar

1. Reproduzir o fluxo correspondente no VS Code de referência e registrar comportamento esperado.
2. Criar fixture mínima, definir contratos e detalhar casos negativos antes da implementação.
3. Implementar incrementalmente sem bloquear a UI nem executar conteúdo não confiável.
4. Comparar resultado/eventos/estado com a referência; anexar testes, captura ou benchmark.
5. Atualizar matriz de gaps e documentação; marcar concluído apenas com evidências.

**Dependências:** [#26](https://github.com/joaogabriel15/editor-code/issues/26), [EC-054](./PARITY-BACKLOG.md#ec-054), [EC-081](./PARITY-BACKLOG.md#ec-081).

**Fontes:** [referência 1](https://github.com/microsoft/vscode-docs/blob/81d76c22e9a4f5c63733c38e4ccedaf8c9f051bf/docs/agents/overview.md)

<a id="ec-086"></a>
## EC-086 — Implementar voz, sinais de acessibilidade e entradas multimodais

[Issue #93](https://github.com/joaogabriel15/editor-code/issues/93)

**Área:** Acessibilidade · **Marco:** P6 — Plataformas, qualidade e distribuição · **Estado:** planejado

Cobrir recursos de interação que extrapolam teclado/mouse.

### Checklist de entrega

- [ ] Speech-to-text/text-to-speech por provider autorizado, start/stop visível, idioma e modo offline quando disponível.
- [ ] Accessible view, sinais sonoros, announcements e navegação de chat/terminal/notebooks para leitores de tela.
- [ ] Fallback sem microfone/provider, privacidade das gravações e testes de permissão; nenhuma promessa de backend proprietário.

### Como executar e comprovar

1. Reproduzir o fluxo correspondente no VS Code de referência e registrar comportamento esperado.
2. Criar fixture mínima, definir contratos e detalhar casos negativos antes da implementação.
3. Implementar incrementalmente sem bloquear a UI nem executar conteúdo não confiável.
4. Comparar resultado/eventos/estado com a referência; anexar testes, captura ou benchmark.
5. Atualizar matriz de gaps e documentação; marcar concluído apenas com evidências.

**Dependências:** [EC-081](./PARITY-BACKLOG.md#ec-081), [#27](https://github.com/joaogabriel15/editor-code/issues/27).

**Fontes:** [referência 1](https://github.com/microsoft/vscode-docs/blob/81d76c22e9a4f5c63733c38e4ccedaf8c9f051bf/docs/configure/accessibility/accessibility.md)

<a id="ec-087"></a>
## EC-087 — Completar acessibilidade, localização e entrada de texto

[Issue #54](https://github.com/joaogabriel15/editor-code/issues/54)

**Área:** Acessibilidade · **Marco:** P6 — Plataformas, qualidade e distribuição · **Estado:** planejado

Paridade por sistema operacional e tecnologia assistiva.

### Checklist de entrega

- [ ] UI Automation/AT-SPI/NSAccessibility conforme plataforma; foco, high contrast, reduced motion e keyboard-only.
- [ ] NVDA/VoiceOver e demais leitores selecionados, IME/dead keys, RTL/bidi, emoji/graphemes e teclado internacional.
- [ ] Language packs/l10n, pluralização e pseudolocalização; testes manuais documentados além de checks automáticos.

### Como executar e comprovar

1. Reproduzir o fluxo correspondente no VS Code de referência e registrar comportamento esperado.
2. Criar fixture mínima, definir contratos e detalhar casos negativos antes da implementação.
3. Implementar incrementalmente sem bloquear a UI nem executar conteúdo não confiável.
4. Comparar resultado/eventos/estado com a referência; anexar testes, captura ou benchmark.
5. Atualizar matriz de gaps e documentação; marcar concluído apenas com evidências.

**Dependências:** [#27](https://github.com/joaogabriel15/editor-code/issues/27), [EC-036](./PARITY-BACKLOG.md#ec-036), [EC-033](./PARITY-BACKLOG.md#ec-033).

**Fontes:** [referência 1](https://github.com/microsoft/vscode-docs/blob/81d76c22e9a4f5c63733c38e4ccedaf8c9f051bf/docs/configure/locales.md) · [referência 2](https://github.com/microsoft/vscode-docs/blob/81d76c22e9a4f5c63733c38e4ccedaf8c9f051bf/docs/configure/accessibility/accessibility.md)

<a id="ec-088"></a>
## EC-088 — Completar CLI, integração com OS e modo portátil

[Issue #79](https://github.com/joaogabriel15/editor-code/issues/79)

**Área:** Plataforma · **Marco:** P6 — Plataformas, qualidade e distribuição · **Estado:** planejado

Entrada e distribuição utilizáveis fora da UI.

### Checklist de entrega

- [ ] CLI new/reuse window, --wait, --goto, diff/merge, stdin, profile, user-data/extensions-dir e gestão de extensões.
- [ ] Protocol handler, file associations, Open With/context menu, launch de terminal, single instance e URLs seguros.
- [ ] Instalação user/system/portable, PATH, logs/diagnostics e exit codes; testar Windows/macOS/Linux e conflitos com VS Code.

### Como executar e comprovar

1. Reproduzir o fluxo correspondente no VS Code de referência e registrar comportamento esperado.
2. Criar fixture mínima, definir contratos e detalhar casos negativos antes da implementação.
3. Implementar incrementalmente sem bloquear a UI nem executar conteúdo não confiável.
4. Comparar resultado/eventos/estado com a referência; anexar testes, captura ou benchmark.
5. Atualizar matriz de gaps e documentação; marcar concluído apenas com evidências.

**Dependências:** [#29](https://github.com/joaogabriel15/editor-code/issues/29), [EC-041](./PARITY-BACKLOG.md#ec-041).

**Fontes:** [referência 1](https://github.com/microsoft/vscode-docs/blob/81d76c22e9a4f5c63733c38e4ccedaf8c9f051bf/docs/configure/command-line.md) · [referência 2](https://github.com/microsoft/vscode-docs/blob/81d76c22e9a4f5c63733c38e4ccedaf8c9f051bf/docs/setup/portable.md)

<a id="ec-089"></a>
## EC-089 — Implementar proxy, certificados, offline e políticas corporativas

[Issue #86](https://github.com/joaogabriel15/editor-code/issues/86)

**Área:** Plataforma · **Marco:** P6 — Plataformas, qualidade e distribuição · **Estado:** planejado

Ambientes de rede e administração reais.

### Checklist de entrega

- [ ] Proxy/auth, certificados do sistema, TLS, metered connection, downloads/cache e modo offline.
- [ ] Políticas gerenciadas para extensões, IA, updates e telemetria com precedência e diagnóstico.
- [ ] Não desabilitar verificação TLS como solução; cobrir firewall, proxy autenticado, revogação e endpoints indisponíveis.

### Como executar e comprovar

1. Reproduzir o fluxo correspondente no VS Code de referência e registrar comportamento esperado.
2. Criar fixture mínima, definir contratos e detalhar casos negativos antes da implementação.
3. Implementar incrementalmente sem bloquear a UI nem executar conteúdo não confiável.
4. Comparar resultado/eventos/estado com a referência; anexar testes, captura ou benchmark.
5. Atualizar matriz de gaps e documentação; marcar concluído apenas com evidências.

**Dependências:** [EC-068](./PARITY-BACKLOG.md#ec-068), [EC-070](./PARITY-BACKLOG.md#ec-070), [#29](https://github.com/joaogabriel15/editor-code/issues/29).

**Fontes:** [referência 1](https://github.com/microsoft/vscode-docs/blob/81d76c22e9a4f5c63733c38e4ccedaf8c9f051bf/docs/setup/network.md) · [referência 2](https://github.com/microsoft/vscode-docs/blob/81d76c22e9a4f5c63733c38e4ccedaf8c9f051bf/docs/enterprise/policies.md)

<a id="ec-090"></a>
## EC-090 — Implementar observabilidade, diagnóstico e Extension Bisect

[Issue #64](https://github.com/joaogabriel15/editor-code/issues/64)

**Área:** Qualidade · **Marco:** P6 — Plataformas, qualidade e distribuição · **Estado:** planejado

Investigar consumo e falhas sem adivinhação.

### Checklist de entrega

- [ ] Process Explorer, startup/performance profiles, running extensions, logs e extension bisect/restart.
- [ ] Issue reporter com preview/sanitização, crash dumps opt-in e correlação de erro por serviço.
- [ ] Telemetria opcional/documentada, redaction, retenção e controles; diagnóstico local funciona sem serviços Microsoft.

### Como executar e comprovar

1. Reproduzir o fluxo correspondente no VS Code de referência e registrar comportamento esperado.
2. Criar fixture mínima, definir contratos e detalhar casos negativos antes da implementação.
3. Implementar incrementalmente sem bloquear a UI nem executar conteúdo não confiável.
4. Comparar resultado/eventos/estado com a referência; anexar testes, captura ou benchmark.
5. Atualizar matriz de gaps e documentação; marcar concluído apenas com evidências.

**Dependências:** [#13](https://github.com/joaogabriel15/editor-code/issues/13), [EC-063](./PARITY-BACKLOG.md#ec-063), [EC-046](./PARITY-BACKLOG.md#ec-046).

**Fontes:** [referência 1](https://github.com/microsoft/vscode-docs/blob/81d76c22e9a4f5c63733c38e4ccedaf8c9f051bf/docs/configure/telemetry.md)

<a id="ec-091"></a>
## EC-091 — Completar atualização, assinatura e distribuição multiplataforma

[Issue #94](https://github.com/joaogabriel15/editor-code/issues/94)

**Área:** Release · **Marco:** P6 — Plataformas, qualidade e distribuição · **Estado:** planejado

Ciclo completo de entrega e manutenção.

### Checklist de entrega

- [ ] Artefatos x64/arm64 previstos por OS, assinatura/notarização quando provisionada e canais stable/preview.
- [ ] Atualização atômica, checksum/signature verification, rollback, migração de dados e portable/offline.
- [ ] SBOM, licenças, cadeia de dependências e testes em máquina limpa; certificado ausente impede declarar pacote assinado.

### Como executar e comprovar

1. Reproduzir o fluxo correspondente no VS Code de referência e registrar comportamento esperado.
2. Criar fixture mínima, definir contratos e detalhar casos negativos antes da implementação.
3. Implementar incrementalmente sem bloquear a UI nem executar conteúdo não confiável.
4. Comparar resultado/eventos/estado com a referência; anexar testes, captura ou benchmark.
5. Atualizar matriz de gaps e documentação; marcar concluído apenas com evidências.

**Dependências:** [#29](https://github.com/joaogabriel15/editor-code/issues/29), [EC-088](./PARITY-BACKLOG.md#ec-088), [EC-089](./PARITY-BACKLOG.md#ec-089).

**Fontes:** [referência 1](https://github.com/microsoft/vscode-docs/blob/81d76c22e9a4f5c63733c38e4ccedaf8c9f051bf/docs/enterprise/updates.md) · [referência 2](https://github.com/microsoft/vscode-docs/blob/81d76c22e9a4f5c63733c38e4ccedaf8c9f051bf/docs/setup/windows.md) · [referência 3](https://github.com/microsoft/vscode-docs/blob/81d76c22e9a4f5c63733c38e4ccedaf8c9f051bf/docs/setup/linux.md) · [referência 4](https://github.com/microsoft/vscode-docs/blob/81d76c22e9a4f5c63733c38e4ccedaf8c9f051bf/docs/setup/mac.md)

<a id="ec-092"></a>
## EC-092 — Criar suíte diferencial funcional e visual contra VS Code

[Issue #95](https://github.com/joaogabriel15/editor-code/issues/95)

**Área:** Qualidade · **Marco:** P6 — Plataformas, qualidade e distribuição · **Estado:** planejado

Provar equivalência em vez de apenas implementar interfaces parecidas.

### Checklist de entrega

- [ ] Fixtures determinísticas executadas no baseline e no editor para edição/arquivos/commands/config/APIs.
- [ ] Golden screenshots por tema/DPI/plataforma com tolerâncias explícitas; comparar eventos/undo/erro/foco.
- [ ] Relatório de diferenças reproduzível, sem marcar teste ausente como aprovado; cada requisito referencia evidência.

### Como executar e comprovar

1. Reproduzir o fluxo correspondente no VS Code de referência e registrar comportamento esperado.
2. Criar fixture mínima, definir contratos e detalhar casos negativos antes da implementação.
3. Implementar incrementalmente sem bloquear a UI nem executar conteúdo não confiável.
4. Comparar resultado/eventos/estado com a referência; anexar testes, captura ou benchmark.
5. Atualizar matriz de gaps e documentação; marcar concluído apenas com evidências.

**Dependências:** [EC-031](./PARITY-BACKLOG.md#ec-031), [EC-032](./PARITY-BACKLOG.md#ec-032), [EC-071](./PARITY-BACKLOG.md#ec-071).

**Fontes:** [referência 1](https://github.com/microsoft/vscode-docs/blob/81d76c22e9a4f5c63733c38e4ccedaf8c9f051bf/api/working-with-extensions/testing-extension.md)

<a id="ec-093"></a>
## EC-093 — Criar testes de resistência, fuzzing e integridade de dados

[Issue #65](https://github.com/joaogabriel15/editor-code/issues/65)

**Área:** Qualidade · **Marco:** P6 — Plataformas, qualidade e distribuição · **Estado:** planejado

Resistência a entradas hostis, cancelamento e crashes.

### Checklist de entrega

- [ ] Property/fuzz tests para buffers, Unicode, parsers, VSIX, RPC, themes e WorkspaceEdit.
- [ ] Fault injection: disco cheio, falha de save, kill/restart, reconnect, extension crash e cancelamento.
- [ ] Soak tests com multi-repo e outputs massivos; invariantes de undo/round-trip e vazamentos monitorados.

### Como executar e comprovar

1. Reproduzir o fluxo correspondente no VS Code de referência e registrar comportamento esperado.
2. Criar fixture mínima, definir contratos e detalhar casos negativos antes da implementação.
3. Implementar incrementalmente sem bloquear a UI nem executar conteúdo não confiável.
4. Comparar resultado/eventos/estado com a referência; anexar testes, captura ou benchmark.
5. Atualizar matriz de gaps e documentação; marcar concluído apenas com evidências.

**Dependências:** [EC-044](./PARITY-BACKLOG.md#ec-044), [EC-045](./PARITY-BACKLOG.md#ec-045), [EC-054](./PARITY-BACKLOG.md#ec-054), [EC-059](./PARITY-BACKLOG.md#ec-059).

**Fontes:** [referência 1](https://code.visualstudio.com/docs)

<a id="ec-094"></a>
## EC-094 — Homologar extensões reais e integrações prioritárias

[Issue #96](https://github.com/joaogabriel15/editor-code/issues/96)

**Área:** Qualidade · **Marco:** P6 — Plataformas, qualidade e distribuição · **Estado:** planejado

Matriz de compatibilidade por versão e capacidade.

### Checklist de entrega

- [ ] Claude e Copilot originais testados separadamente de integrações nativas: login, webviews, comandos, contexto, chat, inline e agente.
- [ ] Amostras de linguagens, debugger, testes, notebook, tema, Git, remote e UI providers com instalação autorizada.
- [ ] Fixar versões/licenças, cenários e gaps; repetir após upgrade e registrar bloqueios externos sem declarar paridade.

### Como executar e comprovar

1. Reproduzir o fluxo correspondente no VS Code de referência e registrar comportamento esperado.
2. Criar fixture mínima, definir contratos e detalhar casos negativos antes da implementação.
3. Implementar incrementalmente sem bloquear a UI nem executar conteúdo não confiável.
4. Comparar resultado/eventos/estado com a referência; anexar testes, captura ou benchmark.
5. Atualizar matriz de gaps e documentação; marcar concluído apenas com evidências.

**Dependências:** [EC-063](./PARITY-BACKLOG.md#ec-063), [EC-066](./PARITY-BACKLOG.md#ec-066), [EC-067](./PARITY-BACKLOG.md#ec-067), [EC-068](./PARITY-BACKLOG.md#ec-068), [EC-070](./PARITY-BACKLOG.md#ec-070), [EC-081](./PARITY-BACKLOG.md#ec-081).

**Fontes:** [referência 1](https://code.visualstudio.com/api) · [referência 2](https://github.com/microsoft/vscode-docs/blob/81d76c22e9a4f5c63733c38e4ccedaf8c9f051bf/docs/configure/extensions/extensions.md)

<a id="ec-095"></a>
## EC-095 — Conferir serviços externos, licenças e identidade do produto

[Issue #46](https://github.com/joaogabriel15/editor-code/issues/46)

**Área:** Governança · **Marco:** P0 — Contrato, inventário e auditoria de paridade · **Estado:** planejado

Tratar dependências fora do Code OSS sem excluí-las silenciosamente.

### Checklist de entrega

- [ ] Matriz para Marketplace, Microsoft/GitHub auth, Sync, Remote Tunnels/Codespaces, Copilot, Claude e colaboração.
- [ ] Para cada serviço: caminho suportado, autenticação/assinatura, redistribuição, alternativa funcional e impacto da divergência.
- [ ] Preservar avisos de código/assets; nome/logos próprios; impedimento aberto até solução ou alteração explícita do escopo.

### Como executar e comprovar

1. Reproduzir o fluxo correspondente no VS Code de referência e registrar comportamento esperado.
2. Criar fixture mínima, definir contratos e detalhar casos negativos antes da implementação.
3. Implementar incrementalmente sem bloquear a UI nem executar conteúdo não confiável.
4. Comparar resultado/eventos/estado com a referência; anexar testes, captura ou benchmark.
5. Atualizar matriz de gaps e documentação; marcar concluído apenas com evidências.

**Dependências:** [EC-031](./PARITY-BACKLOG.md#ec-031), [#4](https://github.com/joaogabriel15/editor-code/issues/4), [#5](https://github.com/joaogabriel15/editor-code/issues/5).

**Fontes:** [referência 1](https://github.com/microsoft/vscode-docs/blob/81d76c22e9a4f5c63733c38e4ccedaf8c9f051bf/docs/supporting/oss-extensions.md) · [referência 2](https://github.com/microsoft/vscode-docs/blob/81d76c22e9a4f5c63733c38e4ccedaf8c9f051bf/docs/remote/faq.md)

<a id="ec-096"></a>
## EC-096 — Cobrir onboarding, walkthroughs e superfícies auxiliares

[Issue #80](https://github.com/joaogabriel15/editor-code/issues/80)

**Área:** Workbench · **Marco:** P1 — Experiência completa do editor · **Estado:** planejado

Não omitir pequenos recursos visíveis na experiência completa.

### Checklist de entrega

- [ ] Welcome/Get Started, walkthroughs, hints/banners, feedback e configuração inicial acessíveis.
- [ ] Auditar surveys, emergency alerts, tags e recursos decorativos/experimentais do baseline; classificar se serviço, experimento ou recurso reproduzível.
- [ ] Não replicar endpoints/branding Microsoft; disponibilizar equivalente próprio ou registrar gap, nunca marcar exclusão como implementada.

### Como executar e comprovar

1. Reproduzir o fluxo correspondente no VS Code de referência e registrar comportamento esperado.
2. Criar fixture mínima, definir contratos e detalhar casos negativos antes da implementação.
3. Implementar incrementalmente sem bloquear a UI nem executar conteúdo não confiável.
4. Comparar resultado/eventos/estado com a referência; anexar testes, captura ou benchmark.
5. Atualizar matriz de gaps e documentação; marcar concluído apenas com evidências.

**Dependências:** [EC-033](./PARITY-BACKLOG.md#ec-033), [EC-065](./PARITY-BACKLOG.md#ec-065).

**Fontes:** [referência 1](https://github.com/microsoft/vscode-docs/blob/81d76c22e9a4f5c63733c38e4ccedaf8c9f051bf/docs/getstarted/overview.md)

<a id="ec-097"></a>
## EC-097 — Implementar adaptadores do ecossistema por linguagem e plataforma

[Issue #97](https://github.com/joaogabriel15/editor-code/issues/97)

**Área:** Linguagens · **Marco:** P2 — Linguagens, Git e ferramentas · **Estado:** planejado

Cobrir cenários populares que o VS Code oferece por extensões externas.

### Checklist de entrega

- [ ] Matriz Python/Jupyter, C/C++/CMake, C#/.NET, Java, Rust, Go, PHP, PowerShell e demais idiomas documentados.
- [ ] Por linguagem: instalação, environments/projects, completion, debug, testes, formatter e package/build tools; registrar provider/licença.
- [ ] Serviços Azure/containers/Kubernetes e ferramentas de dados são adaptadores condicionais; abrir subtarefas por pacote homologado sem supor compatibilidade.

### Como executar e comprovar

1. Reproduzir o fluxo correspondente no VS Code de referência e registrar comportamento esperado.
2. Criar fixture mínima, definir contratos e detalhar casos negativos antes da implementação.
3. Implementar incrementalmente sem bloquear a UI nem executar conteúdo não confiável.
4. Comparar resultado/eventos/estado com a referência; anexar testes, captura ou benchmark.
5. Atualizar matriz de gaps e documentação; marcar concluído apenas com evidências.

**Dependências:** [EC-048](./PARITY-BACKLOG.md#ec-048), [EC-058](./PARITY-BACKLOG.md#ec-058), [EC-060](./PARITY-BACKLOG.md#ec-060), [EC-070](./PARITY-BACKLOG.md#ec-070), [EC-094](./PARITY-BACKLOG.md#ec-094).

**Fontes:** [referência 1](https://github.com/microsoft/vscode-docs/blob/81d76c22e9a4f5c63733c38e4ccedaf8c9f051bf/docs/languages/overview.md) · [referência 2](https://github.com/microsoft/vscode-docs/blob/81d76c22e9a4f5c63733c38e4ccedaf8c9f051bf/docs/python/environments.md) · [referência 3](https://github.com/microsoft/vscode-docs/blob/81d76c22e9a4f5c63733c38e4ccedaf8c9f051bf/docs/java/extensions.md) · [referência 4](https://github.com/microsoft/vscode-docs/blob/81d76c22e9a4f5c63733c38e4ccedaf8c9f051bf/docs/csharp/get-started.md)

<a id="ec-098"></a>
## EC-098 — Auditar paridade final e bloquear release com lacunas não declaradas

[Issue #98](https://github.com/joaogabriel15/editor-code/issues/98)

**Área:** Governança · **Marco:** P0 — Contrato, inventário e auditoria de paridade · **Estado:** planejado

Gate final da meta de funcionar como o VS Code.

### Checklist de entrega

- [ ] Cada entrada do catálogo possui caso de teste, evidência por plataforma e estado; revisar manualmente amostras e áreas críticas.
- [ ] Comparar funcionalidade e RAM/CPU com capacidades equivalentes, incluindo processos Node/webview/LSP/IA/remotos.
- [ ] Publicar relatório de gaps/bloqueios; nenhuma declaração de paridade completa enquanto requisitos estiverem parciais, bloqueados ou sem teste.

### Como executar e comprovar

1. Reproduzir o fluxo correspondente no VS Code de referência e registrar comportamento esperado.
2. Criar fixture mínima, definir contratos e detalhar casos negativos antes da implementação.
3. Implementar incrementalmente sem bloquear a UI nem executar conteúdo não confiável.
4. Comparar resultado/eventos/estado com a referência; anexar testes, captura ou benchmark.
5. Atualizar matriz de gaps e documentação; marcar concluído apenas com evidências.

**Dependências:** [#1](https://github.com/joaogabriel15/editor-code/issues/1), [#2](https://github.com/joaogabriel15/editor-code/issues/2), [#3](https://github.com/joaogabriel15/editor-code/issues/3), [#4](https://github.com/joaogabriel15/editor-code/issues/4), [#5](https://github.com/joaogabriel15/editor-code/issues/5), [#6](https://github.com/joaogabriel15/editor-code/issues/6), [#7](https://github.com/joaogabriel15/editor-code/issues/7), [#8](https://github.com/joaogabriel15/editor-code/issues/8), [#9](https://github.com/joaogabriel15/editor-code/issues/9), [#10](https://github.com/joaogabriel15/editor-code/issues/10), [#11](https://github.com/joaogabriel15/editor-code/issues/11), [#12](https://github.com/joaogabriel15/editor-code/issues/12), [#13](https://github.com/joaogabriel15/editor-code/issues/13), [#14](https://github.com/joaogabriel15/editor-code/issues/14), [#15](https://github.com/joaogabriel15/editor-code/issues/15), [#16](https://github.com/joaogabriel15/editor-code/issues/16), [#17](https://github.com/joaogabriel15/editor-code/issues/17), [#18](https://github.com/joaogabriel15/editor-code/issues/18), [#19](https://github.com/joaogabriel15/editor-code/issues/19), [#20](https://github.com/joaogabriel15/editor-code/issues/20), [#21](https://github.com/joaogabriel15/editor-code/issues/21), [#22](https://github.com/joaogabriel15/editor-code/issues/22), [#23](https://github.com/joaogabriel15/editor-code/issues/23), [#24](https://github.com/joaogabriel15/editor-code/issues/24), [#25](https://github.com/joaogabriel15/editor-code/issues/25), [#26](https://github.com/joaogabriel15/editor-code/issues/26), [#27](https://github.com/joaogabriel15/editor-code/issues/27), [#28](https://github.com/joaogabriel15/editor-code/issues/28), [#29](https://github.com/joaogabriel15/editor-code/issues/29), [#30](https://github.com/joaogabriel15/editor-code/issues/30), [EC-031](./PARITY-BACKLOG.md#ec-031), [EC-032](./PARITY-BACKLOG.md#ec-032), [EC-033](./PARITY-BACKLOG.md#ec-033), [EC-034](./PARITY-BACKLOG.md#ec-034), [EC-035](./PARITY-BACKLOG.md#ec-035), [EC-036](./PARITY-BACKLOG.md#ec-036), [EC-037](./PARITY-BACKLOG.md#ec-037), [EC-038](./PARITY-BACKLOG.md#ec-038), [EC-039](./PARITY-BACKLOG.md#ec-039), [EC-040](./PARITY-BACKLOG.md#ec-040), [EC-041](./PARITY-BACKLOG.md#ec-041), [EC-042](./PARITY-BACKLOG.md#ec-042), [EC-043](./PARITY-BACKLOG.md#ec-043), [EC-044](./PARITY-BACKLOG.md#ec-044), [EC-045](./PARITY-BACKLOG.md#ec-045), [EC-046](./PARITY-BACKLOG.md#ec-046), [EC-047](./PARITY-BACKLOG.md#ec-047), [EC-048](./PARITY-BACKLOG.md#ec-048), [EC-049](./PARITY-BACKLOG.md#ec-049), [EC-050](./PARITY-BACKLOG.md#ec-050), [EC-051](./PARITY-BACKLOG.md#ec-051), [EC-052](./PARITY-BACKLOG.md#ec-052), [EC-053](./PARITY-BACKLOG.md#ec-053), [EC-054](./PARITY-BACKLOG.md#ec-054), [EC-055](./PARITY-BACKLOG.md#ec-055), [EC-056](./PARITY-BACKLOG.md#ec-056), [EC-057](./PARITY-BACKLOG.md#ec-057), [EC-058](./PARITY-BACKLOG.md#ec-058), [EC-059](./PARITY-BACKLOG.md#ec-059), [EC-060](./PARITY-BACKLOG.md#ec-060), [EC-061](./PARITY-BACKLOG.md#ec-061), [EC-062](./PARITY-BACKLOG.md#ec-062), [EC-063](./PARITY-BACKLOG.md#ec-063), [EC-064](./PARITY-BACKLOG.md#ec-064), [EC-065](./PARITY-BACKLOG.md#ec-065), [EC-066](./PARITY-BACKLOG.md#ec-066), [EC-067](./PARITY-BACKLOG.md#ec-067), [EC-068](./PARITY-BACKLOG.md#ec-068), [EC-069](./PARITY-BACKLOG.md#ec-069), [EC-070](./PARITY-BACKLOG.md#ec-070), [EC-071](./PARITY-BACKLOG.md#ec-071), [EC-072](./PARITY-BACKLOG.md#ec-072), [EC-073](./PARITY-BACKLOG.md#ec-073), [EC-074](./PARITY-BACKLOG.md#ec-074), [EC-075](./PARITY-BACKLOG.md#ec-075), [EC-076](./PARITY-BACKLOG.md#ec-076), [EC-077](./PARITY-BACKLOG.md#ec-077), [EC-078](./PARITY-BACKLOG.md#ec-078), [EC-079](./PARITY-BACKLOG.md#ec-079), [EC-080](./PARITY-BACKLOG.md#ec-080), [EC-081](./PARITY-BACKLOG.md#ec-081), [EC-082](./PARITY-BACKLOG.md#ec-082), [EC-083](./PARITY-BACKLOG.md#ec-083), [EC-084](./PARITY-BACKLOG.md#ec-084), [EC-085](./PARITY-BACKLOG.md#ec-085), [EC-086](./PARITY-BACKLOG.md#ec-086), [EC-087](./PARITY-BACKLOG.md#ec-087), [EC-088](./PARITY-BACKLOG.md#ec-088), [EC-089](./PARITY-BACKLOG.md#ec-089), [EC-090](./PARITY-BACKLOG.md#ec-090), [EC-091](./PARITY-BACKLOG.md#ec-091), [EC-092](./PARITY-BACKLOG.md#ec-092), [EC-093](./PARITY-BACKLOG.md#ec-093), [EC-094](./PARITY-BACKLOG.md#ec-094), [EC-095](./PARITY-BACKLOG.md#ec-095), [EC-096](./PARITY-BACKLOG.md#ec-096), [EC-097](./PARITY-BACKLOG.md#ec-097).

**Fontes:** [referência 1](https://code.visualstudio.com/docs)
