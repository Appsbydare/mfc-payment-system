# AI Operating Guide — Malta Fight Co. Payment Automation

Purpose
- Single source of truth for scope, policies, and working rules I must follow every session.

Session kickoff checklist (every new conversation)
- Read `TODO_LIST.md` and reconcile current scope and priorities.
- Assume Google Sheets is the system of record (no database).
- Follow this guide for calculation, verification, exceptions, and Rule Manager.
- Do not push code. Always provide separate git commands for backend/frontend; parent repo for docs.

Data sources (Google Sheets; lowercase sheet names)
- `attendance`: GoTeamUp attendance (cleaned by importer).
- `payments`: Historical payment transactions.
- `rules`: Default/override rules (see fields below).
- `settings`: System-level settings (e.g., `default_monthly_weeks=4.3`).
- `discounts`: Discount detection rules (exact/contains, full/partial).
- `payment_calculator`: Per‑coach monthly summary rows written by backend.
- `payment_calc_detail`: Per‑attendance detail rows written by backend.

Calculation policy
- Classification: Group vs Private from attendance `ClassType` (keywords for private).
- Discounts: 100% discounts ignored entirely; partial discounts included and pro‑rated.
- Fees/Tax: Exclude fee/tax lines from revenue where configured in `settings`.
- Splits (defaults unless rules override):
  - Group: Coach 43.5%, BGM 30%, Management 8.5%, MFC 18%.
  - Private: Coach 80%, Landlord 15%, Management 0%, MFC 5%.
- Multi‑coach: Split units and effective amounts equally among listed instructors.

Verification policy (payments ↔ attendance)
- Create a per‑customer, per‑package ledger to price each attendance:
  - Packs: price ÷ sessions_per_pack applied per attendance until consumed.
  - Monthlies (2x/3x/4x/week): price ÷ (4.3 × per_week) per attendance in period.
  - Unlimited: fixed amounts as configured.
  - Exclude fee/tax lines. Apply discount rules.
- Output to `payment_calc_detail`:
  - `Verified` (true/false), `Category`, `ReasonCode`, `LinkedPaymentIds`, `RuleId`, `UnitPrice`, `EffectiveAmount`.
- Unverified categories to surface:
  1) Info mismatch/no clue (unable to uniquely match or missing/conflicting data).
  2) Prepaid unused (payment made; session not yet taken within the period).
- Report “retained revenue” = prepaid but unused for the period.

Rule Manager scope (sheets/UI)
- Extend `rules` with fields:
  - `pricing_type` (pack|monthly|unlimited|single)
  - `sessions_per_pack` (for packs)
  - `per_week` (for monthly plans)
  - `fixed_rate` (for unlimited/fixed cases)
  - `match_offering_patterns` (comma‑sep contains/regex tokens to map memberships)
  - `allow_late_payment_window_days` (matching window)
  - existing percentages and `is_fixed_rate`, `allow_discounts`, `notes` remain.
- Extend `settings` with:
  - `default_monthly_weeks` (4.3), `fees_keywords` (e.g., "fee,tax,vat").
- UI: CRUD for extended fields; validation (ranges, required combos).

Exceptions handling
- Flag and write exception reasons to detail rows.
- UI Exceptions panel lists categorized items with reasons and allows manual override.

Frontend Payment Calculator UI expectations
- Tabs: Coach Payments, BGM Payments, Management Payments, Exceptions.
- Export CSV available for coach breakdown.
- Summary shows counts, allocated revenues, splits, discounts, retained revenue (when implemented).

Workflow & change management
- After any implementation, update `TODO_LIST.md` (add tasks, mark completed).
- Provide git commands, never push:
  - Backend and frontend separately; parent repo for docs/notes.
  - Use clear, scope‑specific commit messages.

Quality bar
- Keep calculations deterministic and traceable via `payment_calc_detail`.
- Prefer explicit mapping (ledger) over heuristics.
- Avoid broad refactors; keep edits focused and documented in TODO list.


