# Ingestion Strategy

## Overview

This document describes the ingestion strategy for the Smart Factory Command Center’s data layer. It defines the process for loading the four core datasets into the raw layer and preparing them for downstream processing.

## Principles

* Ingest raw data as close to source format as possible.
* Apply schema validation and quality checks at ingestion time.
* Keep raw data immutable and auditable.
* Support repeatable batch ingestion and ad hoc re-ingestion.
* Capture metadata for source, batch, and load status.

## Data Sources

1. AI4I 2020 Predictive Maintenance
2. Steel Plates Faults
3. Store Item Demand Forecasting
4. Supply Chain Analytics

### Source Formats

* CSV, Parquet, or database extracts for historical datasets.
* Optional integration with API or file share for periodic updates.

## Ingestion Layers

### Raw Layer

* Stores source files and raw table records without transformation.
* Preserve original field names and values.
* Store raw ingestion metadata including `source_name`, `ingest_timestamp`, `batch_id`, and `source_path`.

#### Raw Layer Storage Patterns

* `data/raw/ai4i_predictive_maintenance/`
* `data/raw/steel_plates_faults/`
* `data/raw/store_demand_forecasting/`
* `data/raw/supply_chain_analytics/`

### Processed Layer

* Stores cleansed and normalized rows.
* Applies type casting, null handling, and key normalization.
* Records processing provenance with `processed_timestamp`, `raw_batch_id`, and `processing_status`.

### Feature Layer

* Stores engineered features keyed by entity and timestamp.
* Provides consistent feature materialization for training and inference.

### Training Layer

* Stores labeled datasets for model training and evaluation.
* Includes dataset snapshot metadata and split definitions.

## Ingestion Process

### Step 1: Source Acquisition

* Fetch or mount dataset files from the canonical source.
* Validate source integrity using file checksums and expected file names.

### Step 2: Raw Load

* Load source files into the raw layer without changes.
* Add ingestion metadata:
  * `source_name`
  * `batch_id`
  * `ingest_timestamp`
  * `source_path`
  * `row_count`

### Step 3: Schema Validation

* Validate raw schema against expected definitions.
* Detect missing columns, extra columns, data type mismatches, and schema drift.
* Reject or quarantine malformed batches.

### Step 4: Data Quality Checks

* Run data quality rules from `data_quality_rules.md`.
* Capture failures and route invalid rows to a quarantine store.
* Only promote clean batches to the processed layer.

### Step 5: Processed Layer Population

* Normalize keys and timestamps.
* Impute or remove missing values as defined.
* Standardize categorical labels.
* Save processed records with provenance metadata.

### Step 6: Feature Generation

* Execute feature engineering pipelines to populate the feature layer.
* Tag feature records with `feature_version` and `ingest_date`.
* Validate feature completeness and freshness.

### Step 7: Training Dataset Preparation

* Join features with target labels.
* Create training snapshots for the current model version.
* Store dataset artifacts with MLflow experiment references.

## Scheduling and Orchestration

* Use workflow orchestration for batch ingestion, such as Apache Airflow, Prefect, or a custom scheduler.
* Schedule initial batch loads for historical backfill.
* Schedule incremental refreshes for datasets with periodic updates.
* Track pipeline state and retry logic.

## Error Handling

* Failures are classified by severity:
  * Fatal schema error: stop pipeline and alert.
  * Data quality error: quarantine bad rows and continue if configured.
  * Connectivity error: retry with exponential backoff.
* Log errors with context, source batch, and row samples.
* Persist error and reconciliation metadata for auditing.

## Metadata and Lineage

Capture metadata at every ingestion stage:

* `raw_batch_id`
* `processed_batch_id`
* `feature_batch_id`
* `dataset_version`
* `ingest_timestamp`
* `source_uri`
* `record_count`
* `quality_status`

This metadata supports traceability, reproducibility, and data governance.

## Data Retention

* Retain raw layer data as an immutable archive for lineage.
* Retain processed and feature layer records according to business retention policies.
* Purge stale training snapshots only after model refresh and compliance review.
