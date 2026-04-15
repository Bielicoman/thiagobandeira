# Guia de Skills — Portfolio Thiago Sagrillo

## Visão Geral do Projeto

**Portfolio audiovisual** para Thiago Sagrillo (thiagosagrillo) — fotógrafo/cineasta.  
**Stack**: React 19 + Vite (ou Next.js 15) · Tailwind CSS · Framer Motion  
**Conteúdo**: Álbum "THIAGO STILL" — 24 fotos no Flickr (Sony ILCE-6600, E 16-55mm F2.8 G, 2024–2025)  
**Estética**: Dark cinematic · editorial · luxury

---

## Ordem Recomendada de Uso das Skills

```
1. stitch-design         → Design visual (wireframe/mockup das seções)
2. ui-ux-designer        → Validar UX, fluxo e hierarquia visual
3. tailwind-design-system → Criar o design system (tokens, cores, tipografia)
4. frontend-developer    → Implementar o código React/Next.js
5. nextjs-app-router-    → (se Next.js) Configurar SSR, SSG e Server Components
   patterns
6. ui-visual-validator   → Revisar screenshots, validar fidelidade ao design
7. accessibility-        → Auditoria WCAG — teclado, screen reader, contraste
   compliance
8. seo-structure-        → Estrutura de headers H1-H6, schema markup, sitemap
   architect
9. seo-meta-optimizer    → Title tags, meta descriptions, URLs otimizadas
```

---

## 1. STITCH DESIGN

**Quando usar**: Para criar o design visual de cada seção antes de codificar.  
**MCP necessário**: `mcp_StitchMCP_generate_screen_from_text`

### Prompt — Hero Section

```
/stitch-design

Cinematic, full-screen hero section for a high-end photographer/filmmaker portfolio.

**DESIGN SYSTEM (REQUIRED):**
- Platform: Web, Desktop-first (2560px)
- Palette: Obsidian (#0A0A0A for background), Warm White (#F5F0EB for text), 
  Amber Accent (#C9A96E for highlights), Charcoal (#1A1A1A for cards)
- Styles: Sharp corners for structural elements, subtle grain texture overlay,
  cinematic letterbox feel

**PAGE STRUCTURE:**
1. **Full-screen background**: Dark gradient with subtle film grain texture
2. **Navigation**: Minimal fixed nav — "THIAGO SAGRILLO" left-aligned in 
   condensed sans-serif, right side: WORK / ABOUT / CONTACT in small caps
3. **Hero Content**: Vertically centered — oversized display font "THIAGO SAGRILLO"
   (100px+), subtitle "PHOTOGRAPHER · FILMMAKER" in tracked uppercase,
   thin divider line, scroll indicator arrow
4. **Featured image**: Split layout — hero text left 50%, cinematic portrait 
   photo right 50%, with subtle parallax depth

Mood: High-end fashion magazine meets independent cinema. Think Magnum Photos 
meets A24 films aesthetic.
```

### Prompt — Portfolio Gallery Section

```
/stitch-design

Editorial masonry photo gallery for a fine art photography portfolio.

**DESIGN SYSTEM (REQUIRED):**
- Platform: Web, Desktop-first
- Palette: #0A0A0A background, #F5F0EB text, #C9A96E for hover states
- Styles: No borders, full-bleed images, elegant whitespace

**PAGE STRUCTURE:**
1. **Section Header**: "WORK" in large tracked uppercase, thin horizontal rule
2. **Filter Bar**: Minimal text filters — ALL · PORTRAIT · LANDSCAPE · EDITORIAL
3. **Masonry Grid**: 3-column asymmetric grid with varying row heights
   - Portrait photos (683×1024): occupy 1 column, full height
   - Feature photos: span 2 columns occasionally for rhythm
   - Hover state: subtle scale 1.02, overlay with photo title and year
4. **Load More**: Elegant thin-line button "SEE MORE WORK"

Mood: Museum gallery meets editorial magazine spread. Clean, precise, confident.
```

### Prompt — About Section

