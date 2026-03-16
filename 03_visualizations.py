"""
Red Sea Port Orchestration — Publication Charts
APM Terminals Rotterdam MVII | Q1 2026 | Synthetic Data

Generates five publication-quality figures for the executive report,
README, and LinkedIn article. White background, 200 DPI, print-safe.

Maersk color palette applied throughout:
  Maersk Blue    #002147   (primary dark)
  Ocean Blue     #42B0D5   (primary accent)
  Light Blue     #6dcee8   (secondary accent)
  Signal Red     #D62828   (crisis / alert)
  Maersk Gold    #FFD028   (threshold / highlight)
  Mist Grey      #878787   (labels / secondary text)
  Off-White      #EDEDED   (text on dark)
  Deep Navy      #00233D   (plot backgrounds)

Output files (repo root):
  fig1_crisis_window.png        Weekly berth wait time — crisis vs. normal
  fig2_scenario_rankings.png    Value recovered by scenario (horizontal bar)
  fig3_convergence_surge.png    Weekly vessel arrivals by route (stacked bar)
  fig4_financial_exposure.png   SLA + idle cost breakdown by scenario
  fig5_financial_waterfall.png  Baseline exposure to optimized state (waterfall)

Run:
  python 03_visualizations.py
Requires rwg_digital_twin_q1.csv, heatmap_data.csv,
stacked_bar_data.csv, tableau_scenarios.csv in ../01-data/synthetic/
or edit DATA_DIR below.
"""

import os
import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.ticker as mticker

matplotlib.use('Agg')

# ---------------------------------------------------------------------------
# CONFIG
# ---------------------------------------------------------------------------

DATA_DIR   = os.path.join(os.path.dirname(__file__), '01-data', 'synthetic')
OUTPUT_DIR = os.path.dirname(__file__)

# For running standalone with uploaded CSVs in current directory
_LOCAL = os.path.join(os.path.dirname(__file__))

def _load(filename):
    for d in [DATA_DIR, _LOCAL]:
        p = os.path.join(d, filename)
        if os.path.exists(p):
            return pd.read_csv(p)
    raise FileNotFoundError(f'{filename} not found in {DATA_DIR} or {_LOCAL}')

# ---------------------------------------------------------------------------
# MAERSK PALETTE
# ---------------------------------------------------------------------------

MAERSK_BLUE   = '#002147'
OCEAN_BLUE    = '#42B0D5'
LIGHT_BLUE    = '#6dcee8'
SIGNAL_RED    = '#D62828'
MAERSK_GOLD   = '#FFD028'
MIST_GREY     = '#878787'
OFF_WHITE     = '#EDEDED'
DEEP_NAVY     = '#00233D'
WHITE         = '#FFFFFF'

# ---------------------------------------------------------------------------
# SHARED STYLE — white background, Maersk typography
# ---------------------------------------------------------------------------

def apply_base_style():
    plt.rcParams.update({
        'figure.facecolor':      WHITE,
        'axes.facecolor':        WHITE,
        'text.color':            MAERSK_BLUE,
        'axes.labelcolor':       MIST_GREY,
        'xtick.color':           MIST_GREY,
        'ytick.color':           MIST_GREY,
        'axes.spines.right':     False,
        'axes.spines.top':       False,
        'axes.spines.left':      True,
        'axes.spines.bottom':    True,
        'axes.edgecolor':        '#D0D0D0',
        'grid.color':            '#EEEEEE',
        'grid.linewidth':        0.6,
        'font.family':           'sans-serif',
        'font.size':             10,
    })

def title_style(ax, title, subtitle=None):
    ax.set_title(title, color=MAERSK_BLUE, fontsize=13,
                 fontweight='bold', pad=14, loc='left')
    if subtitle:
        ax.text(0, 1.01, subtitle, transform=ax.transAxes,
                color=MIST_GREY, fontsize=9, va='bottom')

def save(fig, filename):
    path = os.path.join(OUTPUT_DIR, filename)
    fig.savefig(path, dpi=200, bbox_inches='tight',
                facecolor=WHITE, edgecolor='none')
    plt.close(fig)
    print(f'  Saved → {filename}')

# ---------------------------------------------------------------------------
# FIG 1 — Crisis Window Profile
# Weekly average berth wait time. Crisis weeks W5-W9 in Signal Red.
# SLA threshold line at 16h in Maersk Gold.
# ---------------------------------------------------------------------------

