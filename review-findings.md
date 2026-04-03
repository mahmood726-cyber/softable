# SoFTable Code Review Findings

**Date:** 2026-04-03
**Reviewer:** Code Audit (Claude)
**File:** sof-table.html (1,479 lines)

## P0 (Critical — must fix before ship)

### P0-1: CSV export lacks formula injection protection
**Location:** `generateCsv()` function (~line 1301-1328)
**Issue:** CSV cells are quoted for commas/newlines but NOT sanitized for formula injection.
User-entered data (outcome names, rationale text, plain language summaries) can start with
`=`, `+`, `@`, tab, or carriage return, which spreadsheet applications (Excel, Google Sheets)
interpret as formulas. An attacker or careless user could inject `=CMD(...)` payloads.
**Fix:** Add `csvSafe()` function that prepends `'` to cells starting with `=+@\t\r`
(NOT `-`, which would corrupt negative medical values like "-0.5 mmHg").

## P1 (Important — fix before submission)

### P1-1: OR-to-absolute conversion assumes p0 < 1
**Location:** `calcAbsoluteEffect()` (~line 532-546)
**Issue:** When `controlRisk = 1000` (i.e., p0 = 1.0), `odds0 = p0/(1-p0)` divides by zero,
producing `Infinity`. The result propagates to the SoF table as `NaN per 1000`.
**Recommendation:** Guard `p0 >= 1.0` with early return or clamp to 0.999.

### P1-2: HR treated as approximate RR for absolute effects
**Location:** `calcAbsoluteEffect()` (~line 548-555)
**Issue:** Comment says "Approximate using HR ~ RR for low event rates" but no warning
is shown to users. For high event rates (>20%), this approximation diverges substantially.
**Recommendation:** Add a footnote or warning when `controlRisk > 200` per 1000 with HR.

## P2 (Minor — nice to have)

### P2-1: No Content-Security-Policy meta tag
**Issue:** Other tools in the portfolio include CSP. SoFTable has one (line 5) -- confirmed present.
Not an issue.

### P2-2: Blob URLs properly revoked
**Location:** `downloadBlob()` (~line 1457-1467)
**Issue:** Correctly calls `URL.revokeObjectURL(url)`. No issue.

### P2-3: Modal Escape listener properly cleaned up
**Location:** `closeAbout()` (~line 787-794)
**Issue:** Correctly removes keydown listener. No issue.

### P2-4: GRADE score not validated on load from localStorage
**Location:** `loadState()` (~line 401-417)
**Issue:** Malicious or corrupted localStorage data could inject unexpected field values.
The code does ensure `grade` defaults exist, but individual grade domain values are not
validated against allowed values (`not-serious`, `serious`, `very-serious`).
**Recommendation:** Add validation on load.

## Summary

| Severity | Count | Fixed |
|----------|-------|-------|
| P0       | 1     | Yes   |
| P1       | 2     | No    |
| P2       | 1     | No    |
| **Total**| **4** |       |
