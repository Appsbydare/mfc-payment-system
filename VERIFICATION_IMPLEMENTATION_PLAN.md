## Plan: Update Verification to Use Invoice/Manual Prices (Latest Process)

### Goals (what changes)
- Always base session pricing on the invoiced payment amount (net of tax), not on rule/package price.
- If no matching payment is found, keep the record Unverified and allow a manual discounted session price.
- Payslips and all downstream calculations must use only Invoice‑verified prices or Manually‑verified prices.

### Affected areas (high level)
- Backend services: verification, discounts, master sheet sync, payslips.
- Frontend: verification UI in `PaymentCalculator` (manual price entry for unverified rows).
- Data model: additional columns in the master sheet (`payment_calc_detail`).

### Data model (master sheet) additions
- `invoiceAmount` – raw amount from matched invoice/payment.
- `invoiceNetAmount` – amount after removing tax.
- `invoiceDiscountedAmount` – net amount after applying discount (if any).
- `invoiceVerifiedSessionPrice` – per‑session price derived from the invoice (used for payouts).
- `manualSessionPrice` – per‑session price entered by a user when no invoice match.
- `priceSource` – `invoice` | `manual` | `none` (controls what payslips use).
- `verificationStatus` – `Verified` (invoice), `Manual Verified`, `Not Verified`.
- Keep existing allocation fields (coach/management/MFC amounts).

### Back‑end changes
1) Verification pipeline (attendance → payment)
   - Keep current matching (customer, similarity, and date priority: on/before, closest days).
   - On match:
     - Base = payment amount → remove tax → apply discount (existing `discountService`).
     - Derive per‑session price using the rule structure only to apportion the invoice (e.g., sessions in package), not to pull a fixed unit price.
     - Compute allocations from this per‑session price.
     - Set: `verificationStatus=Verified`, `priceSource=invoice`, fill `invoice*` fields and `invoiceVerifiedSessionPrice`.
   - On no match:
     - Set: `verificationStatus=Not Verified`, `priceSource=none`.
     - Do NOT fall back to rule/unit price; leave session price empty until manual entry.

2) Manual verification endpoint
   - New route: `POST /verification/manual` with `{ uniqueKey, manualSessionPrice }`.
   - Actions:
     - Recompute allocations from `manualSessionPrice`.
     - Set: `verificationStatus=Manual Verified`, `priceSource=manual`, store `manualSessionPrice`.
     - Persist to master sheet.

3) Calculation helpers
   - `removeTax(amount)` with configurable tax rate (env/setting).
   - `deriveSessionPriceFromInvoice(invoiceNetAmount, rule)` to split per session (uses rule’s structure/session count only).
   - Reuse existing allocation logic to compute coach/management/MFC amounts from the chosen session price.

4) Payslip generation (`backend/src/services/payslipService.ts`)
   - Filter rows where `verificationStatus` in [`Verified`, `Manual Verified`].
   - `netPricePerSession = manualSessionPrice || invoiceVerifiedSessionPrice`.
   - Ensure coach pay and totals derive from the stored allocation fields (already computed in verification).

### Front‑end changes (PaymentCalculator)
- Add Unverified list with inline field to enter `manualSessionPrice` and Save → calls `/verification/manual`.
- Visual indicators for `priceSource` and `verificationStatus`.
- Refresh master after save; keep existing toasts.

### Migration
- Add columns to `payment_calc_detail` (once).
- Optional backfill (safe approach):
  - For rows with existing invoice links where a discount can be inferred, populate `invoiceAmount/net/discounted` and `invoiceVerifiedSessionPrice` using current payments and rules.
  - Leave any rows without payment match as `Not Verified` (no fallback to rule price).

### Config & safeguards
- `TAX_RATE` configuration (env).
- Feature flag (if needed) to switch payslip source to invoice/manual only.
- Input validation for manual prices (non‑negative, sensible bounds).

### Test scope
- Match found → invoice‑based session price equals expected apportioning; allocations correct.
- No match → remains `Not Verified` until manual; after manual, allocations correct.
- Payslip uses only invoice/manual and excludes unverified rows.

### Files/modules to update (reference)
- `backend/dist/services/attendanceVerificationService.js` (verification flow & price derivation).
- `backend/dist/routes/attendanceVerification.js` (add manual verify route).
- `backend/src/services/payslipService.ts` (selection logic for price source).
- `frontend/src/pages/PaymentCalculator.tsx` (manual entry UI for unverified rows).

Outcome: Session prices for payouts are driven by invoices (or manual overrides), never by raw package/unit prices from rules. Unmatched attendances stay unverified until a human provides a price. Payslips reflect only verified prices.


