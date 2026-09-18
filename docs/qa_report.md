# Relatório de Validação QA

**Gerado por:** Agente QA (Quality Assurance Specialist)  
**Baseado em:** 
- Documento de Escopo v1.0 (Agente PO)
- Especificações Técnicas v1.0 (Agente DEV)

**Data:** 2024  
**Versão:** 1.0  
**Status da Validação:** ⏳ Aguardando Implementação

---

## 1. RESUMO EXECUTIVO

Este documento estabelece o **plano de validação** para o projeto "Magic Survival Arena". Como a implementação ainda não foi concluída, este relatório serve como:

1. **Checklist de critérios de aceite** baseados no escopo do PO
2. **Plano de testes** para validação da implementação
3. **Template de reporte de issues** para quando a implementação estiver disponível
4. **Guia de revisão de código** baseado nas especificações do DEV

---

## 2. ANÁLISE DE CONFORMIDADE DO ESCOPO

### 2.1 Critérios de Aceite do MVP (Conforme PO)

#### Movimento e Combate
| ID | Critério | Status | Evidência | Notas |
|----|----------|--------|-----------|-------|
| MV-01 | Personagem move-se suavemente em 8 direções | ⏳ Pendente | - | Testar com input contínuo em todas direções |
| MV-02 | Sistema de colisão funcional com paredes e inimigos | ⏳ Pendente | - | Verificar camadas de colisão |
| MV-03 | Esquiva (dash) com i-frames e cooldown | ⏳ Pendente | - | Testar timing de invencibilidade |
| MV-04 | Pelo menos 3 magias de projétil implementadas | ⏳ Pendente | - | Fogo, Gelo, Raio como mínimo |
| MV-05 | Inimigos spawnam e perseguem o jogador | ⏳ Pendente | - | Testar pathfinding |
| MV-06 | Sistema de dano e morte funcionando | ⏳ Pendente | - | Verificar cálculo de dano |

#### Sistema de Magia
| ID | Critério | Status | Evidência | Notas |
|----|----------|--------|-----------|-------|
| MG-01 | 3 elementos base implementados | ⏳ Pendente | - | Fogo, Gelo, Raio |
| MG-02 | Sistema de cooldown visível na UI | ⏳ Pendente | - | Indicator visual claro |
| MG-03 | Combinação básica de 2 elementos funciona | ⏳ Pendente | - | Ex: Fogo+Raio = híbrido |
| MG-04 | Power-ups aplicam modificações nas magias | ⏳ Pendente | - | Testar multiplicadores |

#### Progressão
| ID | Critério | Status | Evidência | Notas |
|----|----------|--------|-----------|-------|
| PR-01 | Sistema de level up durante run | ⏳ Pendente | - | Thresholds de XP corretos |
| PR-02 | Escolha de power-ups após level up | ⏳ Pendente | - | 3 opções aleatórias |
| PR-03 | Cristais de mana dropam de inimigos | ⏳ Pendente | - | Drop rate balanceado |
| PR-04 | Moeda meta persiste entre runs | ⏳ Pendente | - | Save/load funcional |

#### Inimigos
| ID | Critério | Status | Evidência | Notas |
|----|----------|--------|-----------|-------|
| IN-01 | 3 tipos de inimigos comuns | ⏳ Pendente | - | Melee, Ranged, Swarm |
| IN-02 | 1 chefe implementado com 2 fases | ⏳ Pendente | - | Lord Ignis recomendado |
| IN-03 | Sistema de afíxes em elites | ⏳ Pendente | - | Random affix assignment |
| IN-04 | Pathfinding básico funcionando | ⏳ Pendente | - | NavMesh ou customizado |

#### UI/UX
| ID | Critério | Status | Evidência | Notas |
|----|----------|--------|-----------|-------|
| UI-01 | HUD com HP, Mana, Cristais, Magias | ⏳ Pendente | - | Todas informações visíveis |
| UI-02 | Menu principal funcional | ⏳ Pendente | - | Start, Options, Quit |
| UI-03 | Tela de game over com stats | ⏳ Pendente | - | Tempo, kills, moedas |
| UI-04 | Sistema de pause | ⏳ Pendente | - | Pause/Resume funcionais |

