## Verification Processes (Current vs Latest)

### Current Process (as implemented now)
- Attendance records are loaded for the target date range.
- For each attendance, try to find a matching payment:
  - Match by customer, membership/package similarity, and date.
  - Prefer payments on or before the attendance date; break ties by highest text similarity, then smallest day difference.
- If a payment is matched:
  - Classify session type (group/private variants).
  - Look up a pricing rule for the membership and session type.
  - If rule exists: mark as Verified; use rule.unit_price for session price.
  - If rule is missing: mark as "Package Cannot be found"; still link invoice/payment amount for tracking.
- If no payment is matched: mark as Not Verified (eligible for manual handling in UI).
- Apply discounts if present to derive Discounted Session Price.
- Compute allocations: coach amount, management/MFC amounts, etc., from configured percentages.
- Persist invoice number, amounts, and verification status into the master sheet for reporting and payslips.

Notes/assumptions in current code:
- Explicit tax removal is not clearly separated as a step; payment amounts are used or rule.unit_price is taken directly.
- Manual adjusted price is not a distinct backend branch; handled via UI/overrides or discounts.

### Latest Process (from provided image)
- Attendance occurs (class or private session).
- System attempts automatic verification by matching to the closest payment made before the attendance.
  - If a suitable payment cannot be matched: prompt for manual verification and entry of a package price.
- After matching, determine pricing path:
  - Standard/full price.
  - Manually adjusted price.
  - Discounted price.
- Normalize the price paid by removing tax (and discount if applicable for the discounted path).
- Apply rule to the tax‑removed price paid to calculate the per‑session price.
- Calculate allocations using configured percentages (coach %, management %, MFC %, different for group vs private).
- Store price paid, session price, discounts, tax handling, and invoice reference for downstream reporting.




