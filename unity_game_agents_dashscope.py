"""
CrewAI - Orquestração de Time de Agentes para Desenvolvimento de Jogos Unity
Time composto por: PO (Product Owner), DEV (Engenheiro de Software), QA (Quality Assurance)
Configurado para usar modelo Qwen via DashScope (Alibaba Cloud)
"""

from crewai import Agent, Task, Crew, Process
from langchain_openai import ChatOpenAI
import os
from dotenv import load_dotenv

# Carregar variáveis de ambiente
load_dotenv()

# Configurar LLM para usar Qwen via Alibaba Cloud DashScope
DASHSCOPE_API_KEY = os.getenv("DASHSCOPE_API_KEY")
DASHSCOPE_BASE_URL = "https://dashscope.aliyuncs.com/compatible-mode/v1"
QWEN_MODEL = os.getenv("QWEN_MODEL", "qwen-max")

if not DASHSCOPE_API_KEY:
    print("⚠️  AVISO: DASHSCOPE_API_KEY não configurada!")
    print("   Obtenha sua chave em: https://dashscope.console.aliyun.com/")
    print("   Ou configure no arquivo .env:\n")
    print("   DASHSCOPE_API_KEY=sua_chave_aqui\n")
    exit(1)

# Criar instância da LLM usando DashScope
llm_instance = ChatOpenAI(
    model=QWEN_MODEL,
    temperature=0.7,
    api_key=DASHSCOPE_API_KEY,
    base_url=DASHSCOPE_BASE_URL
)

# ==================== AGENTES ====================

# Agente PO - Product Owner
po_agent = Agent(
    role="Product Owner (PO) Especialista em Jogos Unity",
    goal="""
    Definir o escopo completo do jogo, incluindo mecânicas, funcionalidades, 
    estilo visual e experiência do jogador. Criar documentação clara e detalhada
    que sirva de base para o desenvolvimento.
    
    IMPORTANTE: Se houver ambiguidade ou falta de clareza no conceito do jogo,
    faça questionamentos específicos para obter esclarecimentos antes de prosseguir.
    """,
    backstory="""
    Você é um Product Owner experiente em desenvolvimento de jogos indie,
    especializado em jogos de ação com elementos de RPG e magia. Tem profundo
    conhecimento em design de jogos, balanceamento e definição de escopo para
    equipes ágeis. Seu foco é garantir que o jogo tenha uma visão clara e
    funcionalidades bem definidas.
    """,
    verbose=True,
    allow_delegation=False,
    llm=llm_instance
)

# Agente DEV - Engenheiro de Software Unity
dev_agent = Agent(
    role="Engenheiro de Software Sênior Unity (C#)",
    goal="""
    Transformar o escopo definido pelo PO em especificações técnicas detalhadas,
    plano de desenvolvimento e implementação de código C# para Unity.
    Garantir arquitetura limpa, performance e boas práticas.
    
    IMPORTANTE: Se houver ambiguidade nas especificações do PO, solicite
    esclarecimentos antes de implementar.
    """,
    backstory="""
    Você é um engenheiro de software sênior com 10+ anos de experiência em Unity.
    Especialista em C#, arquitetura de jogos, sistemas de magia, IA de inimigos,
    física 2D/3D e otimização. Conhece profundamente o pipeline de desenvolvimento
    de jogos e sabe traduzir requisitos funcionais em código eficiente e escalável.
    """,
    verbose=True,
    allow_delegation=False,
    llm=llm_instance
)

# Agente QA - Quality Assurance
qa_agent = Agent(
    role="QA Specialist em Jogos Unity",
    goal="""
    Validar a implementação do DEV comparando com o escopo definido pelo PO.
    Identificar bugs, inconsistências, gaps de funcionalidade e problemas de UX.
    Gerar relatórios de teste claros e acionáveis.
    
    IMPORTANTE: Reporte qualquer inconsistência entre escopo e implementação.
    """,
    backstory="""
    Você é um especialista em QA de jogos com foco em Unity. Tem experiência
    em testes funcionais, de regressão, performance e usabilidade. Sabe criar
    planos de teste, executar validações sistemáticas e reportar issues de forma
    clara para a equipe de desenvolvimento.
    """,
    verbose=True,
    allow_delegation=False,
    llm=llm_instance
)

