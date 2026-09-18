# Time de Agentes para Desenvolvimento de Jogos Unity com Qwen

## 🎮 Visão Geral

Este projeto implementa um sistema de orquestração de agentes baseado em **CrewAI** para desenvolvimento de jogos Unity. O time é composto por três agentes especializados que trabalham de forma sequencial e colaborativa, utilizando o modelo **Qwen** da Alibaba.

## 👥 Agentes do Time

### 1. Agente PO (Product Owner)
- **Função:** Definir escopo completo do jogo
- **Entregas:** Mecânicas, funcionalidades, estilo visual Pixel Art HD
- **Diferencial:** Questiona ambiguidades antes de prosseguir

### 2. Agente DEV (Engenheiro de Software Unity)
- **Função:** Criar especificações técnicas e implementar código C#
- **Entregas:** Arquitetura, scripts Unity, plano de desenvolvimento
- **Diferencial:** Segue boas práticas (SOLID, ScriptableObjects, Event System)

### 3. Agente QA (Quality Assurance)
- **Função:** Validar implementação comparando com escopo do PO
- **Entregas:** Relatório de testes, issues, parecer final
- **Diferencial:** Testes abrangentes (happy path, edge cases, error cases)

## 🚀 Como Executar

### Opção 1: Alibaba Cloud DashScope (Recomendado)

1. **Obtenha sua API Key:**
   - Acesse https://dashscope.console.aliyun.com/
   - Crie uma conta e gere uma API Key

2. **Configure o ambiente:**
   ```bash
   cp .env.example .env
   # Edite .env e adicione sua DASHSCOPE_API_KEY
   ```

3. **Instale as dependências:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Execute o script:**
   ```bash
   python unity_game_agents_dashscope.py
   ```

### Opção 2: Ollama Local

1. **Instale o Ollama:**
   - Acesse https://ollama.ai
   - Baixe e instale para seu sistema operacional

2. **Baixe o modelo Qwen:**
   ```bash
   ollama run qwen2.5-coder:32b
   ```

3. **Configure o ambiente:**
   ```bash
   cp .env.example .env
   # Descomente as linhas do Ollama no .env
   ```

4. **Execute o script:**
   ```bash
   python unity_game_agents_crew.py
   ```

## 📁 Estrutura do Projeto

```
/workspace/
├── unity_game_agents_crew.py       # Script para Ollama local
├── unity_game_agents_dashscope.py  # Script para DashScope (recomendado)
├── requirements.txt                # Dependências Python
├── .env.example                    # Template de variáveis de ambiente
├── README.md                       # Este arquivo
└── docs/                           # Documentação gerada pelos agentes
    ├── README_AGENTES.md           # Contexto completo do projeto
    ├── game_scope.md               # Escopo definido pelo PO
    ├── technical_specs.md          # Especificações técnicas do DEV
    └── qa_report.md                # Relatório de validação do QA
```

## 🎨 Estilo Visual Magicraft

O projeto está configurado para jogos com estilo **Pixel Art HD**:

| Elemento | Resolução | Descrição |
|----------|-----------|-----------|
| Personagens | 128x128 a 256x256 | Alta resolução para detalhes |
| Chefes | 128x128 a 256x256 | Detalhes elevados |
| Efeitos de Magia | 128x128 a 256x256 | Partículas complexas |
| Tilesets | 64x64 ou 32x32 | Grade para ambiente |
| Ícones UI | 64x64 | Interface do usuário |

## 🔧 Configuração Personalizada

Para alterar o conceito do jogo, edite a variável `game_concept` no script:

```python
game_concept = """
Descreva aqui o conceito do seu jogo...
Inclua gênero, mecânicas principais, estilo visual, etc.
"""
```

## 📋 Fluxo de Execução

```
Conceito do Jogo
       ↓
┌─────────────┐
│   Agente    │ → Documento de Escopo
│     PO      │   (Mecânicas, Features, Visual)
└──────┬──────┘
       ↓
┌─────────────┐
│   Agente    │ → Especificações Técnicas + Código C#
│     DEV     │   (Arquitetura, Scripts, Plano)
└──────┬──────┘
       ↓
┌─────────────┐
│   Agente    │ → Relatório de Validação
│     QA      │   (Testes, Issues, Parecer)
└──────┬──────┘
       ↓
Entrega Final
```

## ⚠️ Tratamento de Ambiguidades

O sistema foi projetado para identificar e questionar pontos pouco claros:

- **PO:** Lista perguntas sobre requisitos vagos no conceito
- **DEV:** Solicita esclarecimentos sobre especificações ambíguas
- **QA:** Reporta inconsistências entre escopo e implementação

## 📦 Dependências

- `crewai` - Orquestração de agentes
- `langchain-openai` - Integração com LLMs via API compatível
- `python-dotenv` - Gerenciamento de variáveis de ambiente
- `dashscope` - SDK da Alibaba Cloud (opcional)

## 🔗 Links Úteis

- [DashScope Console](https://dashscope.console.aliyun.com/)
- [Ollama Download](https://ollama.ai)
- [CrewAI Documentation](https://docs.crewai.com/)
- [Unity Documentation](https://docs.unity3d.com/)

---

**Versão:** 1.1  
**Framework:** CrewAI + LangChain + Qwen  
**Modelos Suportados:** Qwen-Max, Qwen-Plus, Qwen2.5-Coder
