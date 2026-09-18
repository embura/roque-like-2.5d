# Documento de Escopo do Jogo - Magicraft-style Roguelike

**Gerado por:** Agente PO (Product Owner)  
**Data:** 2024  
**Versão:** 1.0

---

## 1. VISÃO GERAL DO JOGO

### 1.1 Informações Básicas

- **Título Provisório:** Magic Survival Arena
- **Gênero:** Roguelike de Ação em Arena
- **Tema:** Fantasia Mágica
- **Público-Alvo:** Jogadores de 16-35 anos, fãs de jogos indie, roguelikes e sistemas de magia complexos
- **Plataforma:** PC (Windows/Mac/Linux) via Unity
- **Duração Estimada:** Runs de 15-30 minutos, rejogabilidade infinita

### 1.2 Premissa e Narrativa

O jogador é um mago aprendiz que foi preso em uma dimensão de arena mística. Para escapar, deve sobreviver a ondas infinitas de inimigos enquanto domina combinações de magias cada vez mais poderosas. Cada run oferece uma experiência única com power-ups aleatórios e salas proceduralmente geradas.

Não há narrativa linear tradicional - a história é contada através da progressão, descoberta de novas magias e enfrentamento de chefes temáticos.

### 1.3 Duração da Experiência

- **Run Típica:** 15-30 minutos
- **Sessão de Jogo:** 30-60 minutos (múltiplas runs)
- **Progressão Meta:** Desbloqueio permanente de novas magias e upgrades entre runs
- **Rejogabilidade:** Infinita, com combinações variadas de poderes

---

## 2. MECÂNICAS PRINCIPAIS

### 2.1 Sistema de Combate

**Descrição:** Combate em tempo real focado em esquiva e uso estratégico de magias.

**Funcionalidades:**
- Movimento 8-direcional ou analógico
- Ataque básico automático ou manual
- Sistema de cooldown para habilidades
- Invencibilidade temporária após dano (i-frames)
- Hitboxes precisas para ataques e projéteis
- Sistema de knockback em inimigos

**Controles:**
- WASD / Setas: Movimento
- Mouse: Mira (opcional)
- Clique Esquerdo: Lançar magia equipada
- Espaço / Shift: Esquiva (dash)
- 1-4: Trocar magia equipada
- E: Interagir / Pickup

### 2.2 Sistema de Magia Combinatória

**Descrição:** O coração do jogo - combinar diferentes elementos e tipos de magia para criar efeitos únicos.

**Elementos Base:**
- 🔥 **Fogo:** Dano contínuo (DoT), explosões em área
- ❄️ **Gelo:** Lentidão, congelamento, defesa
- ⚡ **Raio:** Dano instantâneo, chain lightning, velocidade
- 🌿 **Natureza:** Cura, veneno, summon de aliados
- 💀 **Trevas:** Dano massivo, life steal, debuffs
- ✨ **Luz:** Buffs, escudos, purificação

**Tipos de Magia:**
- **Projétil:** Fireball, Ice Shard, Lightning Bolt
- **Área (AoE):** Meteor, Blizzard, Chain Lightning
- **Buff Pessoal:** Mana Shield, Haste, Regeneration
- **Debuff Inimigo:** Freeze, Poison, Vulnerability
- **Summon:** Elemental, Skeleton Mage, Spirit Wolf
- **Campo:** Ground Lava, Ice Zone, Lightning Field

**Sistema de Combinação:**
- Cada cajado permite equipar 2-3 magias base
- Combinações criam magias híbridas (ex: Fogo + Raio = Explosão Eletromagnética)
- Upgrades modificam propriedades (dano, área, cooldown, mana cost)
- Sinergias entre elementos ativam bônus especiais

### 2.3 Progressão do Personagem

**Progressão In-Run (durante uma partida):**
- Coleta de cristais de mana dropped por inimigos
- Level up a cada X cristais coletados
- Escolha de 3 power-ups aleatórios por level
- Power-ups categories:
  - **+Dano:** Aumenta dano de magias específicas ou geral
  - **+Velocidade:** Attack speed, cast speed, movement speed
  - **+Defesa:** HP máximo, armor, regeneration
  - **+Efeitos:** Chance de crítico, status effects, area size
  - **Novas Magias:** Desbloqueia slots adicionais

