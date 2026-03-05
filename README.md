# Red Sea Port Orchestration

**$19.2M recovered in 90 days. Zero new infrastructure.**

---

## The Problem

When Suez Canal access is disrupted, vessels reroute around the Cape of
Good Hope — adding 10–14 days to Asia-Europe transit. The consequence at
Rotterdam is a dual-route convergence event: Cape-rerouted vessels and
residual Suez traffic arrive simultaneously, saturating berth capacity and
triggering cascading SLA penalties across the terminal.

During Q1 2026, this convergence drove 94 vessels into SLA risk exposure,
generated $14.54M in penalty liability, and produced $26.74M in idle costs
from vessels anchored awaiting berth.

The standard industry response is capital expenditure. APM Terminals is
currently deploying €1B to expand Rotterdam MVII from 2.7M to 4.7M TEU
by 2027. This model asks a prior question: how much value is recoverable
from the *existing* 2.7M TEU capacity through scheduling precision alone?

---

## The Finding

**$19.23M per quarter. No new berths. No new cranes.**

A Hybrid intervention — combining slow-steaming coordination with
priority berthing for high-criticality cargo — recovers:

- **$9.74M** in SLA penalty avoidance (67% reduction)
- **$17.74M** in idle cost elimination (66% reduction)
- **92.9% schedule reliability** — exceeding the Gemini Cooperation's
  90% benchmark by 2.9 percentage points

| Metric                  | Baseline (Crisis) | Hybrid (Optimized) | Δ          |
|-------------------------|-------------------|--------------------|------------|
| Vessels delayed >24h    | 94                | 28                 | −70%       |
| SLA penalties           | $14.54M           | $4.80M             | −$9.74M    |
| Idle costs              | $26.74M           | $9.00M             | −$17.74M   |
| Schedule reliability    | 83.3%             | 92.9%              | +9.6pp     |

---

## Strategic Context

The Gemini Cooperation — Maersk and Hapag-Lloyd's alliance launched
February 2025 — targets 90% schedule reliability through a hub-and-spoke
model where APM Terminals Rotterdam operates as a primary European hub.
The ME11 and MECL service strings represent the first Gemini services
returning to Suez routing in early 2026.

This model demonstrates that Rotterdam MVII can maintain Gemini-compliant
reliability through the transition window using scheduling interventions
alone — without waiting for the 2027 expansion to come online.

Scaled across APM Terminals' 60-terminal global network, the Hybrid
scenario's efficiency profile represents **$1.14B in annual operational
value** without capital expenditure.

---

## The Intervention

Three levers. No construction required.

**Slow-steaming coordination** — Cape-routed arrivals are delayed 12 hours
during weeks where projected vessel count exceeds 42 (85% of the 49-vessel
weekly threshold), smoothing the arrival curve before it becomes congestion.

**Priority berthing** — Vessels carrying pharmaceutical, perishable, or
time-critical cargo are fast-tracked regardless of arrival sequence,
protecting the highest-value cargo from delay cascades.

**Predictive yard utilization capping** — Yard utilization is held below
80% during surge weeks by pre-positioning empty containers outbound,
preventing the gridlock that occurs above the 85% threshold.

---

## Dashboard

🔗 [View Interactive Dashboard](https://wyattbarandino.github.io/red-sea-port-orchestration/)

The dashboard visualises the full Q1 2026 operational picture across four
interactive panels: arrival timeline, wait time heatmap, scenario gap
analysis, and weekly throughput. Filters for route, period, and scenario
wire directly into all charts simultaneously.

---

## Repository Structure

| Path | Contents |
|------|----------|
| `01-data/synthetic/` | Four datasets: vessel digital twin, heatmap, weekly throughput, scenario KPIs |
| `02-analysis/` | Jupyter notebook — scenario ROI calculation and crisis period analysis |
| `03-dashboard/` | Interactive HTML/Chart.js dashboard |
| `EXECUTIVE_SUMMARY.md` | Standalone brief for recruiters |

---

## Data

All vessel arrival data is synthetically generated using Python (Poisson
distribution calibrated to Rotterdam's public throughput statistics).
No proprietary Maersk or APM Terminals data was used. Full methodology
in `01-data/README.md`.

---

## Author

**Wyatt Barandino** — Strategy & Operations
[LinkedIn](https://www.linkedin.com/in/wyatt-barandino-301897382) ·
wyattrbarandino@gmail.com