#### Visual
| ID | Critério | Status | Evidência | Notas |
|----|----------|--------|-----------|-------|
| VS-01 | Sprite do jogador com animações básicas | ⏳ Pendente | - | Idle, Run, Cast mínimo |
| VS-02 | Sprites de inimigos com animações | ⏳ Pendente | - | Pelo menos idle e hit |
| VS-03 | Tileset funcional para arenas | ⏳ Pendente | - | Chão e paredes |
| VS-04 | Efeitos de partículas para magias | ⏳ Pendente | - | Cast e impact |
| VS-05 | Estilo consistente com Pixel Art HD | ⏳ Pendente | - | Conforme specs Magicraft |

#### Áudio
| ID | Critério | Status | Evidência | Notas |
|----|----------|--------|-----------|-------|
| AU-01 | SFX para ações principais | ⏳ Pendente | - | Cast, hit, death, pickup |
| AU-02 | BGM para gameplay e menu | ⏳ Pendente | - | Pelo menos 2 tracks |
| AU-03 | Mixer de volume funcional | ⏳ Pendente | - | Music, SFX separados |

#### Performance
| ID | Critério | Status | Evidência | Notas |
|----|----------|--------|-----------|-------|
| PF-01 | 60 FPS estáveis com 50 inimigos | ⏳ Pendente | - | Profiler required |
| PF-02 | Loading time < 3 segundos | ⏳ Pendente | - | Cena arena |
| PF-03 | Sem memory leaks em 30+ minutos | ⏳ Pendente | - | Monitorar GC e memória |

---

## 3. PLANO DE TESTES

### 3.1 Testes Funcionais

#### TF-01: Movimento do Jogador
**Objetivo:** Validar movimento 8-direcional

**Pré-condições:**
- Jogo iniciado em cena de arena
- Player spawned e controlável

**Passos:**
1. Pressionar W (cima) e observar movimento
2. Pressionar S (baixo) e observar movimento
3. Pressionar A (esquerda) e observar movimento
4. Pressionar D (direita) e observar movimento
5. Pressionar combinações diagonais (W+A, W+D, S+A, S+D)
6. Manter input e verificar velocidade constante
7. Soltar input e verificar parada imediata

**Resultado Esperado:**
- Personagem move-se em todas 8 direções
- Velocidade constante em todas direções (normalização correta)
- Parada imediata ao soltar input
- Animação de run sincronizada com movimento

**Critério de Aprovação:** Todos os passos executados sem bugs

---

#### TF-02: Sistema de Dash
**Objetivo:** Validar mecânica de esquiva com i-frames

**Pré-condições:**
- Player em cena de teste
- Inimigo com ataque projetil presente

**Passos:**
1. Pressionar Space para ativar dash
2. Observar direção do dash (deve seguir input de movimento)
3. Medir duração do dash (esperado: ~0.2s)
4. Tentar usar dash novamente imediatamente (deve estar em cooldown)
5. Aguardar cooldown (esperado: ~1s) e tentar novamente
6. Durante dash, receber ataque de inimigo

**Resultado Esperado:**
- Dash propulsa personagem na direção do movimento
- Duração corresponde ao configurado
- Cooldown impede uso consecutivo
- Durante dash, player não recebe dano (i-frames)

**Critério de Aprovação:** i-frames funcionam durante dash completo

---

#### TF-03: Casting de Magias
**Objetivo:** Validar sistema de lançamento de magias

**Pré-condições:**
- Player com pelo menos 3 magias equipadas
- Inimigos presentes na cena

**Passos:**
1. Pressionar botão de cast (clique esquerdo)
2. Observar direção do projétil
3. Verificar consumo de mana
4. Observar cooldown da magia
5. Tentar cast durante cooldown
6. Repetir para cada uma das 3 magias base
7. Verificar se projétil causa dano ao inimigo

**Resultado Esperado:**
- Projétil instanciado na direção correta
- Mana reduzida conforme magicData
- Cooldown visível na UI
- Cast bloqueado durante cooldown
- Dano aplicado ao inimigo no impacto

**Critério de Aprovação:** Todas 3 magias funcionais com feedback correto

---

#### TF-04: Sistema de Level Up
**Objetivo:** Validar progressão durante run

**Pré-condições:**
- Run iniciada
- Inimigos spawnando e dropando cristais

**Passos:**
1. Coletar cristais dropped por inimigos
2. Observar barra de XP/progresso
3. Atingir threshold de level up
4. Verificar pausa no gameplay
5. Selecionar um dos 3 power-ups apresentados
6. Retomar gameplay
7. Verificar se power-up aplicou efeito

**Resultado Esperado:**
- Cristais coletados incrementam contador
- Barra de XP preenche proporcionalmente
- Level up triggera selection screen
- Gameplay pausado durante seleção
- Power-up escolhido aplica modificadores corretamente

