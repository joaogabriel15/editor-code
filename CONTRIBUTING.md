# Contribuindo

1. Escolha uma issue cuja dependência esteja resolvida.
2. Registre decisões estruturais em docs/adr/ antes da implementação.
3. Use branch focada e PR vinculada à issue.
4. Execute cargo fmt --all -- --check, cargo clippy --workspace --all-targets -- -D warnings e cargo test --workspace.
5. Teste perda de dados, cancelamento, Unicode e falhas quando aplicável.
6. Para mudanças de desempenho, anexe cenário reproduzível e consumo de todos os processos filhos.
7. Atualize a matriz de compatibilidade e os avisos de terceiros quando necessário.

Uma tarefa termina com comportamento demonstrável, documentação coerente e validação. Scaffold não conta como funcionalidade pronta.
