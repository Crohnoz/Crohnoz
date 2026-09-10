# Crohnoz Labs — Brand System Future 1.0

This directory is the canonical source of truth for the Crohnoz Labs visual identity and public portfolio presentation system.

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
- `assets/crohnoz_icon.ico` — legacy application icon retained as a brand asset only.
- `assets/github-banner.svg` — **premium founder-profile hero** combining Enrique Flores, Crohnoz Labs and the current flagship signal in one first-screen composition.
- `assets/github-banner-mobile.svg` — vertical mobile hero; preferred below `700px`.

### Systems communication

- `assets/crohnoz-operating-model.svg` — canonical visual explanation of how Crohnoz Labs turns real operational problems into scalable systems.
- `assets/fdr-flagship.svg` — flagship product card. Use when one system has materially stronger operational maturity than the rest of the portfolio.
- `assets/fdr-product-showcase.svg` — desktop sanitized reconstruction of implemented FDR product surfaces: professional workspace, public booking and professional presence.
- `assets/fdr-product-showcase-mobile.svg` — stacked mobile reconstruction of the same implemented FDR surfaces; preferred below `700px`.
- `assets/fdr-architecture.svg` — sanitized high-level architecture for the FDR public engineering case study.
- `assets/fdr-evidence-strip.svg` — six-part proof strip for booking integrity, public profiles, lifecycle, privacy, staging and regression controls.
- `assets/portfolio-maturity.svg` — desktop honest maturity map from `L0` through `L4`.
- `assets/portfolio-maturity-mobile.svg` — stacked mobile maturity view; preferred below `700px`.
- `assets/engineering-depth.svg` — capability map organized by engineering problem domain rather than technology count.
- `assets/delivery-contexts.svg` — cross-domain delivery view for healthcare, commerce/operations, public-sector workflows and infrastructure/automation.
- `assets/professional-engagement.svg` — professional conversion layer describing the kinds of engineering engagements that best fit Enrique Flores / Crohnoz Labs.
- `assets/evidence-library.svg` — visual index for the public evidence catalog, separating flagship, selected operational evidence and product R&D.
- `assets/selected-evidence.svg` — legacy exploratory evidence showcase. It may be used below the maturity view, but must not visually compete with the current flagship.

## Premium profile composition

The public GitHub profile should behave like a **portfolio control center**, not a long developer README.

Preferred hierarchy:

1. **Founder hero** — Enrique Flores + role + Crohnoz Labs + current flagship signal.
2. **Primary actions** — engineering case, safe live demo, public evidence library and Crohnoz Labs.
3. **Flagship system** — the strongest current operational proof.
4. **Product surfaces** — sanitized, visually inspectable implemented interfaces.
5. **Engineering proof** — concrete behaviors already enforced by the system.
6. **Engineering depth** — capability by problem domain.
7. **Real-world delivery** — cross-domain transferability.
8. **Operating model** — how Crohnoz moves from problem to evidence.
9. **Portfolio maturity** — honest position of active systems.
10. **Professional collaboration** — best-fit problems and a clear route to the professional profile.
11. **Deep dive** — detailed tables, stack and operating principles collapsed below the primary visual narrative.

The first screen must answer: **who is Enrique, what is Crohnoz, what is the strongest proof, and where can I inspect it?**

## Responsive composition

The profile is designed for both desktop and mobile GitHub surfaces.

Use `<picture>` with `media="(max-width: 700px)"` when a panoramic diagram becomes too dense to remain legible on a narrow screen.

Current responsive pairs:

- `github-banner-mobile.svg` → `github-banner.svg`;
- `fdr-product-showcase-mobile.svg` → `fdr-product-showcase.svg`;
- `portfolio-maturity-mobile.svg` → `portfolio-maturity.svg`.

Mobile variants must **recompose** information rather than merely shrink the desktop canvas. Preserve the same claims and maturity state, but increase text size, stack cards vertically and remove decorative details when necessary.

Do not create a mobile variant when the SVG remains legible as a secondary illustration and the surrounding HTML already carries the essential information.

## Product-surface evidence

A product-surface showcase may reconstruct real implemented interfaces when literal screenshots are unsuitable, unstable or would expose sensitive data.

Requirements:

- every represented surface must exist in the implemented product;
- labels and records must be fictitious or generic;
- the visual must identify itself as a sanitized reconstruction when there is any risk of being mistaken for a literal screenshot;
- it must not invent controls, states or capabilities;
- it should communicate **operability**, not decorative UI concepts;
- when a safe public demo exists, the showcase should link to it.

For FDR, the canonical surfaces are:

- **Professional workspace** — daily agenda, next attention, state-aware actions and operational metrics;
- **Public booking** — service, professional, real availability, review and confirmation;
- **Professional presence** — publication, verification and visibility controls separated from private clinical operations.

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

A maturity label changes only when evidence supports the change. A deployable build, polished UI or large codebase does not by itself advance maturity.

## Portfolio hierarchy

Public surfaces must distinguish **maturity** from **potential**.

The preferred hierarchy is:

1. **Flagship system** — strongest current operational proof; largest visual area and clearest CTA.
2. **Product-surface evidence** — implemented interfaces shown safely.
3. **Engineering proof strip** — concrete, inspectable behaviors already implemented in the flagship.
4. **Engineering depth** — capability by problem domain rather than tool count.
5. **Real-world delivery contexts** — transferability across domains without exposing client-sensitive implementation.
6. **Operating model** — how Crohnoz works across products.
7. **Current portfolio maturity** — where every active system actually sits from L0 to L4.
8. **Professional engagement** — the kinds of problems worth bringing to Enrique / Crohnoz.
9. **Exploratory evidence** — early systems and R&D after the flagship and maturity view.