def fig1_crisis_window():
    apply_base_style()
    heatmap = _load('heatmap_data.csv')

    weekly = (heatmap
              .groupby(['Week_Num', 'Is_Crisis_Week'])
              .agg(avg_wait=('Avg_Wait', 'mean'))
              .reset_index())

    bar_colors = [SIGNAL_RED if c else OCEAN_BLUE
                  for c in weekly['Is_Crisis_Week']]

    fig, ax = plt.subplots(figsize=(12, 4.5))

    ax.bar(weekly['Week_Num'], weekly['avg_wait'],
           color=bar_colors, edgecolor='none', width=0.65, zorder=3)

    ax.axhline(y=16, color=MAERSK_GOLD, linestyle='--',
               linewidth=1.4, zorder=4, label='SLA threshold — 16h')

    # Crisis window shading
    ax.axvspan(4.6, 9.4, alpha=0.06, color=SIGNAL_RED, zorder=1)
    ax.text(7, ax.get_ylim()[1] if ax.get_ylim()[1] > 0 else 20,
            'Crisis window\nW5–W9', ha='center', va='top',
            color=SIGNAL_RED, fontsize=8, style='italic')

    title_style(ax,
                'Average Berth Wait Time by Week — Q1 2026',
                'APM Terminals Rotterdam MVII  ·  563 vessel records  ·  SLA threshold: 16 hours')

    ax.set_xlabel('Week', color=MIST_GREY, fontsize=9)
    ax.set_ylabel('Avg wait (hours)', color=MIST_GREY, fontsize=9)
    ax.set_xticks(weekly['Week_Num'])
    ax.set_xticklabels([f'W{w}' for w in weekly['Week_Num']], fontsize=8)
    ax.yaxis.grid(True, zorder=0)
    ax.set_axisbelow(True)

    crisis_p = mpatches.Patch(color=SIGNAL_RED,  label='Crisis weeks (W5–W9)')
    normal_p = mpatches.Patch(color=OCEAN_BLUE,  label='Normal operations')
    thresh_l = plt.Line2D([0], [0], color=MAERSK_GOLD,
                          linestyle='--', linewidth=1.4, label='SLA threshold (16h)')
    ax.legend(handles=[crisis_p, normal_p, thresh_l],
              fontsize=9, framealpha=0.9, edgecolor='#D0D0D0',
              loc='upper right')

    # Annotate peak
    peak_row = weekly.loc[weekly['avg_wait'].idxmax()]
    ax.annotate(
        f"Peak: {peak_row['avg_wait']:.1f}h\n(W{int(peak_row['Week_Num'])})",
        xy=(peak_row['Week_Num'], peak_row['avg_wait']),
        xytext=(peak_row['Week_Num'] + 1.2, peak_row['avg_wait'] + 0.5),
        fontsize=8, color=SIGNAL_RED, fontweight='bold',
        arrowprops=dict(arrowstyle='->', color=SIGNAL_RED, lw=1.2))

    fig.text(0.01, -0.04,
             'All data synthetically generated. Not affiliated with APM Terminals or Maersk.',
             fontsize=7, color=MIST_GREY)

    plt.tight_layout()
    save(fig, 'fig1_crisis_window.png')


# ---------------------------------------------------------------------------
# FIG 2 — Scenario Rankings
# Horizontal bar — value recovered vs. crisis baseline.
# ---------------------------------------------------------------------------

