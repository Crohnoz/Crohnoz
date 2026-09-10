# Rental Operations · Engineering Case Study

**Selected Operational System · Public Sanitized Evidence**

Small-building administration combines recurring charges, payments, vouchers, contracts, tenant changes and end-of-lease settlements. When those processes live across spreadsheets, documents and manual calculations, the main engineering problem is not simply CRUD: it is preserving **state, traceability and clear operational rules** without increasing administrative friction.

This case study documents the public engineering boundary of the Crohnoz rental-administration system. It intentionally excludes real tenant data, credentials and private deployment details.

## Operational problem

The target workflow requires an administrator to answer questions such as:

- Which units are occupied and by whom?
- What has been charged, paid or partially paid?
- Which voucher belongs to which payment?
- How should small rounding differences be carried forward?
- What must be considered when a tenant leaves?
- How can the operator recover from a local mistake or browser failure?

The system turns those questions into explicit application state rather than leaving them to memory or disconnected paperwork.

## Public / private architecture

The same application supports two deliberately separated modes.

### Public demonstration

- fictitious dataset representing 23 apartments;
- browser-local interaction only;
- no connection to the private database;
- reset capability for restoring the original demonstration state.

### Private operation

- authentication required before rendering operational data;
- centralized workspace backed by Supabase/PostgreSQL;
- Row Level Security used to isolate records by owner;
- temporary browser working copy stored in `sessionStorage`;
- real operational data excluded from the public repository and demo.

The point of this split is not cosmetic. It allows the system to remain inspectable publicly while preserving a separate trust boundary for real operation.

## Domain rules worth inspecting

### Traceable rounding

Charges are rounded to the nearest CLP $100. The difference is not discarded: it is stored with the opposite sign as the next adjustment so the following charge compensates it.

That makes a small accounting rule explicit and auditable rather than hiding it inside a visual total.

### Payment evidence

Voucher generation uses sequential folios and supports thermal-print workflows, keeping a direct relationship between payment activity and operator-visible evidence.

### Exit settlement

The departure workflow models more than a generic “close contract” action. It can account for guarantee, outstanding debt, pending utility retention and discounts before producing the final settlement.

## Security and data boundary

The public architecture is designed around a few simple constraints:

- the demo must never connect to the private database;
- private operation requires an authenticated session;
- authorization must be enforced by database policy rather than UI assumptions;
- browser persistence for private data is limited to the active session;
- privileged service credentials do not belong in the client or repository;
- client-specific identifiers and real records are outside the public evidence layer.

## Current engineering surface

- React
- Vite
- JavaScript
- Supabase Auth
- PostgreSQL / Supabase
- Row Level Security
- Netlify
- JSON backup / restore workflow

## Current limits

The current private model is intentionally narrow: one owner per workspace. A broader multiuser product would require organizations, memberships, explicit roles, per-user audit history and progressive normalization of the domain.

This is therefore presented as a **selected operational engineering case**, not as evidence of a finished multi-tenant SaaS platform.

## Evidence

Public repository:

https://github.com/Crohnoz/sistema_gestion_de_arriendos

The repository contains the sanitized application surface and additional documentation for environment separation and security decisions.

---

**Problem → System → Evidence → Scale**
