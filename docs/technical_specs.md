# Especificações Técnicas e Plano de Desenvolvimento

**Gerado por:** Agente DEV (Engenheiro de Software Sênior Unity)  
**Baseado em:** Documento de Escopo v1.0 (Agente PO)  
**Data:** 2024  
**Versão:** 1.0

---

## 1. ARQUITETURA DO PROJETO UNITY

### 1.1 Estrutura de Pastas

```
Assets/
├── _Project/                    # Pasta principal do projeto
│   ├── Scripts/                 # Todos os scripts C#
│   │   ├── Core/                # Sistemas centrais (GameManager, SceneManager)
│   │   ├── Player/              # Controller do jogador, stats, input
│   │   ├── Magic/               # Sistema de magias, combinações, elementos
│   │   ├── Enemies/             # IA de inimigos, pathfinding, behaviors
│   │   ├── Combat/              # Sistema de dano, hitboxes, projectiles
│   │   ├── Progression/         # Level up, power-ups, economia
│   │   ├── UI/                  # Managers de interface
│   │   ├── Audio/               # Audio managers, music controllers
│   │   └── Utils/               # Helpers, extensions, pools
│   │
│   ├── Prefabs/                 # Prefabs organizados por categoria
│   │   ├── Player/
│   │   ├── Enemies/
│   │   ├── Magic/
│   │   ├── Environment/
│   │   └── UI/
│   │
│   ├── ScriptableObjects/       # Configurações e dados
│   │   ├── Magic/               # MagicData, ElementData, CombinationData
│   │   ├── Enemies/             # EnemyStats, BossPatterns
│   │   ├── Upgrades/            # PowerUpData, PerkData
│   │   └── GameConfig/          # GameBalance, AudioConfig
│   │
│   ├── Sprites/                 # Assets visuais
│   │   ├── Characters/          # Player, enemies, bosses
│   │   ├── Magic/               # Projectiles, effects
│   │   ├── Environment/         # Tilesets, props
│   │   └── UI/                  # Icons, buttons, frames
│   │
│   ├── Animations/              # Animation clips e controllers
│   │   ├── Player/
│   │   ├── Enemies/
│   │   └── Magic/
│   │
│   ├── Particles/               # Particle systems
│   │   ├── Magic/
│   │   ├── Impacts/
│   │   └── Auras/
│   │
│   ├── Audio/                   # Clips de áudio
│   │   ├── Music/
│   │   ├── SFX/
│   │   └── Ambient/
│   │
│   └── Scenes/                  # Cenas do jogo
│       ├── Boot/                # Cena inicial (loading, setup)
│       ├── Menu/                # Menu principal
│       ├── Hub/                 # Hub entre runs
│       ├── Arena/               // Template de arena (reutilizável)
│       └── GameOver/            // Tela de resultados
│
├── Plugins/                     # Assets de terceiros
└── Resources/                   # Recursos carregáveis dinamicamente
```

### 1.2 Padrões de Design Utilizados

| Padrão | Aplicação | Benefício |
|--------|-----------|-----------|
| **Singleton** | GameManager, AudioManager, UIManager | Acesso global controlado |
| **Observer/Event** | Sistema de eventos do jogo | Desacoplamento entre sistemas |
| **Strategy** | Comportamentos de IA de inimigos | Troca dinâmica de behavior |
| **State Machine** | Estados do player, fases de boss | Controle claro de estados |
| **Object Pool** | Projéteis, partículas, inimigos | Performance e GC reduction |
| **Command** | Sistema de input (opcional) | Input buffering, replay system |
| **Factory** | Spawn de inimigos, magias | Criação centralizada |
| **Component** | Arquitetura Unity nativa | Composição sobre herança |

### 1.3 Camadas da Arquitetura