```
/stitch-design

Cinematic about/bio section for a photographer-filmmaker portfolio.

**DESIGN SYSTEM (REQUIRED):**
- Platform: Web, Desktop-first
- Palette: #0A0A0A background, #F5F0EB text, #C9A96E for accents
- Styles: Strong typographic hierarchy, editorial layout

**PAGE STRUCTURE:**
1. **Section Label**: "ABOUT" small caps, amber colored
2. **Split Layout**: Left — large portrait photo in film-strip style frame;
   Right — bio text
3. **Bio Text**: "Thiago Sagrillo é fotógrafo e cineasta baseado em [cidade]."
   Large pull quote style, then body text
4. **Equipment Note**: Small detail — "Shot on Sony ILCE-6600 · E 16-55mm F2.8 G"
5. **Stats Row**: "24+ Projects · 2024–2025 · Sony Alpha Series"

Mood: Personal but professional. Like a director's statement in a film catalog.
```

### Prompt — Contact Section

```
/stitch-design

Minimal luxury contact section for a creative portfolio.

**DESIGN SYSTEM (REQUIRED):**
- Platform: Web, Desktop-first  
- Palette: #0A0A0A background, #F5F0EB text, #C9A96E accents

**PAGE STRUCTURE:**
1. **Large Headline**: "LET'S WORK TOGETHER" — massive display type
2. **Email CTA**: Large clickable email address in amber color
3. **Social Links**: Instagram · Flickr · Vimeo — minimal icon links
4. **Footer**: Copyright line, minimal

Mood: Bold, direct, luxury brand feel. Less form, more direct contact.
```

---

## 2. UI/UX DESIGNER

**Quando usar**: Para validar a experiência do usuário, hierarquia visual e fluxo de navegação antes de codificar.

### Prompt — Revisão de UX do Portfolio

```
/ui-ux-designer

Revise o design UX do portfolio audiovisual de Thiago Sagrillo:

**Contexto**: Portfolio para fotógrafo/cineasta. Audiência: clientes corporativos, 
agências, editoras. Objetivo: conseguir contratações para projetos fotográficos 
e audiovisuais.

**Avalie**:
1. Hierarquia visual — o olho do usuário vai para o lugar certo?
2. Fluxo de navegação — Hero → Gallery → About → Contact faz sentido?
3. Mobile experience — as imagens portrait 683×1024 ficam bem em mobile?
4. Micro-interações — quais animações Framer Motion recomenda para o grid?
5. Calls to action — onde colocar CTAs para maximizar contato?

**Entregue**:
- Lista de problemas UX identificados (prioridade Alta/Média/Baixa)
- Recomendações de interações para o grid de fotos
- Estrutura de navegação recomendada
```

---

## 3. TAILWIND DESIGN SYSTEM

**Quando usar**: Para criar o `tailwind.config.js` com os tokens de design antes de qualquer componente.

### Prompt — Criar Design Tokens

```
/tailwind-design-system

Crie um design system completo no tailwind.config.js para o portfolio audiovisual 
de Thiago Sagrillo com estética dark cinematic.

**Tokens necessários**:

CORES:
- background: #0A0A0A (obsidian black)
- surface: #1A1A1A (charcoal — cards, nav)
- text-primary: #F5F0EB (warm white)
- text-secondary: #9A9590 (muted warm gray)
- accent: #C9A96E (warm gold/amber — highlights, CTAs)
- accent-hover: #E8C88A (lighter gold hover)
- border: #2A2A2A (subtle divider)

TIPOGRAFIA:
- font-display: 'Cormorant Garamond', serif (headlines editoriais)
- font-sans: 'Inter', sans-serif (UI, body text)
- font-mono: 'JetBrains Mono' (labels técnicos, metadados de câmera)

ESPAÇAMENTO:
- Sistema de 8px base
- section-padding: py-24 lg:py-32

ANIMAÇÕES:
- Adicionar keyframes para: fadeInUp, parallaxShift, imageReveal
- Transições: 300ms ease-in-out padrão, 600ms para imagens

**Entregue o arquivo tailwind.config.js completo** pronto para copiar.
```

---

## 4. FRONTEND DEVELOPER

**Quando usar**: Para implementar cada seção em código React + Tailwind + Framer Motion.

### Prompt — Implementar Hero Section