**Progressão Meta (entre runs):**
- Moeda permanente coletada nas runs
- Desbloqueio de novos elementos de magia
- Upgrades permanentes de stats base
- Novos personagens/clases de mago
- Desafios e conquistas

### 2.4 Sistema de Inimigos e Chefes

**Inimigos Comuns:**
- **Melee:** Aproximam e atacam corpo-a-corpo
- **Ranged:** Atiram projéteis à distância
- **Casters:** Usam magias e buffs
- **Tanks:** Alta vida, movimento lento
- **Swarm:** Baixa vida, movem-se rápido em grupo
- **Elites:** Versões aprimoradas com affixes especiais

**Sistema de Afíxes (Elite Enemies):**
- 🔥 Enchanted: Dano elemental adicional
- 💪 Armored: Redução de dano recebido
- ⚡ Swift: Velocidade de movimento aumentada
- 🔄 Regenerating: Regenera vida ao longo do tempo
- 👥 Summoner: Invoca aliados periodicamente
- 💥 Explosive: Explode ao morrer

**Chefes:**
- Encontrados a cada 5-10 salas
- Mecânicas únicas e padrões de ataque complexos
- Fases múltiplas (mudam comportamento ao perder HP)
- Drops garantidos de itens raros
- Temáticas alinhadas aos elementos de magia

**Exemplos de Chefes:**
1. **Lord Ignis (Fogo):** Ataques em área, deixa lava no chão, summon minions de fogo
2. **Frost Queen (Gelo):** Congela arena, projéteis tracking, fase de enrage
3. **Storm Colossus (Raio):** Teletransporte, chain lightning, área denial
4. **Nature's Wrath (Natureza):** Summon trees, poison clouds, heal mechanic

### 2.5 Economia do Jogo

**Moedas In-Game:**
- **Cristais de Mana:** Coletados durante a run, usados para level up
- **Orbs Elementais:** Drops raros de elites/chefes, usados para combinações especiais

**Moedas Meta:**
- **Essência Arcana:** Moeda permanente coletada ao final de cada run
- Usada para desbloqueios permanentes no hub

**Sistema de Shop (entre runs):**
- Compra de novos elementos de magia
- Upgrades permanentes de stats
- Desbloqueio de personagens
- Consumíveis para runs (opcional, estilo roguelite)

---

## 3. ESTILO VISUAL - MAGICRAFT (Pixel Art HD)

### 3.1 Especificações Técnicas de Sprites

| Elemento | Resolução | Quantidade de Frames | Descrição |
|----------|-----------|---------------------|-----------|
| **Personagem Jogador** | 128x128 | 8-12 frames por animação | Idle, run, cast, hit, death |
| **Inimigos Comuns** | 64x64 - 128x128 | 4-8 frames | Varia por tipo de inimigo |
| **Chefes** | 256x256 | 12-20 frames | Animações detalhadas, expressões |
| **Projetéis de Magia** | 64x64 - 128x128 | 4-6 frames | Element-specific designs |
| **Efeitos de Impacto** | 128x128 | 6-10 frames | Explosões, partículas, sparks |
| **Tilesets - Chão** | 64x64 | 1-2 frames | Variedade de temas de sala |
| **Tilesets - Paredes** | 64x64 | 1-2 frames | Bordas e cantos automatizados |
| **Obstáculos** | 64x64 - 128x128 | 1-4 frames | Pilares, estátuas, decoração |
| **Ícones de Magia (UI)** | 64x64 | 1 frame | Um ícone por magia/combinação |
| **Ícones de Power-ups** | 64x64 | 1-2 frames | Raro/animado para lendários |
| **Portais/Transições** | 128x128 | 8-12 frames | Animação loop de entrada/saída |

### 3.2 Características do Estilo Visual

