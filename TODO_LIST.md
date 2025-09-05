# MALTA FIGHT CO. - PAYMENT AUTOMATION SYSTEM
## PRIORITIZED TODO LIST

**CURRENT STATUS**: Backend structure exists, frontend pages created, but core functionality needs implementation.

---

### 🔥 **PHASE 1: CRITICAL CORE FUNCTIONALITY** (Weeks 1-2)

#### **Week 1: Data Integration & Foundation**
- [x] **1.1** Implement CSV import functionality in backend (`/api/data/import`)
- [x] **1.2** Define Google Sheets tab structure for attendance, payment data, rules, and exceptions
- [x] **1.3** Build data validation and cleaning service (BOM trim, header/value trim, duplicate handling)
- [x] **1.4** Connect frontend DataImport page to backend APIs
- [x] **1.5** Implement data preview and validation in frontend

#### **Week 2: Payment Calculation Engine**
- [x] **2.1** Implement payment calculation logic in backend (`/api/payments/calculate`)
- [x] **2.2** Build Group Classes vs Private Sessions revenue distribution
- [x] **2.3** Create discount handling system (100% and partial discounts)
- [x] **2.4** Connect PaymentCalculator frontend to backend
- [x] **2.5** Implement RuleManager backend integration
- [x] **2.6** Extend rules/settings: unit_price & sessions_per_pack; keep pricing_type/per_week/fixed_rate fields ready
- [x] **2.7** RuleManager UI: Session Price field; save `unit_price` & `sessions_per_pack`

---

### 🎯 **PHASE 2: EXCEPTION HANDLING & ADVANCED FEATURES** (Weeks 3-4)

#### **Week 3: Exception System**
- [ ] **3.0** Build rules-driven payment↔attendance verification ledger (packs/monthlies/unlimited; fees excluded; discounts handled)
- [ ] **3.1** Build manual override system for unrecognized packages
- [ ] **3.2** Implement legacy discount name recognition
- [ ] **3.3** Create exception tracking and audit logs
- [ ] **3.4** Add exception handling UI components
- [ ] **3.5** Categorize unverified: (1) info mismatch/no clue, (2) prepaid unused (session not yet taken)
- [ ] **3.6** Write verification outputs to `payment_calc_detail` (Verified, Category, ReasonCode, LinkedPaymentIds)
- [ ] **3.7** Add retained revenue metric to summary and Sheets
 - [x] **3.8** Add backend `/payments/verify` API and frontend verification table with sort/filter

#### **Week 4: Reporting & Export**
- [ ] **4.1** Implement report generation system (monthly summaries, payslips)
- [ ] **4.2** Create PDF/Excel export functionality
- [ ] **4.3** Build Reports page backend integration
- [ ] **4.4** Add report history and download management

---

### 🔧 **PHASE 3: POLISH & DEPLOYMENT** (Week 5)

#### **Week 5: Final Integration**
- [ ] **5.1** Complete Settings page functionality
- [ ] **5.2** Implement authentication and user management
- [ ] **5.3** Add error handling and validation throughout
- [ ] **5.4** Performance optimization and testing
- [ ] **5.5** Deployment preparation and documentation

---

### ✅ **COMPLETED TASKS**

#### **Project Structure & Setup**
- [x] **PROJECT_STRUCTURE** Separate frontend and backend projects created
- [x] **DEPLOYMENT_CONFIG** Vercel deployment configuration for both projects
- [x] **BACKEND_FRAMEWORK** Express.js backend with TypeScript setup
- [x] **FRONTEND_FRAMEWORK** React.js frontend with TypeScript and Tailwind CSS
- [x] **ROUTING** Basic API routes structure created
- [x] **PAGES** All main frontend pages created (Dashboard, DataImport, PaymentCalculator, Reports, RuleManager, Settings)

#### **Backend Infrastructure**
- [x] **API_ROUTES** Basic route structure for data, payments, reports, and auth
- [x] **SERVICES** Google Sheets service and Rule service created
- [x] **CONFIG** Environment configuration and middleware setup
- [x] **DEPLOYMENT** Vercel configuration for backend deployment

#### **Frontend Infrastructure**
- [x] **UI_FRAMEWORK** Tailwind CSS configuration with custom theme
- [x] **COMPONENTS** Basic component structure and layout
- [x] **PAGES** All main pages created with basic UI
- [x] **SERVICES** API service layer structure
- [x] **STORE** State management structure
- [x] **TYPES** TypeScript type definitions

#### **Rule Management System**
- [x] **RULE_SERVICE** Backend rule service with CRUD operations
- [x] **RULE_API** API endpoints for rule management
- [x] **RULE_UI** Frontend RuleManager page with UI components

#### **Data Import Improvements**
- [x] **CSV_IMPORT_FIXES** Ensure Column A populated (BOM/header/value trimming)
- [x] **DUPLICATES_LOGGING** Append duplicates to `duplicates` sheet (with `SourceSheet`)
- [x] **PREVIEW_REFRESH** Allow repeated uploads to refresh preview
- [x] **UI_CLEANUP** Remove redundant lower import summary block
- [x] **BUILD_FIX** Resolve TS6133 (unused variable) in `DataImport.tsx`

#### **Payment Calculator**
- [x] **PAYMENT_SHEETS_WRITE** Write calc summary to `payment_calculator` and details to `payment_calc_detail`
- [x] **PAYMENT_MAPPING** Map payments to sessions for per-attendance detail and per-coach gross
- [x] **RULES_DISCOUNTS_SHEETS** Use `rules`, `settings`, and `discounts` sheets for percentages and detection
- [x] **UI_TABS_BGM_MGMT** Add BGM and Management tabs with totals
- [x] **UI_EXCEPTIONS_PANEL** Add Exceptions panel with discount counts (basic)
- [x] **EXPORT_CSV** Add CSV export of coach breakdown in PaymentCalculator

---

### 📋 **IMMEDIATE NEXT STEPS** (This Week)

**Priority 1 - Verification & Rules Enhancements:**
- [ ] Implement verification ledger and write Verified/Category/Reason to `payment_calc_detail`
- [x] Extend `rules` tab to include `unit_price` and `sessions_per_pack` (sheets + backend)
- [x] Add frontend verification table (sort/filter) and `/payments/verify` endpoint
- [ ] Exceptions panel: list categorized unverified items with reasons
- [ ] Add retained revenue metric to summary

**Priority 2 - Data Import follow-ups (optional):**
- [ ] Add basic column mapping UI for unexpected headers
- [ ] Add import history view

---

### 🎯 **SUCCESS CRITERIA**
- [ ] CSV files import correctly
- [ ] Payment calculations match manual verification
- [ ] Exception handling works for discounts
- [ ] Reports generate accurately
- [ ] UI is responsive and intuitive
 - [ ] Verification ledger identifies unverified categories correctly
 - [ ] Retained revenue (unused/prepaid) reported accurately

---

### 📊 **PROGRESS TRACKING**

**Overall Progress**: 46% Complete
- **Phase 1**: 40% Complete (4/10 tasks)
- **Phase 2**: 25% Complete (2/8 tasks)  
- **Phase 3**: 0% Complete (0/5 tasks)
- **Infrastructure**: 100% Complete (All setup tasks done)

**Next Milestone**: Complete Phase 1 - Data Integration & Payment Calculation Engine

---

### 📝 **NOTES**
- Backend structure is solid and ready for implementation
- Frontend UI framework is complete and responsive
- Rule management system is partially implemented
- Need to focus on core data processing and calculation logic
- Google Sheets tab structure needs to be designed and implemented