```
/frontend-developer

Implemente o Hero Section do portfolio de Thiago Sagrillo.

**Tech Stack**: React 19 + Vite, Tailwind CSS, Framer Motion

**Design Reference**: (cole o HTML do Stitch aqui, ou descreva)
- Full-screen hero (#0A0A0A background)
- Nav fixa: "THIAGO SAGRILLO" à esquerda, links à direita
- Texto hero: nome em 100px Cormorant Garamond, subtitle "PHOTOGRAPHER · FILMMAKER"
- Split layout: texto esquerda 50%, imagem portrait direita 50%
- Scroll indicator animado

**Animações Framer Motion necessárias**:
- Fade-in staggered do texto (nome → subtitle → divider → scroll indicator)
- Parallax no background ao scroll
- Nav que some/aparece ao fazer scroll

**Imagem hero**: Use a primeira foto do álbum Flickr (URL no flickr_album_data.json)

Entregue: componente `Hero.tsx` com todas as animações.
```

### Prompt — Implementar Galeria Masonry

```
/frontend-developer

Implemente a seção Gallery/Portfolio em React.

**Tech Stack**: React 19, Tailwind CSS, Framer Motion

**Dados**: Arquivo `flickr_album_data.json` com 24 fotos do Flickr
- Maioria portrait 683×1024
- URLs das fotos já estão no JSON

**Grid Layout**:
- Masonry grid — use CSS Grid com `grid-auto-rows` e `grid-row: span N`
- 3 colunas desktop, 2 tablet, 1 mobile
- Fotos portrait: span 2 rows; fotos landscape: span 1 row

**Comportamentos**:
- Lazy loading com `loading="lazy"` e IntersectionObserver
- Hover: scale(1.02) + overlay escuro com título e ano
- Click: lightbox modal com navegação prev/next
- Animação de entrada: staggered fade-up usando Framer Motion quando entrar no viewport

**Entregue**: componente `Gallery.tsx` + `Lightbox.tsx`
```

### Prompt — Implementar About Section

```
/frontend-developer

Implemente a seção About do portfolio.

**Tech Stack**: React 19, Tailwind CSS, Framer Motion

**Layout**:
- Split 50/50: imagem esquerda, texto direita
- Imagem: portrait photo em frame com grain texture CSS
- Texto: bio curta, pull quote, detalhe de equipamento

**Conteúdo do texto**:
- Nome: Thiago Sagrillo
- Bio: fotógrafo e cineasta (você pode sugerir 2-3 frases de bio genérica 
  elegante que o usuário pode personalizar depois)
- Equipment: "Sony ILCE-6600 · E 16-55mm F2.8 G"

**Animação**: Scroll-triggered reveal — imagem desliza da esquerda, 
texto da direita, usando Framer Motion `useInView`

Entregue: componente `About.tsx`
```

### Prompt — Implementar Contact Section

```
/frontend-developer

Implemente a seção Contact do portfolio.

**Tech Stack**: React 19, Tailwind CSS, Framer Motion

**Layout**:
- Headline gigante: "LET'S WORK TOGETHER"
- Email clicável em cor amber #C9A96E
- Links sociais: Instagram, Flickr, Vimeo
- Footer minimalista

**Animação**: Contador scroll, headline com split-text reveal (char by char)

Entregue: componente `Contact.tsx` + `Footer.tsx`
```

### Prompt — Integrar tudo no App

```
/frontend-developer

Integre todas as seções no App.tsx/page.tsx do portfolio.

**Seções na ordem**:
1. <Hero /> — full-screen
2. <Gallery /> — masonry grid com 24 fotos
3. <About /> — split layout
4. <Contact /> — headline + footer

**Comportamentos globais**:
- Smooth scroll entre seções (CSS `scroll-behavior: smooth`)
- Nav com indicador de seção ativa (Intersection Observer)
- Cursor customizado sutil (ponto amber que segue o mouse)
- Page loading screen com fade-out elegante

**Performance**:
- Lazy loading de imagens
- Prefetch das fotos Flickr mais importantes
- Font display: swap para evitar FOIT

Entregue: `App.tsx` integrado + `useScrollProgress.ts` hook
```