**Hand-painted High-Res Pixel Art:**
- Pixels visíveis mas com acabamento pintado à mão digital
- Shading suave entre cores mantendo estética pixelada
- Contornos definidos mas não excessivamente grossos
- Detalhes internos ricos (expressões faciais, texturas de roupas)

**Paleta de Cores por Elemento:**

| Elemento | Cores Primárias | Cores Secundárias | Atmosfera |
|----------|----------------|-------------------|-----------|
| 🔥 Fogo | Vermelho, Laranja, Amarelo | Preto, Cinza escuro | Intenso, agressivo |
| ❄️ Gelo | Azul claro, Ciano, Branco | Azul marinho, Cinza azulado | Frio, calmo |
| ⚡ Raio | Amarelo elétrico, Branco | Roxo, Azul escuro | Energético, caótico |
| 🌿 Natureza | Verde, Marrom | Rosa, Amarelo suave | Orgânico, vital |
| 💀 Trevas | Roxo escuro, Preto | Verde tóxico, Vermelho sangue | Sombrio, ameaçador |
| ✨ Luz | Dourado, Branco | Azul celeste, Rosa pálido | Divino, puro |

**Atmosfera Visual Geral:**
- Contraste alto entre personagens e cenário
- Efeitos de glow/bloom em magias e partículas
- Screen shake em impactos significativos
- Flash de dano em inimigos atingidos
- Rastros de movimento em projéteis rápidos
- Partículas abundantes mas otimizadas

### 3.3 Efeitos de Partículas Complexos

**Sistemas de Partículas Necessários:**
- **Trail:** Rastro em projéteis e movimentos rápidos
- **Impact:** Explosão no ponto de impacto
- **Aura:** Efeito contínuo ao redor do personagem (buffs)
- **Ground:** Efeitos no chão (áreas elementais)
- **Status:** Partículas indicando status effects (veneno, freeze, burn)
- **Death:** Explosão/desaparecimento de inimigos
- **Pickup:** Brilho/coleta de cristais e items
- **Level Up:** Efeito dramático de power-up

**Especificações Técnicas:**
- Máximo de 500 partículas ativas simultaneamente
- Uso de sprite sheets animadas para partículas
- Sorting layers adequados (atrás/em frente do personagem)
- Pooling de partículas para performance
- Variação de tamanho, rotação e cor por partícula

### 3.4 Direção de Arte de Cenários

**Temas de Sala:**
1. **Arena de Pedra:** Clássico, neutro, bom contraste
2. **Templo Antigo:** Ornamentos mágicos, runas brilhantes
3. **Caverna Cristalina:** Cristais emissores de luz natural
4. **Laboratório Arcano:** Livros, poções, equipamentos místicos
5. **Dimensão do Caos:** Flutuante, surreal, cores vibrantes

**Elementos de Cenário:**
- Pisos com padrão de grade sutil (para orientação)
- Paredes com variação para evitar repetição visual
- Obstáculos destrutíveis (barris, estátuas)
- Elementos interativos (portais, switches, shrines)
- Decoração de fundo (não colidível, apenas visual)

---

## 4. FUNCIONALIDADES DETALHADAS

### 4.1 Sistemas de UI/UX Necessários

**HUD In-Game:**
- Barra de Vida (HP) - canto superior esquerdo
- Barra de Mana - abaixo da barra de vida
- Contador de Cristais - centro superior ou canto
- Magias Equipadas - barra inferior (1-4 slots)
- Minimap (opcional) - canto superior direito
- Timer da Run - topo central
- Contador de Inimigos Restantes - se aplicável

**Menus:**
- **Menu Principal:** Start, Continue, Options, Quit
- **Hub entre Runs:** Shop, Upgrade Tree, Challenge Board, Start Run
- **Pause Menu:** Resume, Options, Quit to Hub
- **Game Over Screen:** Stats da run, Moedas ganhas, Botões de retry/quit

**Telas de Informação:**
- **Inventory:** Magias desbloqueadas, combinações descobertas
- **Codex:** Inimigos derrotados, chefes, conquistas
- **Stats:** Tempo total, kills, deaths, combos descobertos

**Feedback Visual:**
- Damage numbers flutuantes (customizável on/off)
- Texto de level up pop-up
- Notificações de combinações descobertas
- Tutorial tooltips (primeiras runs)