**Critério de Aprovação:** Fluxo completo de level up funcional

---

#### TF-05: Combinação de Elementos
**Objetivo:** Validar sistema de magias combinatórias

**Pré-condições:**
- Player com slots de magia disponíveis
- Pelo menos 2 elementos desbloqueados (ex: Fogo, Raio)

**Passos:**
1. Equipar magia de Fogo no slot 1
2. Equipar magia de Raio no slot 2
3. Observar se combinação é detectada
4. Verificar se nova magia híbrida é criada
5. Testar cast da magia combinada
6. Comparar efeitos com magias base individuais

**Resultado Esperado:**
- Sistema detecta combinação Fogo+Raio
- Nova magia híbrida é disponibilizada
- Efeito visual distinto da combinação
- Dano/efeito da combinação é único

**Critério de Aprovação:** Combinação detectada e funcional

---

#### TF-06: IA de Inimigos
**Objetivo:** Validar comportamento de inimigos

**Pré-condições:**
- Inimigos de tipos variados na cena
- Player presente e detectável

**Passos:**
1. Spawnar inimigo melee e observar comportamento
2. Spawnar inimigo ranged e observar comportamento
3. Spawnar inimigo swarm e observar comportamento
4. Player move-se para longe e verifica perseguição
5. Player para e verifica se inimigo ataca
6. Receber ataque e verificar knockback (se aplicável)

**Resultado Esperado:**
- Melee aproxima e ataca em curto range
- Ranged mantém distância e atira projéteis
- Swarm move-se rapidamente em grupo
- Todos perseguem player quando detectado
- Ataque causa dano e knockback apropriado

**Critério de Aprovação:** Cada tipo comporta-se conforme design

---

#### TF-07: Boss Fight
**Objetivo:** Validar mecânicas de chefe com múltiplas fases

**Pré-condições:**
- Boss (Lord Ignis) spawned na arena
- Player preparado para combate

**Passos:**
1. Iniciar combate com boss
2. Observar padrão de ataques na fase 1
3. Reduzir HP do boss para threshold de transição (~50%)
4. Verificar mudança de comportamento/fase
5. Observar novos ataques na fase 2
6. Derrotar boss
7. Verificar drop de loot garantido

**Resultado Esperado:**
- Fase 1 tem pattern de ataques reconhecível
- Transição de fase ocorre no HP threshold
- Boss invulnerável durante transição
- Fase 2 tem attacks diferentes/mais intensos
- Loot raro dropa ao derrotar boss

**Critério de Aprovação:** Ambas fases funcionais com mecânicas únicas

---

#### TF-08: Save/Load Meta-Progression
**Objetivo:** Validar persistência de dados entre runs

**Pré-condições:**
- Run completada ou terminada em game over
- Moeda meta acumulada

**Passos:**
1. Completar run (vitória ou derrota)
2. Verificar tela de resultados com moedas ganhas
3. Retornar ao hub/menu principal
4. Verificar se moeda total foi atualizada
5. Fechar jogo completamente
6. Reabrir jogo
7. Verificar se progresso meta persistiu

**Resultado Esperado:**
- Moedas ganhas exibidas na tela de game over
- Total de moeda meta atualizado no hub
- Dados persistem após fechar jogo
- Desbloqueios comprados permanecem disponíveis

**Critério de Aprovação:** Dados persistem corretamente entre sessões

---

### 3.2 Casos de Teste - Edge Cases

#### EC-01: Input Simultâneo Conflitante
**Cenário:** Player pressiona inputs opostos simultaneamente

**Passos:**
1. Pressionar W + S simultaneamente
2. Pressionar A + D simultaneamente
3. Pressionar todas 4 direções simultaneamente

**Resultado Esperado:**
- Personagem não se move (inputs se cancelam)
- Não há crash ou behavior inesperado
- Animação retorna para idle

---

#### EC-02: Spam de Casting
**Cenário:** Player tenta cast repetidamente durante cooldown

**Passos:**
1. Castear magia
2. Imediatamente pressionar botão de cast múltiplas vezes
3. Continuar pressionando durante cooldown inteiro

**Resultado Esperado:**
- Apenas primeiro cast é executado
- Inputs subsequentes são ignorados
- Não há erro ou crash
- Cooldown countdown é preciso

---

#### EC-03: Morte no Momento Exato de Level Up
**Cenário:** Player morre ao mesmo tempo que coleta cristal para level up