---

## 5. NEXT.JS APP ROUTER PATTERNS

**Quando usar**: Se migrar para Next.js 15 (recomendado para SEO e performance).

### Prompt — Setup Next.js com App Router

```
/nextjs-app-router-patterns

Configure o portfolio de Thiago Sagrillo em Next.js 15 com App Router.

**Estrutura de rotas necessária**:
- `/` — página principal do portfolio (Hero + Gallery + About + Contact)
- `/work/[slug]` — página individual de cada projeto (futuro)
- `/api/flickr` — route handler para buscar fotos do Flickr com cache

**Otimizações necessárias**:
1. Imagens do Flickr: usar `next/image` com `remotePatterns` para live.staticflickr.com
2. Gallery: Server Component que busca o JSON das fotos + Client Component para 
   animações
3. Metadata API: title, description, OpenGraph para cada página
4. Font optimization: Cormorant Garamond + Inter via `next/font`
5. Static generation das fotos do álbum

**Entregue**:
- `app/layout.tsx` com metadata global e fonts
- `app/page.tsx` com Server Component principal  
- `app/api/flickr/route.ts` com cache de 1 hora
- `next.config.js` com remotePatterns para Flickr
```

---

## 6. UI VISUAL VALIDATOR

**Quando usar**: Depois de implementar cada seção, para validar fidelidade visual ao design Stitch.

### Prompt — Validar Hero

```
/ui-visual-validator

Valide a implementação do Hero Section do portfolio de Thiago Sagrillo.

**Design original**: [cole a screenshot do Stitch]
**Implementação**: [cole screenshot do localhost:5173]

**Pontos de validação**:
- [ ] Tipografia correta (Cormorant Garamond para o nome, tamanho ~100px)
- [ ] Cores: background #0A0A0A, texto #F5F0EB, accent #C9A96E
- [ ] Layout split 50/50 correto
- [ ] Animações Framer Motion funcionando (fade-in staggered)
- [ ] Responsive: como fica em 375px (iPhone)?
- [ ] Performance: imagem hero carrega rápido com lazy load?

Reporte desvios com prioridade (Alto = visível ao usuário / Baixo = detalhe)
```

---

## 7. ACCESSIBILITY COMPLIANCE

**Quando usar**: Após o desenvolvimento, antes de publicar.

### Prompt — Auditoria de Acessibilidade

```
/accessibility-compliance

Faça auditoria WCAG 2.1 AA do portfolio de Thiago Sagrillo.

**Escopo**: Site completo — Hero, Gallery, About, Contact
**WCAG Level**: AA

**Checklist obrigatório**:

CONTRASTE:
- [ ] Texto #F5F0EB sobre #0A0A0A — ratio 4.5:1 mínimo?
- [ ] Texto #9A9590 sobre #0A0A0A — ratio suficiente para texto secundário?
- [ ] Accent #C9A96E sobre #0A0A0A — ratio ok para interactive elements?

IMAGENS:
- [ ] Todas as fotos têm `alt` text descritivo?
- [ ] Alt text das fotos de portrait descreve o conteúdo?

TECLADO:
- [ ] Nav navegável com Tab?
- [ ] Lightbox da gallery fecha com Escape?
- [ ] Focus visible em todos os elementos interativos?

SEMÂNTICA:
- [ ] Um único H1 por página?
- [ ] Landmarks corretos (nav, main, section, footer)?
- [ ] Botões são `<button>`, links são `<a>`?

Entregue lista de problemas + código de correção para cada item.
```

---

## 8. SEO STRUCTURE ARCHITECT

**Quando usar**: Para otimizar a estrutura de headers e adicionar schema markup.

### Prompt — Estrutura SEO do Portfolio

```
/seo-structure-architect

Crie a estrutura SEO completa para o portfolio de Thiago Sagrillo.

**Informações**:
- Nome: Thiago Sagrillo (thiagosagrillo)
- Câmera: Sony ILCE-6600 com E 16-55mm F2.8 G
- Conteúdo: 24 fotos de still photography, portrait e landscape
- Localização: [cidade — a definir]

**Hierarquia de Headers**:
```
H1: Thiago Sagrillo — Fotógrafo e Cineasta
  H2: Portfolio de Fotografia
    H3: [Nome de cada série/projeto]
  H2: Sobre Thiago Sagrillo
  H2: Contato
