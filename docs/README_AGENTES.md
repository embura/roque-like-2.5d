# Documentação do Projeto - Time de Agentes para Desenvolvimento de Jogos Unity

## Visão Geral

Este projeto implementa um sistema de orquestração de agentes baseado em **CrewAI** para desenvolvimento de jogos Unity. O time é composto por três agentes especializados que trabalham de forma sequencial e colaborativa.

---

## Arquitetura dos Agentes

### 1. Agente PO (Product Owner)

**Role:** Product Owner Especialista em Jogos Unity

**Objetivo:**
- Definir o escopo completo do jogo
- Estabelecer mecânicas, funcionalidades e estilo visual
- Criar documentação clara para base do desenvolvimento

**Responsabilidades:**
- Definir visão geral do jogo (gênero, tema, público-alvo)
- Especificar mecânicas principais (combate, magia, progressão, IA)
- Estabelecer estilo visual (Pixel Art HD estilo Magicraft)
- Listar funcionalidades detalhadas
- Definir critérios de aceite

**Backstory:**
Product Owner experiente em desenvolvimento de jogos indie, especializado em jogos de ação com elementos de RPG e magia.

---

### 2. Agente DEV (Engenheiro de Software)

**Role:** Engenheiro de Software Sênior Unity (C#)

**Objetivo:**
- Transformar o escopo do PO em especificações técnicas
- Criar plano de desenvolvimento
- Implementar código C# para Unity

**Responsabilidades:**
- Definir arquitetura do projeto Unity
- Estruturar pastas e organização do projeto
- Aplicar padrões de design adequados
- Criar plano de desenvolvimento por fases/sprints
- Implementar scripts C# completos e comentados
- Seguir princípios SOLID e boas práticas

**Tecnologias e Práticas:**
- ScriptableObjects para configurações
- Event system para desacoplamento
- Object pooling para performance
- State machines para IA e estados
- Arquitetura limpa e escalável

**Backstory:**
Engenheiro de software sênior com 10+ anos de experiência em Unity, especialista em C#, arquitetura de jogos, sistemas de magia, IA de inimigos e otimização.

---

### 3. Agente QA (Quality Assurance)

**Role:** QA Specialist em Jogos Unity

**Objetivo:**
- Validar a implementação comparando com o escopo do PO
- Identificar bugs, inconsistências e gaps
- Gerar relatórios de teste acionáveis

**Responsabilidades:**
- Análise de conformidade com o escopo original
- Revisão de código (boas práticas, bugs potenciais)
- Criação de casos de teste funcionais
- Definição de cenários de teste (happy path, edge cases, error cases)
- Relatório de validação com issues classificados
- Parecer final (aprovado/reprovado/com ressalvas)

**Backstory:**
Especialista em QA de jogos com foco em Unity, experiente em testes funcionais, de regressão, performance e usabilidade.

---

## Fluxo de Trabalho (Workflow)

```
┌─────────────────┐
│     CONCEITO    │
│     DO JOGO     │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│   AGENTE PO     │
│  Define Escopo  │
│  e Funcionalidades│
└────────┬────────┘
         │ (Documento de Escopo)
         ▼
┌─────────────────┐
│   AGENTE DEV    │
│ Especificações  │
│ Técnicas + Código│
└────────┬────────┘
         │ (Implementação)
         ▼
┌─────────────────┐
│   AGENTE QA     │
│   Validação e   │
│    Testes       │
└────────┬────────┘
         │ (Relatório Final)
         ▼
┌─────────────────┐
│   ENTREGA       │
│   APROVADA      │
└─────────────────┘
```

### Processo Sequencial

1. **Fase 1 - PO:** Cria documento de escopo completo
2. **Fase 2 - DEV:** Recebe escopo do PO, cria especificações técnicas e implementa código
3. **Fase 3 - QA:** Recebe escopo do PO e implementação do DEV, valida e gera relatório

---

## Estilo Visual do Jogo (Magicraft - Pixel Art HD)

### Especificações Técnicas Visuais

| Elemento | Resolução | Descrição |
|----------|-----------|-----------|
| Personagens | 128x128 a 256x256 | Alta resolução para detalhes, expressões e deformações suaves |
| Chefes | 128x128 a 256x256 | Detalhes elevados e efeitos complexos |
| Efeitos de Magia | 128x128 a 256x256 | Partículas complexas e animações fluidas |
| Tilesets (pisos, paredes) | 64x64 ou 32x32 | Grade para obstáculos e ambiente |
| Ícones de Interface | 64x64 | Ícones de magias, inventário, cajados |

### Características do Estilo

- **Hand-painted High-Res Pixel Art**: Arte pixelada de alta resolução com acabamento pintado à mão
- **Paleta de Cores**: Atmosfera visual definida conforme tema do jogo
- **Partículas Complexas**: Efeitos visuais elaborados para magias e habilidades
- **Animações Suaves**: Deformações e transições fluidas entre frames

---

## Configuração Técnica

### Framework Utilizado

- **CrewAI**: Orquestração de agentes autônomos
- **LangChain**: Integração com LLMs
- **ChatOpenAI (Compatível)**: Interface para modelos Qwen via API compatível

### Modelo de Linguagem: Qwen

O sistema foi configurado para utilizar o modelo **Qwen** (da série Qwen2.5), oferecendo as seguintes opções de deployment:

#### Opção 1: Ollama Local (Recomendado para Desenvolvimento)
- **URL Base:** `http://localhost:11434/v1`
- **Modelo:** `qwen2.5-coder:32b` (ou variantes como `qwen2.5:72b`)
- **API Key:** `not-needed` (não requer autenticação para uso local)
- **Vantagens:** Gratuito, roda offline, privacidade total
- **Instalação:** 
  ```bash
  # Instale o Ollama em https://ollama.ai
  ollama run qwen2.5-coder:32b
  ```

#### Opção 2: Alibaba Cloud DashScope
- **URL Base:** `https://dashscope.aliyuncs.com/compatible-mode/v1`
- **Modelo:** `qwen-max` ou `qwen-plus`
- **API Key:** Requer cadastro em https://dashscope.console.aliyun.com/
- **Vantagens:** Alta performance, escalabilidade, modelos mais recentes

#### Opção 3: Outros Provedores Compatíveis
- Qualquer provedor que ofereça API compatível com OpenAI
- Configure `QWEN_BASE_URL`, `QWEN_API_KEY` e `QWEN_MODEL` no `.env`

## Estrutura do Projeto

```
/workspace/
├── unity_game_agents_crew.py    # Script principal de orquestração dos agentes
├── requirements.txt             # Dependências Python (crewai, langchain, openai)
├── .env.example                 # Template de variáveis de ambiente
├── README.md                    # Documentação principal
└── docs/                        # Documentação gerada pelos agentes
    ├── README_AGENTES.md        # Contexto do projeto e funcionamento dos agentes
    ├── game_scope.md            # Escopo definido pelo Agente PO
    ├── technical_specs.md       # Especificações técnicas e plano do Agente DEV
    └── qa_report.md             # Relatório de validação e testes do Agente QA
```

### Variáveis de Ambiente Necessárias

Configure no arquivo `.env` (copie de `.env.example`):

```bash
# Para Ollama Local (Recomendado)
QWEN_BASE_URL=http://localhost:11434/v1
QWEN_API_KEY=not-needed
QWEN_MODEL=qwen2.5-coder:32b

# OU para Alibaba Cloud DashScope
# QWEN_BASE_URL=https://dashscope.aliyuncs.com/compatible-mode/v1
# QWEN_API_KEY=sua_chave_dashscope_aqui
# QWEN_MODEL=qwen-max
```

---

## Como Executar

### 1. Instalar Dependências

```bash
pip install -r requirements.txt
```

### 2. Configurar Qwen

**Opção A - Ollama Local (Recomendado):**
```bash
# Instale o Ollama em https://ollama.ai
ollama run qwen2.5-coder:32b

# Em outro terminal, configure o .env
cp .env.example .env
# Edite .env com as configurações do Ollama (já vem pré-configurado)
```

**Opção B - Alibaba Cloud DashScope:**
```bash
cp .env.example .env
# Edite .env e adicione sua chave da API DashScope
```

### 3. Executar o Crew

```bash
python unity_game_agents_crew.py
```

### 4. Personalizar Conceito do Jogo

Edite a variável `game_concept` no arquivo `unity_game_agents_crew.py`:

```python
game_concept = """
Descreva aqui o conceito do seu jogo...
"""
```

---

## Critérios de Qualidade

### Para o Agente PO

- [ ] Escopo claro e sem ambiguidades
- [ ] Todas as mecânicas principais definidas
- [ ] Estilo visual especificado com detalhes técnicos
- [ ] Critérios de aceite mensuráveis
- [ ] Funcionalidades listadas completamente

### Para o Agente DEV

- [ ] Arquitetura bem estruturada
- [ ] Código seguindo boas práticas (SOLID)
- [ ] Scripts completos e comentados
- [ ] Plano de desenvolvimento realista
- [ ] Instruções claras de integração

### Para o Agente QA

- [ ] Validação completa contra escopo
- [ ] Casos de teste abrangentes
- [ ] Issues classificados por severidade
- [ ] Sugestões de melhoria construtivas
- [ ] Parecer final fundamentado

---

## Tratamento de Ambiguidades

Quando qualquer agente identificar pontos de ambiguidade ou falta de clareza:

1. **PO**: Deve questionar o usuário para esclarecer requisitos vagos
2. **DEV**: Deve solicitar esclarecimentos ao PO antes de implementar
3. **QA**: Deve reportar inconsistências entre escopo e implementação

O sistema foi projetado para ser iterativo e colaborativo, garantindo que dúvidas sejam resolvidas antes de prosseguir para a próxima fase.

---

## Próximos Passos

1. Executar o crew com o conceito do jogo
2. Revisar documentação gerada na pasta `docs/`
3. Iterar sobre feedbacks do QA
4. Implementar código gerado no projeto Unity
5. Executar testes manuais no Unity Editor

---

## Contribuição

Para adicionar novos agentes ou modificar o fluxo:

1. Edite `unity_game_agents_crew.py`
2. Adicione novos agentes na seção `==================== AGENTES ====================`
3. Crie novas tarefas na seção `==================== TAREFAS ====================`
4. Atualize a Crew na seção `==================== ORQUESTRAÇÃO (CREW) ====================`

---

**Versão:** 1.1  
**Última Atualização:** 2024  
**Framework:** CrewAI + LangChain + Qwen (via API compatível OpenAI)  
**Modelos Suportados:** Qwen2.5-Coder (32B, 72B), Qwen-Max, Qwen-Plus
