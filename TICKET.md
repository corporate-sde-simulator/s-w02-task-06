# FINSERV-4119: Refactor email notification template system

**Status:** In Progress · **Priority:** Medium
**Sprint:** Sprint 24 · **Story Points:** 5
**Reporter:** Priya Menon (Notifications Lead) · **Assignee:** You (Intern)
**Due:** End of sprint (Friday)
**Labels:** `backend`, `python`, `notifications`, `refactor`
**Task Type:** Code Maintenance

---

## Description

The email template renderer **works correctly** — it substitutes placeholders and sends emails. The code duplicates placeholder resolution logic, uses string concatenation for HTML, and has no template caching.

## Acceptance Criteria

- [ ] All `# TODO (code review):` items addressed
- [ ] Placeholder resolution logic deduplicated
- [ ] Template caching added for frequently used templates
- [ ] HTML built with proper escaping, not string concatenation
- [ ] All existing tests still pass
