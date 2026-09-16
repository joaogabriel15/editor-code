# Instruções do projeto

Leia README.md, docs/ARCHITECTURE.md e a issue antes de implementar.
- O produto é um editor novo em Rust inspirado no VS Code. Não substituir por um fork sem decisão documentada.
- Preferir MCP codebase-memory-mcp para descoberta de código: search_graph, trace_path, get_code_snippet, query_graph, get_architecture. Se indisponível ou insuficiente, usar rg.
- Manter editor-core independente da UI, rede e plataforma.
- Toolkit de UI permanece pendente da ADR e do protótipo de viabilidade.
- Nenhum serviço pesado deve iniciar para todos os repositórios por padrão.
- Não afirmar compatibilidade de extensões ou ganhos de memória sem testes e métricas.
- Validar interfaces oficiais e licenças para Claude/Copilot; não contornar autenticação ou restrições.
- Não executar conteúdo de workspace não confiável automaticamente.
- Registrar código de terceiros em THIRD_PARTY_NOTICES.md.
- Validar cargo fmt, clippy e testes relevantes; atualizar documentação e issue com evidências.
- Não publicar credenciais, caminhos pessoais, código de outros repositórios ou dados de benchmark privados.

## Paridade e conclusão
- Ler docs/EXECUTION-CHECKLIST.md e docs/PARITY-AUDIT.md.
- Basear comparações no SHA fixado, separando main/docs posteriores.
- Não encerrar requisitos sem evidência; impedimento externo permanece visível.
- Atualizar docs/planning/parity-plan.json ao alterar dependências/estado e executar python scripts/verify_planning.py --require-published.
