# Cenários mínimos de homologação

Estes roteiros complementam os critérios das issues. Usar fixtures sintéticas, VS Code 1.137.0 e extensões fixadas. Um caso aprovado não comprova todos os métodos de uma API; EC-032 deve expandir o catálogo para cada contrato.

Para cada cenário: registrar OS, versão, configuração, evidência e diferença. A referência determina detalhes de foco, seleção, eventos e undo.

| ID | Requisitos | Preparação e ação | Resultado a comprovar |
| --- | --- | --- | --- |
| T01 | EC-006/035/036/087 | Arquivo com acentos, emoji, CRLF, tabs, linha longa e texto bidi. Selecionar, multicursor, substituir, undo/redo e IME. | Conteúdo e seleção corretos; nenhuma divisão inválida de caractere ou congelamento. |
| T02 | EC-007/044/093 | Documento salvo e untitled alterados. Simular crash durante edição/save em fixture. Reiniciar. | Recuperar conteúdo; estado dirty correto; arquivo anterior íntegro ou erro explícito. |
| T03 | EC-033/034/040 | Abrir 12 arquivos, dividir grupos, fixar abas, mover para segunda janela/monitor e usar histórico/atalhos. | Foco, seleção, posições e arquivos não salvos persistem conforme contrato. |
| T04 | EC-038 | Workspace com arquivos ignored, binários e CRLF. Buscar regex e substituir vários arquivos com preview. Cancelar e desfazer. | Escopo e contagens corretos; ignorados respeitados; edições e undo consistentes. |
| T05 | EC-039/041/042 | Dois perfis, overrides de linguagem/folder e dois dispositivos simulados. Alterar settings offline e sincronizar. | Precedência correta, conflito visível, rollback possível e nenhum segredo sincronizado. |
| T06 | EC-043/045 | Renomear somente capitalização, mover entre roots, seguir link, tentar gravar readonly e desconectar provider. | Identidade de URI preservada; erros recuperáveis; sem acessar fora do escopo. |
| T07 | EC-010/047 | Tema redistribuível com includes/scopes/semantic colors e ícones; alternar light/dark/high contrast. | Mapas e precedência corretos; screenshots comparáveis; gaps listados. |
| T08 | EC-012/013/014/028 | Cadastrar 50 repos sintéticos, ativar 2, alternar e suspender um, disparar tempestade de mudanças. | Apenas serviços necessários ativos; filas limitadas; UI responsiva; memória inclui filhos. |
| T09 | EC-017/049/066 | LSP/provider fixture com respostas atrasadas. Editar durante completion/rename, cancelar e reiniciar servidor. | Resultado obsoleto descartado; sem corrupção; posições e eventos corretos. |
| T10 | EC-048/050/051 | Projetos JS/TS referenciados, HTML/CSS, JSON schema e snippet com transformação. | Completions/refactors/validation/snippets equivalentes; built-ins têm casos próprios. |
| T11 | EC-053/054/073 | Repos descartáveis com branches divergentes, worktree e submódulo. Stage parcial, commit, merge e review. | Diff e resolução corretos; operação perigosa explícita; comentários ligados à versão correta. |
| T12 | EC-055/057 | Task background com matcher multiline, dependência, input e saída massiva. Cancelar enquanto roda. | Problemas atualizados, terminal reutilizado corretamente, filhos encerrados e sem bloqueio. |
| T13 | EC-056 | Debug fixture com child process, exception, conditional breakpoint, source map e watch. Attach e reconnect. | Estado das threads/variáveis correto e capacidades ausentes claramente sinalizadas. |
| T14 | EC-058/067 | Provider de testes com discovery lazy, falha, cobertura e teste longo. Run/debug/continuous e cancel. | Resultados/output/coverage vinculados aos arquivos e profiles; cancelamento consistente. |
| T15 | EC-059/060 | Notebook com metadados, Markdown, outputs MIME e kernel fixture. Editar/salvar, crash, executar, interromper e diff. | Round-trip sem perda; outputs/estado/order corretos; conteúdo ativo respeita confiança. |
| T16 | EC-061/062 | Extensão fixture com webview e custom binary editor. Mensagens, reload e tentativa de acessar URI fora de localResourceRoots. | Estado restaurado, save/undo corretos, origem e recursos isolados. |
| T17 | EC-063–072 | Extensão fixture de cada namespace/contribution point. Ativar, alterar workspace/profile, cancelar chamadas, crash e desativar. | Ordem de eventos e disposal corretos; APIs sem suporte falham explicitamente; suite diferencial por símbolo. |
| T18 | EC-068/089 | Sessões de conta com scopes diferentes, token revogado, proxy autenticado e certificado inválido. | Consentimento/erro corretos; secrets protegidos; TLS não é desabilitado. |
| T19 | EC-074/075/078 | Host remoto de teste com latência e queda de rede. Editar, executar terminal/debug e abrir porta. | Reconexão e persistência; sem duplicar comandos; exposição de portas somente autorizada. |
| T20 | EC-076/077 | Duas distros WSL e container descartável com devcontainer.json. Reopen, rebuild falho e restart. | Paths/env/serviços corretos, dados preservados e limpeza controlada. |
| T21 | EC-079/080 | Cliente web sem Node local e preview de app via porta remota. Offline/reload/permission denial. | Capabilities e limites visíveis; cache e browser state corretos; isolamento de sessão. |
| T22 | EC-081/082/084 | Provider de IA e servidor MCP fixtures, streaming, ferramenta lenta, handoff e cancelamento. | Sessões/contextos isolados, eventos ordenados, permissões respeitadas e consumo mensurável. |
| T23 | EC-083/085/094 | Workspace com instrução maliciosa e edição humana concorrente à sugestão de agente. Revisar e aceitar parcialmente. | Conteúdo não concede autoridade; conflito detectado; rollback não apaga edição humana. |
| T24 | EC-086/087 | Navegar editor/terminal/chat/notebook apenas por teclado e leitor de tela; mudar idioma e DPI. | Nome/role/foco/announcements corretos; input não perdido; fallback de voz sem provider. |
| T25 | EC-088/090/091 | Máquina limpa, modo portátil, CLI --wait/diff, update interrompido, rollback e diagnóstico. | Artefato íntegro, exit codes e paths corretos, dados migrados, logs sanitizados. |
| T26 | EC-094/095/097 | Versões fixas das extensões reais: Claude, Copilot e amostra de linguagens/debug/notebooks/remoto. | Separar extensão original, integração nativa e serviço; registrar cada bloqueio com evidência. |
| T27 | EC-092/093/098 | Suite completa, soak multi-repo e fuzzing de parsers/edições/VSIX/RPC. | Relatório reproduzível, nenhum gap escondido; comparação de consumo com funcionalidades equivalentes. |

## Registro

Copiar [o modelo de validação](templates/VALIDATION.md) e anexar à PR/issue. Segredos e código privado não entram nas fixtures. Cada falha mantém o requisito parcial/bloqueado, mesmo se outros cenários passarem.
