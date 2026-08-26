# Business Insights & Recommendations
**Project:** Finance Customer Risk & Profitability Analytics
**Domain:** Banking / Consumer Finance
**Data:** 5,000 customers, `banking_features.csv` (post cleaning + feature engineering)

---

## 1. Executive Summary

This project analyzed 5,000 banking customers using SQL and Python to understand customer value, financial behavior, credit exposure, and risk. Customer-level metrics — Credit Utilization %, Loan-to-Balance Ratio, a business-rule Risk Score, and a Customer Value Score — were engineered and combined into a Value × Risk framework.

Three headline results shape the recommendations below:

- The portfolio is **value-concentrated**: only 20% of customers (1,014) are High Value, holding avg. balances of ~$8,214 vs. ~$1,734 for Low Value customers.
- Risk is **broad-based, not extreme**: 14.3% of customers are High Risk by the business-rule score, while the pre-existing Anomaly flag marks a much narrower 6% (300 customers) as statistically unusual.
- Only **7% of customers ("Grow")** sit in the ideal high-value/low-risk quadrant, while **13.2% ("Monitor")** are valuable but risky — the segment with the most to protect.

The findings support four business actions: **Grow** valuable, low-risk customers; **Monitor** valuable customers with elevated risk; **Develop** lower-value customers with healthy behavior; and **Review** customers showing weaker value and stronger risk indicators.

---

## 2. Key Business Findings

### Finding 1 — The customer base is value-concentrated
**Evidence:** Customer Value Segment split — High Value: 1,014 (20.3%), Medium Value: 3,096 (61.9%), Low Value: 890 (17.8%). Average Account Balance rises from $1,733.72 (Low) → $4,984.01 (Medium) → $8,214.34 (High).
**Business Meaning:** A fifth of the base anchors a disproportionate share of balances and loan exposure — the natural focus for retention investment.

### Finding 2 — Risk is more widespread under the business-rule score than under the raw anomaly flag
**Evidence:** Risk Level distribution: Low 36.5%, Medium 49.2%, High 14.3% (716 customers). The original Anomaly flag marks only 6.0% (300 customers) as Flagged.
**Business Meaning:** The engineered Risk Score (utilization, late payment, loan size, unresolved complaints) surfaces a broader early-warning population than the anomaly flag alone — useful for proactive management, but it should be validated, not treated as confirmed fraud/default risk.

### Finding 3 — Credit utilization is the strongest behavioral driver of the risk score
**Evidence:** In the correlation matrix, Credit Utilization % correlates with Risk Score at **r = 0.47** — the strongest relationship of any variable tested — while Account Balance and Loan Amount show near-zero correlation with Risk Score (r = 0.01 and 0.18 respectively). 28.2% of customers (1,410) carry utilization ≥ 70%.
**Business Meaning:** Credit utilization is the single best simple signal for early risk detection, well ahead of balance or loan size.

### Finding 4 — The "Monitor" segment carries the highest risk profile in the portfolio
**Evidence:** Average Credit Utilization by Value×Risk segment: Grow 32.86%, Develop 51.31%, Monitor 73.82%, Review 142.00%. Monitor customers average an Account Balance of $8,194.74, nearly identical to Grow ($8,251.19), but with more than double the utilization.
**Business Meaning:** Monitor customers are just as valuable as Grow customers financially, but their credit behavior looks materially riskier — the clearest case for active relationship management rather than passive retention.

### Finding 5 — The "Review" segment shows utilization far above 100%, an internal data-quality signal
**Evidence:** Average Credit Utilization % for the Review segment is 142.00%, well above the theoretical 100% ceiling and far higher than any other segment.
**Business Meaning:** This likely reflects records where Credit Card Balance exceeds Credit Limit in the source data. This should be flagged for data-quality investigation before being used to justify account-level action, and is noted under Limitations.

### Finding 6 — Loan approval/rejection outcomes look evenly spread across loan types
**Evidence:** Approved/Closed/Rejected counts are close across Mortgage (591/592/529), Auto (566/554/525), and Personal (553/514/576) loans, out of 1,710 Approved, 1,660 Closed, and 1,630 Rejected overall.
**Business Meaning:** No single loan product stands out as disproportionately risky or favorable by approval outcome alone; loan type does not appear to be a strong differentiator of loan status in this dataset.

