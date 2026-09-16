# Arquitetura proposta

Status: proposta inicial. Apenas editor-core e o executável de bootstrap existem.

## Camadas previstas
- **editor-core:** buffers, transações, seleção e histórico, sem UI e sem processos.
- **UI nativa:** janela, renderização, abas, painéis, acessibilidade. Toolkit depende de ADR.
- **workspace:** catálogo de raízes, estados ativo/inativo/suspenso e persistência.
- **supervisor:** filas limitadas, prioridade, cancelamento, timeouts e processos filhos.
- **serviços:** I/O, busca, watchers, Git, LSP, DAP e PTY.
- **compatibilidade:** temas, atalhos/configuração e host de extensões via RPC; a prova inicial é parcial, a meta final cobre os contratos do baseline.
- **documentos ricos:** notebooks, custom editors e webviews com motor web isolado quando necessário.
- **remoto/web:** servidor próprio, transportes SSH/WSL/containers/túneis, host remoto e cliente web conforme capabilities.
- **perfis e sync:** armazenamento versionado, resolução de conflitos e adaptadores de serviço.
- **QA de paridade:** inventário de contratos e testes diferenciais por plataforma.
- **IA:** adaptadores específicos com contexto controlado, streaming e revisão de alterações.

## Fluxo
A UI envia comandos ao núcleo; serviços retornam eventos versionados. Trabalho de disco, Git, análise e rede não bloqueia a thread da interface. Resultados antigos são descartados pelo identificador/versão do documento.

## Repositórios
Cadastrar uma raiz não inicia LSP ou varredura contínua. Ativação cria somente serviços necessários. Suspensão cancela filas e encerra processos dispensáveis. Arquivos abertos e edições não salvas preservam seu estado.

## Limites de confiança
Processo separado não é sandbox. O host de extensões precisará de modelo de permissões e política de confiança antes de executar pacotes. Comandos recebidos de arquivos ou agentes passam por autorização apropriada. Segredos ficam fora dos arquivos do repo.

## Interfaces e decisões
Contratos mínimos e versionados; backpressure em canais e limite de payload. LSP/DAP em processos separados. Node não é dependência do editor-core; sua introdução no host depende da PoC de compatibilidade. APIs propostas ficam versionadas. Estudar custo do motor web sem afirmar que webviews são renderizáveis nativamente por Rust.

## Contrato ampliado
A ADR 0002 amplia a meta para paridade funcional. Delimitação de APIs em fases iniciais não remove o restante do backlog. Comportamentos intencionalmente diferentes, como ativação sob demanda, exigem critérios de equivalência e documentação.