**Passos:**
1. Estar perto do threshold de level up
2. Coletar cristal enquanto recebe dano fatal
3. Observar ordem de execução dos eventos

**Resultado Esperado:**
- Sistema resolve conflito de forma consistente
- Ou level up ocorre antes da morte, ou morte prevalece
- Não há estado inconsistente (morto mas jogável)

---

#### EC-04: Spawn de Inimigos Fora dos Limites
**Cenário:** Verificar se inimigos spawnam dentro da arena válida

**Passos:**
1. Observar spawn points definidos
2. Verificar se algum spawn point está fora da arena (dentro de paredes)
3. Spawnar inimigo e verificar se está em posição válida

**Resultado Esperado:**
- Todos spawns ocorrem dentro da área jogável
- Inimigos não spawnam dentro de paredes/obstáculos
- Se spawn inválido, inimigo é reposicionado ou spawn cancelado

---

#### EC-05: Memory Leak em Longa Sessão
**Cenário:** Executar jogo por 30+ minutos com muitas ações

**Passos:**
1. Iniciar jogo e abrir Profiler
2. Jogar normalmente por 30 minutos
3. Monitorar memória RAM usada
4. Monitorar GC allocations
5. Contar objetos ativos no hierarchy

**Resultado Esperado:**
- Memória permanece estável (±50MB variação)
- GC occurs periodicamente mas não cresce indefinidamente
- Objetos pooled são retornados ao pool
- Não há crescimento contínuo de memória

---

### 3.3 Critérios de Performance

| Métrica | Target | Método de Medição | Status |
|---------|--------|-------------------|--------|
| FPS médio (gameplay) | ≥ 60 FPS | Unity Profiler | ⏳ Pendente |
| FPS mínimo (50 inimigos) | ≥ 60 FPS | Stress test | ⏳ Pendente |
| Loading time (arena) | < 3s | Cronômetro manual | ⏳ Pendente |
| Memory usage | < 512 MB | Task Manager / Profiler | ⏳ Pendente |
| CPU usage (quad-core) | < 50% | Task Manager | ⏳ Pendente |
| GC alloc/frame | < 100 KB | Unity Profiler | ⏳ Pendente |

---

## 4. REVISÃO DE CÓDIGO

### 4.1 Checklist de Boas Práticas

#### Arquitetura e Design Patterns
- [ ] Singleton implementado corretamente (thread-safe se necessário)
- [ ] EventBus usado para desacoplamento entre sistemas
- [ ] Object Pool implementado para projéteis e partículas
- [ ] ScriptableObjects usados para configurações e dados
- [ ] State Machine para comportamentos complexos (player, boss)

#### Qualidade de Código
- [ ] Nomes de variáveis/métodos descritivos (inglês ou português consistente)
- [ ] Métodos pequenos e com responsabilidade única (SRP)
- [ ] Comentários apenas onde necessário (código deve ser autoexplicativo)
- [ ] Classes com coesão alta e acoplamento baixo
- [ ] Tratamento de erros/nulos adequado

#### Performance
- [ ] Uso de `GetComponent` cacheado em `Awake`/`Start`
- [ ] Evitar `Find`, `FindWithTag`, `GetComponent` em `Update`
- [ ] Coroutines usadas apropriadamente (não para lógica crítica de tempo)
- [ ] Physics usando layers/masks para filtrar colisões desnecessárias
- [ ] Allocs de memória minimizados em loops e Update

#### Segurança e Robustez
- [ ] Validação de inputs do jogador
- [ ] Check de null antes de acessar referências
- [ ] Try-catch em operações de I/O (save/load)
- [ ] Timeout em operações assíncronas
- [ ] Sanitização de dados persistentes

---

### 4.2 Code Smells para Observar

| Code Smell | O Que Procurar | Ação Recomendada |
|------------|----------------|------------------|
| **God Class** | GameManager com 1000+ linhas | Extrair responsabilidades para classes menores |
| **Magic Numbers** | Valores hard-coded (ex: `if (health > 50)`) | Usar constantes ou ScriptableObjects |
| **Spaghetti Code** | Lógica complexa em Update() | Extrair métodos, usar State Machine |
| **Duplicate Code** | Mesma lógica em múltiplos lugares | Criar método/base class compartilhada |
| **Feature Envy** | Método acessa mais dados de outra classe | Mover método para classe apropriada |
| **Tight Coupling** | Classe referencia muitas outras diretamente | Usar interfaces, events, dependency injection |

---

