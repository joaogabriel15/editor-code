# Checklist de execução do Editor Code

## O que está pronto agora

- [x] Repositório público e base Rust compilável.
- [x] Conferência estrutural contra VS Code 1.137.0 e revisão das 30 tarefas iniciais.
- [x] Escopo ampliado, 98 tarefas técnicas, critérios de aceite e dependências.
- [x] Matriz com origem e responsável para 736 entradas estruturais.
- [x] Check automático de consistência do planejamento.
- [ ] Interface do editor implementada.
- [ ] Compatibilidade de extensões comprovada.
- [ ] Claude e Copilot homologados.
- [ ] Paridade funcional comprovada por testes.
- [ ] Consumo menor comprovado com capacidades equivalentes.

As caixas marcadas acima são entregas de planejamento. Não são funcionalidades prontas.

## Checklist clicável no GitHub

Use o [checklist mestre #99](https://github.com/joaogabriel15/editor-code/issues/99) para acompanhar as 98 tarefas. Os números EC e os números GitHub são diferentes; siga os links do índice.

## Por onde começar

1. **EC-001:** medir VS Code. Usar projeto sintético; registrar versão, hardware, processos, memória e latência. Não publicar seus repositórios pessoais.
2. **EC-003:** auditar os formatos/APIs prioritários do upstream. Entregar matriz inicial com limitações.
3. **EC-031:** congelar o contrato de paridade. A versão 1.137.0 é a referência, e diferenças precisam ser registradas.
4. **EC-032:** extrair cada comando/configuração/API e ligar a um teste. O mapa de pastas atual não substitui esse trabalho.
5. **EC-002:** escolher UI por protótipo e medições de acessibilidade, texto e webviews.
6. **EC-004 e EC-005:** provar os caminhos de Copilot/Claude cedo. Elas dependem da auditoria inicial; não esperar o editor ficar pronto.
7. **EC-006 → EC-007 → EC-008:** buffer, persistência e janela. Provar abrir/editar/salvar/recuperar antes de aumentar o escopo.
8. **EC-009 → EC-012 → EC-013:** comandos, catálogo multi-repo e supervisor sob demanda.
9. Continuar pela ordem de dependências no [índice de issues](GITHUB-ISSUES.md); marcos P agrupam áreas e não são uma sequência rígida.
10. Chegar ao gate EC-098 somente após homologação, performance e resolução dos gaps.

As provas de viabilidade e a infraestrutura podem avançar em frentes independentes. Isso não dispensa dependências funcionais nem exige rodar todas as tarefas de uma vez.

## Rotina para cada tarefa

### Antes de implementar

- [ ] Ler a issue, fontes fixadas e dependências; marcar como bloqueada se faltar uma capacidade necessária.
- [ ] Reproduzir o fluxo no VS Code de referência, com extensões e configurações anotadas.
- [ ] Escrever entradas, saídas, eventos, atalhos, erros e comportamento de undo esperado.
- [ ] Separar API estável, proposta, implementação interna e serviço externo.
- [ ] Preparar fixtures públicas/sintéticas; conferir licenças de assets/pacotes.
- [ ] Registrar ADR quando a decisão alterar arquitetura, contrato ou custo de recursos.
- [ ] Dividir a tarefa em PRs menores se houver mais de um contrato independente.

### Durante a implementação

- [ ] Manter I/O, parsing pesado, rede e processos fora da thread da interface.
- [ ] Definir limites, timeout, cancelamento e descarte de resultado antigo.
- [ ] Preservar dados não salvos, undo/redo e restauração após falha.
- [ ] Tratar erros e estado incompleto de forma visível.
- [ ] Não executar código de workspace/extension/agent sem a autorização adequada.
- [ ] Não substituir API não suportada por retorno de sucesso fictício.
- [ ] Instrumentar consumo quando criar serviço, watcher, subprocesso ou motor web.

### Antes de concluir

- [ ] Executar format, Clippy e testes relevantes.
- [ ] Executar cenário positivo, erro, cancelamento e reinício quando aplicáveis.
- [ ] Comparar contra o baseline, incluindo foco, acessibilidade e atalhos.
- [ ] Testar Windows primeiro e plataformas afetadas; não inferir runtime de aprovação apenas pela compilação.
- [ ] Anexar evidência: teste automatizado, log sanitizado, captura ou benchmark reproduzível.
- [ ] Atualizar README/guia/compatibilidade quando o comportamento do produto mudar.
- [ ] Atualizar o estado do requisito e vincular PR.
- [ ] Fechar a issue apenas quando **todos os critérios aplicáveis** tiverem evidência.
- [ ] Se depender de fornecedor indisponível, registrar bloqueio e impacto; não chamar isso de implementado.

## Comandos básicos

Na raiz do repositório:

```powershell
cargo fmt --all -- --check
cargo clippy --workspace --all-targets --locked -- -D warnings
cargo test --workspace --locked
cargo build --workspace --release --locked
python scripts/verify_planning.py --require-published
```

O bootstrap atualmente não possui testes funcionais de editor. Um resultado com zero testes não comprova comportamento.

## Evidência por capacidade

Use [o modelo de validação](templates/VALIDATION.md) e os [27 cenários de homologação](TEST-SCENARIOS.md). Registre:

| Campo | O que preencher |
| --- | --- |
| Requisito | EC e item do inventário/API |
| Ambiente | OS, arquitetura, hardware, versão e extensões |
| Cenário | Fixture, configuração, passos e comando reproduzível |
| Referência | Resultado esperado no VS Code 1.137.0 |
| Editor Code | Resultado observado e diferenças |
| Falhas | Cancelamento, crash, rede/disco indisponíveis, input inválido |
| Recursos | RAM da árvore de processos, CPU, latência se aplicável |
| Evidência | Link para CI, captura, relatório e revisão |
| Estado | Planejado / implementado / verificado / parcial / bloqueado |

## Checklist dos grandes fluxos antes de usar diariamente

- [ ] Criar, abrir, alterar e salvar arquivos sem perda, inclusive após crash.
- [ ] Trabalhar com vários repos, alternar e suspender serviços com resultado correto.
- [ ] Usar todos os atalhos e configurações do contrato de paridade.
- [ ] Buscar/substituir com preview e undo, local e global.
- [ ] Aplicar temas, ícones, snippets e perfis com fidelidade documentada.
- [ ] Obter diagnóstico, completion, refactor, navegação e formatação.
- [ ] Fazer todo o fluxo Git com revisão e recuperação de conflitos.
- [ ] Executar tarefas, terminal, testes e debugger.
- [ ] Abrir/editar/executar notebooks e previews com isolamento.
- [ ] Instalar, desenvolver e executar extensões homologadas.
- [ ] Usar SSH, WSL, containers e cliente web nos cenários suportados.
- [ ] Usar Claude/Copilot originais e integrações nativas conforme matriz separada.
- [ ] Controlar agentes, ferramentas, MCP, contexto e alterações de código.
- [ ] Usar leitores de tela, IME, alto contraste e múltiplos monitores.
- [ ] Migrar/sincronizar dados, atualizar e reverter instalação.
- [ ] Comparar funcionalidade e consumo antes de afirmar que é equivalente e mais leve.

## Condições que impedem chamar de “igual ao VS Code”

APIs sem teste, extensão que não ativa, perdas no tema, fluxo remoto incompleto, dados não recuperados, plataforma não validada ou serviço externo inacessível. Cada diferença deve permanecer no relatório de gaps, mesmo quando houver alternativa funcional.

A identidade visual e os serviços proprietários não são automaticamente reutilizáveis. O objetivo de paridade funcional continua no plano; impedimentos precisam de decisão explícita, não exclusão silenciosa.

## Repetir a conferência estrutural

Executar `python scripts/audit_upstream.py` consulta a árvore pública do SHA fixado. O verificador compara os sete grupos estruturais; APIs e semântica continuam exigindo a auditoria EC-032 e testes.