def fig2_scenario_rankings():
    apply_base_style()
    scenarios = _load('tableau_scenarios.csv')
    ordered   = scenarios.sort_values('ROI_M', ascending=True)

    palette = {
        'Baseline (Crisis)':      MIST_GREY,
        'Priority Berthing Only': LIGHT_BLUE,
        'Slow-Steam Only':        OCEAN_BLUE,
        'Hybrid (Optimized)':     MAERSK_BLUE,
    }
    colors = [palette.get(s, OCEAN_BLUE) for s in ordered['Scenario']]

    fig, ax = plt.subplots(figsize=(10, 4))

    bars = ax.barh(ordered['Scenario'], ordered['ROI_M'],
                   color=colors, edgecolor='none', height=0.5, zorder=3)

    ax.axvline(x=0, color='#CCCCCC', linewidth=0.8)
    ax.xaxis.grid(True, zorder=0)
    ax.set_axisbelow(True)

    for bar, val, scenario in zip(bars, ordered['ROI_M'], ordered['Scenario']):
        if val > 0:
            label = f'+${val}M'
            x_pos = val + 0.3
            color = MAERSK_BLUE
        else:
            label = 'Baseline'
            x_pos = 0.3
            color = MIST_GREY
        ax.text(x_pos, bar.get_y() + bar.get_height() / 2,
                label, va='center', color=color,
                fontsize=10, fontweight='bold')

    # Reliability callouts
    rel_map = dict(zip(scenarios['Scenario'], scenarios['Reliability_Pct']))
    for bar, scenario in zip(bars, ordered['Scenario']):
        rel = rel_map.get(scenario, 0)
        ax.text(-0.4, bar.get_y() + bar.get_height() / 2,
                f'{rel}%', va='center', ha='right',
                color=MIST_GREY, fontsize=8)
    ax.text(-0.4, len(bars) - 0.1, 'Reliability',
            ha='right', color=MIST_GREY, fontsize=8, style='italic')

    # Gemini benchmark line
    hybrid_roi = scenarios.loc[
        scenarios['Scenario'] == 'Hybrid (Optimized)', 'ROI_M'].values[0]
    ax.axvline(x=hybrid_roi, color=MAERSK_GOLD, linestyle=':',
               linewidth=1.2, zorder=5)
    ax.text(hybrid_roi + 0.1, 0.05, 'Gemini\n90% met',
            color=MAERSK_GOLD, fontsize=7, va='bottom')

    title_style(ax,
                'Value Recovered vs. Crisis Baseline — Four Scenarios',
                'Q1 2026  ·  APM Terminals Rotterdam MVII  ·  Figures in USD millions')

    ax.set_xlabel('Value created ($M)', color=MIST_GREY, fontsize=9)
    ax.set_xlim(left=-2)

    fig.text(0.01, -0.06,
             'All data synthetically generated. Not affiliated with APM Terminals or Maersk.',
             fontsize=7, color=MIST_GREY)

    plt.tight_layout()
    save(fig, 'fig2_scenario_rankings.png')


# ---------------------------------------------------------------------------
# FIG 3 — Convergence Surge (Stacked Bar by Route)
# Weekly vessel arrivals, Cape vs. Suez, capacity threshold line.
# ---------------------------------------------------------------------------

def fig3_convergence_surge():
    apply_base_style()
    weekly = _load('stacked_bar_data.csv')

    cape = weekly[weekly['Route'] == 'Cape'].set_index('Week_Num')
    suez = weekly[weekly['Route'] == 'Suez'].set_index('Week_Num')
    weeks = sorted(weekly['Week_Num'].unique())

    cape_vals = [cape.loc[w, 'Vessel_Count'] if w in cape.index else 0 for w in weeks]
    suez_vals = [suez.loc[w, 'Vessel_Count'] if w in suez.index else 0 for w in weeks]
    total     = [c + s for c, s in zip(cape_vals, suez_vals)]
    crisis    = [weekly[weekly['Week_Num'] == w]['Is_Crisis_Week'].max() for w in weeks]

    edge_colors = [SIGNAL_RED if c else 'none' for c in crisis]

    fig, ax = plt.subplots(figsize=(12, 4.5))

    b1 = ax.bar(weeks, suez_vals, color=MAERSK_BLUE, edgecolor='none',
                width=0.65, label='Suez route', zorder=3)
    b2 = ax.bar(weeks, cape_vals, bottom=suez_vals, color=OCEAN_BLUE,
                edgecolor='none', width=0.65, label='Cape route', zorder=3)

    # Crisis week outlines
    for i, (w, ec) in enumerate(zip(weeks, edge_colors)):
        if ec != 'none':
            ax.bar(w, total[i], color='none', edgecolor=SIGNAL_RED,
                   linewidth=1.5, width=0.65, zorder=4)

    ax.axhline(y=49, color=MAERSK_GOLD, linestyle='--',
               linewidth=1.4, zorder=5, label='Capacity threshold (49 vessels)')

    # Crisis window shading
    ax.axvspan(4.6, 9.4, alpha=0.05, color=SIGNAL_RED, zorder=1)

    title_style(ax,
                'Weekly Vessel Arrivals by Route — Convergence Surge Q1 2026',
                'Dual-route convergence: Cape-rerouted + residual Suez traffic arrive simultaneously at Rotterdam MVII')

    ax.set_xlabel('Week', color=MIST_GREY, fontsize=9)
    ax.set_ylabel('Vessels', color=MIST_GREY, fontsize=9)
    ax.set_xticks(weeks)
    ax.set_xticklabels([f'W{w}' for w in weeks], fontsize=8)
    ax.yaxis.grid(True, zorder=0)
    ax.set_axisbelow(True)

    ax.legend(fontsize=9, framealpha=0.9, edgecolor='#D0D0D0',
              loc='upper left')

    # Annotate peak week
    peak_w = weeks[total.index(max(total))]
    ax.annotate(
        f'Peak: {max(total)} vessels\n(W{peak_w})',
        xy=(peak_w, max(total)),
        xytext=(peak_w + 1, max(total) + 2),
        fontsize=8, color=SIGNAL_RED, fontweight='bold',
        arrowprops=dict(arrowstyle='->', color=SIGNAL_RED, lw=1.2))

    fig.text(0.01, -0.04,
             'All data synthetically generated. Not affiliated with APM Terminals or Maersk.',
             fontsize=7, color=MIST_GREY)

    plt.tight_layout()
    save(fig, 'fig3_convergence_surge.png')


