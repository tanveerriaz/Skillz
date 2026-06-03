---
name: api-service-pattern
description: Use when building or refactoring backend API endpoints. Applies a clean layering — thin route handler, service layer for business logic, repository for data access — with input validation, consistent error handling, and dependency injection, so endpoints stay testable, secure, and easy to extend.
---

# Purpose

Keep backend code clean and testable by separating concerns. Endpoints rot when route handlers hold business logic and raw SQL. This skill applies a thin-handler / service / repository layering with validation and consistent errors, the structure that keeps APIs maintainable and safe.

# When to Use

Use when adding a new endpoint, refactoring a fat route handler, building a backend service, or standardizing how an API handles validation and errors.

# Inputs

- The endpoint's purpose and contract (inputs, outputs, auth requirements).
- The data the endpoint reads/writes and where it lives.
- The project's framework and conventions.

# Outputs

- A thin route handler that validates input, calls a service, and shapes the response.
- A service layer holding business logic, independent of the web framework.
- A repository/data-access layer isolating storage.
- Consistent validation and error handling.

# Procedure

1. **Keep the handler thin.** The route parses/validates the request, delegates to a service, and formats the response/status. No business logic or queries here.
2. **Put logic in a service.** Business rules live in framework-agnostic service functions/classes that are unit-testable without HTTP.
3. **Isolate data access.** All storage calls go through a repository layer; the service depends on its interface, not on the database directly (repository pattern + dependency injection).
4. **Validate at the boundary.** Validate and type the request before it reaches the service; reject invalid input early (see input-validation-prompt-safety).
5. **Enforce authz** in the handler or a middleware before invoking the service — never deep inside business logic only.
6. **Handle errors consistently.** Map domain errors to appropriate status codes; return a uniform error shape; never leak stack traces or secrets to clients.
7. **Type everything** and parameterize all queries.
8. **Make it testable.** Because logic is in services with injected repositories, write unit tests without spinning up the web layer.

# Quality Checklist

- [ ] Route handler is thin (validate → delegate → respond)
- [ ] Business logic lives in a framework-agnostic service
- [ ] Data access isolated behind a repository
- [ ] Dependencies injected, not hardcoded
- [ ] Input validated and typed at the boundary
- [ ] Authorization enforced before business logic
- [ ] Errors mapped to consistent statuses; no leaked internals
- [ ] Queries parameterized

# Edge Cases

- **Trivial CRUD:** a lighter version is fine — don't add layers that earn nothing — but keep validation and parameterized queries.
- **Cross-cutting concerns (logging, auth, rate limiting):** use middleware rather than repeating them per handler.
- **Transactional operations:** keep transaction boundaries in the service, not scattered across repositories.
- **External API calls:** wrap them behind their own client/adapter the service depends on.

# Safety Rules

- Never build SQL by string interpolation — always parameterize.
- Never return stack traces, secrets, or internal details in error responses.
- Never place authorization only inside deep logic where a new caller can bypass it.
- Validate every external input at the boundary, including "internal" callers.

# Examples

**Good:** `POST /orders` handler validates the body, calls `order_service.create(...)`, which applies rules and calls `order_repo.insert(...)`; a domain `OutOfStockError` maps to HTTP 409; unit tests cover the service with a fake repo.

**Bad:** A route handler that validates nothing, builds an `INSERT` via f-string from the request body, runs it inline, and returns the raw DB exception to the client.