### Finding 7 — High-risk customers file more complaints and leave more of them unresolved
**Evidence:** Complaint Flag rate is 39.4% for High Risk customers vs. 31.6% (Low) and 33.4% (Medium); Pending Feedback rate is 54.1% for High Risk vs. ~49–50% for the other groups.
**Business Meaning:** Service friction and unresolved complaints cluster with financial risk — resolving service issues faster for at-risk customers may reduce both dissatisfaction and risk-flag creep.

---

## 3. Customer Value Insights

- **Distribution:** Medium Value dominates the base (61.9%), with High Value (20.3%) and Low Value (17.8%) roughly split at the tails.
- **Value driver:** Customer Value Score correlates most strongly with Account Balance (r = 0.81) and moderately with Loan Amount (r = 0.48) — balance is by far the dominant input, consistent with its 50% weighting in the scoring formula.
- **Loan exposure scales with value:** Average Loan Amount rises from $15,022 (Low Value) to $25,344 (Medium) to $35,178 (High Value) — high-value customers are also the bank's largest loan counterparties, meaning value and credit exposure grow together.
- **Activity is not a value differentiator:** Average Transaction Recency is nearly flat across segments (High 185.0 days, Medium 185.5 days, Low 175.1 days), so recent transaction activity alone does not currently distinguish value tiers.
- **Reactivation opportunity:** Of the 1,014 High Value customers, 509 (50.2%) have a Transaction Recency beyond 180 days — half of the most valuable segment looks dormant on recent activity, a concrete retention target (see Recommendation 4).

## 4. Risk Insights

- **Anomaly flag vs. engineered risk score:** The two measures diverge — Anomaly flags 6.0% of customers, while the Risk Score flags 14.3% as High Risk. Flagged (anomaly) customers do show modestly higher average utilization (65.69% vs. 63.08%) and materially later payment timing (avg. +13.06 days past due vs. -0.84 days for Normal), which supports the risk score's payment-timing component but shows the anomaly flag and utilization are only loosely aligned.
- **Loan size is not a strong risk differentiator on its own:** Flagged customers actually carry a slightly *lower* average Loan Amount ($25,103.51) than Normal customers ($25,526.42) — loan amount by itself is a weak individual predictor, even though it contributes to the composite Risk Score.
- **Utilization concentration:** 28.2% of the portfolio (1,410 customers) sits at or above 70% utilization, the threshold used in the SQL medium-risk rule — a sizeable population worth monitoring even before they reach High Risk classification.
- **Service signal:** High Risk customers file complaints at a higher rate and leave more of them pending, reinforcing that risk shows up in both financial behavior and customer service friction.

## 5. Value × Risk Analysis

```
                    RISK
                 Low        High
High Value      GROW       MONITOR
Low/Medium      DEVELOP    REVIEW
 Value
```

| Segment | Share of Base | Count | Avg. Balance | Avg. Loan Amount | Avg. Credit Utilization |
|---|---|---|---|---|---|
| Grow | 7.0% | 352 | $8,251.19 | $34,294.32 | 32.86% |
| Monitor | 13.2% | 662 | $8,194.74 | $35,647.68 | 73.82% |
| Develop | 68.4% | 3,421 | $4,265.63 | $22,725.13 | 51.31% |
| Review | 11.3% | 565 | $4,213.79 | $24,941.88 | 142.00%* |

*\*Flagged for data-quality investigation — see Finding 5 and Limitations.*

### Grow — High Value + Low Risk (7.0%, 352 customers)
Retain, cross-sell, and deepen the relationship. Offer premium products and prioritized service; this is the lowest-risk group carrying the most balance and loan exposure.

### Monitor — High Value + High/Medium Risk (13.2%, 662 customers)
Protect the relationship while managing exposure. Review credit utilization and payment timing closely; this segment has Grow-level value but more than double Grow's utilization.

### Develop — Lower/Medium Value + Low/Medium Risk (68.4%, 3,421 customers)
The largest segment by far. Cross-sell and engagement campaigns to grow value without materially adding risk.

### Review — Lower/Medium Value + High Risk (11.3%, 565 customers)
Apply tighter risk controls, cap additional exposure, and investigate the utilization outliers noted in Finding 5 before broad action.