## 5. TEMPLATE DE REPORTE DE ISSUES

Quando bugs forem encontrados durante testes, usar seguinte template:

```markdown
### Issue #XXX: [Título Descritivo]

**Severidade:** Crítico / Major / Minor / Cosmetic

**Descrição:**
[Descrição clara e concisa do problema]

**Pré-condições:**
- [Condição 1]
- [Condição 2]

**Passos para Reproduzir:**
1. [Passo 1]
2. [Passo 2]
3. [Passo 3]

**Resultado Atual:**
[O que acontece atualmente]

**Resultado Esperado:**
[O que deveria acontecer conforme escopo/design]

**Frequência:**
[ ] Sempre (100%)
[ ] Frequentemente (>50%)
[ ] Às vezes (<50%)
[ ] Raramente

**Ambiente:**
- Unity Version: [ex: 2022.3.15f1]
- OS: [ex: Windows 11]
- Hardware: [ex: GTX 1060, i5-9400F, 16GB RAM]

**Evidências:**
- Screenshots: [anexar]
- Vídeo: [link se aplicável]
- Logs: [trecho relevante]

**Possível Causa Raiz:**
[Se identificável, especular sobre origem do bug]

**Sugestão de Correção:**
[Se aplicável, sugerir abordagem de fix]
```

---

## 6. CLASSIFICAÇÃO DE SEVERIDADE

| Severidade | Definição | Exemplo | Prazo de Resolução |
|------------|-----------|---------|-------------------|
| **Crítico** | Impede continuidade do jogo, crash, perda de dados | Crash ao iniciar, save corrompido | Imediato (24h) |
| **Major** | Feature principal não funciona, mas jogo continua | Magia não causa dano, boss não spawn | Alta prioridade (1 semana) |
| **Minor** | Feature secundária com problema, workaround existe | UI desalinhada, som não toca | Prioridade média (2 semanas) |
| **Cosmetic** | Problema visual menor, não afeta gameplay | Partícula com cor errada, typo | Backlog (próxima sprint) |

---

## 7. PARECER FINAL

### Status Atual: ⏳ AGUARDANDO IMPLEMENTAÇÃO

**Resumo:**
Os documentos de escopo (PO) e especificações técnicas (DEV) foram revisados e estão **APROVADOS** como base para desenvolvimento. Os critérios de aceite estão claros e mensuráveis.

**Próximos Passos:**
1. Agente DEV inicia implementação conforme plano de desenvolvimento
2. Ao final de cada fase, submeter para validação parcial deste QA
3. Ao completar MVP, executar bateria completa de testes
4. Reportar issues encontrados com template definido
5. Iterar até todos critérios MVP estarem atendidos

**Riscos Identificados:**
- Escopo pode crescer além do MVP definido → Manter foco nos critérios listados
- Performance pode ser negligenciada no início → Profiling desde Fase 1
- Balanceamento requer playtesting real → Planejar sessões de teste externas

**Recomendações:**
- Implementar CI/CD para builds automáticas
- Usar Unity Test Framework para testes automatizados
- Manter changelog detalhado de cada versão
- Documentar decisões técnicas importantes (ADR - Architecture Decision Records)

---

**Validado Por:** Agente QA  
**Data:** 2024  
**Próxima Revisão:** Após conclusão da Fase 4 (Inimigos e Combate) para validação parcial

---

## APÊNDICE A: Matriz de Rastreabilidade

| Requisito PO | Spec DEV | Caso de Teste QA | Status |
|--------------|----------|------------------|--------|
| MV-01 a MV-06 | PlayerController.cs | TF-01, TF-02 | ⏳ Pendente |
| MG-01 a MG-04 | MagicSystem.cs, MagicData.cs | TF-03, TF-05 | ⏳ Pendente |
| PR-01 a PR-04 | LevelUpSystem.cs, PowerUpData.cs | TF-04, TF-08 | ⏳ Pendente |
| IN-01 a IN-04 | EnemyBase.cs, EnemyAI.cs, BossController.cs | TF-06, TF-07 | ⏳ Pendente |
| UI-01 a UI-04 | UIManager.cs, HUDController.cs | TF-04, TF-08 | ⏳ Pendente |
| VS-01 a VS-05 | Asset pipeline, Animators | Visual review | ⏳ Pendente |
| AU-01 a AU-03 | AudioManager.cs | Audio review | ⏳ Pendente |
| PF-01 a PF-03 | ObjectPool.cs, optimizations | Performance tests | ⏳ Pendente |