```
┌─────────────────────────────────────┐
│         Apresentação (UI)           │
│  - HUD, Menus, Feedback Visual      │
├─────────────────────────────────────┤
│         Lógica de Jogo              │
│  - Combate, Magia, Progressão       │
├─────────────────────────────────────┤
│         Sistemas Core               │
│  - GameManager, EventBus, Pools     │
├─────────────────────────────────────┤
│         Dados & Configuração        │
│  - ScriptableObjects, Save System   │
└─────────────────────────────────────┘
```

---

## 2. SISTEMAS PRINCIPAIS

### 2.1 Sistema de Gerenciamento Core

**GameManager (Singleton)**
- Controla estado do jogo (Menu, Playing, Paused, GameOver)
- Gerencia transição entre cenas
- Coordena sistemas principais
- Handle de game over e vitória

**SceneLoader**
- Carregamento assíncrono de cenas
- Telas de loading com dicas
- Persistência de dados entre cenas

**EventBus (Observer Pattern)**
```csharp
// Eventos principais do jogo
public enum GameEvent {
    PlayerDamaged,
    PlayerHealed,
    PlayerDied,
    EnemyKilled,
    LevelUp,
    MagicCast,
    ComboDiscovered,
    RunStarted,
    RunEnded
}
```

### 2.2 Sistema do Jogador

**PlayerController**
- Movimento 8-direcional com normalização vetorial
- Integração com Input System da Unity (novo ou legacy)
- Colisão com paredes e obstáculos
- Sistema de dash com i-frames

**PlayerStats (ScriptableObject reference)**
- HP, Mana, Armor, Speed
- Dano mágico, velocidade de conjuração
- Crítico, regeneração
- Modificadores temporários (buffs/debuffs)

**PlayerStateMachine**
- Estados: Idle, Moving, Casting, Dashing, Hit, Dead
- Transições controladas por condições
- Animações sincronizadas com estados

### 2.3 Sistema de Magia

**MagicData (ScriptableObject)**
```csharp
[CreateAssetMenu]
public class MagicData : ScriptableObject {
    public string magicName;
    public ElementType element;
    public MagicType type;
    public float baseDamage;
    public float cooldown;
    public float manaCost;
    public GameObject projectilePrefab;
    public GameObject impactEffect;
    public AudioClip castSound;
    // ... mais propriedades
}
```

**MagicSystem**
- Gerencia cooldowns das magias equipadas
- Valida recursos (mana) para casting
- Instancia projéteis via ObjectPool
- Aplica damage calculations

**CombinationSystem**
- Detecta combinações de elementos equipados
- Retorna MagicData híbrida quando aplicável
- Notifica UI de combinação descoberta
- Salva combinações no codex do jogador

**ElementData (ScriptableObject)**
- Define propriedades de cada elemento (Fogo, Gelo, Raio, etc.)
- Cores, ícones, efeitos de partícula padrão
- Modificadores de dano tipo (rock-paper-scissors)

### 2.4 Sistema de Inimigos

**EnemyBase (Classe abstrata)**
- Stats básicos (HP, dano, velocidade)
- Referência a EnemyData ScriptableObject
- Estados: Idle, Chasing, Attacking, Hit, Dead
- Interface para dano e morte

**EnemyAI (State Machine)**
- Patrol state (se aplicável)
- Chase state (pathfinding para player)
- Attack state (verifica range, cooldown)
- Retreat state (se configurado)

**Pathfinding**
- Unity NavMesh para navegação
- Ou sistema customizado para grid-based
- Avoidance de outros inimigos (separação de boids)

**EnemySpawner**
- Wave management
- Spawn points definidos por sala
- Dificuldade progressiva por onda
- Elite spawn chance calculation

**BossController**
- Múltiplas fases baseadas em HP thresholds
- Pattern attacks predefinidos
- Invencibilidade durante transições
- Spawn de minions em fases específicas

### 2.5 Sistema de Combate

**DamageSystem**
- Calcula dano final: `baseDamage * modifiers - armor`
- Aplica elementos e status effects
- Trigger de eventos de dano
- Suporte a números flutuantes de dano

**HitboxSystem**
- Hitboxes para player, inimigos, projéteis
- Layers e masks para filtrar colisões
- Trigger vs Collision baseado em necessidade
- I-frames após dano recebido

