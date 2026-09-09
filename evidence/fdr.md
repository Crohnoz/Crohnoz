# FDR — Flagship Engineering Case Study

[← Public Evidence](README.md)

> **Maturity:** `L2+ · Advanced Pilot / Production-Oriented`
>
> This case study is intentionally sanitized. It documents engineering decisions and observable product behavior without exposing private clinical data, credentials, production topology, private repositories or client-sensitive implementation details.

## Context

FDR is a healthcare operations platform designed around real clinical and administrative workflows rather than a generic CRUD model. The system connects public booking, professional availability, patient operations, clinical workflow boundaries and controlled delivery.

The product is currently the most mature system in the Crohnoz portfolio and is treated as the primary reference for production-oriented engineering practices.

## Operational problem

Healthcare scheduling is not simply a calendar problem. A valid public reservation depends on several conditions being true at the same time:

- the professional belongs to the correct organization;
- the professional is active and publicly available;
- the public profile is published;
- the professional accepts new patients;
- the requested service is active and publicly bookable;
- the professional actually offers that service;
- the selected time slot belongs to the same valid scope.

The system therefore treats booking as a domain contract, not as a front-end form.

## System design

### Public booking contract

The public booking flow enforces the relationship:

`Organization → Professional → Service Offering → Availability → Reservation`

Server-side validation prevents a manipulated request from selecting a professional, service or slot outside the allowed scope. The UI is only a projection of the same domain rules enforced by the backend.

### Reservation lifecycle

Reservations have explicit operational states rather than a single boolean confirmation flag.

`SCHEDULED → CONFIRMED → CHECKED_IN → COMPLETED`

with additional outcomes such as:

`CANCELLED · NO_SHOW`

Calendar exports reflect the real reservation state instead of presenting every newly created reservation as confirmed.

### Public and private boundaries

The platform separates public discovery and booking surfaces from authenticated operational views. Public URLs and client-side interactions are designed to avoid unnecessary exposure of patient contact data or internal clinical context.

### Professional public layer

Professional profiles and structured service offerings are modeled as explicit publication data rather than inferred from internal records. This allows public availability to have a controlled publication contract independent from private operational data.

## Reliability and regression thinking

FDR includes targeted regression coverage for operational contracts such as:

- professional × service × availability scope;
- rejection of manipulated public booking requests;
- reservation lifecycle behavior;
- calendar/ICS status mapping;
- privacy behavior on public booking surfaces;
- professional profile publication behavior;
- reproducible staging data aligned with the public booking contract.

The engineering approach favors narrow, explicit regressions around domain invariants rather than relying only on broad end-to-end happy paths.

## Delivery model

The project uses a controlled release workflow with a dedicated production-oriented branch and staged changes through focused pull requests. Staging data is generated through reproducible bootstrap logic rather than unmanaged manual fixtures.

CI workflows are treated as an operational resource: coverage, execution cost and redundant runs are managed intentionally instead of assuming unlimited automation capacity.

## What FDR demonstrates

| Capability | Evidence |
|---|---|
| **Domain modeling** | Booking requires a valid organization, professional, offering, service and slot relationship |
| **Backend integrity** | Invalid manipulated selections are rejected server-side |
| **Workflow design** | Explicit reservation lifecycle rather than generic confirmation flags |
| **Privacy thinking** | Public surfaces minimize unnecessary personal-data exposure |
| **Product architecture** | Public directory, booking and private operations use controlled boundaries |
| **Testing discipline** | Regression suites encode operational invariants |
| **Delivery engineering** | Staging, controlled releases and CI resource management are part of the system |

## Current maturity

FDR is represented as **L2+ Advanced Pilot / Production-Oriented**, not as a fully scaled L3/L4 product.

This means the system already demonstrates substantial production-oriented engineering and real operational depth, while still leaving room for additional hardening, operational evidence, scale validation and long-term production metrics before claiming full maturity.

## Why it matters

FDR demonstrates the type of work Crohnoz Labs is intended to represent: understanding a real operation, translating it into explicit domain contracts, protecting the public/private boundary, building measurable regression controls and evolving the product through controlled delivery.

It is the current flagship reference for the Crohnoz operating model:

**Problem → System → Evidence → Scale.**