```

**Schema Markup necessário**:
1. `Person` schema — quem é Thiago Sagrillo
2. `ImageGallery` + `ImageObject` — para cada foto do álbum
3. `CreativeWork` — para o portfolio geral
4. `ContactPage` — para a seção de contato

Entregue o JSON-LD completo para cada schema, pronto para inserir no `<head>`.
```

---

## 9. SEO META OPTIMIZER

**Quando usar**: Para criar title tags e meta descriptions otimizadas.

### Prompt — Metadados SEO

```
/seo-meta-optimizer

Crie os metadados SEO otimizados para o portfolio de Thiago Sagrillo.

**Informações**:
- Fotógrafo/cineasta: Thiago Sagrillo
- Especialidade: fotografia still, retratos, natureza
- Câmera: Sony ILCE-6600
- Álbum: "THIAGO STILL" — 24 fotos 2024-2025

**Entregue**:

URL da página principal:
- Recomendação de URL (deve ter < 60 chars, incluir keyword principal)

Title Tag:
- 50-60 chars, keyword no início, power word, brand
- Exemplo base: "Thiago Sagrillo — Fotógrafo e Cineasta"

Meta Description:
- 150-160 chars, CTA, benefício claro, keywords secundárias
- Inclua "Sony ILCE-6600" se couber naturalmente

Open Graph:
- og:title, og:description, og:image (sugira a melhor foto do álbum como hero)

Twitter Card:
- twitter:card: summary_large_image
- twitter:creator: @thiagosagrillo (verificar handle)

Entregue código HTML completo do `<head>` pronto para copiar.
```

---

## Workflow Completo Recomendado

### Fase 1 — Design (1-2h)
1. Usar `/stitch-design` para gerar Hero, Gallery, About, Contact
2. Baixar HTMLs e screenshots em `.stitch/designs/`
3. Usar `/ui-ux-designer` para validar fluxo e propor ajustes

### Fase 2 — Sistema de Design (30min)
4. Usar `/tailwind-design-system` para gerar `tailwind.config.js`
5. Configurar fontes: Cormorant Garamond + Inter

### Fase 3 — Desenvolvimento (3-4h)
6. Usar `/frontend-developer` para cada componente (Hero → Gallery → About → Contact)
7. Se Next.js: usar `/nextjs-app-router-patterns` para SSR e otimizações
8. Testar localmente com `npm run dev`

### Fase 4 — Qualidade (1h)
9. Usar `/ui-visual-validator` para comparar implementação vs. design Stitch
10. Usar `/accessibility-compliance` para auditoria WCAG

### Fase 5 — SEO (30min)
11. Usar `/seo-structure-architect` para schema markup e estrutura H1-H6
12. Usar `/seo-meta-optimizer` para title, description, Open Graph

---

## Arquivos de Referência do Projeto

| Arquivo | Conteúdo |
|---------|----------|
| `flickr_album_data.json` | 24 fotos do álbum THIAGO STILL com URLs, dimensões e metadados |
| `tailwind.config.js` | Tokens de design (gerado pela skill) |
| `.stitch/designs/` | HTMLs e screenshots das seções geradas no Stitch |
| `.stitch/DESIGN.md` | Design system consolidado (gerado pela skill stitch-design) |

---

## Paleta de Cores de Referência Rápida

```
#0A0A0A  — Obsidian Black (background)
#1A1A1A  — Charcoal (cards, nav background)
#2A2A2A  — Dark Border (dividers)
#9A9590  — Warm Gray (text secondary, metadata)
#F5F0EB  — Warm White (text primary, headlines)
#C9A96E  — Amber Gold (accent, CTAs, hover states)
#E8C88A  — Light Gold (hover do accent)
```

## Tipografia de Referência Rápida

```
Display/Headlines → Cormorant Garamond (serif, editorial)
Body/UI         → Inter (sans-serif, legível)
Metadata/Labels → JetBrains Mono (monospace, técnico)
```