**ProjectilePool**
- Object pooling para performance
- Reset de estado ao retornar ao pool
- Lifetime máximo para cleanup
- Tracking de projéteis ativos

**StatusEffectSystem**
- Burn, Freeze, Poison, Shock, etc.
- Duration-based ou stack-based
- Visual indicators (particles, icons)
- Damage over time calculation

### 2.6 Sistema de Progressão

**LevelUpSystem**
- Track de cristais coletados na run
- Thresholds de XP por level
- Trigger de selection screen
- Aplicação de power-ups escolhidos

**PowerUpData (ScriptableObject)**
- Tipo de poder (dano, velocidade, defesa, novo slot)
- Valores de upgrade
- Ícone e descrição
- Requisitos (se houver)

**MetaProgression**
- Save/Load de desbloqueios permanentes
- Currency accumulation entre runs
- Upgrade tree data structure
- Achievement tracking

### 2.7 Sistema de UI

**UIManager (Singleton)**
- Controle de screens e panels
- Transições animadas
- Input blocking durante modais
- Event-driven updates

**HUDController**
- Update de barras de HP/Mana
- Display de cristais e moedas
- Cooldown indicators das magias
- Damage numbers popup

**MenuNavigation**
- Stack-based menu system
- Back button functionality
- Keyboard e gamepad navigation
- Sound feedback em selections

---

## 3. PLANO DE DESENVOLVIMENTO

### Fase 1 - Fundação (Semana 1-2)

**Objetivo:** Setup do projeto e sistemas core básicos

**Tarefas:**
- [ ] Configurar estrutura de pastas do projeto
- [ ] Implementar GameManager e SceneLoader
- [ ] Criar EventBus system
- [ ] Setup do Input System (Unity New Input System recomendado)
- [ ] Implementar ObjectPool genérico
- [ ] Criar ScriptableObjects base (GameConfig, ElementData)

**Critérios de Aceite:**
- Projeto compilando sem erros
- Transição entre cenas funcionando
- Sistema de eventos operacional
- Input respondendo em teste básico

### Fase 2 - Jogador e Movimento (Semana 2-3)

**Objetivo:** Player controller completo e responsivo

**Tarefas:**
- [ ] Implementar PlayerController com movimento 8-direcional
- [ ] Adicionar sistema de colisão com ambiente
- [ ] Implementar dash com i-frames e cooldown
- [ ] Integrar animações básicas (idle, run)
- [ ] Criar PlayerStats com ScriptableObject
- [ ] Setup de camera follow smooth

**Critérios de Aceite:**
- Personagem move-se suavemente em todas direções
- Colisões funcionando corretamente
- Dash responsivo com visual feedback
- Camera segue player sem jitter

### Fase 3 - Sistema de Magia Básico (Semana 3-4)

**Objetivo:** Casting de magias e projéteis funcionais

**Tarefas:**
- [ ] Criar MagicData ScriptableObject para 3 magias base
- [ ] Implementar MagicSystem com cooldowns
- [ ] Criar ProjectilePool para instanciamento
- [ ] Implementar targeting básico (direção do mouse ou movimento)
- [ ] Adicionar efeitos de partícula para casts
- [ ] Integrar sons de casting

**Critérios de Aceite:**
- 3 magias diferentes lançáveis
- Cooldowns visíveis na UI (placeholder)
- Projéteis usando object pool
- Feedback visual e sonoro ao conjurar

### Fase 4 - Inimigos e Combate (Semana 4-6)

**Objetivo:** Inimigos funcionais e sistema de dano

**Tarefas:**
- [ ] Implementar EnemyBase class
- [ ] Criar AI state machine simples (chase + attack)
- [ ] Setup de NavMesh para pathfinding
- [ ] Implementar DamageSystem completo
- [ ] Criar hitboxes para player e inimigos
- [ ] Adicionar 3 tipos de inimigos (melee, ranged, swarm)
- [ ] Implementar sistema de knockback