### 4.2 Áudio e Trilha Sonora

**Efeitos Sonoros (SFX):**
- Cast de cada magia (variação por elemento)
- Impactos de projéteis
- Hits em inimigos
- Death sounds (inimigos e jogador)
- Pickup de cristais e items
- UI sounds (click, hover, confirm)
- Ambient sounds por tema de sala
- Boss intro/outro sounds

**Trilha Sonora (BGM):**
- **Menu/Hub:** Calma, misteriosa, exploratória
- **Run Normal:** Intensa mas não caótica, ritmo médio
- **Boss Fight:** Épica, alta intensidade, orquestral
- **Victory:** Triunfante, curta (tela de resultados)
- **Game Over:** Melancólica, transitória

**Especificações Técnicas de Áudio:**
- Format: WAV/OGG
- Sample Rate: 44.1kHz ou 48kHz
- Spatial Audio: Para efeitos posicionais (opcional)
- Mixer groups: Master, Music, SFX, UI
- Volume settings ajustáveis pelo jogador

### 4.3 Controles e Input

**Suporte de Input:**
- Keyboard + Mouse (padrão PC)
- Gamepad (XInput - Xbox/PS controllers)
- Rebindable keys (teclado)
- Vibration/rumble (gamepad)

**Configurações de Controle:**
- Sensibilidade do mouse ajustável
- Toggle vs Hold para dash/esquiva
- Auto-cast option (mira automática no inimigo mais próximo)
- Gamepad vibration on/off
- Deadzone adjustment para analógicos

**Acessibilidade:**
- Colorblind modes (deuteranopia, protanopia, tritanopia)
- Opção para aumentar tamanho de UI
- Toggle para screen shake (motion sickness)
- Subtitles para diálogos (se houver)
- Remapping completo de controles

### 4.4 Sistema de Save/Load

**Dados Salvos Localmente:**
- Progresso meta (desbloqueios, upgrades permanentes)
- Estatísticas do jogador
- Conquistas completadas
- Configurações de opções
- High scores (se aplicável)

**Formato de Save:**
- JSON ou binary format
- Auto-save após cada run
- Múltiplos save slots (opcional)
- Cloud save support (Steam Cloud, opcional)

---

## 5. CRITÉRIOS DE ACEITE

### 5.1 Funcionalidades Core (MVP - Minimum Viable Product)

**Movimento e Combate:**
- [ ] Personagem move-se suavemente em 8 direções
- [ ] Sistema de colisão funcional com paredes e inimigos
- [ ] Esquiva (dash) com i-frames e cooldown
- [ ] Pelo menos 3 magias de projétil implementadas
- [ ] Inimigos spawnam e perseguem o jogador
- [ ] Sistema de dano e morte funcionando

**Sistema de Magia:**
- [ ] 3 elementos base implementados (ex: Fogo, Gelo, Raio)
- [ ] Sistema de cooldown visível na UI
- [ ] Combinação básica de 2 elementos funciona
- [ ] Power-ups aplicam modificações nas magias

**Progressão:**
- [ ] Sistema de level up durante run
- [ ] Escolha de power-ups após level up
- [ ] Cristais de mana dropam de inimigos
- [ ] Moeda meta persiste entre runs

**Inimigos:**
- [ ] 3 tipos de inimigos comuns (melee, ranged, swarm)
- [ ] 1 chefe implementado com 2 fases
- [ ] Sistema de afíxes em elites
- [ ] Pathfinding básico funcionando

**UI/UX:**
- [ ] HUD com HP, Mana, Cristais, Magias equipadas
- [ ] Menu principal funcional
- [ ] Tela de game over com stats
- [ ] Sistema de pause

**Visual:**
- [ ] Sprite do jogador com animações básicas (idle, run, cast)
- [ ] Sprites de inimigos com animações
- [ ] Tileset funcional para arenas
- [ ] Efeitos de partículas para magias principais
- [ ] Estilo consistente com Pixel Art HD

