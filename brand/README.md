# Crohnoz Labs — Brand System Future 1.0

This directory is the canonical source of truth for the Crohnoz Labs visual identity and public portfolio system.

## Core identity

- **Master brand:** Crohnoz Labs
- **Primary claim:** **Tecnología que resuelve problemas reales.**
- **Signature:** `IDEAS · SOFTWARE · IMPACTO`
- **Operating language:** `BUILD · INTEGRATE · AUTOMATE · OBSERVE · PROTECT · IMPROVE`
- **Systems narrative:** `PROBLEM → SYSTEM → EVIDENCE → SCALE`
- **Primary mark:** vertical signal / waveform bars

## Visual tokens

| Token | HEX | Role |
|---|---|---|
| Deep Space | `#0A0B14` | Primary background |
| Purple | `#8B5CF6` | Core innovation accent |
| Magenta | `#EC4899` | Energy / selected action |
| Cyan | `#06B6D4` | Technology / confidence |
| Blue | `#3B82F6` | Stability / evidence |
| Violet Glow | `#A855F7` | Controlled highlight only |
| Light Neutral | `#F8FAFC` | High-contrast typography |

**Display:** Sora Bold / Semibold.  
**Body / UI:** Inter Regular / Medium / Semibold.  
Use system sans-serif fallbacks when required.

---

## Premium profile principle

The public profile should feel like a **calm product interface**, not a decorated developer README.

Premium composition means:

- strong hierarchy before decoration;
- generous negative space;
- one clear flagship;
- no more than **three primary first-screen actions**;
- secondary destinations presented as quiet text navigation;
- subtle gradients and low-opacity glow rather than gaming-style neon;
- repeated information removed when the visual already communicates it;
- engineering depth available without forcing every visitor through it.

> **If everything is highlighted, nothing is prioritized.**

### First-screen questions

The first screen must answer four things quickly:

1. Who is Enrique?
2. What is Crohnoz Labs?
3. What is the strongest current proof?
4. Where can that proof be inspected?

### Current primary actions

1. **FDR engineering case**
2. **FDR safe live demo**
3. **Public evidence library**

Crohnoz Labs, the professional profile, language selection and the Brand System are **secondary navigation**, not competing primary buttons.

---

## Canonical profile assets

### Founder surface

- `assets/github-banner.svg` — desktop founder hero.
- `assets/github-banner-mobile.svg` — mobile founder hero below `700px`.
- `assets/cta-fdr-case.svg` — primary case-study CTA.
- `assets/cta-fdr-demo.svg` — primary safe-demo CTA.
- `assets/cta-evidence.svg` — primary public-evidence CTA.

### Flagship / evidence

- `assets/fdr-flagship.svg` — desktop FDR flagship card.
- `assets/fdr-flagship-mobile.svg` — mobile flagship card.
- `assets/fdr-product-showcase.svg` — sanitized desktop product-surface reconstruction.
- `assets/fdr-product-showcase-mobile.svg` — mobile reconstruction.
- `assets/fdr-architecture.svg` — sanitized architecture.
- `assets/fdr-evidence-strip.svg` — implemented engineering proof strip.
- `assets/evidence-library.svg` — evidence catalog header.

### Portfolio system

- `assets/engineering-depth.svg` — capability by engineering problem domain.
- `assets/delivery-contexts.svg` — cross-domain delivery contexts.
- `assets/crohnoz-operating-model.svg` — canonical operating model.
- `assets/portfolio-maturity.svg` — desktop maturity map.
- `assets/portfolio-maturity-mobile.svg` — mobile maturity map.
- `assets/professional-engagement.svg` — professional-fit layer.

### Case-study headers

- `assets/case-rental-operations.svg` / `assets/case-rental-operations-mobile.svg`
- `assets/case-forge.svg` / `assets/case-forge-mobile.svg`
- `assets/case-fresh-market.svg` / `assets/case-fresh-market-mobile.svg`
- `assets/case-inclume.svg` / `assets/case-inclume-mobile.svg`

---

## Preferred profile sequence

1. **Founder hero** — identity, role and current flagship signal.
2. **Three primary actions** — case, demo, evidence.
3. **Flagship engineering case** — strongest operational proof.
4. **Product surfaces** — implemented interfaces shown safely.
5. **Engineering proof** — behavior already enforced.
6. **Engineering depth** — capability by problem class.
7. **Portfolio maturity** — honest product position.
8. **Operating model** — how Crohnoz works.
9. **Real-world delivery** — transferability across domains.
10. **Professional collaboration** — where the approach creates value.
11. **Deep dive** — optional technical detail.