**Critérios de Aceite:**
- Inimigos perseguem player corretamente
- Dano é calculado e aplicado
- Inimigos morrem e dropam cristais
- Player recebe dano e tem i-frames

### Fase 5 - Progressão e Power-ups (Semana 6-7)

**Objetivo:** Sistema de level up e escolha de poderes

**Tarefas:**
- [ ] Implementar LevelUpSystem com thresholds de XP
- [ ] Criar PowerUpData para 10+ power-ups
- [ ] Implementar seleção de power-ups (UI)
- [ ] Aplicar modificadores de stats dinamicamente
- [ ] Sistema de coleta de cristais
- [ ] Meta-progression save/load básico

**Critérios de Aceite:**
- Level up ocorre ao coletar cristais suficientes
- Escolha de 3 power-ups aleatórios funciona
- Stats são modificados corretamente
- Progresso meta persiste entre runs

### Fase 6 - Sistema de Salas e Spawning (Semana 7-8)

**Objetivo:** Arenas funcionais com waves de inimigos

**Tarefas:**
- [ ] Criar template de sala/arena
- [ ] Implementar EnemySpawner com wave management
- [ ] Sistema de transição entre salas (portais)
- [ ] Definição de spawn points
- [ ] Dificuldade progressiva por wave
- [ ] Condição de vitória da sala (todos inimigos mortos)

**Critérios de Aceite:**
- Inimigos spawnam em ondas organizadas
- Transição entre salas funcional
- Dificuldade aumenta progressivamente
- Sala "limpa" quando todos inimigos derrotados

### Fase 7 - Chefe e Fases Múltiplas (Semana 8-9)

**Objetivo:** Boss fight com mecânicas únicas

**Tarefas:**
- [ ] Implementar BossController com fase transitions
- [ ] Criar 1 boss completo (Lord Ignis - Fogo)
- [ ] Pattern attacks predefinidos
- [ ] Spawn de minions durante fight
- [ ] Invencibilidade durante transições de fase
- [ ] Loot guarantee de boss kill

**Critérios de Aceite:**
- Boss tem 2-3 fases distintas
- Ataques seguem patterns reconhecíveis
- Minions spawnam em momentos específicos
- Drop raro garantido ao vencer

### Fase 8 - UI Completa e Feedback (Semana 9-10)

**Objetivo:** Interface polida e feedback visual rico

**Tarefas:**
- [ ] Implementar HUD completo (HP, Mana, Cristais, Magias)
- [ ] Criar Menu Principal funcional
- [ ] Tela de Game Over com stats
- [ ] Damage numbers flutuantes
- [ ] Cooldown indicators visuais
- [ ] Notificações de level up e combos
- [ ] Pause menu funcional

**Critérios de Aceite:**
- Todas informações críticas visíveis no HUD
- Menus navegáveis com teclado e gamepad
- Feedback visual claro para ações importantes
- UI responsiva e sem bugs

### Fase 9 - Áudio e Polish (Semana 10-11)

**Objetivo:** Áudio integrado e refinamentos finais

**Tarefas:**
- [ ] Implementar AudioManager com mixer groups
- [ ] Adicionar todas SFX necessárias
- [ ] Integrar BGM por contexto (menu, gameplay, boss)
- [ ] Screen shake em impactos significativos
- [ ] Flash de dano em inimigos
- [ ] Otimização de performance (profiling)
- [ ] Bug fixing geral

**Critérios de Aceite:**
- Áudio balanceado e imersivo
- Feedback visual refinado
- 60 FPS estáveis com 50+ inimigos
- Bugs críticos resolvidos

### Fase 10 - MVP Ready (Semana 11-12)

**Objetivo:** Preparar para teste externo

**Tarefas:**
- [ ] Playtest interno completo
- [ ] Balanceamento de dificuldade
- [ ] Fix de issues reportados
- [ ] Build de distribuição (Windows/Mac/Linux)
- [ ] Documentação técnica final
- [ ] Checklist de critérios de aceite do PO

