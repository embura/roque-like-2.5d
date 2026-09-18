"""
Skill de Orquestração para Time de Desenvolvimento de Jogos Unity
Framework: CrewAI
Agentes: PO (Product Owner), DEV (Engenheiro de Software), QA (Quality Assurance)
"""

import os
from crewai import Agent, Task, Crew, Process
from langchain_openai import ChatOpenAI

# Configuração do LLM (Certifique-se de ter a variável de ambiente OPENAI_API_KEY configurada)
llm = ChatOpenAI(model="gpt-4o", temperature=0.7)

def create_unity_dev_crew(game_idea: str):
    """
    Cria e executa a crew de desenvolvimento de jogos Unity.
    
    Args:
        game_idea (str): A ideia inicial ou descrição breve do jogo.
    """

    # --- Definição dos Agentes ---

    # 1. Product Owner (PO)
    po_agent = Agent(
        role='Product Owner (PO) de Jogos Unity',
        goal='Definir o escopo claro, funcionalidades e requisitos do jogo, garantindo que não haja ambiguidades.',
        backstory='Você é um PO experiente em desenvolvimento de jogos. Sua especialidade é transformar ideias vagas em documentos de design de jogo (GDD) estruturados. Se a ideia inicial for vaga, você deve fazer perguntas clarificadoras antes de prosseguir.',
        verbose=True,
        allow_delegation=False,
        llm=llm
    )

    # 2. Engenheiro de Software (DEV)
    dev_agent = Agent(
        role='Engenheiro de Software Unity (DEV)',
        goal='Criar especificações técnicas, plano de implementação e gerar o código C# necessário para as funcionalidades definidas pelo PO.',
        backstory='Você é um desenvolvedor sênior Unity especializado em C#. Você recebe o escopo do PO e cria a arquitetura, scripts de controle, física e UI. Você só começa a codificar após aprovar a clareza dos requisitos.',
        verbose=True,
        allow_delegation=False,
        llm=llm
    )

    # 3. Quality Assurance (QA)
    qa_agent = Agent(
        role='Quality Assurance (QA) de Jogos',
        goal='Validar a implementação e as especificações técnicas comparando-as estritamente com o escopo definido pelo PO.',
        backstory='Você é um tester rigoroso. Sua função é garantir que o que o DEV planejou/codificou atenda exatamente ao que o PO escreveu. Se houver divergência ou falta de cobertura de requisitos, você deve reportar falhas.',
        verbose=True,
        allow_delegation=False,
        llm=llm
    )

    # --- Definição das Tarefas ---

    # Tarefa do PO
    task_po = Task(
        description=f"""
        Analise a seguinte ideia de jogo: "{game_idea}".
        
        1. Avalie se há ambiguidades ou falta de clareza.
        2. Se houver ambiguidade, gere uma lista de perguntas para o usuário (simulado) antes de finalizar o escopo. 
           (Nota: Neste fluxo automático, se houver dúvida, assuma o padrão mais comum de mercado mas destaque as suposições feitas).
        3. Escreva o Escopo do Jogo e a Lista de Funcionalidades (Game Design Document - GDD resumido).
        4. O documento deve incluir: Gênero, Mecânicas Principais, Controles, Condição de Vitória/Derrota e Estética sugerida.
        
        Saída esperada: Um documento de escopo estruturado.
        """,
        expected_output='Documento de Escopo do Jogo (GDD Resumido) com funcionalidades claras e sem ambiguidades.',
        agent=po_agent
    )

    # Tarefa do DEV
    task_dev = Task(
        description="""
        Com base no Documento de Escopo criado pelo PO:
        
        1. Crie as Especificações Técnicas: Arquitetura de pastas, padrões de design a serem usados (ex: Singleton, Observer), e dependências Unity necessárias.
        2. Elabore um Plano de Desenvolvimento passo-a-passo.
        3. Implemente (gere o código) dos scripts C# principais para as mecânicas centrais definidas no escopo.
           - Inclua comentários explicativos no código.
           - Foque em scripts como: PlayerController, GameManager, InputHandler, etc., conforme necessário.
        
        Certifique-se de que cada funcionalidade listada pelo PO tenha uma contraparte técnica/código.
        """,
        expected_output='Especificações Técnicas, Plano de Desenvolvimento e Blocos de Código C# para Unity.',
        agent=dev_agent,
        context=[task_po] # Dependência da tarefa do PO
    )

    # Tarefa do QA
    task_qa = Task(
        description="""
        Valide a entrega do DEV comparando com o Escopo do PO.
        
        1. Verifique se todas as funcionalidades listadas no Escopo do PO foram contempladas nas Especificações Técnicas e no Código do DEV.
        2. Identifique quaisquer lacunas, erros de lógica ou desvios do escopo original.
        3. Gere um Relatório de Validação contendo:
           - Status (Aprovado / Reprovado / Aprovado com Ressalvas).
           - Lista de requisitos atendidos.
           - Lista de problemas encontrados ou sugestões de melhoria.
           
        Se houver falha crítica na cobertura dos requisitos, descreva o que falta para o DEV refazer.
        """,
        expected_output='Relatório de Validação de QA comparando Escopo vs Implementação.',
        agent=qa_agent,
        context=[task_po, task_dev] # Dependência das tarefas do PO e DEV
    )

    # --- Criação da Crew (Orquestração) ---
    
    crew = Crew(
        agents=[po_agent, dev_agent, qa_agent],
        tasks=[task_po, task_dev, task_qa],
        process=Process.sequential,  # Garante a ordem: PO -> DEV -> QA
        verbose=2,
        llm=llm
    )

    return crew

if __name__ == "__main__":
    # Exemplo de uso
    ideia_jogo = input("Descreva sua ideia de jogo para o time Unity: ")
    
    if not ideia_jogo.strip():
        ideia_jogo = "Um jogo de plataforma 2D onde um robô coleta baterias em um cenário pós-apocalíptico e evita armadilhas elétricas."

    print(f"Iniciando orquestração para o jogo: {ideia_jogo}...")
    
    crew = create_unity_dev_crew(ideia_jogo)
    resultado = crew.kickoff()
    
    print("\n--- Resultado Final ---")
    print(resultado)
