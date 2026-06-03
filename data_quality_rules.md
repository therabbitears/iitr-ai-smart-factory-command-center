# Data Quality Rules

## Overview

This document defines the data quality rules for the Smart Factory Command Center. Rules are grouped by layer and dataset to ensure consistent, reliable input for feature engineering and modeling.

## Quality Rule Categories

* Completeness
* Accuracy
* Consistency
* Validity
* Timeliness
* Uniqueness

## Cross-Cutting Rules

1. Required field validation for entity keys and timestamps.
2. Non-null numeric values for core sensor and inventory fields.
3. Categorical label validation against allowed value sets.
4. Date and time normalization to UTC or a consistent timezone.
5. Duplicate row detection based on natural keys.
6. Schema drift detection against expected raw schema.

---

## Raw Layer Rules

### AI4I 2020 Predictive Maintenance

* `machine_id` must be present and non-empty.
* `timestamp` must parse as datetime and be within expected date range.
* `air_temperature`, `process_temperature`, `rotational_speed`, `torque`, and `tool_wear` must be numeric and non-null.
* `machine_failure` must be in {0, 1}.
* `failure_type` must be one of the known classes.
* Reject rows with invalid or missing labels.

### Steel Plates Faults

* `plate_id` must be present.
* All numeric measurement fields must be non-null and within physically plausible ranges.
* `class` must map to valid defect classes.
* Ensure no duplicate `plate_id` / `inspection_date` pairs.

### Store Item Demand Forecasting

* `date`, `store`, and `item` must be non-null.
* `sales` must be numeric and greater than or equal to 0.
* Event and promotion indicator fields must be boolean or normalized to boolean values.
* Ensure the combination `date` + `store` + `item` is unique.

### Supply Chain Analytics

* `product_id`, `warehouse_id`, and `date` must be non-null.
* `on_hand`, `reorder_point`, `lead_time_days`, and `demand_forecast` must be numeric.
* `lead_time_days` must be positive.
* `stockouts` must be integer and greater than or equal to 0.

---

## Processed Layer Rules

* All entity keys are standardized and normalized.
* Missing values are handled according to defined imputation rules.
* Derived fields are validated for expected value ranges.
* Data type casting is enforced for every column.
* Referential integrity checks ensure foreign keys reference master entities.
* Timestamp continuity is validated for time series data.

### Specific Processed Checks

* Predictive Maintenance: `health_score` must be between 0 and 1.
* Quality Inspection: engineered surface metrics must preserve physical bounds.
* Demand Forecasting: lag features must be non-negative and align with prior dates.
* Inventory Optimization: `safety_stock` must be greater than or equal to 0.

---

## Feature Layer Rules

* Feature records must include `feature_version`, `ingest_date`, and entity keys.
* No null values in required feature columns.
* Feature freshness rule: record age must not exceed acceptable latency for the use case.
* Historical feature values must be consistent with source time series.
* Versioned feature definitions must be audited as part of the feature lineage.

### Feature-Specific Validations

* Demand forecasting features: `rolling_mean_7` and `rolling_std_7` are computed using at least 7 prior observations.
* Inventory optimization features: `stockout_risk` must be calculated from the latest valid demand and on-hand inventory.
* Predictive maintenance features: `wear_rate` must not be negative.

---

## Training Layer Rules

* Training datasets must be complete for the selected split.
* All target labels must be validated and aligned to features by the correct timestamp.
* Train/validation/test splits must be mutually exclusive and time-consistent.
* No data leakage: future information must not exist in past training records.
* Experiment metadata must be recorded for every dataset version.

### Split Validation

* Temporal splits should preserve chronological order for forecasting and maintenance models.
* Holdout sets should account for entity-level separation when needed.

---

## Monitoring and Alerts

* Data quality checks are run at ingestion and before training.
* Failed checks generate alerts with dataset name, rule, and offending row sample.
* A data quality dashboard tracks pass/fail rates and quality trend over time.
* Quality test results are archived alongside training artifacts.

## Remediation Guidelines

1. Log and isolate bad records in a quarantine store.
2. Notify data owners for schema or content issues.
3. Retry ingestion after correcting source anomalies.
4. Record root-cause and corrective action in data quality metadata.