**Critérios de Aceite:**
- Todos critérios do MVP atendidos
- Build estável para playtesters
- Documentação completa
- Pronto para feedback externo

---

## 4. ESTIMATIVAS DE ESFORÇO

| Fase | Duração | Complexidade | Dependências |
|------|---------|--------------|--------------|
| 1 - Fundação | 2 semanas | Média | Nenhuma |
| 2 - Jogador | 1.5 semanas | Baixa | Fase 1 |
| 3 - Magia | 1.5 semanas | Média | Fase 2 |
| 4 - Inimigos | 2 semanas | Alta | Fase 3 |
| 5 - Progressão | 1.5 semanas | Média | Fase 4 |
| 6 - Salas/Spawn | 1.5 semanas | Média | Fase 4, 5 |
| 7 - Chefe | 1.5 semanas | Alta | Fase 4, 6 |
| 8 - UI | 1.5 semanas | Média | Fases 3-7 |
| 9 - Áudio/Polish | 1.5 semanas | Baixa-Média | Fases 1-8 |
| 10 - MVP Ready | 1 semana | Baixa | Todas anteriores |

**Tempo Total Estimado:** 14-15 semanas (3.5 - 4 meses)

**Riscos e Mitigações:**

| Risco | Impacto | Probabilidade | Mitigação |
|-------|---------|---------------|-----------|
| Escopo creep | Alto | Alta | Manter foco no MVP, features pós-MVP em backlog |
| Performance issues | Alto | Média | Profiling constante, object pooling desde início |
| Balanceamento difícil | Médio | Alta | Playtests frequentes, dados ajustáveis via ScriptableObjects |
| Assets visuais atrasam | Médio | Média | Usar placeholders, integrar assets gradualmente |
| Bugs de integração | Médio | Alta | Testes contínuos, CI/CD se possível |

---

## 5. IMPLEMENTAÇÃO DE CÓDIGO - EXEMPLOS CORE

### 5.1 PlayerController.cs

```csharp
using UnityEngine;
using UnityEngine.Events;

public class PlayerController : MonoBehaviour
{
    [Header("Movement")]
    [SerializeField] private float moveSpeed = 5f;
    [SerializeField] private float dashSpeed = 15f;
    [SerializeField] private float dashDuration = 0.2f;
    [SerializeField] private float dashCooldown = 1f;
    
    [Header("Combat")]
    [SerializeField] private float invincibilityDuration = 0.5f;
    
    private Vector2 movement;
    private Rigidbody2D rb;
    private bool isDashing;
    private bool canDash = true;
    private bool isInvincible;
    private float dashTimeRemaining;
    private float dashCooldownTime;
    private float invincibilityTimeRemaining;
    
    // Events
    public UnityEvent OnDashStarted;
    public UnityEvent OnDashEnded;
    public UnityEvent<float> OnHealthChanged;
    
    void Awake()
    {
        rb = GetComponent<Rigidbody2D>();
        OnDashStarted = new UnityEvent();
        OnDashEnded = new UnityEvent();
        OnHealthChanged = new UnityEvent<float>();
    }
    
    void Update()
    {
        if (isDashing)
        {
            dashTimeRemaining -= Time.deltaTime;
            if (dashTimeRemaining <= 0)
            {
                EndDash();
            }
            return;
        }
        
        if (dashCooldownTime > 0)
            dashCooldownTime -= Time.deltaTime;
            
        if (invincibilityTimeRemaining > 0)
            invincibilityTimeRemaining -= Time.deltaTime;
        
        GetInput();
        
        if (Input.GetKeyDown(KeyCode.Space) && canDash)
        {
            StartDash();
        }
    }
    
    void FixedUpdate()
    {
        if (isDashing)
        {
            rb.velocity = movement.normalized * dashSpeed;
        }
        else
        {
            rb.velocity = movement.normalized * moveSpeed;
        }
    }
    
    void GetInput()
    {
        movement.x = Input.GetAxisRaw("Horizontal");
        movement.y = Input.GetAxisRaw("Vertical");
    }
    
    void StartDash()
    {
        isDashing = true;
        canDash = false;
        dashTimeRemaining = dashDuration;
        dashCooldownTime = dashCooldown;
        OnDashStarted?.Invoke();
    }
    
    void EndDash()
    {
        isDashing = false;
        Invoke(nameof(ResetDash), dashCooldown);
        OnDashEnded?.Invoke();
    }
    
    void ResetDash()
    {
        canDash = true;
    }
    
    public void TakeDamage(float damage)
    {
        if (isInvincible) return;
        
        // Apply damage logic here
        float currentHealth = /* get from stats */ 100f;
        currentHealth -= damage;
        
        OnHealthChanged?.Invoke(currentHealth);
        
        StartCoroutine(InvincibilityCoroutine());
    }
    
    System.Collections.IEnumerator InvincibilityCoroutine()
    {
        isInvincible = true;
        invincibilityTimeRemaining = invincibilityDuration;
        
        while (invincibilityTimeRemaining > 0)
        {
            yield return null;
        }
        
        isInvincible = false;
    }
}
```

