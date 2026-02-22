# PR Review - Email notification template renderer (by Vikram Singh)

## Reviewer: Ravi Iyer
---

**Overall:** Good foundation but critical bugs need fixing before merge.

### `templateRenderer.py`

> **Bug #1:** Placeholder replacement uses single pass so nested placeholders fail
> This is the higher priority fix. Check the logic carefully and compare against the design doc.

### `placeholderResolver.py`

> **Bug #2:** HTML special characters in user data are not escaped creating XSS vulnerability in email bodies
> This is more subtle but will cause issues in production. Make sure to add a test case for this.

---

**Vikram Singh**
> Acknowledged. I have documented the issues for whoever picks this up.
