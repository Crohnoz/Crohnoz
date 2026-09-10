<div align="center">

<a href="README.md"><img src="https://img.shields.io/badge/←_PUBLIC_EVIDENCE-0A0B14?style=for-the-badge&logo=readme&logoColor=white" height="34" alt="Back to Public Evidence" /></a>
<a href="https://github.com/Crohnoz/Crohnoz-Rental-Ops"><img src="https://img.shields.io/badge/OPEN-PUBLIC_REPOSITORY-A855F7?style=for-the-badge&logo=github&logoColor=white" height="34" alt="Open Rental Operations repository" /></a>

# Rental Operations · Selected Operational Case

`CURATED OPERATIONAL EVIDENCE · NON-FLAGSHIP`

**Charges · payments · vouchers · settlements · RLS · public/private isolation**

</div>

> This case exists to show transferable operational engineering beyond healthcare. It is deliberately **not** presented as a finished multi-tenant SaaS product or as a peer to the FDR flagship.

---

## Operational problem

Small-building administration combines recurring charges, payments, vouchers, contracts, tenant changes and end-of-lease settlements. When those processes live across spreadsheets, documents and manual calculations, the engineering challenge is preserving **state, traceability and clear financial rules** without increasing operator friction.

## What exists today

Crohnoz Rental Ops provides a sanitized public surface around a deliberately separated operating model:

- a fictitious-data demo for inspectable workflows;
- an authenticated private mode backed by Supabase/PostgreSQL;
- owner-level Row Level Security boundaries;
- browser-session working state;
- backup/restore-oriented continuity behavior.

## Operational rules worth inspecting

| Rule | Engineering meaning |
|---|---|
| **Traceable rounding** | Small CLP rounding differences are carried forward rather than silently discarded |
| **Payment evidence** | Sequential voucher folios preserve an operator-visible relationship with payment activity |
| **Exit settlement** | Guarantee, debt, retained utilities and discounts are modeled as explicit settlement inputs |
| **Environment separation** | Public demonstration and private operational data do not share the same trust boundary |
| **Database authorization** | Ownership isolation is enforced by RLS rather than UI assumptions |

## Public / private system view

<div align="center">

### `PUBLIC DEMO → FICTITIOUS DATA → BROWSER-LOCAL WORKFLOW`

### `PRIVATE MODE → AUTH → POSTGRESQL / SUPABASE → RLS → OWNER DATA`

</div>

## Security boundary

The public architecture is designed around several constraints:

- the demo must never depend on the private operational database;
- private operation requires authentication;
- authorization is enforced at the data layer;
- privileged service credentials never belong in the browser or public repository;
- real records and client-specific identifiers stay outside the public evidence layer.

## Current engineering surface

`React · Vite · JavaScript · Supabase Auth · PostgreSQL · Row Level Security · Netlify · JSON backup / restore`

## Current limits

The current private model is intentionally narrow: one owner per workspace. A broader multi-user product would require organizations, memberships, explicit roles, per-user audit history and progressive domain normalization.

That limitation is part of the case study rather than something hidden from it.

## Public evidence

<div align="center">

<a href="https://github.com/Crohnoz/Crohnoz-Rental-Ops"><img src="https://img.shields.io/badge/INSPECT-SANITIZED_PUBLIC_REPO-A855F7?style=for-the-badge&logo=github&logoColor=white" height="36" alt="Inspect sanitized Rental Operations repository" /></a>

</div>

---

<div align="center">

**Operational rules → explicit state → traceable evidence.**

<a href="README.md"><img src="https://img.shields.io/badge/RETURN-PUBLIC_EVIDENCE-8B5CF6?style=for-the-badge" height="34" alt="Return to Public Evidence" /></a>

</div>