### 5.2 MagicData.cs (ScriptableObject)

```csharp
using UnityEngine;

[CreateAssetMenu(fileName = "NewMagic", menuName = "Magic/Magic Data")]
public class MagicData : ScriptableObject
{
    [Header("Basic Info")]
    public string magicName;
    public Sprite icon;
    public ElementType element;
    public MagicType type;
    
    [Header("Stats")]
    public float baseDamage;
    public float cooldown;
    public float manaCost;
    public float castRange;
    public float areaSize;
    
    [Header("References")]
    public GameObject projectilePrefab;
    public GameObject impactEffect;
    public AudioClip castSound;
    public AudioClip impactSound;
    
    [Header("Modifiers")]
    public float damageMultiplier = 1f;
    public float cooldownMultiplier = 1f;
    public float areaMultiplier = 1f;
    
    [Header("Visuals")]
    public Color projectileColor;
    public ParticleSystem castParticles;
    
    public float GetActualDamage() => baseDamage * damageMultiplier;
    public float GetActualCooldown() => cooldown * cooldownMultiplier;
    public float GetActualArea() => areaSize * areaMultiplier;
}

public enum ElementType { Fire, Ice, Lightning, Nature, Dark, Light }
public enum MagicType { Projectile, AoE, Buff, Debuff, Summon, Field }
```

### 5.3 EventBus.cs (Observer Pattern)

```csharp
using System.Collections.Generic;
using UnityEngine.Events;

public static class EventBus
{
    private static Dictionary<GameEvent, UnityEvent> events = 
        new Dictionary<GameEvent, UnityEvent>();
    
    public static void Subscribe(GameEvent gameEvent, UnityAction action)
    {
        if (!events.ContainsKey(gameEvent))
        {
            events[gameEvent] = new UnityEvent();
        }
        events[gameEvent].AddListener(action);
    }
    
    public static void Unsubscribe(GameEvent gameEvent, UnityAction action)
    {
        if (events.ContainsKey(gameEvent))
        {
            events[gameEvent].RemoveListener(action);
        }
    }
    
    public static void Trigger(GameEvent gameEvent)
    {
        if (events.ContainsKey(gameEvent))
        {
            events[gameEvent].Invoke();
        }
    }
    
    public static void Trigger<T>(GameEvent gameEvent, T parameter)
    {
        // Implementation for events with parameters
        // Would need UnityEvent<T> dictionary
    }
}

public enum GameEvent
{
    PlayerDamaged,
    PlayerHealed,
    PlayerDied,
    EnemyKilled,
    LevelUp,
    MagicCast,
    ComboDiscovered,
    RunStarted,
    RunEnded,
    CrystalCollected,
    RoomCleared
}
```

### 5.4 ObjectPool.cs (Generic)

