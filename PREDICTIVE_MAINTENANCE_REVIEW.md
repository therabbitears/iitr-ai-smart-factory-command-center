# Predictive Maintenance Module - Code Review Report

## Executive Summary

The Predictive Maintenance module has a solid foundational structure but contains several critical issues that must be addressed before production deployment. The most critical issues are:

1. **Data Leakage**: Feature engineering happens before train-test split
2. **Incomplete Train/Validation/Test Split**: No proper validation set for hyperparameter tuning
3. **Metric Selection**: Lack of class imbalance analysis and hard-coded thresholds
4. **Code Quality**: Duplicated constants, missing docstrings, dead code
5. **Production Readiness**: No logging, monitoring, or error handling

---

## Detailed Findings

### 1. Data Leakage Review - CRITICAL

#### Issue 1.1: Feature Engineering Before Train-Test Split
**Location**: `pipeline.py:run()` lines 30-31

```python
df = clean_data(df)
df = add_engineered_features(df)  # ← Applied to entire dataset
X_train, X_test, y_train, y_test = split_data(df)  # ← Then split
```

**Problem**: Derived features (`temp_delta`, `wear_rate`, `torque_ratio`, `temperature_ratio`) use aggregate statistics that are influenced by the test set.

**Impact**: Model evaluation metrics are optimistically biased; production performance will degrade.

**Fix**: Apply feature engineering separately to train and test sets.

---

#### Issue 1.2: Scaler Fit on Full Dataset
**Location**: `train.py:build_classifiers()` - StandardScaler within pipeline

**Problem**: StandardScaler is part of the pipeline, so it fits on training data correctly, but feature engineering constants/parameters should not be computed from test data.

**Impact**: Derived features leak statistical information from test set.

**Fix**: Create a FeatureEngineer class that captures statistics only from training data.

---

### 2. Feature Engineering Review

#### Issue 2.1: Division-by-Zero Workaround
**Location**: `features.py:add_engineered_features()` lines 6-9

```python
df["wear_rate"] = df["tool_wear"] / df["rotational_speed"].replace(0, 1)
df["torque_ratio"] = df["torque"] / df["rotational_speed"].replace(0, 1)
```

**Problem**: Silently replacing 0 with 1 masks data quality issues and introduces a non-physical value.

**Impact**: Misleading features; hard to debug failed training runs.

**Fix**: Explicitly handle zero values with conditional logic or remove rows with zero rotational speed.

---

#### Issue 2.2: Incomplete Feature Engineering
**Location**: `features.py`

**Problem**: Missing:
- Temporal/cyclical features (hour-of-day, day-of-week)
- Lagged features (prior temperature, wear history)
- Rolling statistics (moving average of temperature)
- Interaction terms with domain significance

**Impact**: Model underfits; predictive power limited.

**Fix**: Expand feature set with domain-driven engineering.

---

### 3. Model Evaluation Review - CRITICAL

#### Issue 3.1: No Class Imbalance Analysis
**Location**: `pipeline.py:run()` - entire method

**Problem**: No check for class balance; F1 score used as primary metric without validation that it's appropriate.

**Impact**: Models may achieve high accuracy on majority class while failing on minority (failure) class.

**Fix**: Add class distribution analysis and choose metrics accordingly.

---

#### Issue 3.2: Hard-Coded Decision Threshold
**Location**: `evaluate.py:predict_model()` line 19

```python
predictions = (probabilities >= 0.5).astype(int)
```

**Problem**: 0.5 threshold is arbitrary and not tuned for imbalanced data. May not be optimal.

**Impact**: Suboptimal precision-recall tradeoff.

**Fix**: Compute threshold based on ROC curve or use probability-based predictions.

---

#### Issue 3.3: No Cross-Validation
**Location**: `pipeline.py:_train_models()`

**Problem**: Single train-test split provides high variance in performance estimates.

**Impact**: Model selection unreliable; overconfident metrics.

**Fix**: Implement k-fold cross-validation.

---

#### Issue 3.4: ANN Validation Split Issues
**Location**: `pipeline.py:_train_models()` lines 72-77

```python
X_ann_train, X_ann_val, y_ann_train, y_ann_val = split_data(
    pd.concat([X_train, y_train], axis=1), test_size=0.2, random_state=42
)
```

**Problem**: Validation set for ANN is created from ALREADY-SPLIT training data. The test set is never used for ANN training/validation. Inconsistent with other models.

**Impact**: ANN may be incomparable to sklearn models.