Detailed stack badges should never interrupt the first-screen narrative.

---

## Calm UI rules

### Density

- Prefer **3 primary CTAs** over 6–8 competing badges.
- Avoid repeating the same destination immediately above and below the same visual.
- Prefer short proof statements over dense microcopy.
- Use whitespace to separate changes in narrative intent.

### Light and color

- Deep Space remains dominant.
- Magenta / purple / cyan are accents, not full-surface paint.
- Glow should support focus, not define every boundary.
- Panel borders should generally remain low opacity.
- Neutral surfaces carry most information; chromatic accents indicate hierarchy.

### Buttons

- Primary actions should use Crohnoz-owned SVG components rather than split-label badge styling.
- Buttons in the same action group should share height, radius and typography.
- Color communicates role: purple = case/evidence, cyan = live product proof, blue = library/navigation.
- Secondary navigation should usually be inline text.

### Copy

Prefer short, operational statements:

- **I turn operational complexity into working systems.**
- **Evidence, not claims.**
- **Operational contracts first. UI second.**

Avoid inflated language, generic “hire me” copy and feature-count marketing.

---

## Responsive composition

Use `<picture>` with `media="(max-width: 700px)"` when a panoramic visual becomes too dense.

Canonical responsive pairs:

- `github-banner-mobile.svg` → `github-banner.svg`
- `fdr-flagship-mobile.svg` → `fdr-flagship.svg`
- `fdr-product-showcase-mobile.svg` → `fdr-product-showcase.svg`
- `portfolio-maturity-mobile.svg` → `portfolio-maturity.svg`
- all current case-study header mobile/desktop pairs

Mobile variants must **recompose**, not simply scale down. Increase text size, stack evidence and remove decorative detail when needed.

---

## Evidence-first system

Public evidence may include:

- sanitized architecture;
- implemented product behavior;
- demos with fictitious data;
- sanitized product-surface reconstructions;
- security and reliability practices;
- engineering decisions;
- stable non-sensitive evidence;
- honest maturity status.

Keep private:

- credentials and secrets;
- production/customer data;
- private topology;
- complete proprietary implementations;
- client-confidential logic.

**Evidence is public by design. Product implementation is private by default.**

### Product-surface reconstruction

A reconstruction is acceptable only when:

- every represented surface exists in the implemented product;
- labels and records are fictitious or generic;
- the visual is clearly identified as sanitized when necessary;
- no controls or states are invented;
- the purpose is to demonstrate operability, not concept art.

---

## Product maturity

| Level | Name | Meaning |
|---|---|---|
| `L0` | Idea | Problem and opportunity defined |
| `L1` | Prototype | Core concept proven |
| `L2` | Pilot | Operation validated with real workflows |
| `L2+` | Advanced Pilot | Strong production-oriented engineering without claiming full production maturity |
| `L3` | Production | Reliable production evidence |
| `L4` | Scale | Repeatable growth, continuity and improvement |

Maturity changes only when evidence supports it. A polished interface, deployment or large codebase does not upgrade a product by itself.

Current hierarchy:

- **FDR** — `L2+ · Advanced Pilot`, current flagship.
- **Rental Operations** — selected operational evidence, non-flagship.
- **Forge** — `L1 · Prototype / R&D`.
- **Fresh Market** — `L1 · Prototype / R&D`.
- **IncluMe** — `L1 · Early Product`.

---

## Public case-study contract

Every file under `evidence/` should make these explicit:

1. current status / maturity;
2. real problem;
3. what exists today;
4. inspectable engineering evidence;
5. public/private boundary;
6. what is not claimed;
7. next maturity gate for early products;
8. clear navigation to the library and safe public surfaces.

Do not compensate for missing evidence with marketing language.

---

## Profile repository hygiene

`Crohnoz/Crohnoz` is editorial portfolio infrastructure, not an application workspace.

Allowed root responsibilities:

- profile README variants;
- `brand/`;
- `evidence/`;
- `.github/` validation;
- minimal repository metadata such as `.gitignore`.

Do not commit virtual environments, dependency trees, executables, installers, runtime databases, packaged ZIPs or build output.

The `Profile Contract` CI must protect local references, responsive assets, maturity hierarchy, SVG validity and repository hygiene.

---

## Maintenance

Review the public surface whenever one of these changes:

- flagship maturity;
- demo URL;
- public/private boundary;
- a product advances or is retired;
- a new capability becomes demonstrable;
- professional positioning changes.

Do not update maturity from commit count, feature count or visual polish.

## Brand principles

**Impacto real · Soluciones prácticas · Ingeniería con sentido · Innovación accesible · Personas primero**