```csharp
using System.Collections.Generic;
using UnityEngine;

public class ObjectPool<T> where T : MonoBehaviour
{
    private Queue<T> pool = new Queue<T>();
    private T prefab;
    private Transform parent;
    private int initialSize;
    
    public ObjectPool(T prefab, int initialSize, Transform parent = null)
    {
        this.prefab = prefab;
        this.initialSize = initialSize;
        this.parent = parent ?? new GameObject($"Pool_{prefab.name}").transform;
        
        InitializePool();
    }
    
    void InitializePool()
    {
        for (int i = 0; i < initialSize; i++)
        {
            T obj = CreateNew();
            pool.Enqueue(obj);
        }
    }
    
    T CreateNew()
    {
        T obj = Object.Instantiate(prefab, parent);
        obj.gameObject.SetActive(false);
        
        // If object has IPoolable interface, call OnReturnedToPool
        if (obj is IPoolable poolable)
        {
            poolable.OnReturnedToPool();
        }
        
        return obj;
    }
    
    public T Get(Vector3 position, Quaternion rotation)
    {
        T obj;
        
        if (pool.Count > 0)
        {
            obj = pool.Dequeue();
        }
        else
        {
            obj = CreateNew();
        }
        
        obj.transform.position = position;
        obj.transform.rotation = rotation;
        obj.gameObject.SetActive(true);
        
        // If object has IPoolable interface, call OnTakenFromPool
        if (obj is IPoolable poolable)
        {
            poolable.OnTakenFromPool();
        }
        
        return obj;
    }
    
    public void Return(T obj)
    {
        obj.gameObject.SetActive(false);
        pool.Enqueue(obj);
        
        if (obj is IPoolable poolable)
        {
            poolable.OnReturnedToPool();
        }
    }
    
    public void ExpandPool(int additionalAmount)
    {
        for (int i = 0; i < additionalAmount; i++)
        {
            T obj = CreateNew();
            pool.Enqueue(obj);
        }
    }
}

public interface IPoolable
{
    void OnTakenFromPool();
    void OnReturnedToPool();
}
```

---

## 6. INSTRUÇÕES DE INTEGRAÇÃO NO UNITY

### 6.1 Setup Inicial do Projeto

1. **Criar Novo Projeto Unity**
   - Template: 2D Core
   - Unity Version: 2022.3 LTS ou superior
   - Nome: MagicSurvivalArena

2. **Importar Pacotes Necessários**
   ```
   Window > Package Manager:
   - 2D Animation
   - 2D Common
   - 2D Pixel Perfect
   - Input System (recomendado novo sistema)
   - TextMeshPro
   ```

3. **Configurar Project Settings**
   - Physics 2D: Disable collision entre layers desnecessários
   - Quality: Setar para Medium como default
   - Player: Configurar Company Name, Product Name

4. **Configurar Layers**
   ```
   Layers necessárias:
   - Player (6)
   - Enemies (7)
   - Projectiles (8)
   - Environment (9)
   - Triggers (10)
   ```

5. **Setup de Sorting Layers (para sprites)**
   ```
   Background
   Environment
   Enemies
   Player
   Projectiles
   Effects
   UI
   ```

### 6.2 Primeiros Passos Após Setup

1. **Criar estrutura de pastas** conforme seção 1.1
2. **Implementar GameManager** como primeiro script
3. **Criar cena Boot** com setup inicial
4. **Testar Input System** com cube placeholder
5. **Commit inicial** no version control

### 6.3 Pipeline de Desenvolvimento Recomendada

```
Daily:
- Pull changes
- Work em feature branch
- Commit frequente com mensagens claras
- Push ao final do dia

Weekly:
- Merge develop branch
- Playtest da build atual
- Adjustments baseados em feedback
- Update de documentação

Milestone (por fase):
- Branch release para testing
- QA pass completo
- Bug fixing sprint
- Merge para main
- Build de distribuição
```

---

**Documento Criado Por:** Agente DEV  
**Próximo Passo:** Implementar código conforme plano de desenvolvimento  
**Para QA:** Este documento serve como base para validação da implementação
