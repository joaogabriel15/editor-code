# Plano de desempenho

Nenhuma meta numérica foi validada e nenhum ganho foi medido.

## Baseline
Criar fixtures sintéticas reproduzíveis com 1, 10 e 50 repos; registrar quantidade de arquivos, bytes, linguagens e exclusões. Incluir muitos arquivos pequenos e documentos grandes. Não publicar conteúdo de projetos pessoais.

Comparar: VS Code sem extensões adicionais; VS Code com ferramentas equivalentes; Editor Code com as mesmas capacidades habilitadas. Congelar versões, hardware e cenário.

## Métricas
Startup frio/quente, RAM de toda a árvore de processos, CPU após estabilização, quantidade de watchers/processos, latência p50/p95 de edição, abertura e busca. Medir repos cadastrados versus ativos e cancelamento de tarefas.

## Método
Separar custo de compilação de runtime. Usar build release. Executar aquecimento e repetições; registrar variância, scripts e resultados brutos sanitizados. Avaliar perda de funcionalidade junto com a economia de recursos.

## Gate
Definir orçamentos numéricos após baseline. Regressões relevantes precisam de justificativa. Repos inativos não devem disparar LSP/Git/watchers pesados por padrão.