# ---------------------------------------------------------------------------
# FIG 4 — Financial Exposure Breakdown
# Grouped bar: SLA penalty + idle cost by scenario.
# ---------------------------------------------------------------------------

def fig4_financial_exposure():
    apply_base_style()
    scenarios = _load('tableau_scenarios.csv')

    order  = ['Baseline (Crisis)', 'Priority Berthing Only',
              'Slow-Steam Only', 'Hybrid (Optimized)']
    scenarios = scenarios.set_index('Scenario').loc[order].reset_index()

    x      = np.arange(len(scenarios))
    width  = 0.35

    fig, ax = plt.subplots(figsize=(11, 5))

    b1 = ax.bar(x - width/2, scenarios['SLA_Penalty_M'],
                width, color=SIGNAL_RED, edgecolor='none',
                label='SLA penalties ($M)', zorder=3)
    b2 = ax.bar(x + width/2, scenarios['Idle_Cost_M'],
                width, color=MAERSK_BLUE, edgecolor='none',
                label='Idle costs ($M)', zorder=3)

    # Value labels
    for bar in list(b1) + list(b2):
        h = bar.get_height()
        ax.text(bar.get_x() + bar.get_width() / 2, h + 0.3,
                f'${h:.1f}M', ha='center', va='bottom',
                fontsize=8.5, color=MAERSK_BLUE, fontweight='bold')

    # Reliability annotations — placed below x-axis labels
    for i, (_, row) in enumerate(scenarios.iterrows()):
        ax.text(i, -3.5,
                f"{row['Reliability_Pct']}% reliability",
                ha='center', fontsize=8, color=MIST_GREY)

    ax.yaxis.grid(True, zorder=0)
    ax.set_axisbelow(True)
    ax.set_xticks(x)
    ax.set_xticklabels(scenarios['Scenario'], fontsize=9)
    ax.set_ylabel('Cost ($M)', color=MIST_GREY, fontsize=9)

    title_style(ax,
                'Financial Exposure by Scenario — SLA Penalties and Idle Costs',
                'Q1 2026  ·  APM Terminals Rotterdam MVII  ·  Figures in USD millions')

    ax.legend(fontsize=9, framealpha=0.9, edgecolor='#D0D0D0')

    fig.text(0.01, -0.04,
             'All data synthetically generated. Not affiliated with APM Terminals or Maersk.',
             fontsize=7, color=MIST_GREY)

    plt.tight_layout()
    save(fig, 'fig4_financial_exposure.png')


# ---------------------------------------------------------------------------
# FIG 5 — Financial Waterfall
# Baseline total exposure stepping down through interventions to optimized.
# ---------------------------------------------------------------------------