---

## 6. Key Business Recommendations

### Recommendation 1 — Build a utilization-first early-warning system
Credit Utilization % is the strongest single correlate of the Risk Score (r = 0.47), stronger than balance or loan size. A monitoring rule flagging customers crossing the 70% utilization threshold (already 28.2% of the base) — combined with payment-timing and complaint signals — would surface risk earlier than relying on the anomaly flag alone.

### Recommendation 2 — Actively manage the Monitor segment, don't just label it risky
Monitor customers (13.2%, 662 people) carry Grow-level balances and loan exposure but double the utilization. Treat this as a relationship-protection priority: proactive outreach on utilization and payment timing rather than passive risk scoring.

### Recommendation 3 — Prioritize Grow customers for retention and cross-sell
The 352 Grow customers combine the highest value with the lowest risk (32.86% avg. utilization). They are the clearest, lowest-risk targets for premium products and relationship deepening.

### Recommendation 4 — Reactivate dormant high-value customers
509 of 1,014 High Value customers (50.2%) have gone more than 180 days without a transaction. Since value is driven almost entirely by balance and loan relationship rather than recent activity, this dormant-but-valuable group is a concrete, sizeable reactivation opportunity.

### Recommendation 5 — Investigate the Review segment's utilization outliers before acting on them
Review-segment average utilization of 142% indicates likely data cases where Credit Card Balance exceeds Credit Limit. Validate these records before using utilization to drive account-level restrictions for this group, so risk controls are applied to genuine risk rather than data artifacts.

---

## 7. Segment-Specific Actions

| Segment | Primary Action | Supporting Actions |
|---|---|---|
| Grow | Retain & cross-sell | Premium product offers, priority service, relationship-manager assignment |
| Monitor | Protect & manage exposure | Utilization/payment-timing outreach, exposure review, complaint follow-up |
| Develop | Grow engagement | Cross-sell entry products, activity incentives, reactivation for dormant high-value subset |
| Review | Control & investigate | Cap new exposure, validate utilization data quality, apply tighter approval criteria |

---

## 8. Expected Business Impact

The proposed approach could help the organization:

- Improve retention of valuable, low-risk customers through prioritized service and cross-sell.
- Identify emerging financial risk earlier by tracking utilization and payment timing rather than waiting on the anomaly flag alone.
- Focus risk-management resources on the Monitor and Review segments, where value or risk (or both) are concentrated.
- Recover value from the dormant half of the High Value segment through targeted reactivation.
- Balance growth and risk management by tailoring actions to each of the four Value × Risk segments rather than treating all customers uniformly.

These are expected benefits based on the analysis; the recommendations have not yet been implemented or tested against outcomes.

---

## 9. Analytical Limitations

- **Anomaly is a pre-existing flag, not confirmed fraud or default.** It should be treated as one risk signal among several, not ground truth.
- **Correlation does not imply causation.** The relationships identified (e.g., utilization–risk score) describe association, not a causal mechanism.
- **Value and risk thresholds are analytical business rules**, not regulatory or empirically calibrated cutoffs (e.g., the 70%/7,500/4,000 thresholds used in scoring).
- **Utilization values above 100%** (seen in the Review segment) suggest data-quality issues — likely Credit Card Balance exceeding Credit Limit in source records — that should be resolved before further use.
- **The dataset is a snapshot**, combining each customer with their most recent associated transaction, loan, card, and feedback record rather than full history.
- **Real banking decisions require further validation** against historical outcomes (actual defaults, charge-offs, fraud confirmations) and applicable regulatory and compliance requirements before any of these recommendations are operationalized.

---

## 10. Final Conclusion

The Value × Risk framework built from this dataset separates a small, low-risk, high-value Grow segment (7.0%) worth retaining, a similarly valuable but riskier Monitor segment (13.2%) that needs active management, a large Develop majority (68.4%) with cross-sell potential, and a Review segment (11.3%) requiring both risk controls and data-quality investigation. Credit utilization — more than balance or loan size — is the strongest behavioral signal available for early risk detection, and roughly half of the bank's highest-value customers show reduced recent activity, representing a clear reactivation opportunity. Together, these findings turn the underlying SQL and Python analysis into a specific, segment-by-segment set of actions for the business.
