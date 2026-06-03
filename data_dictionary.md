# Data Dictionary

## Overview

This data dictionary documents the core datasets used by the Smart Factory Command Center. Each dataset is broken into the raw schema, primary keys, semantic meaning, and intended use for AI modules.

---

## 1. AI4I 2020 Predictive Maintenance

### Dataset Purpose
Predict machine failures and classify failure types based on sensor telemetry and process variables.

### Raw Schema

| Column | Type | Description | Example | Usage |
|---|---|---|---|---|
| `air_temperature` | numeric | Ambient air temperature around the machine | 20.5 | Feature engineering, model input |
| `process_temperature` | numeric | Temperature of the manufacturing process | 45.3 | Feature engineering, model input |
| `rotational_speed` | numeric | Machine spindle or conveyor RPM | 1500 | Feature engineering |
| `torque` | numeric | Torque applied to machine components | 35.0 | Feature engineering |
| `tool_wear` | numeric | Estimated tool wear percentage | 0.5 | Feature engineering |
| `machine_failure` | integer | Failure indicator label (0 = no failure, 1 = failure) | 0 | Target variable |
| `failure_type` | categorical | Failure type label | `Tool wear`, `Heat dissipation failure`, `Power failure`, `Overstrain failure` | Multi-class target |
| `timestamp` | datetime | Event time of the measurement | `2020-09-01T08:00:00Z` | Time-based feature engineering |
| `machine_id` | string | Unique identifier for the machine | `M-1001` | Entity key |

### Notes
- `machine_id` is the natural entity key used to join telemetry to machine metadata and audit logs.
- `timestamp` is used to construct time-window features and to align labeled failures with sensor readings.
- The raw data is typically imported from CSV or sensor export files.

---

## 2. Steel Plates Faults

### Dataset Purpose
Detect product quality defects from steel plate production parameters.

### Raw Schema

| Column | Type | Description | Example | Usage |
|---|---|---|---|---|
| `X_Minimum` | numeric | Minimum value of a specific surface measurement | 0.0 | Defect feature |
| `X_Maximum` | numeric | Maximum value of a surface measurement | 0.0 | Defect feature |
| `Y_Minimum` | numeric | Minimum value of another surface metric | 0.0 | Defect feature |
| `Y_Maximum` | numeric | Maximum value of that surface metric | 0.0 | Defect feature |
| `Pixel_area` | numeric | Total area of inspected pixels | 1413 | Defect feature |
| `Bare_Nuclei` | numeric | Number of bare nuclei detected | 1.0 | Defect feature |
| `class` | categorical | Label indicating fault class | `1` through `7` | Target variable |
| `plate_id` | string | Unique plate identifier | `P-0001` | Entity key |
| `inspection_date` | datetime | Date of quality inspection | `2020-08-15T00:00:00Z` | Time-based analysis |

### Notes
- The `class` label is a categorical defect label used for classification.
- Raw fields are direct measurements from the steel plate inspection process.
- Every record should have a valid `plate_id` and non-null numeric measurements.

---

## 3. Store Item Demand Forecasting

### Dataset Purpose
Forecast store-level item demand across time and product categories.

### Raw Schema

| Column | Type | Description | Example | Usage |
|---|---|---|---|---|
| `date` | date | Observation date | `2020-01-01` | Time index |
| `store` | integer | Store identifier | 1 | Entity key |
| `item` | integer | Item identifier | 1 | Entity key |
| `sales` | numeric | Number of units sold | 13 | Target variable |
| `onpromotion` | boolean | If item was on promotion | `True` | Feature indicator |
| `dayofweek` | integer | Day of week index | 3 | Temporal feature |
| `month` | integer | Month of year | 1 | Seasonal feature |
| `year` | integer | Year | 2013 | Temporal feature |
| `event_name_1` | string | Event name if present | `Mother's Day` | Categorical feature |
| `snap_CA` | boolean | California SNAP benefits event | `False` | External driver |
| `snap_TX` | boolean | Texas SNAP benefits event | `False` | External driver |
| `snap_WI` | boolean | Wisconsin SNAP benefits event | `False` | External driver |

### Notes
- The dataset is designed for hierarchical forecasting by store and item.
- The `date` field is the primary time key used to generate lag and seasonality features.
- Promotion and event variables are critical for demand signal amplification.

---

## 4. Supply Chain Analytics

### Dataset Purpose
Optimize inventory and procurement decisions using supply chain variables.

### Raw Schema

| Column | Type | Description | Example | Usage |
|---|---|---|---|---|
| `date` | date | Inventory snapshot date | `2020-01-01` | Time index |
| `product_id` | string | Product identifier | `SKU-1001` | Entity key |
| `warehouse_id` | string | Warehouse identifier | `WH-01` | Entity key |
| `on_hand` | numeric | Current inventory quantity | 380 | Inventory feature |
| `reorder_point` | numeric | Reorder threshold quantity | 100 | Policy feature |
| `lead_time_days` | numeric | Supplier lead time in days | 7 | Supply chain feature |
| `demand_forecast` | numeric | Expected demand quantity | 120 | Model input |
| `supplier_score` | numeric | Supplier reliability score | 0.83 | Risk feature |
| `stockouts` | integer | Historical stockout count | 0 | Target signal |
| `reorder_quantity` | numeric | Recommended reorder quantity | 200 | Output variable |

### Notes
- The dataset supports inventory optimization and stockout risk modeling.
- `product_id` + `warehouse_id` + `date` form the composite natural key.
- Supplier and lead time features are used to compute safety stock and reorder recommendations.

---

## Data Entity Definitions

### Core Entities

* `machine` — machine asset monitored for predictive maintenance.
* `plate` — steel plate unit inspected for quality.
* `store-item` — combination of store and item for demand forecasting.
* `product-warehouse` — inventory product at a warehouse for optimization.

### Key Fields

* Raw layer: preserve original dataset keys from source files.
* Processed layer: maintain stable entity keys and time indices.
* Feature layer: reference entity key plus feature version and expiration metadata.

---

## Quality and Validation Notes

* Nullability should be validated at ingestion for required fields.
* Numeric ranges should be enforced for sensor and inventory values.
* Categorical labels require explicit mapping and consistency across dataset versions.
* All date/time columns should be normalized to UTC or a consistent timezone.
