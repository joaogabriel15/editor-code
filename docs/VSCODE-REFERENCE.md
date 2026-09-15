# Referência: VS Code

Inspeção inicial em 2026-09-15. Revisão de referência: 29d5c1ecf1086c8ba833108afa45a766f6cc9f0b.
Upstream: https://github.com/microsoft/vscode

A inspeção cobriu a documentação de organização, árvore de src/vs, manifesto principal, declaração de API e manifesto Rust da CLI. Não foi uma auditoria completa nem um benchmark.

## Mapa para pesquisa
- src/vs/base e src/vs/platform: utilitários e serviços.
- src/vs/editor: núcleo do editor de texto; estudar comportamento e invariantes.
- src/vs/workbench: composição da interface e serviços.
- src/vs/workbench/api: ponte entre host de extensões e aplicação.
- src/vscode-dts/vscode.d.ts: contrato público de extensão.
- extensions/: recursos distribuídos como extensões.
- cli/Cargo.toml: já existe Rust na CLI; isso não torna a interface nativa Rust.

## Estratégia
Usar formatos e comportamentos como referência; escrever núcleo e UI novos. Qualquer incorporação literal de código requer rastreabilidade e preservação dos avisos aplicáveis.

## Fontes
- https://github.com/microsoft/vscode/wiki/Source-Code-Organization
- https://github.com/microsoft/vscode/tree/29d5c1ecf1086c8ba833108afa45a766f6cc9f0b/src/vs
- https://github.com/microsoft/vscode/blob/29d5c1ecf1086c8ba833108afa45a766f6cc9f0b/src/vscode-dts/vscode.d.ts
- https://github.com/microsoft/vscode/blob/29d5c1ecf1086c8ba833108afa45a766f6cc9f0b/LICENSE.txt

Code OSS tem licença MIT. Distribuição da Microsoft, extensões, serviços e marcas devem ser avaliados separadamente.
