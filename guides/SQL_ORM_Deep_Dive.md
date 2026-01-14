# SQL & SQLAlchemy Deep Dive

One consolidated reference for relational design, advanced querying, and SQLAlchemy 2.0 patterns. Combines SQL DDL/Advanced Queries and SQLAlchemy CRUD/Relationships/Advanced Patterns content.

## Table of Contents
1. Relational Foundations (DDL)
2. Querying Patterns (SQL)
3. SQLAlchemy 2.0 Model Design
4. CRUD Patterns
5. Relationships & Loading Strategies
6. Advanced ORM Patterns
7. Testing Database Code
8. Performance & Troubleshooting

---

## 1) Relational Foundations (DDL)
- **Core objects:** databases, schemas, tables, views, indexes, sequences.
- **Column design:** types (INT, TEXT, UUID, JSONB), nullability, defaults, check constraints.
- **Keys:** primary keys (single or surrogate), unique constraints, foreign keys with `ON DELETE/UPDATE` behavior.
- **Migrations:** forward-only scripts; avoid destructive changes without backups; add columns with defaults carefully; manage enum changes explicitly.

## 2) Querying Patterns (SQL)
- **Filtering:** `WHERE`, `IN`, `BETWEEN`, `ILIKE`, null-safe comparisons (`IS NULL`).
- **Aggregation:** `GROUP BY`, `HAVING`, window functions (`ROW_NUMBER`, `LAG`, `SUM OVER`).
- **Joins:** INNER/LEFT/RIGHT/FULL; prefer explicit join conditions; ensure selective predicates to avoid blowups.
- **Pagination:** `LIMIT/OFFSET` for basics; keyset pagination for large data.
- **Common patterns:** `EXISTS` vs `IN`; `CASE WHEN`; CTEs for readability; materialized views for heavy joins.

## 3) SQLAlchemy 2.0 Model Design
- **Typed models:** `Mapped[T]` + `mapped_column`; dataclasses optional; `__tablename__` explicit.
- **Defaults:** server_default vs python default; timestamps via `func.now()`; `Enum` with `validate_strings=True`.
- **Metadata:** naming conventions for constraints to keep Alembic diffs stable.
- **Base patterns:** declarative base in `models/__init__.py`; import models in `models/__all__.py` to register for migrations.

## 4) CRUD Patterns
- **Create:** instantiate model, add to session, flush to get PK, commit in service layer.
- **Read:** use `select(Model).where(...)`; prefer `scalars()`; handle `NoResultFound`/`MultipleResultsFound`.
- **Update:** load row, mutate fields, commit; for bulk, use `update()` with care (skips ORM events).
- **Delete:** soft-delete column for business-critical data; otherwise `session.delete(obj)` with cascade awareness.
- **Transactions:** context managers or explicit `session.begin()`; avoid nested commits in request handlers.

## 5) Relationships & Loading Strategies
- **Relationships:** `relationship` with `back_populates`; specify `cascade` explicitly; `secondary` tables for many-to-many.
- **Loading:** default to `selectinload` to avoid N+1; `joinedload` for small/1-1; `lazy="raise"` to catch accidental lazy loads in APIs.
- **Cardinality patterns:** `one-to-many` via FK + backref; `one-to-one` via unique FK; `many-to-many` via association table or association object with extra columns.
- **Ordering:** set `order_by` on relationships when deterministic ordering matters.

## 6) Advanced ORM Patterns
- **Domain services:** keep business logic out of models; use services for workflows.
- **Repositories (optional):** wrap session queries when you need abstraction; otherwise, pass session explicitly.
- **Soft deletes:** `deleted_at` filters via query property or helper functions; ensure unique constraints account for soft deletes.
- **Versioning/audit:** history tables or event listeners; include actor/context columns.
- **Bulk operations:** `session.execute(insert(Model).values(...))` for large imports; be aware of bypassed ORM events.
- **Schema evolution:** feature flags around new columns; backfill jobs for non-nullable additions.

## 7) Testing Database Code
- **Fixtures:** session fixture with rollback per test; use nested transactions or `sessionmaker(bind=engine, expire_on_commit=False)`.
- **Factories:** build test data with factory functions; avoid random data that hides determinism.
- **Isolation:** mark tests that hit DB; avoid sharing sessions across tests; seed reference data per test module.
- **Assertions:** verify both data and constraints (unique violations, FK errors); assert eager loading to avoid lazy access in APIs.
- **Contract with API tests:** reuse the same factories in API layer tests for realistic payloads.

## 8) Performance & Troubleshooting
- **Explain plans:** run `EXPLAIN ANALYZE` on heavy queries; add indexes for filter/join columns; composite indexes ordered by selectivity.
- **Connection management:** pool sizing (gunicorn workers × expected concurrency); timeouts for long-running queries.
- **N+1 detection:** enable `lazy="raise"` in tests; log SQL to spot chatter; use `selectinload`/`joinedload`.
- **Locks & contention:** keep transactions short; avoid long-running migrations during peak.
- **Monitoring:** metrics for query latency, errors, pool saturation; logs with query params stripped of PII.