def fig5_financial_waterfall():
    apply_base_style()
    scenarios = _load('tableau_scenarios.csv')

    baseline = scenarios[scenarios['Scenario'] == 'Baseline (Crisis)'].iloc[0]
    hybrid   = scenarios[scenarios['Scenario'] == 'Hybrid (Optimized)'].iloc[0]

    baseline_total = baseline['SLA_Penalty_M'] + baseline['Idle_Cost_M']  # 41.28
    hybrid_total   = hybrid['SLA_Penalty_M'] + hybrid['Idle_Cost_M']       # 13.80
    total_saved    = baseline_total - hybrid_total                          # 27.48
    # Net ROI from model is 19.23 (net of intervention costs)
    net_roi        = hybrid['ROI_M']  # 19.23

    sla_saved  = baseline['SLA_Penalty_M'] - hybrid['SLA_Penalty_M']   # 9.74
    idle_saved = baseline['Idle_Cost_M']   - hybrid['Idle_Cost_M']      # 17.74

    labels  = ['Baseline\nexposure', 'SLA penalty\nreduction',
               'Idle cost\nreduction', 'Optimized\nexposure']
    values  = [baseline_total, -sla_saved, -idle_saved, hybrid_total]
    running = [baseline_total,
               baseline_total - sla_saved,
               baseline_total - sla_saved - idle_saved,
               0]
    bottoms = [0, running[1], running[2], 0]

    colors = [MAERSK_BLUE, OCEAN_BLUE, LIGHT_BLUE, MAERSK_GOLD]
    bar_h  = [baseline_total, sla_saved, idle_saved, hybrid_total]
    bar_b  = [0, running[1], running[2], 0]

    fig, ax = plt.subplots(figsize=(10, 5.5))

    bars = ax.bar(labels, bar_h, bottom=bar_b,
                  color=colors, edgecolor='none', width=0.5, zorder=3)

    # Connector lines between bars
    for i in range(len(labels) - 1):
        top = bar_b[i] + bar_h[i]
        ax.plot([i + 0.25, i + 0.75],
                [top, top], color='#CCCCCC', linewidth=0.8, zorder=2)

    # Value labels
    label_vals = [
        f'${baseline_total:.2f}M',
        f'-${sla_saved:.2f}M',
        f'-${idle_saved:.2f}M',
        f'${hybrid_total:.2f}M',
    ]
    label_y = [
        bar_b[0] + bar_h[0] + 0.5,
        bar_b[1] + bar_h[1] / 2,
        bar_b[2] + bar_h[2] / 2,
        bar_b[3] + bar_h[3] + 0.5,
    ]
    label_colors = [MAERSK_BLUE, WHITE, WHITE, MAERSK_BLUE]
    va_opts      = ['bottom', 'center', 'center', 'bottom']

    for i, (lv, ly, lc, va) in enumerate(
            zip(label_vals, label_y, label_colors, va_opts)):
        ax.text(i, ly, lv, ha='center', va=va,
                color=lc, fontsize=10, fontweight='bold')

    # Net ROI callout
    ax.annotate(
        f'$19.23M\nrecovered',
        xy=(3, hybrid_total + 0.5),
        xytext=(2.3, 30),
        fontsize=10, color=MAERSK_BLUE, fontweight='bold', ha='center',
        arrowprops=dict(arrowstyle='->', color=MAERSK_BLUE, lw=1.3))

    ax.yaxis.grid(True, zorder=0)
    ax.set_axisbelow(True)
    ax.set_ylabel('Cost exposure ($M)', color=MIST_GREY, fontsize=9)
    ax.set_ylim(bottom=0)

    title_style(ax,
                'Q1 2026 Financial Exposure: Baseline to Optimized',
                f'Total baseline: ${baseline_total:.2f}M  ·  Optimized: ${hybrid_total:.2f}M  ·  Net recovered: $19.23M')

    fig.text(0.01, -0.04,
             'All data synthetically generated. Not affiliated with APM Terminals or Maersk.',
             fontsize=7, color=MIST_GREY)

    plt.tight_layout()
    save(fig, 'fig5_financial_waterfall.png')


# ---------------------------------------------------------------------------
# MAIN
# ---------------------------------------------------------------------------

if __name__ == '__main__':
    print('Ghost Burn — Red Sea Port Orchestration')
    print('Generating publication charts...\n')

    fig1_crisis_window()
    fig2_scenario_rankings()
    fig3_convergence_surge()
    fig4_financial_exposure()
    fig5_financial_waterfall()

    print('\nAll 5 figures generated at 200 DPI.')
    print('Maersk color palette applied throughout.')
    print('Safe to commit to repo root.')
