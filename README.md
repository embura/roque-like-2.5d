# 🎮 CrewAI - Time de Agentes para Desenvolvimento de Jogos Unity

Skill de orquestração usando **CrewAI** para criar um time de 3 agentes especializados em desenvolvimento de jogos Unity:

## 👥 Agentes

1. **PO (Product Owner)** - Define o escopo do jogo
   - Visão geral e mecânicas
   - Estilo visual (Pixel Art HD estilo Magicraft)
   - Funcionalidades detalhadas
   - Critérios de aceite

2. **DEV (Engenheiro de Software Unity)** - Implementa o jogo
   - Especificações técnicas
   - Plano de desenvolvimento
   - Código C# completo
   - Arquitetura e boas práticas

3. **QA (Quality Assurance)** - Valida a implementação
   - Análise de conformidade com o escopo
   - Revisão de código
   - Casos de teste
   - Relatório de validação

## 🎨 Estilo Visual Magicraft

O PO está configurado para especificar assets no estilo **Magicraft**:
- **Personagens/Chefes/Efeitos**: 128x128 a 256x256 pixels
- **Tilesets (pisos/paredes)**: 64x64 ou 32x32 pixels
- **Ícones de UI**: 64x64 pixels
- **Estilo**: Hand-painted High-Res Pixel Art

## 📋 Instalação

```bash
# Instalar dependências
pip install -r requirements.txt

# Configurar variáveis de ambiente
cp .env.example .env
# Edite .env e adicione sua chave OpenAI
```

## 🚀 Uso

### Opção 1: Executar diretamente

```bash
python unity_game_agents_crew.py
```

### Opção 2: Importar como módulo

```python
from unity_game_agents_crew import run_game_dev_crew

# Definir conceito do jogo
game_concept = """
Um jogo de ação roguelike em arena com sistema de magia combinatória.
O jogador é um mago que deve sobreviver a ondas de inimigos em salas fechadas,
coletando cristais de mana para desbloquear novas magias e combinações.
"""

# Executar o time de agentes
result = run_game_dev_crew(game_concept)
print(result)
```

## 🔄 Fluxo de Execução

```
┌─────────────┐      ┌─────────────┐      ┌─────────────┐
│     PO      │ ───► │     DEV     │ ───► │     QA      │
│  (Escopo)   │      │(Implement.) │      │ (Validação) │
└─────────────┘      └─────────────┘      └─────────────┘
       │                    │                    │
       ▼                    ▼                    ▼
  Documento de        Especificações       Relatório de
  Escopo Completo     Técnicas + Código    Validação
```

## 📁 Estrutura de Arquivos

```
/workspace/
├── unity_game_agents_crew.py  # Script principal
├── requirements.txt           # Dependências Python
├── .env.example              # Template de variáveis de ambiente
└── README.md                 # Este arquivo
```

## ⚙️ Configuração Personalizada

Para customizar o conceito do jogo, edite a variável `game_concept` no script principal:

```python
game_concept = """
Descreva aqui seu jogo:
- Gênero
- Mecânicas principais
- Tema/ambientação
- Qualquer requisito específico
"""
```

## 🔍 Questionamentos Automáticos

Os agentes foram instruídos a identificar e questionar:
- Ambiguidades no escopo
- Requisitos conflitantes
- Falta de clareza em funcionalidades
- Gaps na documentação

Se houver dúvidas durante a execução, os agentes solicitarão esclarecimentos antes de prosseguir.

## 📝 Saída Esperada

Ao final da execução, você receberá:

1. **Documento de Escopo** (PO)
   - Visão completa do jogo
   - Mecânicas detalhadas
   - Especificações visuais
   - Critérios de aceite

2. **Documentação Técnica** (DEV)
   - Arquitetura do projeto
   - Plano de desenvolvimento
   - Código C# dos sistemas principais

3. **Relatório de Validação** (QA)
   - Conformidade com escopo
   - Issues encontrados
   - Casos de teste
   - Parecer final

## 💡 Dicas

- Use conceitos claros e objetivos para melhores resultados
- Revise o output do PO antes de prosseguir se quiser ajustar algo
- O QA pode identificar gaps que precisam ser corrigidos pelo DEV
- Salve os outputs em arquivos separados para referência futura
