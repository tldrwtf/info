# Flask API Build, Secure, Ship Handbook

Single, end-to-end guide for building production-grade Flask APIs: architecture, auth, AI-readiness, testing, and delivery. Consolidates prior Flask, Library-Api, auth, testing, CI/CD, and Docker guides.

## Table of Contents
1. Modern Flask Architecture
2. Data Layer (see SQL/ORM Deep Dive)
3. Authentication & Token Management
4. AI-Ready APIs
5. Advanced Patterns & Observability
6. Testing & Quality Gates
7. Delivery, Ops, and Production Readiness
8. Reference Patterns & Checklists

---

## 1) Modern Flask Architecture
- **App factory + blueprints:** Use `create_app(config_name)` to defer setup; register blueprints per domain (users, books, admin) with URL prefixes for clean routing.
- **Extension initialization:** Centralize `db`, `migrate`, `ma`, `jwt`, `limiter`, `cache` in `extensions.py`; init in factory to keep globals testable.
- **Configuration management:** Base config + env-specific overrides via env vars; never bake secrets. Use `instance/` or `.env` only for local.
- **Request lifecycle hooks:** `before_request` for auth/metrics guards; `teardown_appcontext` for cleanup; `after_request` for headers and caching hints.
- **Validation & serialization:** Marshmallow schemas for request/response contracts; prefer schema `load` for input validation and `dump` for outputs.
- **Pagination pattern:** Standardize query params `page`, `per_page`, `sort`; return `{items, page, per_page, total}`.
- **Common HTTP status codes:** 200/201/204 for success; 400/401/403/404/409/422/429 for errors; always include `code`, `message`, `details`.

## 2) Data Layer (see SQL/ORM Deep Dive)
- Keep models lean (attributes/relationships only) and move business rules into services.
- Use SQLAlchemy 2.0 style with typed models and `Mapped[]`.
- Relationship defaults: lazy=`selectin`, back_populates everywhere, cascades explicit (`save-update, merge`).
- Transactions: service layer coordinates commits; avoid committing inside views to keep tests simple.
- For details on CRUD, relationships, advanced patterns, and testing, jump to `SQL_ORM_Deep_Dive.md`.

## 3) Authentication & Token Management
- **API keys & basic:** For internal or legacy integrations; restrict scope; rotate often.
- **Bearer tokens:** Standard header `Authorization: Bearer <token>`.
- **OAuth2 flows:** Client Credentials for service-to-service; Auth Code + PKCE for user delegation; handle token acquisition, refresh, and storage securely (encrypt at rest, short-lived access tokens).
- **JWTs:** Issue short-lived access tokens; include `sub`, `exp`, `iat`, `scope`; validate audience/issuer; blocklist on logout if required; rotate signing keys.
- **Session auth:** For web apps; HttpOnly, Secure cookies; CSRF protection on state-changing requests.
- **Error handling:** Return 401 for missing/expired, 403 for scope/role violations; include machine-readable error codes.
- **Best practices:** Principle of least privilege; scope-based authorization; rate-limit auth endpoints; log failures without leaking secrets.

## 4) AI-Ready APIs
- **OpenAPI as contract:** Keep `/openapi.json` accurate; regenerate on changes; serve Swagger UI for humans and raw JSON for agents.
- **Descriptive docs:** Docstrings explaining params, validation rules, enums, and error shapes; include example payloads.
- **Atomic endpoints:** Prefer single-purpose routes with clear inputs/outputs so agents can compose workflows.
- **Error clarity:** Deterministic error formats with hints for correction (e.g., required fields, allowed values).
- **Discoverability:** Provide index endpoints and link relations in responses where useful.
- **Testing AI readiness:** Lint OpenAPI; run contract tests to ensure examples match reality.

## 5) Advanced Patterns & Observability
- **Rate limiting:** `Flask-Limiter` with sensible defaults per identity + IP; exempt health checks; return `Retry-After`.
- **Caching:** `Flask-Caching` with key functions per resource; cache GETs; bust on mutations; set TTLs based on data volatility.
- **Proxy & edge:** Use reverse proxy (NGINX/Cloud) for TLS, gzip/br, request size limits; forward `X-Request-ID`.
- **Decorator stacking order:** `@bp.route` -> auth/permissions -> validation -> caching -> business logic -> response schema.
- **Routing patterns:** Prefer nouns and sub-resources (`/users/{id}/loans`); support bulk operations carefully; use idempotent PUT/PATCH semantics.
- **Observability:** Structured logs (json) with correlation IDs; metrics for request counts/latency/errors; tracing where available.

## 6) Testing & Quality Gates
- **Unit tests:** Schema validation, service functions, auth helpers with pytest; use factories/fixtures for data.
- **Integration/API tests:** `FlaskClient`/`pytest-flask` or `httpx` against app factory; seed data via fixtures; assert status codes + payload shape.
- **Contract tests:** Validate responses against OpenAPI examples; ensure auth headers required where expected.
- **Performance & limits:** Test rate-limit responses, pagination correctness, and cache headers.
- **CI checks:** Lint, type check, tests, coverage thresholds; fail on missing migrations vs models drift.

## 7) Delivery, Ops, and Production Readiness
- **Containerization:** Multi-stage Dockerfile (builder -> slim runtime); run as non-root; pin Python base image; install only needed system deps.
- **Configuration:** 12-factor; secrets via env/secret store; separate config for dev/stage/prod; feature flags for risky rollouts.
- **Database migrations:** Alembic migrations in CI + gated on review; backup before applying in prod; promote with zero-downtime strategy.
- **CI/CD pipeline:** Steps: lint -> tests -> build image -> scan -> push -> deploy; block deploy on failing checks.
- **Runtime hardening:** Gunicorn/uwsgi with timeouts; health checks (`/healthz`, `/readiness`); request body limits; CORS configured explicitly.
- **Resilience:** Retry external calls with backoff; circuit breakers where heavy; timeouts everywhere; idempotency keys for mutation endpoints.

## 8) Reference Patterns & Checklists
- **Project structure (template):**
  ```
  app/
    __init__.py        # app factory
    extensions.py      # db, cache, limiter, jwt, ma
    config.py          # BaseConfig, DevConfig, ProdConfig
    blueprints/
      users/
      auth/
      catalog/
    schemas/
    services/
    models/
    tests/
  ```
- **Best practices checklist:**
  - App factory used; extensions init centralized.
  - OpenAPI served and current; examples verified.
  - Auth flows documented; tokens scoped; secrets rotated.
  - Pagination, rate limits, caching standardized.
  - Tests cover schemas, services, routes; CI blocking.
  - Docker image minimal; configs via env; health/readiness live.
