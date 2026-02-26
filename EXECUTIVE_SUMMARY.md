# Executive Summary
## Red Sea Port Orchestration — APM Terminals Rotterdam MVII

**Wyatt Barandino** · Strategy & Operations Analyst  
[LinkedIn](https://www.linkedin.com/in/wyatt-barandino-301897382) · wyattrbarandino@gmail.com

---

## Situation

The Red Sea disruption — driven by Houthi militant attacks beginning late 2023 —
forced a 66% reduction in Suez Canal traffic across the Asia-Europe corridor.
Carriers mass-rerouted around the Cape of Good Hope, adding 10–14 days to
transit times and fundamentally changing the arrival pattern at European hub
terminals.

At APM Terminals Maasvlakte II (Rotterdam), this created a measurable
operational crisis: Cape-rerouted vessels and residual Suez-routed traffic
began arriving simultaneously, producing a dual-route convergence surge that
saturated berth capacity across Weeks 5–9 of Q1 2026. Four consecutive weeks
exceeded the 49-vessel weekly threshold, with terminal yard utilization peaking
at 105.4% — above physical capacity. Crane productivity degraded from 30 to
14.8 moves per hour at the crisis floor. Ninety-four vessels entered SLA
penalty risk. Total financial exposure reached **$41.28M** in combined penalty
and idle cost liability.

The industry default response to capacity pressure is capital expenditure.
APM Terminals is currently deploying €1B to expand Rotterdam MVII from 2.7M
to 4.7M TEU by 2027. This analysis asks a prior question: how much of that
$41.28M exposure is recoverable from the *existing* 2.7M TEU capacity through
scheduling precision alone — before a single euro of expansion spend is needed?

---

## Finding

**$19.23M recovered per quarter. No new infrastructure.**

A Hybrid intervention — combining slow-steaming coordination with priority
berthing for high-criticality cargo — recovers the majority of crisis-period
financial exposure without CapEx. The model tested four scenarios against the
unmanaged Crisis Baseline:

| Scenario | Reliability | Vessels Delayed | SLA Penalty | Idle Cost | Value Created |
|----------|-------------|-----------------|-------------|-----------|---------------|
| Baseline (Crisis) | 83.3% | 94 | $14.54M | $26.74M | — |
| Priority Berthing Only | 86.0% | 62 | $8.20M | $18.00M | +$7.00M |
| Slow-Steam Only | 88.0% | 55 | $9.50M | $16.00M | +$9.00M |
| **Hybrid (Optimized)** | **92.9%** | **28** | **$4.80M** | **$9.00M** | **+$19.23M** |

The Hybrid scenario outperforms every single-lever alternative by a factor
of 2x or more. Neither slow-steaming nor priority berthing alone is sufficient —
the compounding effect of both is required to clear the performance threshold
that matters strategically.

At 92.9% schedule reliability, the Hybrid exceeds the **Gemini Cooperation's
90% benchmark** by 2.9 percentage points — positioning Rotterdam MVII as a
dependable anchor in the Maersk-Hapag-Lloyd hub-and-spoke network during
the stepwise return to Suez routing in early 2026.

---

## The Intervention

Three scheduling levers. No construction required.

**Slow-steaming coordination** smooths the arrival curve before it becomes
congestion. Cape-routed vessels are delayed 12 hours during any week where
projected arrivals exceed 42 (85% of the 49-vessel weekly threshold). This
prevents the stacking effect that drove four consecutive weeks over capacity
during the crisis window.

**Priority berthing** protects the highest-value cargo from delay cascades.
Vessels carrying pharmaceutical, perishable, or time-critical freight are
fast-tracked regardless of arrival sequence. This recovers $9.74M in SLA
penalty avoidance — a 67% reduction against baseline exposure.

**Predictive yard utilization capping** prevents the gridlock that occurs
above 85% utilization. By pre-positioning empty containers outbound during
surge weeks, yard utilization is held below 80%, keeping crane throughput
above the productivity floor that triggers cascading delays.

---

## Strategic Implication

This model directly supports two of Maersk's most consequential near-term
operational priorities.

**Gemini Cooperation reliability.** The Gemini Cooperation (Maersk and
Hapag-Lloyd, launched February 2025) set a published 90% schedule reliability
target as its primary competitive differentiator. Rotterdam MVII is a primary
European hub in that network. The Hybrid scenario delivers 92.9% reliability —
demonstrating that hub-level performance targets are achievable through
scheduling discipline during the transition window, without waiting for the
2027 physical expansion.

**Pre-expansion value extraction.** With €1B committed to Rotterdam MVII
expansion, the 18–36 month construction window represents a period where
physical capacity cannot be increased. This model provides the operational
playbook for extracting maximum value from existing infrastructure during
that window — $19.23M per quarter at a single terminal.

Scaled across APM Terminals' 60-terminal global network, systematic
replication of the Hybrid scheduling discipline represents an indicative
**$1.14B in annual operational value** — before the Rotterdam expansion
adds a single TEU of new capacity.

---

## Model Parameters

| Parameter | Value |
|-----------|-------|
| Terminal | APM Terminals Maasvlakte II, Rotterdam |
| Analysis period | Q1 2026 (Jan 1 – Mar 31) |
| Vessel records modelled | 563 |
| Crisis window | Weeks 5–9 (Jan 26 – Mar 1, 2026) |
| Benchmark | Gemini Cooperation 90% schedule reliability |
| Data source | Synthetic (Poisson-distributed, calibrated to public statistics) |

All vessel arrival data is synthetically generated using Python. No proprietary
Maersk or APM Terminals data was used at any point. Generation methodology and
dataset schemas are documented in `01-data/README.md`.

---

*Portfolio case study.  
All data is synthetic. No proprietary information was used.*
