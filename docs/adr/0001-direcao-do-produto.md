# ADR 0001 — Implementação nova em Rust

Status: aceita como direção inicial do projeto.

## Contexto
O usuário deseja preparar um editor do zero, inspirado no VS Code, com temas, IA e melhor comportamento em muitos repositórios.

## Decisão
Iniciar workspace Rust independente, usando VS Code como referência de comportamento e formatos. Manter núcleo sem UI. Escolher toolkit somente após protótipos. Planejar compatibilidade de extensões como camada opcional e parcial.

## Consequências
Maior custo para implementar edição e interface; liberdade para controlar serviços por repositório. Não há herança automática de extensões, temas perfeitos ou acesso a serviços. Redução de consumo exige validação.

## Alternativas
Fork Code OSS preservaria mais compatibilidade, mas manteria a arquitetura de interface atual. A troca de direção deve ser uma nova ADR.
