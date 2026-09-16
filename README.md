# Editor Code

Editor nativo em Rust, inspirado na experiência do VS Code e planejado para muitos repositórios com consumo controlado.

**Status: fundação e planejamento. Ainda não há interface gráfica nem editor funcional.** O executável atual apenas identifica o projeto. Claude, Copilot e extensões são trabalho futuro, condicionado às provas de viabilidade.

## Direção
- Implementação nova em Rust; este repositório não é um fork do Code OSS.
- Windows primeiro, com separação de plataforma para Linux/macOS.
- Repositórios cadastrados não devem iniciar serviços pesados automaticamente.
- Meta ampliada: paridade funcional verificável com VS Code 1.137.0, incluindo notebooks, remoto, web e APIs de extensões.
- As 30 tarefas iniciais são a fundação; o plano possui 98 tarefas técnicas e 736 entradas de responsabilidade.
- Não há promessa de compatibilidade universal de extensões ou de redução de memória antes dos benchmarks.

## Comece pelo checklist

[Checklist mestre no GitHub](https://github.com/joaogabriel15/editor-code/issues/99) · [Passo a passo de execução](docs/EXECUTION-CHECKLIST.md) · [Cenários de teste](docs/TEST-SCENARIOS.md)

## Desenvolvimento
Instale Rust stable com rustfmt e clippy e um linker compatível com a plataforma. No Windows, use o toolchain MSVC e as ferramentas C++ correspondentes.

```sh
cargo run -p editor-code
cargo fmt --all -- --check
cargo clippy --workspace --all-targets -- -D warnings
cargo test --workspace
```

## Documentação
- [Visão e escopo](docs/VISION.md)
- [Arquitetura proposta](docs/ARCHITECTURE.md)
- [Estudo do VS Code](docs/VSCODE-REFERENCE.md)
- [Compatibilidade](docs/COMPATIBILITY.md)
- [Plano de desempenho](docs/PERFORMANCE.md)
- [Roadmap](docs/ROADMAP.md)
- [Backlog detalhado](docs/BACKLOG.md)
- [Índice de issues](docs/GITHUB-ISSUES.md)
- [Comece aqui: checklist de execução](docs/EXECUTION-CHECKLIST.md)
- [Conferência de paridade](docs/PARITY-AUDIT.md)
- [Backlog detalhado de paridade](docs/PARITY-BACKLOG.md)
- [Matriz de cobertura](docs/PARITY-MATRIX.md)
- [Contribuição](CONTRIBUTING.md)

## Acompanhamento
[Issues](https://github.com/joaogabriel15/editor-code/issues) · [Milestones](https://github.com/joaogabriel15/editor-code/milestones)

Projeto independente, sem afiliação à Microsoft, GitHub ou Anthropic. Código original sob MIT; componentes de terceiros mantêm suas próprias licenças.
