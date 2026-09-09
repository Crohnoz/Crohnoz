# Crohnoz Labs — Brand System Future 1.0

This directory is the canonical source of truth for the Crohnoz Labs visual identity.

## Core identity

- **Master brand:** Crohnoz Labs
- **Primary claim:** **Tecnología que resuelve problemas reales.**
- **Signature:** `IDEAS · SOFTWARE · IMPACTO`
- **Operating language:** `BUILD · INTEGRATE · AUTOMATE · OBSERVE · PROTECT · IMPROVE`
- **Systems narrative:** `PROBLEM → SYSTEM → EVIDENCE → SCALE`
- **Primary mark:** vertical signal / waveform bars. Do not substitute cubes, waves, monograms or unrelated symbols.

## Official palette

| Token | HEX | Use |
|---|---|---|
| Deep Space | `#0A0B14` | Primary background |
| Purple | `#8B5CF6` | Innovation / gradient core |
| Magenta | `#EC4899` | Energy / action |
| Cyan | `#06B6D4` | Technology / confidence |
| Blue | `#3B82F6` | Stability / development |
| Violet Glow | `#A855F7` | Accent / future |
| Light Neutral | `#F8FAFC` | Contrast / legibility |

## Typography

- **Display / headlines:** Sora Bold / Semibold
- **Body / UI:** Inter Regular / Medium / Semibold
- Fall back to system sans-serif when the preferred fonts are unavailable.

## Asset hierarchy

### Core identity

- `assets/logo-horizontal-dark.svg` — default master lockup for dark surfaces.
- `assets/logo-horizontal-light.svg` — light-surface lockup.
- `assets/logo-stacked-dark.svg` — vertical / compact lockup.
- `assets/mark.svg` — stand-alone mark.
- `assets/favicon.svg` — web favicon source.
- `assets/crohnoz_icon.ico` — Windows / PyInstaller icon.
- `assets/github-banner.svg` — technical profile / repository banner.

### Systems communication

- `assets/crohnoz-operating-model.svg` — canonical visual explanation of how Crohnoz Labs turns real operational problems into scalable systems.
- `assets/fdr-flagship.svg` — flagship product card. Use when one system has materially stronger operational maturity than the rest of the portfolio.
- `assets/portfolio-maturity.svg` — canonical honest maturity map from `L0` through `L4`.
- `assets/engineering-depth.svg` — capability map organized by engineering problem domain rather than technology count.
- `assets/selected-evidence.svg` — legacy exploratory evidence showcase. It may be used below the maturity view, but must not visually compete with the current flagship.

## Crohnoz Operating Model

The **Crohnoz Operating Model** is the canonical systems diagram for public profiles, presentations and high-level product documentation.

It communicates five layers:

1. **Leadership** — Enrique Flores · Founder · Product & Systems Architecture.
2. **Core ecosystem** — Crohnoz Labs as the technology and product system.
3. **Capabilities** — Product, Engineering, AI & Automation, Hardware and Operations.
4. **Delivery** — cross-functional execution through a shared delivery engine.
5. **Lifecycle and maturity** — `DISCOVER → DESIGN → BUILD → VALIDATE → DEPLOY → OPERATE → IMPROVE`, progressing from `L0 IDEA` to `L4 SCALE`.

### Product maturity levels

| Level | Name | Meaning |
|---|---|---|
| `L0` | Idea | Problem and opportunity defined |
| `L1` | Prototype | Core concept proven |
| `L2` | Pilot | Operation validated with real users or workflows |
| `L2+` | Advanced Pilot | Substantial production-oriented engineering exists, but full production maturity is not yet claimed |
| `L3` | Production | Reliable operational delivery with production evidence |
| `L4` | Scale | Repeatable growth, continuity and improvement |

The visual should remain intentionally high-level. Do not turn it into a detailed infrastructure, org-chart or repository-dependency diagram.

## Portfolio hierarchy

Public surfaces must distinguish **maturity** from **potential**.

The preferred hierarchy is:

1. **Flagship system** — the strongest current operational proof. It receives the largest visual area and the clearest CTA.
2. **Engineering evidence** — domain contracts, reliability, privacy and delivery practices that can be demonstrated without exposing private implementation.
3. **Operating model** — explains how Crohnoz works across products.
4. **Current portfolio maturity** — shows where every active system actually sits from L0 to L4.
5. **Exploratory evidence** — early systems and R&D appear after the flagship and maturity view.

Do not present prototypes as production systems. Honest maturity increases credibility.

## Flagship component

The flagship visual should answer four questions immediately:

- **What is the system?**
- **What operational domain does it serve?**
- **What maturity does it honestly have?**
- **What engineering evidence can be inspected?**

The entire flagship visual should be clickable when the surface supports it, linking to a sanitized engineering case study.

## Engineering Depth component

Engineering capability should be grouped by the kind of problem being solved:

- Product Systems
- Backend & Data
- Security & Trust
- Operations
- AI & Automation
- Physical Systems

Technology badges are secondary evidence. They should not be the primary way expertise is communicated.

## Rules

1. Keep the mark proportions intact.
2. Preserve the magenta → purple → cyan gradient as the principal chromatic signature.
3. Prefer Deep Space backgrounds. On light backgrounds use the official light lockup.
4. Do not add unapproved symbols or replace the signal mark.
5. Maintain generous clear space around the mark and wordmark.
6. Use the claim exactly as written in Spanish unless a localized campaign explicitly requires translation.
7. New Crohnoz products should inherit these tokens before introducing product-level accent colors.
8. Use the Operating Model for public ecosystem explanation; use technical architecture diagrams for implementation detail.
9. Keep public diagrams outcome-oriented: problem, capability, delivery, evidence and maturity before infrastructure detail.
10. A flagship must have materially stronger evidence than surrounding products.
11. Never give L1 prototypes the same visual weight as L2+/L3 systems.
12. Public case studies must remain sanitized: evidence first, proprietary implementation private by default.
13. Primary navigation and case-study actions should use large, high-contrast CTAs on profile surfaces; avoid relying only on small inline Markdown links.

## Brand principles

**Impacto real · Soluciones prácticas · Ingeniería con sentido · Innovación accesible · Personas primero**

The previous root-level logo files are deprecated by this system. Code should reference `brand/assets/` instead.