Do not present prototypes as production systems. Honest maturity increases credibility.

## Flagship component

The flagship visual should answer four questions immediately:

- **What is the system?**
- **What operational domain does it serve?**
- **What maturity does it honestly have?**
- **What engineering evidence can be inspected?**

The entire flagship visual should be clickable when the surface supports it, linking to a sanitized engineering case study.

## Engineering proof component

A proof strip summarizes **implemented engineering behavior**, not aspirations. Every card must be traceable to a public case-study statement or safe observable product behavior.

Preferred proof categories include domain integrity, public/private boundaries, explicit workflow state, privacy/security behavior, reproducible delivery/staging and regression/reliability controls.

Avoid vanity metrics or numerical claims unless their source and interpretation are stable.

## Engineering Depth component

Engineering capability should be grouped by the kind of problem being solved:

- Product Systems
- Backend & Data
- Security & Trust
- Operations
- AI & Automation
- Physical Systems

Technology badges are secondary evidence. They should not be the primary way expertise is communicated.

## Real-world delivery component

The delivery-context visual exists to show that the engineering approach transfers across operational domains.

Use broad categories when client attribution is private or unnecessary. Describe the **type of operational challenge**, not client names, infrastructure, datasets or confidential implementation details.

## Professional engagement component

The professional-engagement layer converts technical credibility into a clear next step without turning the profile into generic sales copy.

Preferred engagement categories:

- **Product & Systems Architecture** — domain boundaries, workflows and technical direction;
- **Operational Software** — Django/APIs/data workflows and role-aware interfaces;
- **Backend Integrity & Modernization** — scope, security, reliability, testing, observability and CI/CD;
- **Applied AI & Automation** — agents, workflows, operational intelligence and human-in-the-loop systems.

Rules:

- describe **problems worth solving**, not generic “hire me” claims;
- link to a maintained professional profile or contact surface;
- do not claim availability, delivery dates, rates or guarantees unless they are deliberately maintained elsewhere;
- preserve the evidence-first tone: inspect capability before asking for contact.

## Public case-study contract

Every case study in `evidence/` should answer the same core questions so the library remains comparable and maintainable.

Required elements:

1. **Status / maturity** — current level or explicit non-flagship classification.
2. **Problem** — the real operational or product problem being addressed.
3. **What exists today** — distinguish implemented behavior from intended roadmap.
4. **Inspectable engineering evidence** — rules, boundaries, workflows, tests or public product behavior.
5. **Public/private boundary** — what can safely be shown and what remains intentionally private.
6. **What is not claimed** — mandatory for early products where polished demos could imply more maturity than exists.
7. **Next maturity gate** — required for L0/L1/L2 systems.
8. **Clear navigation** — return to the evidence library plus demo/repository CTA when a safe public surface exists.

Do not use a case study to compensate for missing evidence with marketing language.

## Public Evidence Library

The evidence library is a curated **portfolio index**, not a repository list.

Preferred grouping:

- **Flagship engineering case** — currently FDR;
- **Selected operational engineering** — mature enough to show concrete rules, but not presented as flagship;
- **Product R&D** — L0/L1 explorations whose value is learning, framing or prototype evidence.

A repository can exist publicly without deserving top-level portfolio weight.

## Navigation hierarchy

Primary actions on a profile or case study should use large, high-contrast CTAs. Preferred order:

1. flagship engineering case;
2. safe live demo when available;
3. public evidence catalog;
4. Crohnoz Labs / professional profile.

Small inline Markdown links may remain as secondary navigation only.

## Profile repository hygiene

`Crohnoz/Crohnoz` is an **editorial portfolio repository**, not an application build workspace.

The root should remain limited to:

- profile README variants;
- `brand/`;
- `evidence/`;
- minimal repository metadata such as `.gitignore`.

Do not commit virtual environments, compiled executables, installers, PyInstaller output, build directories, dependency trees, runtime databases or packaged ZIP distributions to the profile repository.

When historical non-profile material must be removed from the public surface, preserve a recovery branch before cleanup when useful. Application code belongs in a dedicated product repository.

## Maintenance standard

A premium portfolio degrades when its claims become stale. Review the public surface when any of these change:

- flagship maturity;
- live-demo location;
- public/private boundary;
- a product advances or is retired;
- a major engineering capability becomes demonstrable;
- professional positioning changes.

Do not update maturity automatically from commit count, feature count or visual polish.

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
14. Proof visuals must describe implemented behavior; do not use them for roadmap claims.
15. Cross-domain visuals should use generic operational categories when attribution would expose unnecessary client context.
16. Do not add numerical proof points unless they can be maintained accurately over time.
17. Detailed stack and principle sections should not interrupt the first-screen product narrative; collapse or move them below the primary evidence path.
18. Product-surface reconstructions must be clearly sanitized and must never be presented as literal screenshots when they are illustrative reconstructions.
19. Early-product case studies must state both the current maturity and the next evidence gate.
20. The profile repository must remain free of application build artifacts and local runtime environments.
21. Professional CTAs should follow evidence, not replace it.
22. Responsive profile visuals must recompose dense content for narrow screens rather than simply shrinking desktop artwork.

## Brand principles

**Impacto real · Soluciones prácticas · Ingeniería con sentido · Innovación accesible · Personas primero**

The previous root-level logo/application files are deprecated by this system. Public profile code and documentation should reference `brand/assets/` only.