**Fix**: Use consistent train/val/test split across all models.

---

### 4. Code Quality Review

#### Issue 4.1: Duplicated Feature Columns
**Location**: `preprocessing.py`, `train.py`, `features.py`

**Problem**: `NUMERIC_COLUMNS` defined in three places with different scopes.

**Impact**: Maintenance burden; risk of inconsistency.

**Fix**: Define once in a constants module; import everywhere.

---

#### Issue 4.2: Dead Code
**Location**: `preprocessing.py:encode_labels()` lines 29-30

```python
def encode_labels(df: pd.DataFrame) -> pd.DataFrame:
    return df.copy()
```

**Problem**: Function does nothing; misleads developers.

**Fix**: Remove unused function.

---

#### Issue 4.3: Missing Docstrings
**Location**: All functions in `features.py`, `train.py`, `evaluate.py`

**Problem**: No documentation of function purpose, parameters, returns; makes it hard for new developers.

**Fix**: Add comprehensive docstrings (Google style).

---

#### Issue 4.4: Inconsistent Type Hints
**Location**: `pipeline.py:_train_models()` parameters

**Problem**: Complex return types not fully specified; model dict uses `Any` which loses type safety.

**Fix**: Use `TypedDict` or dataclass for better typing.

---

### 5. Production Readiness Review

#### Issue 5.1: No Logging
**Location**: Entire module

**Problem**: No logging of feature engineering steps, model training progress, or errors. Debugging production issues will be difficult.

**Impact**: Poor observability; hard to troubleshoot failures.

**Fix**: Add structured logging at key decision points.

---

#### Issue 5.2: No Input Validation
**Location**: `loader.py`, `pipeline.py`

**Problem**: No validation of input data schema or required columns before processing.

**Impact**: Cryptic errors if input data is malformed.

**Fix**: Add explicit column and type checks before feature engineering.

---

#### Issue 5.3: No Error Handling
**Location**: `pipeline.py:run()`, `train.py`

**Problem**: No try/catch for expected failure modes (empty data, NaN values, model training failure).

**Impact**: Pipeline crashes instead of gracefully failing with context.

**Fix**: Add comprehensive error handling.

---

#### Issue 5.4: Hard-Coded Hyperparameters
**Location**: `train.py:build_classifiers()`, `train.py:build_ann_model()`

**Problem**: Hyperparameters are baked into the code; no tuning framework.

**Impact**: Suboptimal models; no way to experiment without code changes.

**Fix**: Move hyperparameters to a config file or hyperparameter registry.

---

#### Issue 5.5: No Model Explainability
**Location**: Entire module

**Problem**: No interpretability layer (SHAP, feature importance, etc.).

**Impact**: Cannot explain predictions to stakeholders; audit trail missing.

**Fix**: Add SHAP values to MLflow artifacts.

---

#### Issue 5.6: Inconsistent Model Persistence
**Location**: `model_store.py`, `pipeline.py`

**Problem**: Models are saved to disk but with inconsistent paths and naming; no registry/metadata.

**Impact**: Hard to track which model is deployed; difficult to load/serve.

**Fix**: Implement standardized model versioning and metadata registry.

---

## Summary Table

| Issue | Severity | Category | Fix Effort |
|-------|----------|----------|-----------|
| Feature engineering before split | CRITICAL | Data Leakage | High |
| No class imbalance analysis | HIGH | Evaluation | Medium |
| Hard-coded decision threshold | HIGH | Evaluation | Medium |
| No cross-validation | HIGH | Evaluation | High |
| Duplicated feature columns | MEDIUM | Code Quality | Low |
| Dead code (`encode_labels`) | LOW | Code Quality | Low |
| Missing docstrings | MEDIUM | Code Quality | Medium |
| No logging | HIGH | Production | Medium |
| No input validation | HIGH | Production | Medium |
| Hard-coded hyperparameters | MEDIUM | Production | High |
| No explainability layer | MEDIUM | Production | High |

---

## Recommended Next Steps

1. **Immediate** (before any production use):
   - Fix data leakage in feature engineering
   - Add class imbalance analysis
   - Implement cross-validation

2. **Short-term** (next sprint):
   - Add logging and error handling
   - Consolidate feature column definitions
   - Add input validation
   - Remove dead code

3. **Medium-term** (upcoming releases):
   - Implement hyperparameter tuning framework
   - Add SHAP explainability
   - Enhance feature engineering with domain-driven features
   - Implement proper model registry and versioning
