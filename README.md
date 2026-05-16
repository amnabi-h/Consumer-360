# Consumer-360
# Consumer360: End-to-End Enterprise Retail Analytics Platform
### 🛠️ Individual Comprehensive Engineering Rebuild (V2)

---

## 📌 1. Project Overview & Strategic Vision

In the corporate retail sector, raw transactional data is frequently locked away in isolated operational ledgers or unstructured spreadsheets, rendering rapid decision-making impossible. **Consumer360** solves this critical business problem. 

This platform is a fully realized analytical ecosystem designed to ingest unstructured enterprise sales records, establish a secure relational staging layer, automate advanced customer behavioral segmentation, execute unsupervised machine learning to discover hidden product affinities, and serve high-impact visual intelligence to organizational stakeholders.

### 💡 The Core Business Value Propositions:
* **Customer Health Tracking:** Identifying precisely who drives revenue and who is slipping into churn.
* **Cross-Selling Engine:** Spotting micro-affinities between different product sub-categories to drive predictive inventory and bundles.
* **Executive Visibility:** Consolidating thousands of cross-state sales records into a singular, unified truth for the executive leadership.

---

## ✊ 2. Statement of Individuality: The V2 Evolution

> **CRITICAL PORTFOLIO NOTE:** This repository represents a complete, ground-up individual engineering overhaul. While an earlier version was explored collaboratively, **this V2 architecture was built 100% independently** to transition the proof-of-concept into a production-ready data product.

### How this individual version drastically outperforms the legacy baseline:
1.  **Architecture Migration:** Replaced volatile flat-file data manipulation loops with a standardized relational SQL database infrastructure (`Consumer360_Database.db`).
2.  **Algorithmic Rigor & Tie-Breaking:** Rewrote the customer scoring distribution engine to use mathematical rank-ordering logic. This permanently eliminated standard quantile errors caused by thousands of low-frequency identical customer behaviors.
3.  **Production-Grade Defensive Programming:** Injected custom string sanitization layers (`ascii-ignore` wrappers) directly into data streams. This protects downstream systems from crashing due to hidden Excel formatting metadata traps and non-standard text artifacts.
4.  **UI/UX Redesign:** Completely overhauled the Power BI tier from scratch, creating an intuitive dashboard experience built on rigorous interface design standards and dimensional filtering.

---

## 📂 3. Repository Blueprint & Data Dictionary

```text
├── data/
│   ├── 01_Sales Dataset.xlsx             # Raw unstructured enterprise sales ledger
│   ├── Consumer360_Database.db           # Optimized SQLite relational staging layer
│   ├── Final_Customer_Segmentation.xlsx  # Downstream output: Algorithmic RFM Cohorts
│   └── Market_Basket_Rules.xlsx          # Downstream output: Machine Learning Association Rules
│
├── notebooks/
│   ├── Project_Discovery_EDA.ipynb       # Interactive Data Discovery Lab & trend modeling
│   └── SQL_Database_Proof.ipynb          # Staging database orchestration & structural schemas
│
├── scripts/
│   ├── rfm_analysis.py                   # Production Script: Algorithmic Segmentation Engine
│   └── basket_analysis.py                # Production Script: Unsupervised Data Mining Engine
│
├── dashboard/
│   ├── Con360dashboard.pbix              # Enterprise Power BI Interactive Package
│   ├── Executive Overview.png            # Dashboard UI: Strategic KPI View
│   └── Customers and product deep dive.png # Dashboard UI: Granular Cohort Analysis View
└── README.md
