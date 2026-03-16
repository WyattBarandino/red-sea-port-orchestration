# Data — Synthetic Generation Methodology

All datasets in this project are synthetically generated using Python.
No proprietary Maersk or APM Terminals data was used at any point.
This is a portfolio case study modelling a hypothetical Q1 2026 scenario.

## Generation Approach

Vessel arrivals are modelled using a **Poisson distribution** calibrated
to Rotterdam's publicly reported throughput of approximately 2.7M TEU
annually, equating to a peak of ~52 vessels per week across both routes.

The February crisis window (Weeks 5–9, covering Jan 26 – Mar 1 2026)
reflects the documented 66% reduction in Suez Canal traffic during the
Red Sea disruption period, which forced mass rerouting to the Cape of
Good Hope and added 10–14 days to Asia-Europe transit times.

AIS signal integrity is acknowledged as a real-world constraint not
fully captured in synthetic data. In the actual Red Sea corridor,
vessels routinely disable AIS transponders for security, creating
tracking gaps. A production version of this model would integrate
secondary positioning sources to handle dark-zone periods.

## Dataset Reference

| File | Records | Description |
|------|---------|-------------|
| `rwg_digital_twin_q1.csv` | 563 | Vessel-level simulation — arrivals, wait times, yard utilization, SLA exposure |
| `heatmap_data.csv` | 90 | Daily aggregates — avg/max wait time, vessel count, crisis flag |
| `stacked_bar_data.csv` | 28 | Weekly throughput by route with capacity threshold |
| `tableau_scenarios.csv` | 4 | Scenario-level KPI summary for gap analysis |

## Crisis Window Definition

`Is_Crisis_Week = 1` is applied to Weeks 5–9, defined as the period
when Cape-rerouted vessels (displaced by the Suez closure) begin
arriving at Rotterdam simultaneously with residual Suez-routed traffic.
This dual-route convergence is the core operational event the model
addresses.

## Public Sources Used for Calibration

- Port of Rotterdam Authority annual throughput statistics
- APM Terminals public capacity disclosures
- MarineTraffic historical AIS vessel tracking data (public feeds)
- UNCTAD maritime transport disruption reports, 2024