# ==================== TAREFAS ====================

def create_scope_task(game_concept: str):
    """Tarefa do PO: Definir escopo do jogo"""
    return Task(
        description=f"""
        Como Product Owner, defina o escopo completo do jogo com base no conceito:
        "{game_concept}"
        
        Sua entrega deve incluir:
        
        1. **VISÃO GERAL DO JOGO**
           - Gênero, tema, público-alvo
           - Premissa e narrativa (se aplicável)
           - Duração estimada da experiência
        
        2. **MECÂNICAS PRINCIPAIS**
           - Sistema de combate (se houver)
           - Sistema de magia/habilidades
           - Progressão do personagem
           - Sistema de inimigos e chefes
           - Economia do jogo (moedas, upgrades, etc.)
        
        3. **ESTILO VISUAL - MAGICRAFT (Pixel Art HD)**
           - Personagens, chefes e efeitos: 128x128 a 256x256 pixels
           - Tilesets (pisos, paredes, obstáculos): 64x64 ou 32x32 pixels
           - Ícones de interface: 64x64 pixels
           - Estilo hand-painted high-res pixel art
           - Paleta de cores e atmosfera visual
           - Efeitos de partículas complexos
        
        4. **FUNCIONALIDADES DETALHADAS**
           - Lista completa de features jogáveis
           - Sistemas de UI/UX necessários
           - Áudio e trilha sonora
           - Controles e input
        
        5. **CRITÉRIOS DE ACEITE**
           - O que define que cada funcionalidade está completa
           - Métricas de qualidade esperadas
        
        Escreva de forma clara, estruturada e sem ambiguidades para que o 
        engenheiro possa implementar sem dúvidas.
        
        SE HOUVER AMBIGUIDADES: Liste as perguntas que precisam ser respondidas
        antes de prosseguir para a próxima fase.
        """,
        expected_output="""
        Documento de escopo completo do jogo contendo:
        - Visão geral
        - Mecânicas principais
        - Especificações visuais (Pixel Art HD estilo Magicraft)
        - Lista detalhada de funcionalidades
        - Critérios de aceite claros
        - (Opcional) Perguntas para esclarecimento de ambiguidades
        """,
        agent=po_agent
    )

def create_implementation_task():
    """Tarefa do DEV: Criar especificações técnicas e implementar"""
    return Task(
        description="""
        Como Engenheiro de Software Unity, com base no escopo fornecido pelo PO:
        
        1. **ESPECIFICAÇÕES TÉCNICAS**
           - Arquitetura do projeto Unity
           - Estrutura de pastas e organização
           - Padrões de design a serem utilizados
           - Sistemas principais (combate, magia, IA, etc.)
        
        2. **PLANO DE DESENVOLVIMENTO**
           - Fases/sprints de implementação
           - Dependências entre sistemas
           - Estimativa de esforço por feature
           - Riscos técnicos e mitigação
        
        3. **IMPLEMENTAÇÃO DE CÓDIGO**
           - Scripts C# para os sistemas principais
           - Componentes Unity necessários
           - Configurações de prefabs
           - Integração entre sistemas
           
        Gere código C# completo, comentado e seguindo boas práticas:
        - SOLID principles
        - ScriptableObjects para configurações
        - Event system para desacoplamento
        - Pooling para performance
        - State machines para IA e estados do jogador
        
        Inclua exemplos de:
        - Controller do personagem
        - Sistema de magia/habilidades
        - IA de inimigos básicos
        - Sistema de spawn/inimigos
        - UI manager
        
        SE HOUVER AMBIGUIDADES: Liste as questões técnicas que precisam de
        esclarecimento antes de implementar.
        """,
        expected_output="""
        Documento técnico contendo:
        - Especificações técnicas detalhadas
        - Plano de desenvolvimento por fases
        - Código C# completo dos sistemas principais
        - Instruções de integração no Unity
        - (Opcional) Questões técnicas para esclarecimento
        """,
        agent=dev_agent,
        context=[]  # Será preenchido com output do PO
    )

