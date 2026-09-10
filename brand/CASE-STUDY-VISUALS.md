# Crohnoz Labs — Case Study Visual System

This document defines the public visual contract for non-flagship engineering case studies in the Crohnoz portfolio.

The goal is to give every public case a recognizable Crohnoz entry point **without flattening differences in product maturity**.

## Hierarchy

The current public portfolio hierarchy remains:

1. **FDR** — flagship, `L2+ · Advanced Pilot / Production-Oriented`.
2. **Rental Operations** — selected operational engineering evidence.
3. **Crohnoz Forge** — `L1 · Prototype / R&D`.
4. **Crohnoz Fresh Market** — `L1 · Prototype / R&D`.
5. **IncluMe** — `L1 · Early Product`.

A visual upgrade never changes maturity by itself.

## Responsive case-study pairs

| Case | Desktop | Mobile | Capability signal |
|---|---|---|---|
| **Forge** | `assets/case-forge.svg` | `assets/case-forge-mobile.svg` | Product reasoning · discovery · evidence · stage gates · local-first handoff |
| **Fresh Market** | `assets/case-fresh-market.svg` | `assets/case-fresh-market-mobile.svg` | Perishable inventory · write integrity · operational continuity |
| **IncluMe** | `assets/case-inclume.svg` | `assets/case-inclume-mobile.svg` | Inclusive product design · citizen contribution · review boundary · feedback loop |

Use the desktop/mobile pair through `<picture>` with the mobile source selected below `700px`.

```html
<picture>
  <source media="(max-width: 700px)" srcset="../brand/assets/case-example-mobile.svg" />
  <img src="../brand/assets/case-example.svg" alt="Descriptive case-study label" width="100%" />
</picture>
```

## Required visual content

Every case header should communicate, at a glance:

- product/system name;
- current maturity or explicit portfolio role;
- the distinct capability the case proves;
- three concise evidence themes;
- an outcome-oriented workflow or system sequence.

The visual should **summarize evidence already present in the case study**. It must not introduce roadmap features, adoption claims, scale claims or technical behavior that the public case cannot support.

## Desktop composition

Desktop case headers may use a panoramic layout with three evidence cards when the text remains readable at GitHub content width.

Preferred order:

`CAPABILITY → SYSTEM → MATURITY → EVIDENCE THEMES → FLOW`

Keep type large enough to survive GitHub scaling. Decorative elements must remain secondary to the product name, maturity and proof themes.

## Mobile composition

Mobile variants must recompose rather than shrink the desktop canvas.

Preferred structure:

1. capability eyebrow;
2. system name;
3. one-line positioning statement;
4. maturity pill;
5. three vertically stacked proof cards;
6. simplified flow.

Remove decorative density before reducing type size.

## Visual semantics

The current case accents intentionally distinguish capability while inheriting the Crohnoz master palette:

- **Forge:** magenta → purple → blue — product reasoning and exploration;
- **Fresh Market:** cyan → blue → purple — operational/data integrity;
- **IncluMe:** magenta → violet → cyan — inclusive multi-stakeholder workflows.

Deep Space `#0A0B14` remains the base background. Sora is used for display text and Inter for supporting text.

## Maturity integrity

Visual polish must never be read as a maturity upgrade.

- `L1` means the core concept is proven as a prototype or early product.
- `L2` requires validated operation with real users/workflows.
- `L3` requires reliable production evidence.
- `L4` requires repeatable scale, continuity and improvement.

When a product advances, update **the case-study text, maturity map, profile surface and visual header together** so public claims remain internally consistent.

## Publication boundary

Case headers are public communication assets. They may contain product/problem abstractions and sanitized engineering concepts, but must not contain:

- credentials or secrets;
- private infrastructure details;
- customer or patient data;
- private repository structure;
- confidential client logic;
- unverifiable metrics.

## Principle

**Visual hierarchy should make evidence easier to inspect—not make an early product look more mature than it is.**
