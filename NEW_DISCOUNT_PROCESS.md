# New Discount Process - Implementation Plan

## Current Issue
- Only one discount is applying for the whole data
- This is incorrect as different invoices should have different discounts

## New Discount Process Requirements

### 1. **Timing**: After Main Payment Verification
- Apply discounts **AFTER** the main payment verification is complete
- Do NOT interfere with the current verification process

### 2. **Discount Detection**: Invoice Number + Memo Matching
- Check each verified record's **Invoice Number**
- Look up that invoice in the **Payment Data** file
- Check the **Memo column** for discount names (EXACT matching)
- If discount name found in Memo → Apply discount to that specific record

### 3. **Discount Application Process**
```
For each verified record:
1. Get Invoice Number from verified data
2. Find matching payment record by Invoice Number
3. Check Memo column for discount name (exact match)
4. If discount found:
   - Get discount name → Update "Discount" column
   - Get discount % from discount database → Update "Discount %" column
   - Calculate: Discounted Session Price = Session Price × (1 - discount%)
   - Recalculate all amounts based on Discounted Session Price
```

### 4. **Data Updates Required**
- **Discount Column**: Discount name from Memo
- **Discount % Column**: Percentage from discount database
- **Discounted Session Price**: Session Price × (1 - discount%)
- **Coach Amount**: Recalculated with discounted price
- **BGM Amount**: Recalculated with discounted price
- **Management Amount**: Recalculated with discounted price
- **MFC Amount**: Recalculated with discounted price

### 5. **Preserve Original Values**
- **Package Price**: Keep original (from rules)
- **Session Price**: Keep original (from rules)
- **Amount**: Keep original (from payment)

### 6. **Example Calculation**
```
Original Session Price: $100
Discount Found in Memo: "Private Session 10-Pack Discount"
Discount % from Database: 20%
Discount Factor: 1 - (20/100) = 0.8

Discounted Session Price: $100 × 0.8 = $80

Recalculated Amounts:
- Coach Amount (30%): $80 × 0.30 = $24
- BGM Amount (25%): $80 × 0.25 = $20
- Management Amount (5%): $80 × 0.05 = $4
- MFC Amount (40%): $80 × 0.40 = $32
```

### 7. **Implementation Strategy**
- **Option A**: Remove existing discount process entirely and implement new one
- **Option B**: Modify existing discount process to match new requirements
- **Recommendation**: Option B (modify existing) to avoid disrupting current verification

### 8. **Key Benefits**
- ✅ Per-invoice discount application (not global)
- ✅ Exact memo matching for accuracy
- ✅ Preserves original verification process
- ✅ Recalculates all amounts correctly
- ✅ Maintains data integrity

### 9. **Files to Modify**
- `backend/src/services/attendanceVerificationService.ts`
  - Modify `applyDiscountsByInvoice()` method
  - Update discount matching logic
  - Ensure per-invoice processing

### 10. **Testing Requirements**
- Test with multiple invoices having different discounts
- Verify exact memo matching works
- Confirm amounts are recalculated correctly
- Ensure original values are preserved