def create_validation_task():
    """Tarefa do QA: Validar implementação"""
    return Task(
        description="""
        Como QA Specialist, valide a implementação do DEV comparando com o escopo do PO:
        
        1. **ANÁLISE DE CONFORMIDADE**
           - Todas as funcionalidades do escopo foram implementadas?
           - Há desvios dos requisitos originais?
           - Os critérios de aceite foram atendidos?
        
        2. **REVISÃO DE CÓDIGO**
           - O código segue boas práticas?
           - Há potenciais bugs ou code smells?
           - A arquitetura está adequada?
        
        3. **TESTES FUNCIONAIS**
           - Crie casos de teste para cada funcionalidade
           - Defina cenários de teste (happy path, edge cases, error cases)
           - Especifique critérios de aprovação/reprovação
        
        4. **RELATÓRIO DE VALIDAÇÃO**
           - Liste issues encontrados (críticos, majors, minors)
           - Sugira melhorias
           - Aprovação ou reprovação da entrega
           - Próximos passos recomendados
        
        Seja rigoroso mas construtivo. Aponte problemas específicos com referências
        ao escopo original e sugira correções claras.
        """,
        expected_output="""
        Relatório de validação contendo:
        - Análise de conformidade com o escopo
        - Revisão de código
        - Casos de teste definidos
        - Lista de issues (se houver)
        - Parecer final (aprovado/reprovado/com ressalvas)
        """,
        agent=qa_agent,
        context=[]  # Será preenchido com outputs do PO e DEV
    )

# ==================== ORQUESTRAÇÃO (CREW) ====================

def run_game_dev_crew(game_concept: str):
    """
    Executa o time de agentes para desenvolvimento do jogo
    
    Args:
        game_concept: Descrição inicial do conceito do jogo
    
    Returns:
        Resultado completo da execução do crew
    """
    
    # Criar tarefas
    scope_task = create_scope_task(game_concept)
    implementation_task = create_implementation_task()
    validation_task = create_validation_task()
    
    # Configurar contexto das tarefas dependentes
    implementation_task.context = [scope_task]
    validation_task.context = [scope_task, implementation_task]
    
    # Criar Crew
    crew = Crew(
        agents=[po_agent, dev_agent, qa_agent],
        tasks=[scope_task, implementation_task, validation_task],
        process=Process.sequential,  # Execução sequencial: PO -> DEV -> QA
        verbose=True,
        memory=True,  # Manter contexto entre tarefas
        cache=True    # Cache de resultados
    )
    
    # Executar
    print("=" * 60)
    print("🎮 INICIANDO TIME DE DESENVOLVIMENTO DE JOGOS UNITY")
    print("=" * 60)
    print(f"\nConceito do Jogo: {game_concept}\n")
    print("=" * 60)
    print(f"Modelo Qwen: {QWEN_MODEL}")
    print(f"Base URL: {DASHSCOPE_BASE_URL}")
    print("=" * 60)
    
    result = crew.kickoff()
    
    print("\n" + "=" * 60)
    print("✅ PROCESSO CONCLUÍDO")
    print("=" * 60)
    
    return result

# ==================== EXECUÇÃO ====================

if __name__ == "__main__":
    # Conceito inicial do jogo
    game_concept = """
    Um jogo de ação roguelike em arena com sistema de magia combinatória.
    O jogador é um mago que deve sobreviver a ondas de inimigos em salas fechadas,
    coletando cristais de mana para desbloquear novas magias e combinações.
    Cada run é única com power-ups aleatórios e salas proceduralmente geradas.
    
    ESTILO VISUAL - MAGICRAFT (Pixel Art HD):
    - Personagens, chefes e efeitos: 128x128 a 256x256 pixels
    - Tilesets (pisos, paredes, obstáculos): 64x64 ou 32x32 pixels
    - Ícones de interface: 64x64 pixels
    - Estilo hand-painted high-res pixel art
    - Paleta de cores vibrante com atmosfera mágica
    - Efeitos de partículas complexos para magias
    """
    
    # Executar o crew
    result = run_game_dev_crew(game_concept)
    
    # Exibir resultados
    print("\n" + "=" * 60)
    print("📋 RESULTADOS COMPLETOS")
    print("=" * 60)
    print(result)

