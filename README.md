# Red Sea Port Orchestration

**$19.23M recovered per quarter. Zero new infrastructure.**

A scheduling optimization case study built around the Q1 2026 dual-route convergence surge at APM Terminals Rotterdam MVII — and a direct response to the pattern repeating as US-Iran tensions push carriers back off the Suez corridor in 2026.

[**→ View Interactive Dashboard**](https://wyattbarandino.github.io/red-sea-port-orchestration/) · [**LinkedIn**](https://linkedin.com/in/wyattbarandino)

---

## What This Is

Red Sea Port Orchestration is a FinOps-style scheduling analysis applied to maritime logistics. It simulates a realistic Q1 2026 operational crisis at APM Terminals Rotterdam MVII, models four intervention scenarios against an unmanaged baseline, and produces a scheduling playbook that recovers $19.23M in quarterly value without capital expenditure.

The model tests a single question: how much of a $41.28M financial exposure is recoverable from *existing* 2.7M TEU capacity through scheduling precision alone — before a euro of the €1B expansion program is needed?

---

## Audit Results

| Metric | Value |
|---|---|
| Analysis period | Q1 2026 (Jan 1 – Mar 31) |
| Terminal | APM Terminals Maasvlakte II, Rotterdam |
| Vessel records modelled | 563 |
| Crisis window | Weeks 5–9 (Jan 26 – Mar 1, 2026) |
| Baseline financial exposure | $41.28M (SLA penalties + idle costs) |
| Value recovered — Hybrid scenario | $19.23M per quarter |
| Schedule reliability — Hybrid | 92.9% |
| Gemini Cooperation benchmark | 90.0% |
| Margin above benchmark | +2.9 percentage points |

### Four Scenario Findings

| Scenario | Reliability | Vessels Delayed | SLA Penalty | Idle Cost | Value Created |
|---|---|---|---|---|---|
| Baseline (Crisis) | 83.3% | 94 | $14.54M | $26.74M | — |
| Priority Berthing Only | 86.0% | 62 | $8.20M | $18.00M | +$7.00M |
| Slow-Steam Only | 88.0% | 55 | $9.50M | $16.00M | +$9.00M |
| **Hybrid (Optimized)** | **92.9%** | **28** | **$4.80M** | **$9.00M** | **+$19.23M** |

The Hybrid outperforms every single-lever alternative by more than 2x. Neither slow-steaming nor priority berthing alone clears the Gemini 90% threshold. The compounding effect of both is required.

### Scale Extrapolation

The model covers one terminal. The scheduling logic scales across APM Terminals' 60-terminal global network.

- 1 terminal → **$19.23M** recovered per quarter
- 60 terminals → **$1.14B** in indicative annual operational value

---

## Project Structure

```
red-sea-port-orchestration/
├── index.html                        # Interactive dashboard (GitHub Pages)
├── README.md                         # This file
├── EXECUTIVE_SUMMARY.md              # Standalone executive brief
├── LICENSE                           # MIT
│
├── 01-data/
│   ├── README.md                     # Data generation methodology
│   └── synthetic/
│       ├── rwg_digital_twin_q1.csv   # 563 vessel-level records
│       ├── heatmap_data.csv          # 90 daily aggregates
│       ├── stacked_bar_data.csv      # 28 weekly throughput rows
│       └── tableau_scenarios.csv    # 4 scenario KPI rows
│
├── 02-analysis/
│   └── red_sea_scenario_analysis.ipynb   # ROI analysis + crisis characterisation
│
├── 03_visualizations.py              # Standalone chart generator (5 figures)
│
├── fig1_crisis_window.png            # Weekly berth wait time — crisis vs. normal
├── fig2_scenario_rankings.png        # Value recovered by scenario
├── fig3_convergence_surge.png        # Weekly vessel arrivals by route
├── fig4_financial_exposure.png       # SLA + idle cost breakdown by scenario
└── fig5_financial_waterfall.png      # Baseline to optimized financial exposure
```

---

## File Guide

### `01-data/synthetic/rwg_digital_twin_q1.csv`
563 vessel-level records covering Q1 2026. Each row is one vessel arrival at Rotterdam MVII with fields for route, vessel class, size (TEU), scheduled ETA, actual arrival, wait time, yard utilization percentage, crane moves per hour, SLA penalty risk, and truck turn time.

Key design decisions:
- Vessel arrivals modelled using Poisson distribution calibrated to Rotterdam's publicly reported peak throughput of approximately 52 vessels per week
- Crisis window (Weeks 5–9) reflects the documented 66% reduction in Suez Canal traffic during the Red Sea disruption, which forced mass Cape rerouting and created the dual-route convergence event
- A non-linear efficiency cliff is applied above 80% yard utilization, consistent with published terminal congestion research — crane productivity degrades from 30 to 14.8 moves per hour at the crisis floor

### `01-data/synthetic/heatmap_data.csv`
90 daily aggregate rows. Fields: date, day name, week number, month, average wait time, max wait time, vessel count, vessels delayed, and crisis week flag (`Is_Crisis_Week = 1` for Weeks 5–9).

Used for: crisis window characterisation, SLA threshold analysis, weekly wait time visualisation.

### `01-data/synthetic/stacked_bar_data.csv`
28 weekly rows split by route (Cape / Suez). Fields: week number, route, vessel count, month, crisis flag, weekly threshold (49), and week label. Used for convergence surge visualisation showing the simultaneous arrival of both route streams above the 49-vessel capacity threshold.

### `01-data/synthetic/tableau_scenarios.csv`
4 scenario rows. Fields: scenario name, schedule reliability percentage, vessels delayed, SLA penalty ($M), idle cost ($M), and ROI ($M). The ROI figure is net of intervention costs. This is the authoritative source for all scenario comparison figures.

### `02-analysis/red_sea_scenario_analysis.ipynb`
Six-section analysis notebook covering:
- Data scope and assumption modeling (563 records, 2.7M TEU baseline, efficiency cliff calibration)
- Operational integrity audit (route distribution validation, crisis vs. non-crisis wait time contrast)
- Crisis window characterisation (Weeks 5–9 pattern, SLA threshold analysis)
- Comparative ROI analysis ($19.23M net recovery, SLA and idle cost decomposition)
- Scenario rankings (all four scenarios, value recovered vs. baseline)
- Strategic implication (Gemini Cooperation benchmark, $1.14B scale extrapolation)

Charts within the notebook use the Maersk color palette. Standalone regeneration of publication figures uses `03_visualizations.py`.

### `03_visualizations.py`
Standalone chart generator. Produces all five publication-quality figures at 200 DPI with white background and Maersk color palette applied throughout. Reads directly from the four CSV files in `01-data/synthetic/`. Outputs PNGs to the repo root.

| Figure | Chart type | Key insight |
|---|---|---|
| Fig 1 | Weekly bar — crisis highlighted | W7 peak at 14.3h average wait, SLA threshold at 16h |
| Fig 2 | Horizontal bar — scenario ROI | Hybrid at +$19.23M, 2x+ over single-lever alternatives |
| Fig 3 | Stacked bar — route split | Convergence surge: Cape + Suez simultaneously over 49-vessel threshold |
| Fig 4 | Grouped bar — cost breakdown | $26.74M idle costs dwarf $14.54M SLA penalties at baseline |
| Fig 5 | Waterfall | $41.28M baseline reduced to $13.80M, $19.23M net recovered |

**Run in Google Colab:**
```python
!git clone https://github.com/wyattbarandino/red-sea-port-orchestration.git
%cd red-sea-port-orchestration
!pip install pandas numpy matplotlib
!python 03_visualizations.py
```

### `EXECUTIVE_SUMMARY.md`
Standalone brief covering the situation (dual-route convergence crisis), the finding ($19.23M recovered), the three intervention levers, and the strategic implication for Maersk's Gemini Cooperation. Includes the full scenario comparison table and model parameters.

---

## The Three Scheduling Levers

**Slow-steaming coordination** smooths the arrival curve before it becomes congestion. Cape-routed vessels are delayed 12 hours during any week where projected arrivals exceed 42 (85% of the 49-vessel weekly threshold). This prevents the stacking effect that drove four consecutive weeks over capacity during the crisis window.

**Priority berthing** protects the highest-value cargo from delay cascades. Vessels carrying pharmaceutical, perishable, or time-critical freight are fast-tracked regardless of arrival sequence, recovering $9.74M in SLA penalty avoidance — a 67% reduction against baseline.

**Predictive yard utilization capping** prevents the gridlock that occurs above 85% utilization. By pre-positioning empty containers outbound during surge weeks, yard utilization is held below 80%, keeping crane throughput above the productivity floor that triggers cascading delays.

---

## Why This Is Relevant Now

The model was built during the first Red Sea crisis. It became a live reference when the second act began.

In December 2025, Maersk's Sebarok transited the Bab el-Mandeb for the first time in nearly two years. By February 28, 2026, in response to US and Israeli strikes on Iran, the Houthis announced resumed attacks. Maersk withdrew voyages. CMA CGM reversed three services back to the Cape of Good Hope.

As of March 2026, the corridor remains unstable. Any carrier that spent the January-February window recalibrating back toward Suez — reassigning capacity, resetting SLA commitments, adjusting terminal yard plans — is now facing the same convergence problem this model addresses. The pattern is repeating. The analytical framework here was built for exactly this frequency of disruption.

---

## Schema Reference

The simulation uses a purpose-built vessel digital twin schema. Key fields:

| Field | Description |
|---|---|
| `Vessel_ID` | MAEU-prefixed unique identifier |
| `Route` | Cape or Suez |
| `Vessel_Class` | Feeder / New Panamax / ULCV |
| `Size_TEU` | Vessel capacity in TEU |
| `Scheduled_ETA` / `Actual_Arrival` | Planned vs. actual arrival timestamps |
| `Wait_Time_Hrs` | Hours from arrival to berth assignment |
| `Yard_Util_Pct` | Terminal yard utilization at time of arrival |
| `Crane_MPH` | Crane moves per hour at time of arrival |
| `SLA_Penalty_Risk` | Estimated penalty exposure in USD |
| `Pct_Critical_Cargo` | Share of cargo with time-critical SLA |

---

## AI Transparency

Dashboard UI and code implementation were developed with AI assistance. All analytical design, scenario architecture, scheduling logic, and remediation recommendations are my own work, validated against public port operations and maritime logistics research.

---

## Synthetic Data Disclaimer

All vessel arrival data is 100% synthetically generated. No proprietary Maersk, APM Terminals, or carrier data was used at any point. The simulation is calibrated exclusively from publicly available Rotterdam port statistics, UNCTAD maritime transport reports, and MarineTraffic public AIS data. This project is entirely independent and is not affiliated with, endorsed by, sponsored by, or produced in partnership with Maersk, APM Terminals, or any carrier. No confidential or proprietary information was accessed, used, or referenced.

---

## License

MIT — see `LICENSE`

---

*Red Sea Port Orchestration · Wyatt Barandino · March 2026 · [linkedin.com/in/wyattbarandino](https://linkedin.com/in/wyattbarandino)*