**Áudio:**
- [ ] SFX para ações principais (cast, hit, death, pickup)
- [ ] BGM para gameplay e menu
- [ ] Mixer de volume funcional

**Performance:**
- [ ] 60 FPS estáveis com até 50 inimigos na tela
- [ ] Loading time < 3 segundos
- [ ] Sem memory leaks em sessions de 30+ minutos

### 5.2 Funcionalidades Pós-MVP (Versão Completa)

**Expansão de Conteúdo:**
- [ ] 6 elementos de magia totalmente implementados
- [ ] 15+ magias base diferentes
- [ ] 50+ combinações de magias descobertas
- [ ] 10+ tipos de inimigos
- [ ] 5 chefes únicos com mecânicas distintas
- [ ] 5 temas de sala diferentes

**Sistemas Avançados:**
- [ ] Sistema de conquistas
- [ ] Codex de inimigos e magias
- [ ] Daily challenges/runs
- [ ] Leaderboards online (opcional)
- [ ] New Game+ ou dificuldade escalonável

**Polish:**
- [ ] Transições suaves entre salas
- [ ] Screen shake e feedback visual refinado
- [ ] Tutorial integrado nas primeiras runs
- [ ] Opções de acessibilidade completas
- [ ] Suporte a ultrawide e múltiplas resoluções

### 5.3 Métricas de Qualidade Esperadas

**Gameplay:**
- Tempo médio para primeira vitória: 60-90 minutos
- Taxa de retenção (segunda run): > 40%
- Dificuldade progressiva sentida como justa
- Combinações de magias sentidas como distintas e úteis

**Performance Técnica:**
- 60 FPS mínimo em hardware alvo (GTX 1060 ou equivalente)
- Memory usage < 512MB
- CPU usage < 50% em quad-core
- Zero crashes em testing de 100+ horas

**Qualidade Visual:**
- Consistência artística em todos os assets
- Animações fluidas (mínimo 8 FPS effective para personagens)
- Legibilidade clara de ações e efeitos
- UI limpa e informativa sem clutter

**Qualidade de Áudio:**
- Mix balanceado (música não abafa SFX críticos)
- SFX distintos e reconhecíveis
- Loop points无缝 em músicas

---

## 6. ESCOPO EXCLUÍDO (Fora do Escopo Inicial)

Para manter foco e viabilidade do projeto, os seguintes itens estão **FORA** do escopo inicial:

- ❌ Modo multiplayer cooperativo ou competitivo
- ❌ Narrativa extensa com cutscenes e diálogos
- ❌ Sistema de crafting complexo
- ❌ Mundo aberto ou exploração não-linear
- ❌ Microtransações ou loot boxes
- ❌ DLCs ou conteúdo pós-lançamento (planejar base sólida primeiro)
- ❌ Portes para console/mobile (focar em PC primeiro)
- ❌ Modding support oficial (pode ser adicionado posteriormente)

---

## 7. RESUMO EXECUTIVO

**Magic Survival Arena** é um roguelike de ação focado em combate mágico combinatório em arenas fechadas. O jogador controla um mago que deve sobreviver a ondas de inimigos enquanto coleta cristais para desbloquear power-ups e combinações de magias únicas.

**Diferenciais Principais:**
1. Sistema profundo de combinação de magias (6 elementos × múltiplos tipos)
2. Estilo visual Pixel Art HD de alta qualidade (inspirado em Magicraft)
3. Rejogabilidade infinita com progressão meta significativa
4. Combate fluido e satisfatório com feedback visual rico
5. Acessível para iniciantes, profundo para mastery

**Público-Alvo:** Fãs de Vampire Survivors, Magicraft, Roguelikes, jogos de magia, action games indie.

**Platforma de Lançamento:** PC (Steam, itch.io)  
**Engine:** Unity 2022 LTS ou superior  
**Tempo Estimado de Desenvolvimento (MVP):** 3-6 meses com equipe pequena  
**Tempo Estimado (Versão Completa):** 9-12 meses

---

**Documento Aprovado Por:** Agente PO  
**Próximo Passo:** Enviar para Agente DEV criar especificações técnicas e plano de implementação
