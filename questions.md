# Capstone AI/ML Implementation Question Bank

This is a rebuilt, non-padded viva/interview preparation file based on the actual AI/ML-related Python files in the repository. Questions are grouped by module, include file references, and call out real implementation decisions, formulas, risks, and known gaps.

## Files Audited

- `app/backend/src/app/ml/predictive_maintenance/train.py`
- `app/backend/src/app/ml/predictive_maintenance/preprocessing.py`
- `app/backend/src/app/ml/predictive_maintenance/features.py`
- `app/backend/src/app/ml/predictive_maintenance/evaluate.py`
- `app/backend/src/app/ml/predictive_maintenance/pipeline.py`
- `app/backend/src/app/ml/predictive_maintenance/model_store.py`
- `app/backend/src/app/ml/quality_inspection/train.py`
- `app/backend/src/app/ml/quality_inspection/preprocessing.py`
- `app/backend/src/app/ml/quality_inspection/features.py`
- `app/backend/src/app/ml/quality_inspection/evaluate.py`
- `app/backend/src/app/ml/quality_inspection/pipeline.py`
- `app/backend/src/app/ml/demand_forecasting/train.py`
- `app/backend/src/app/ml/demand_forecasting/preprocessing.py`
- `app/backend/src/app/ml/demand_forecasting/features.py`
- `app/backend/src/app/ml/demand_forecasting/evaluate.py`
- `app/backend/src/app/ml/demand_forecasting/pipeline.py`
- `app/backend/src/app/ml/demand_forecasting/model_store.py`
- `ml/inventory_optimization/train.py`
- `ml/inventory_optimization/preprocessing.py`
- `ml/inventory_optimization/features.py`
- `ml/inventory_optimization/evaluate.py`
- `ml/inventory_optimization/pipeline.py`
- `ml/inventory_optimization/mlflow_utils.py`
- `app/backend/src/app/data/loaders.py`
- `app/backend/src/app/data/validation.py`
- `app/backend/src/app/data/profiling.py`
- `app/backend/src/app/data/versioning.py`
- `app/backend/services.py`
- `app/backend/metrics.py`

## Core Formula Sheet

- StandardScaler: `z = (x - mean) / std`.
- Sigmoid: `p = 1 / (1 + exp(-z))`.
- Binary crossentropy: `-mean(y log(p) + (1-y) log(1-p))`.
- Softmax: exponentiate class scores and normalize so class probabilities sum to 1.
- Sparse categorical crossentropy: multiclass crossentropy for integer class labels.
- RMSE: `sqrt(mean((y_true - y_pred)^2))`.
- MAE: `mean(abs(y_true - y_pred))`.
- MAPE: `mean(abs((y_true - y_pred) / y_true)) * 100`, with epsilon protection in this code.
- R2: proportion of variance in the target explained by the model.
- Precision: `TP / (TP + FP)`.
- Recall: `TP / (TP + FN)`.
- F1: `2 * precision * recall / (precision + recall)`.

## Questions

## Project and Architecture

### Q1. What is the central AI/ML idea of the capstone?

The project is an AI operations platform for a smart factory. It combines predictive maintenance, quality inspection, demand forecasting, and inventory optimization instead of stopping at one isolated model.

**File reference:** `architecture.md:1`

### Q2. Why is this stronger than a single Kaggle notebook?

A notebook usually ends at model metrics. This repo includes validation, profiling, versioning, feature engineering, model comparison, persistence, API contracts, and observability.

**File reference:** `architecture.md:84`

### Q3. Which module is safest to present as the primary capstone?

Predictive maintenance is the most complete because it has load, validate, clean, profile, balance analysis, leakage-aware feature engineering, model comparison, MLflow logging, and persistence.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/pipeline.py:25`

### Q4. Which modules should be presented as extensions?

Quality inspection, demand forecasting, and inventory optimization show breadth, but should be presented as extensions because some have implementation gaps.

**File reference:** `app/backend/src/app/ml/quality_inspection/pipeline.py:25; app/backend/src/app/ml/demand_forecasting/pipeline.py:28; ml/inventory_optimization/pipeline.py:12`

### Q5. What is the MLOps story in the repo?

Training pipelines produce metrics and artifacts. Predictive maintenance and demand forecasting use MLflow-style logging, while inventory has MLflow registration with local fallback.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/model_store.py:14; ml/inventory_optimization/mlflow_utils.py:1`

### Q6. What is the data-engineering story?

Raw datasets are loaded, normalized, schema-validated, profiled, versioned, cleaned, and transformed before model training.

**File reference:** `app/backend/src/app/data/loaders.py:14`

### Q7. What is the biggest deployment gap?

The API service currently returns deterministic heuristics rather than loading the persisted trained model artifacts.

**File reference:** `app/backend/services.py:14`

### Q8. What is the best anti-leakage design decision?

Predictive maintenance and quality inspection split data before fitting feature engineering statistics, so test-set information is not used during training transformation.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/pipeline.py:45; app/backend/src/app/ml/quality_inspection/pipeline.py:66`

### Q9. What common ML workflow pattern appears across modules?

The pattern is clean data, validate columns, split data, engineer features, train candidate models, compare metrics, choose a winner, and persist/log artifacts.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/pipeline.py:25`

### Q10. How should you honestly explain prototype parts?

Say that training pipelines are implemented, while some serving and extension-module pieces are prototypes that need artifact loading and missing-file fixes.

**File reference:** `app/backend/services.py:14; app/backend/src/app/ml/quality_inspection/pipeline.py:21`

## Data Loading, Validation, Profiling, and Versioning

### Q11. Why support CSV and Parquet?

CSV is common for Kaggle data, while Parquet is efficient for larger columnar data. Supporting both makes ingestion flexible.

**File reference:** `app/backend/src/app/data/loaders.py:39`

### Q12. Why parse configured date columns during loading?

Date parsing is needed for time features, temporal splits, and `.dt` operations in forecasting modules.

**File reference:** `app/backend/src/app/data/loaders.py:41`

### Q13. Why strip whitespace from column names?

Whitespace in CSV headers can cause false schema failures. Stripping headers prevents this common ingestion bug.

**File reference:** `app/backend/src/app/data/loaders.py:49`

### Q14. Why reject unsupported file extensions?

Rejecting unknown formats prevents silent misreads and gives a clear error when the data source is wrong.

**File reference:** `app/backend/src/app/data/loaders.py:45`

### Q15. Why make schema an abstract property?

Every dataset has its own required columns and checks, so each loader must define a schema contract.

**File reference:** `app/backend/src/app/data/loaders.py:21`

### Q16. Why use Pandera strict=True?

It rejects unexpected columns that could cause schema drift or target leakage.

**File reference:** `app/backend/src/app/data/loaders.py:138`

### Q17. Why validate machine_failure as 0 or 1?

The predictive-maintenance model is binary; sigmoid output and binary loss assume two classes.

**File reference:** `app/backend/src/app/data/loaders.py:135`

### Q18. Why range-check temperatures?

Range checks catch impossible or suspicious physical readings before model training.

**File reference:** `app/backend/src/app/data/loaders.py:130`

### Q19. Why check torque and rotational speed as non-negative?

Negative values would not match the physical interpretation of these machine signals.

**File reference:** `app/backend/src/app/data/loaders.py:132`

### Q20. Why does SteelPlatesDatasetLoader use integer class labels?

Quality inspection is multiclass classification, and integer labels work with sparse categorical crossentropy.

**File reference:** `app/backend/src/app/data/loaders.py:168`

### Q21. What mismatch exists in the demand schema?

The shared schema expects `sales`, while the demand pipeline expects `demand`. This should be standardized.

**File reference:** `app/backend/src/app/data/loaders.py:198; app/backend/src/app/ml/demand_forecasting/preprocessing.py:38`

### Q22. Why validate supplier_score between 0 and 1?

It is treated as a normalized supplier-performance signal, so bounded values are safer.

**File reference:** `app/backend/src/app/data/loaders.py:240`

### Q23. Why call Pandera validate with lazy=True?

Lazy validation collects multiple validation errors instead of stopping at the first error.

**File reference:** `app/backend/src/app/data/validation.py:16`

### Q24. Why return ValidationResult instead of only raising?

A structured success/errors object is easier to log, return, and inspect in pipelines.

**File reference:** `app/backend/src/app/data/validation.py:17`

### Q25. What is a limitation of catching only SchemaError?

Some Pandera or runtime errors may not be SchemaError and will propagate directly.

**File reference:** `app/backend/src/app/data/validation.py:18`

### Q26. Why profile row_count and column_count?

They reveal whether loading or cleaning unexpectedly changed dataset size.

**File reference:** `app/backend/src/app/data/profiling.py:11`

### Q27. Why compute missing_percent?

Percentages make missingness comparable across datasets of different sizes.

**File reference:** `app/backend/src/app/data/profiling.py:15`

### Q28. Why compute numeric summary statistics?

Min, max, mean, median, and std quickly reveal outliers, scale, and suspicious constants.

**File reference:** `app/backend/src/app/data/profiling.py:24`

### Q29. Why use std(ddof=0) in profiling?

For dataset profiling, population-style standard deviation is consistent for the observed dataset snapshot.

**File reference:** `app/backend/src/app/data/profiling.py:38`

### Q30. Why store top five values per column?

Top values reveal dominant categories, default values, and possible class imbalance.

**File reference:** `app/backend/src/app/data/profiling.py:44`

### Q31. Why hash the raw file?

The checksum proves whether the underlying dataset content changed between experiments.

**File reference:** `app/backend/src/app/data/versioning.py:13`

### Q32. Why hash the schema separately?

Schema hash detects column/type changes even when file size or row count looks similar.

**File reference:** `app/backend/src/app/data/versioning.py:22`

### Q33. Why combine raw checksum, schema checksum, row count, and column count?

Together they form a reproducible dataset version identity for model lineage.

**File reference:** `app/backend/src/app/data/versioning.py:29`

### Q34. Why hash files in 8192-byte chunks?

Chunking avoids loading large datasets fully into memory while computing checksums.

**File reference:** `app/backend/src/app/data/versioning.py:16`

### Q35. Why store created_at in dataset version info?

It records when the dataset version was generated for audit and experiment traceability.

**File reference:** `app/backend/src/app/data/versioning.py:42`

### Q36. Why does ingest raise on validation failure?

Training on invalid data would make metrics meaningless, so the pipeline fails early.

**File reference:** `app/backend/src/app/data/loaders.py:86`

### Q37. Why provide analyze_missing?

It gives a reusable missing-value report before deciding whether to drop or impute.

**File reference:** `app/backend/src/app/data/loaders.py:54`

### Q38. Why report memory_usage_mb?

It helps decide whether Pandas is sufficient or larger-scale processing is needed.

**File reference:** `app/backend/src/app/data/loaders.py:69`

### Q39. Why is date_columns class-level?

Each dataset declares its own temporal fields while BaseDatasetLoader handles parsing generically.

**File reference:** `app/backend/src/app/data/loaders.py:15`

### Q40. What quality-label validation should be added?

The `class` column should be checked to ensure labels are in the expected seven-class range.

**File reference:** `app/backend/src/app/data/loaders.py:168; app/backend/src/app/ml/quality_inspection/train.py:37`

## Predictive Maintenance

### Q41. What exact ML task does predictive maintenance solve?

It solves binary classification: predict whether `machine_failure` is 0 or 1 from machine sensor features.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/preprocessing.py:18`

### Q42. Why use only five raw numeric sensor columns?

They are direct, numeric, physically meaningful machine signals suitable for sklearn and Keras models.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/preprocessing.py:8`

### Q43. Why does clean_data copy the DataFrame?

It prevents accidental mutation of raw loaded data, which helps debugging and profiling.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/preprocessing.py:22`

### Q44. Why drop duplicate machine records?

Duplicate rows can overweight repeated observations and bias model training.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/preprocessing.py:25`

### Q45. Why convert timestamp to UTC?

UTC avoids timezone ambiguity and prepares the data for future temporal features.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/preprocessing.py:28`

### Q46. Why drop rows with missing feature or target values?

Supervised training needs complete core features and labels. Missing required values make the sample unsafe.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/preprocessing.py:30`

### Q47. Why validate numeric dtypes?

Scikit-learn and Keras expect numeric arrays; object/string columns can break or distort training.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/preprocessing.py:34`

### Q48. What is wrong with the current imbalance_ratio warning?

The code computes class_1/class_0 and warns when >10, but rare failures usually produce a ratio below 1. A majority/minority ratio would be better.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/preprocessing.py:50; app/backend/src/app/ml/predictive_maintenance/pipeline.py:51`

### Q49. Why use stratify=y in split_data?

It preserves the failure/non-failure ratio in both train and test splits.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/preprocessing.py:75`

### Q50. Why use test_size=0.2?

It keeps 80 percent for training and 20 percent for unseen evaluation, a practical tabular default.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/preprocessing.py:67`

### Q51. Why use random_state=42?

It makes splits and model randomness reproducible for defense and reruns.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/preprocessing.py:68`

### Q52. What does temp_delta represent?

It is process_temperature minus air_temperature, capturing thermal load above ambient conditions.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/features.py:49`

### Q53. Is wear_rate a true physical wear rate?

Not exactly. The code divides tool_wear by a training-set minimum speed, so it is a normalized proxy rather than wear per time or revolution.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/features.py:50`

### Q54. Why use max(min_speed, 1.0)?

It prevents division by zero or tiny denominators in ratio features.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/features.py:37`

### Q55. Why does FeatureEngineer have _is_fitted?

It prevents transformation before training-set statistics are captured.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/features.py:46`

### Q56. Why split before feature engineering?

It prevents test-set statistics from leaking into training transformations.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/pipeline.py:45`

### Q57. Why return feature columns in a fixed order?

Training and inference must use the same feature order; otherwise predictions become invalid.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/features.py:59`

### Q58. Why include Logistic Regression?

It provides an interpretable baseline for binary classification.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/train.py:62`

### Q59. Why use solver='liblinear'?

It is a reliable solver for smaller binary classification problems.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/train.py:63`

### Q60. Why use L2 regularization?

L2 discourages large coefficients and reduces overfitting.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/train.py:64`

### Q61. Why set max_iter=1000?

It gives the optimizer enough iterations to converge after scaling.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/train.py:66`

### Q62. Why include Random Forest?

It captures nonlinear thresholds and interactions among machine sensor features.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/train.py:76`

### Q63. Why use 200 trees in Random Forest?

Two hundred trees is a stable default that reduces variance without excessive cost.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/train.py:77`

### Q64. Why cap Random Forest max_depth at 12?

Depth control reduces memorization while allowing nonlinear rules.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/train.py:78`

### Q65. Why include XGBoost?

Boosted trees are highly competitive for structured tabular data and correct previous errors sequentially.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/train.py:90`

### Q66. Why use XGBoost learning_rate=0.1?

The learning rate shrinks each tree contribution and is a common balanced default.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/train.py:93`

### Q67. Why use eval_metric='logloss'?

Log loss evaluates probability quality for binary classification.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/train.py:95`

### Q68. Why does the ANN use Dense(1, sigmoid)?

A single sigmoid neuron outputs the positive-class probability.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/train.py:35`

### Q69. Why use binary_crossentropy?

It is the standard loss for binary labels with sigmoid probability output.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/train.py:40`

### Q70. Why use Dense(64) followed by Dense(32)?

The network learns a wider nonlinear representation and then compresses it before binary output.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/train.py:31`

### Q71. Why use Dropout(0.2) then Dropout(0.1)?

The wider first layer gets stronger regularization; the smaller second layer gets lighter dropout.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/train.py:32`

### Q72. Why use Adam with learning_rate=0.001?

Adam is an adaptive optimizer and 0.001 is a stable default starting point.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/train.py:39`

### Q73. Why use EarlyStopping?

It stops training when validation loss stops improving and restores the best weights.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/train.py:127`

### Q74. Why patience=5 for the PM ANN?

It gives a small binary ANN several chances to improve without training indefinitely.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/train.py:127`

### Q75. Why branch on predict_proba in evaluation?

Sklearn classifiers expose predict_proba, while Keras models return probabilities through predict.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/evaluate.py:39`

### Q76. Why threshold probabilities at 0.5?

It is the default binary cutoff, though production should tune it using business costs.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/evaluate.py:41`

### Q77. Why sort models by F1?

F1 balances precision and recall, which matters for imbalanced failure data.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/evaluate.py:75`

### Q78. Why include ROC-AUC?

ROC-AUC evaluates ranking quality across thresholds, useful when the operating threshold may change.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/evaluate.py:29`

### Q79. Why use zero_division=0?

It avoids metric crashes when a model predicts no positive examples.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/evaluate.py:26`

### Q80. Why log feature_engineer_params?

Ratio features depend on fitted denominators, so these values are needed for reproducibility.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/pipeline.py:84`

### Q81. Why stratify the ANN validation split?

The validation set should preserve class proportions so early stopping is not biased.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/pipeline.py:156`

### Q82. What is odd about _train_models_with_validation?

It accepts X_test and y_test but does not use them, so the signature is misleading.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/pipeline.py:119`

### Q83. Why choose mlflow.keras for Keras models?

Keras and sklearn artifacts need different MLflow serialization flavors.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/model_store.py:33`

### Q84. Why persist the best model locally too?

Local persistence provides a deployment artifact even without querying MLflow.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/model_store.py:40`

### Q85. What is needed before real PM deployment?

The API must load the persisted model and apply the same feature engineering used during training.

**File reference:** `app/backend/services.py:20; app/backend/src/app/ml/predictive_maintenance/model_store.py:40`

## Quality Inspection

### Q86. What ML task does quality inspection solve?

It performs multiclass classification of steel plate defect classes.

**File reference:** `app/backend/src/app/ml/quality_inspection/train.py:37`

### Q87. Why Dense(7, softmax)?

There are seven fault classes, and softmax outputs a probability distribution across them.

**File reference:** `app/backend/src/app/ml/quality_inspection/train.py:37`

### Q88. Why sparse_categorical_crossentropy?

The target labels are integer class IDs rather than one-hot vectors.

**File reference:** `app/backend/src/app/ml/quality_inspection/train.py:41`

### Q89. Why is the quality ANN deeper than PM ANN?

Multiclass defect geometry can need more representational capacity than binary machine failure.

**File reference:** `app/backend/src/app/ml/quality_inspection/train.py:31`

### Q90. Why use dropout 0.3, 0.2, 0.1?

Wider early layers get stronger regularization; smaller later layers get less.

**File reference:** `app/backend/src/app/ml/quality_inspection/train.py:32`

### Q91. Why include DecisionTreeClassifier?

It gives an interpretable rule-based baseline for defect geometry.

**File reference:** `app/backend/src/app/ml/quality_inspection/train.py:58`

### Q92. Why decision tree max_depth=12?

It limits overfitting while allowing moderately complex defect boundaries.

**File reference:** `app/backend/src/app/ml/quality_inspection/train.py:64`

### Q93. Why min_samples_split=5?

It prevents splits based on very tiny sample groups.

**File reference:** `app/backend/src/app/ml/quality_inspection/train.py:65`

### Q94. Why min_samples_leaf=2?

It prevents leaves containing only one sample, reducing memorization.

**File reference:** `app/backend/src/app/ml/quality_inspection/train.py:66`

### Q95. Why use RBF SVM?

The RBF kernel models nonlinear boundaries in scaled geometric feature space.

**File reference:** `app/backend/src/app/ml/quality_inspection/train.py:79`

### Q96. Why SVC probability=True?

The evaluation function expects probabilities; SVC needs probability=True for predict_proba.

**File reference:** `app/backend/src/app/ml/quality_inspection/train.py:82`

### Q97. Why gamma='scale'?

It adapts kernel width based on feature count and variance, making it a safer default.

**File reference:** `app/backend/src/app/ml/quality_inspection/train.py:81`

### Q98. Why quality XGBoost num_class=7?

The model is configured for seven multiclass defect labels.

**File reference:** `app/backend/src/app/ml/quality_inspection/train.py:97`

### Q99. Why eval_metric='mlogloss'?

Multiclass log loss evaluates probability quality across all classes.

**File reference:** `app/backend/src/app/ml/quality_inspection/train.py:98`

### Q100. Why quality XGBoost max_depth=8?

Defect classification may need more complex boundaries than the PM binary task.

**File reference:** `app/backend/src/app/ml/quality_inspection/train.py:95`

### Q101. What does x_range measure?

It measures horizontal defect extent: X_Maximum minus X_Minimum.

**File reference:** `app/backend/src/app/ml/quality_inspection/features.py:62`

### Q102. What does y_range measure?

It measures vertical defect extent: Y_Maximum minus Y_Minimum.

**File reference:** `app/backend/src/app/ml/quality_inspection/features.py:63`

### Q103. Why create area_ratio?

It normalizes defect pixel area relative to the training-set mean.

**File reference:** `app/backend/src/app/ml/quality_inspection/features.py:64`

### Q104. Why create nuclei_density?

It measures Bare_Nuclei per unit Pixel_area, a density-style defect feature.

**File reference:** `app/backend/src/app/ml/quality_inspection/features.py:65`

### Q105. Why replace zero Pixel_area with 1.0?

It prevents division by zero when computing density.

**File reference:** `app/backend/src/app/ml/quality_inspection/features.py:65`

### Q106. Why create shape_ratio?

It distinguishes elongated and compact defect shapes by comparing x_range and y_range.

**File reference:** `app/backend/src/app/ml/quality_inspection/features.py:66`

### Q107. Why store pixel_area_mean?

It lets area_ratio use training-set statistics only, avoiding test leakage.

**File reference:** `app/backend/src/app/ml/quality_inspection/features.py:45`

### Q108. Why is pixel_area_std suspicious?

It is stored during fit but not used in transform, so it may be leftover or planned future work.

**File reference:** `app/backend/src/app/ml/quality_inspection/features.py:46`

### Q109. Why split before quality feature engineering?

It avoids leaking test geometry statistics into training transformations.

**File reference:** `app/backend/src/app/ml/quality_inspection/pipeline.py:66`

### Q110. What is weak about the quality ANN validation split?

It slices the last 20 percent of the training data rather than doing a stratified split.

**File reference:** `app/backend/src/app/ml/quality_inspection/pipeline.py:78`

### Q111. Why compute macro metrics?

Macro metrics weight each defect class equally and reveal minority-class performance.

**File reference:** `app/backend/src/app/ml/quality_inspection/evaluate.py:30`

### Q112. Why compute weighted metrics?

Weighted metrics account for class frequency and summarize overall multiclass performance.

**File reference:** `app/backend/src/app/ml/quality_inspection/evaluate.py:31`

### Q113. Why sort by f1_weighted?

It balances precision and recall while respecting class support.

**File reference:** `app/backend/src/app/ml/quality_inspection/evaluate.py:86`

### Q114. How does ANN prediction become a class?

The code uses np.argmax over softmax probabilities to select the most likely class.

**File reference:** `app/backend/src/app/ml/quality_inspection/evaluate.py:55`

### Q115. What serious quality pipeline gap exists?

It imports app.ml.quality_inspection.model_store, but that file is missing in the repo.

**File reference:** `app/backend/src/app/ml/quality_inspection/pipeline.py:21`

### Q116. What label validation should be added?

The `class` label should be checked to fall within the expected seven class IDs.

**File reference:** `app/backend/src/app/data/loaders.py:168`

## Demand Forecasting

### Q117. What ML task is demand forecasting?

It is regression/time-series forecasting of numeric demand.

**File reference:** `app/backend/src/app/ml/demand_forecasting/train.py:20`

### Q118. Why include Linear Regression?

It is a simple baseline for engineered lag, rolling, and calendar features.

**File reference:** `app/backend/src/app/ml/demand_forecasting/train.py:20`

### Q119. Why include RandomForestRegressor?

It captures nonlinear interactions among lag, rolling, store/item, and calendar features.

**File reference:** `app/backend/src/app/ml/demand_forecasting/train.py:33`

### Q120. Why Random Forest max_depth=20?

Demand patterns can be complex, so the forest is allowed more depth than PM while still capped.

**File reference:** `app/backend/src/app/ml/demand_forecasting/train.py:39`

### Q121. Why min_samples_split=5 and min_samples_leaf=2?

They reduce overfitting by preventing tiny branches and single-record leaves.

**File reference:** `app/backend/src/app/ml/demand_forecasting/train.py:40`

### Q122. Why include XGBRegressor?

Boosted trees are strong for tabular forecasting features.

**File reference:** `app/backend/src/app/ml/demand_forecasting/train.py:53`

### Q123. Why objective='reg:squarederror'?

The target is continuous demand, so squared-error regression is appropriate.

**File reference:** `app/backend/src/app/ml/demand_forecasting/train.py:62`

### Q124. Why subsample=0.8 and colsample_bytree=0.8?

They add row and feature sampling to reduce overfitting in boosting.

**File reference:** `app/backend/src/app/ml/demand_forecasting/train.py:60`

### Q125. Why include LSTM?

LSTM can learn temporal dependencies over ordered sequences.

**File reference:** `app/backend/src/app/ml/demand_forecasting/train.py:69`

### Q126. Why reshape LSTM input to samples x lookback x 1?

Keras LSTM expects 3D sequence input: samples, timesteps, features.

**File reference:** `app/backend/src/app/ml/demand_forecasting/train.py:112`

### Q127. Why first LSTM return_sequences=True?

The second LSTM layer needs a sequence from the first layer.

**File reference:** `app/backend/src/app/ml/demand_forecasting/train.py:78`

### Q128. Why second LSTM return_sequences=False?

It outputs one final representation before Dense regression layers.

**File reference:** `app/backend/src/app/ml/demand_forecasting/train.py:80`

### Q129. Why Dense(1) without activation?

Demand is a continuous numeric target, not a probability.

**File reference:** `app/backend/src/app/ml/demand_forecasting/train.py:84`

### Q130. Why train LSTM with MSE and MAE?

MSE penalizes large errors; MAE gives an interpretable average absolute error.

**File reference:** `app/backend/src/app/ml/demand_forecasting/train.py:89`

### Q131. Why lag windows 7, 14, and 30?

They represent weekly, two-week, and monthly historical demand patterns.

**File reference:** `app/backend/src/app/ml/demand_forecasting/features.py:10`

### Q132. Why rolling windows 7, 14, and 30?

They summarize recent trend and volatility at useful retail horizons.

**File reference:** `app/backend/src/app/ml/demand_forecasting/features.py:11`

### Q133. Why use series.shift(lag)?

It creates past-demand features without using future demand.

**File reference:** `app/backend/src/app/ml/demand_forecasting/features.py:43`

### Q134. Why rolling std fillna(0)?

The first rolling observations may lack enough values, so zero indicates no observed variation yet.

**File reference:** `app/backend/src/app/ml/demand_forecasting/features.py:57`

### Q135. Why create day_of_week?

It captures weekly seasonality in demand.

**File reference:** `app/backend/src/app/ml/demand_forecasting/features.py:71`

### Q136. Why create is_weekend?

Weekend demand can differ from weekday demand.

**File reference:** `app/backend/src/app/ml/demand_forecasting/features.py:75`

### Q137. Why fit demand_mean and demand_std?

They are logged training statistics, though not currently used in transform.

**File reference:** `app/backend/src/app/ml/demand_forecasting/features.py:30`

### Q138. What is a limitation of transforming val/test separately?

Early validation/test rows lose historical context from previous splits, which can weaken or misalign lag features.

**File reference:** `app/backend/src/app/ml/demand_forecasting/pipeline.py:98`

### Q139. Why lookback=30?

The LSTM uses about one month of history for each sequence.

**File reference:** `app/backend/src/app/ml/demand_forecasting/pipeline.py:34`

### Q140. Why lookahead=1?

The sequence generator predicts the next time step.

**File reference:** `app/backend/src/app/ml/demand_forecasting/features.py:128`

### Q141. What target index does create_sequences use?

It uses i + lookback + lookahead - 1, which is the next target when lookahead is 1.

**File reference:** `app/backend/src/app/ml/demand_forecasting/features.py:151`

### Q142. Why drop duplicates by date, store, item?

There should be one demand record per store-item-date key.

**File reference:** `app/backend/src/app/ml/demand_forecasting/preprocessing.py:25`

### Q143. Why warn rather than fail on negative demand?

The code treats negative demand as suspicious but not fatal; production should likely reject or correct it.

**File reference:** `app/backend/src/app/ml/demand_forecasting/preprocessing.py:48`

### Q144. Why preserve time order in split_time_series?

Random splits would leak future patterns into training.

**File reference:** `app/backend/src/app/ml/demand_forecasting/preprocessing.py:57`

### Q145. Why require split sizes to sum to 1?

The entire time series should be partitioned cleanly into train, validation, and test.

**File reference:** `app/backend/src/app/ml/demand_forecasting/preprocessing.py:80`

### Q146. Why aggregate by date, store, and item?

It establishes consistent forecasting granularity.

**File reference:** `app/backend/src/app/ml/demand_forecasting/preprocessing.py:100`

### Q147. Why allow optional store_id and item_id filters?

They support focused experiments for a single store or item.

**File reference:** `app/backend/src/app/ml/demand_forecasting/pipeline.py:76`

### Q148. What scaling inconsistency exists in demand pipeline?

External scaled arrays are used for LSTM, while sklearn pipelines train on unscaled X_train because they already contain StandardScaler.

**File reference:** `app/backend/src/app/ml/demand_forecasting/pipeline.py:119`

### Q149. What bug exists in demand predict_model?

hasattr(model, 'predict') is true for both sklearn and Keras, so the intended Keras else branch is unreachable.

**File reference:** `app/backend/src/app/ml/demand_forecasting/evaluate.py:43`

### Q150. Why trim y_true and y_pred to the same length?

LSTM sequence predictions can be shorter than raw targets, but trimming can hide alignment mistakes.

**File reference:** `app/backend/src/app/ml/demand_forecasting/evaluate.py:24`

### Q151. Why add 1e-6 in MAPE?

It prevents division by zero when true demand is zero.

**File reference:** `app/backend/src/app/ml/demand_forecasting/evaluate.py:30`

### Q152. Why sort demand models by R2?

R2 ranks explained variance, but it should be reviewed with RMSE and MAE.

**File reference:** `app/backend/src/app/ml/demand_forecasting/pipeline.py:162`

### Q153. What is risky about Keras model detection in ModelStore?

Keras models usually have both predict and fit, so the current check can misclassify them as sklearn objects.

**File reference:** `app/backend/src/app/ml/demand_forecasting/model_store.py:77`

### Q154. Why save sklearn models with joblib?

Joblib serializes sklearn pipelines efficiently for local artifact storage.

**File reference:** `app/backend/src/app/ml/demand_forecasting/model_store.py:86`

### Q155. What demand schema mismatch must be fixed?

Shared validation expects `sales`, while this pipeline expects `demand`.

**File reference:** `app/backend/src/app/data/loaders.py:198; app/backend/src/app/ml/demand_forecasting/preprocessing.py:38`

## Inventory Optimization

### Q156. What does inventory optimization predict?

The standalone module trains regressors to predict demand from inventory/time-series features.

**File reference:** `ml/inventory_optimization/pipeline.py:40`

### Q157. Why include Linear Regression?

It is a transparent baseline for demand prediction.

**File reference:** `ml/inventory_optimization/train.py:10`

### Q158. Why include RandomForestRegressor?

It learns nonlinear relations among stock, on-order values, lead time, lags, and calendar features.

**File reference:** `ml/inventory_optimization/train.py:19`

### Q159. Why include XGBRegressor?

Boosted trees are strong for tabular demand prediction.

**File reference:** `ml/inventory_optimization/train.py:28`

### Q160. Why objective='reg:squarederror'?

The target is numeric demand, so squared-error regression fits the task.

**File reference:** `ml/inventory_optimization/train.py:24`

### Q161. Why allow custom XGBoost params?

It supports tuning without rewriting the pipeline builder.

**File reference:** `ml/inventory_optimization/train.py:23`

### Q162. Why return models as a dictionary?

It simplifies evaluation, model selection, logging, and registration by model name.

**File reference:** `ml/inventory_optimization/train.py:33`

### Q163. Why use joblib in save_model?

It is a standard way to persist sklearn pipelines.

**File reference:** `ml/inventory_optimization/train.py:52`

### Q164. Why lags 1, 7, and 14?

They capture immediate, weekly, and two-week demand recurrence.

**File reference:** `ml/inventory_optimization/features.py:13`

### Q165. Why rolling windows 7 and 30?

They capture weekly and monthly demand trends and volatility.

**File reference:** `ml/inventory_optimization/features.py:13`

### Q166. Why is fit a placeholder?

The inventory feature engineer does not learn statistics currently, but fit keeps the API consistent.

**File reference:** `ml/inventory_optimization/features.py:18`

### Q167. Why create fallback dates if date is missing?

It lets temporal features be generated, but it is risky because synthetic dates may not reflect reality.

**File reference:** `ml/inventory_optimization/features.py:44`

### Q168. Why drop NaNs after lag creation?

Lag features produce missing early rows; complete rows are needed for model training.

**File reference:** `ml/inventory_optimization/features.py:54`

### Q169. What is wrong with clean_data conversion order?

It drops NaNs before pd.to_numeric, so invalid numeric strings converted to NaN may remain.

**File reference:** `ml/inventory_optimization/preprocessing.py:9`

### Q170. Why aggregate by warehouse, sku, date?

Inventory decisions are made at SKU-warehouse-date granularity.

**File reference:** `ml/inventory_optimization/preprocessing.py:21`

### Q171. Why sum numeric fields during aggregation?

Multiple records for the same SKU/warehouse/date need one aggregate value.

**File reference:** `ml/inventory_optimization/preprocessing.py:31`

### Q172. Why use temporal split?

Demand forecasting should train on earlier rows and test on later rows.

**File reference:** `ml/inventory_optimization/pipeline.py:27`

### Q173. What is df_val used for?

It is created but not used, which is an implementation gap for validation or tuning.

**File reference:** `ml/inventory_optimization/pipeline.py:33`

### Q174. Why exclude date, warehouse, sku, demand from features?

IDs/date are not directly numeric model inputs here, and demand is the target.

**File reference:** `ml/inventory_optimization/pipeline.py:40`

### Q175. Why sort inventory models by R2?

The code selects the model explaining the most target variance on the test set.

**File reference:** `ml/inventory_optimization/evaluate.py:18`

### Q176. Why compute both RMSE and MAE?

RMSE emphasizes large errors; MAE is interpretable in demand units.

**File reference:** `ml/inventory_optimization/evaluate.py:7`

### Q177. Why have MLflow fallback logic?

The pipeline still works when MLflow is unavailable by saving local models and metadata.

**File reference:** `ml/inventory_optimization/mlflow_utils.py:11`

### Q178. Why log n_features?

It documents the input dimensionality expected by the model.

**File reference:** `ml/inventory_optimization/mlflow_utils.py:57`

### Q179. Why create registered model names with a prefix?

A prefix prevents registry name collisions and groups inventory models.

**File reference:** `ml/inventory_optimization/mlflow_utils.py:71`

### Q180. Why transition versions to Staging?

Staging marks trained candidates that are not yet production models.

**File reference:** `ml/inventory_optimization/mlflow_utils.py:79`

### Q181. What does promote_model do?

It transitions an MLflow model version to a target stage such as Production.

**File reference:** `ml/inventory_optimization/mlflow_utils.py:111`

### Q182. What is risky about archive_existing_versions=False for Staging?

Multiple models can remain in Staging, which can confuse deployment decisions.

**File reference:** `ml/inventory_optimization/mlflow_utils.py:79`

### Q183. What packaging inconsistency exists?

Inventory optimization lives under top-level ml/, while other modules live under app/backend/src/app/ml.

**File reference:** `ml/inventory_optimization/pipeline.py:1`

## API, Serving, and Observability

### Q184. What does predict_maintenance currently serve?

It serves a tanh-based average-sensor heuristic, not the trained predictive-maintenance model.

**File reference:** `app/backend/services.py:20`

### Q185. Why use tanh in the maintenance heuristic?

tanh bounds increasing sensor magnitude into a stable risk-like score, but it is not calibrated probability.

**File reference:** `app/backend/services.py:27`

### Q186. Why set eta_hours=24 above score 0.7?

It is a simple business-rule placeholder for high-risk maintenance urgency.

**File reference:** `app/backend/services.py:28`

### Q187. What is risky about averaging all sensor readings?

Different sensor scales get mixed, so a large-scale sensor can dominate the score.

**File reference:** `app/backend/services.py:23`

### Q188. What does predict_quality currently do?

It computes a pass-rate heuristic from metric variation, not a trained quality classifier.

**File reference:** `app/backend/services.py:43`

### Q189. Why add 1e-6 to quality mean?

It prevents division by zero in std/mean.

**File reference:** `app/backend/services.py:49`

### Q190. Why compute defects_expected from pass_rate?

It turns a pass-rate heuristic into a rough expected defect count for API output.

**File reference:** `app/backend/services.py:50`

### Q191. What does forecast_demand currently serve?

It repeats the average of the last seven demand points across the requested horizon.

**File reference:** `app/backend/services.py:62`

### Q192. Why require at least seven demand history points?

The naive forecast uses a last-seven average, so a week of history is required.

**File reference:** `app/backend/schemas.py:47`

### Q193. What does assess_inventory_risk compute?

It compares summed future demand against current stock and recommends reorder quantity if short.

**File reference:** `app/backend/services.py:81`

### Q194. Why add 1e-6 in inventory risk denominator?

It prevents division by zero when future demand is zero.

**File reference:** `app/backend/services.py:84`

### Q195. Why use max(0.0, recommended_order)?

It prevents negative order recommendations when stock is sufficient.

**File reference:** `app/backend/services.py:86`

### Q196. Why record model latency?

Latency monitoring helps detect slow inference paths.

**File reference:** `app/backend/services.py:33; app/backend/metrics.py:21`

### Q197. Why increment prediction volume?

Prediction counts show usage per model or heuristic.

**File reference:** `app/backend/services.py:34; app/backend/metrics.py:26`

### Q198. Why gracefully handle missing prometheus_client?

The app can run without observability dependencies but still emit metrics when available.

**File reference:** `app/backend/metrics.py:6`

### Q199. What does timed_model provide?

It is a context manager that records model latency for a code block.

**File reference:** `app/backend/metrics.py:36`

### Q200. Why bound failure_risk and risk_score?

Risk outputs should stay between 0 and 1; Pydantic enforces that contract.

**File reference:** `app/backend/schemas.py:19; app/backend/schemas.py:65`

### Q201. Why cap forecast horizon at 90?

It prevents unreasonable long-horizon requests from weak or prototype forecasting logic.

**File reference:** `app/backend/schemas.py:48`

### Q202. Why include explanation in MaintenanceResponse?

Operators need to know whether the result came from a heuristic or model.

**File reference:** `app/backend/schemas.py:21`

### Q203. What is the biggest serving improvement?

Load persisted model artifacts and apply the same feature engineering at inference time.

**File reference:** `app/backend/services.py:14; app/backend/src/app/ml/predictive_maintenance/model_store.py:40`

## Algorithms, Metrics, and Defense Concepts

### Q204. How does binary classification differ from multiclass classification here?

PM uses one sigmoid output and binary crossentropy; QI uses seven softmax outputs and sparse categorical crossentropy.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/train.py:35; app/backend/src/app/ml/quality_inspection/train.py:37`

### Q205. How do classification and regression metrics differ?

Classification uses accuracy/precision/recall/F1/ROC-AUC; regression uses RMSE/MAE/MAPE/R2.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/evaluate.py:24; app/backend/src/app/ml/demand_forecasting/evaluate.py:27`

### Q206. What is precision?

Precision is TP/(TP+FP), measuring how many predicted positives are correct.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/evaluate.py:26`

### Q207. What is recall?

Recall is TP/(TP+FN), measuring how many actual positives are caught.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/evaluate.py:27`

### Q208. What is F1?

F1 is 2PR/(P+R), balancing precision and recall.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/evaluate.py:28`

### Q209. What is RMSE?

RMSE is sqrt(mean squared error), emphasizing large forecast errors.

**File reference:** `app/backend/src/app/ml/demand_forecasting/evaluate.py:27`

### Q210. What is MAE?

MAE is average absolute error in the target's unit.

**File reference:** `app/backend/src/app/ml/demand_forecasting/evaluate.py:28`

### Q211. What is MAPE's weakness?

MAPE is unstable when true demand is zero or very small.

**File reference:** `app/backend/src/app/ml/demand_forecasting/evaluate.py:30`

### Q212. What is R2?

R2 measures explained variance; it can be negative for poor models.

**File reference:** `app/backend/src/app/ml/demand_forecasting/evaluate.py:31`

### Q213. Why scale features before SVM?

RBF SVM uses distances, so unscaled features distort similarity.

**File reference:** `app/backend/src/app/ml/quality_inspection/train.py:75`

### Q214. Why scale features for neural networks?

Gradient descent trains more reliably when feature magnitudes are comparable.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/train.py:59`

### Q215. Why do tree models need scaling less?

Trees split by thresholds and are not distance/gradient based, though pipelines use scaling for consistency.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/train.py:73`

### Q216. What is sigmoid?

sigmoid(z)=1/(1+exp(-z)), mapping a score to a probability.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/train.py:35`

### Q217. What is softmax?

Softmax normalizes class scores into probabilities that sum to one.

**File reference:** `app/backend/src/app/ml/quality_inspection/train.py:37`

### Q218. What is binary crossentropy?

It penalizes difference between binary labels and predicted probabilities.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/train.py:40`

### Q219. What is sparse categorical crossentropy?

It is multiclass crossentropy for integer labels.

**File reference:** `app/backend/src/app/ml/quality_inspection/train.py:41`

### Q220. What is MSE loss?

It averages squared regression errors and penalizes large misses.

**File reference:** `app/backend/src/app/ml/demand_forecasting/train.py:89`

### Q221. Why compare multiple algorithms?

Comparison prevents assuming one model family is best and makes selection evidence-based.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/train.py:47`

### Q222. Why not use only ANN?

ANNs are not always best for small tabular data; tree and linear models are often stronger or more interpretable.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/train.py:20`

### Q223. Why not use only XGBoost?

XGBoost is strong but less interpretable; baselines prove whether complexity is justified.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/train.py:56`

### Q224. How is overfitting controlled?

Depth limits, min sample limits, dropout, early stopping, train/test splits, and validation sets are used.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/train.py:78; app/backend/src/app/ml/quality_inspection/train.py:65`

### Q225. How is reproducibility handled?

random_state=42, MLflow tracking, and dataset versioning support reproducible experiments.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/train.py:47; app/backend/src/app/data/versioning.py:29`

### Q226. What is bagging versus boosting?

Random Forest trains many trees independently; XGBoost adds trees sequentially to correct errors.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/train.py:76; app/backend/src/app/ml/predictive_maintenance/train.py:90`

### Q227. Why are lag features leakage-sensitive?

If lag construction accidentally uses future values, the model sees the answer.

**File reference:** `app/backend/src/app/ml/demand_forecasting/features.py:43`

### Q228. Why can rolling features leak?

If computed with future-inclusive windows or wrong split order, they can include test-period information.

**File reference:** `app/backend/src/app/ml/demand_forecasting/features.py:56`

### Q229. How should limitations be defended?

Acknowledge them directly, show implemented parts, and explain concrete next fixes.

**File reference:** `app/backend/src/app/ml/quality_inspection/pipeline.py:21; app/backend/services.py:14`

## Known Issues and Improvements

### Q230. What is the most important quality-inspection bug?

The pipeline imports a missing model_store module, so it cannot complete until that file is added.

**File reference:** `app/backend/src/app/ml/quality_inspection/pipeline.py:21`

### Q231. What is the most important demand-forecasting bug?

Keras model detection in evaluate.py and model_store.py is flawed because both sklearn and Keras have predict.

**File reference:** `app/backend/src/app/ml/demand_forecasting/evaluate.py:43`

### Q232. What is the most important PM imbalance fix?

Use majority/minority imbalance ratio and add class_weight, resampling, or threshold tuning.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/preprocessing.py:50`

### Q233. What is the most important serving fix?

Replace heuristics with actual persisted model loading and matching preprocessing.

**File reference:** `app/backend/services.py:14`

### Q234. What tests are missing?

End-to-end tests for quality, demand, and inventory pipelines are missing compared with predictive maintenance.

**File reference:** `app/backend/src/app/tests/test_predictive_maintenance_pipeline.py:7`

### Q235. What feature persistence is missing?

Feature-engineering state should be saved with models so inference can reproduce training transformations.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/pipeline.py:84`

### Q236. What explainability improvement would help?

Add feature importance or SHAP explanations for tree models and XGBoost.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/train.py:90`

### Q237. What PM metric improvement is needed?

Add confusion matrix, PR-AUC, and threshold-specific precision/recall.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/evaluate.py:17`

### Q238. What demand validation improvement is needed?

Use rolling-origin backtesting instead of one static split.

**File reference:** `app/backend/src/app/ml/demand_forecasting/preprocessing.py:57`

### Q239. What inventory cleaning fix is needed?

Convert numeric columns before dropping NaNs so coerced invalid values are removed.

**File reference:** `ml/inventory_optimization/preprocessing.py:15`

### Q240. What MLflow consistency improvement is needed?

Use shared app settings for MLflow tracking across all modules.

**File reference:** `app/backend/src/app/core/config.py:12; app/backend/src/app/ml/demand_forecasting/model_store.py:17`

### Q241. What packaging improvement is needed?

Move inventory optimization under the same app ML namespace or package it explicitly.

**File reference:** `ml/inventory_optimization/pipeline.py:1`

### Q242. What schema improvement is needed?

Fix demand sales/demand naming and constrain quality class labels.

**File reference:** `app/backend/src/app/data/loaders.py:198; app/backend/src/app/data/loaders.py:168`

### Q243. What UI/API integration improvement is needed?

Expose model version, confidence, and explanation metadata to frontend responses.

**File reference:** `app/backend/schemas.py:17`

### Q244. What is the safest way to phrase the project status?

Say predictive maintenance is the main implemented pipeline, while other modules are staged extensions with known fixes.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/pipeline.py:25`

## Additional Implementation Questions

### Q245. Why keep PM NUMERIC_COLUMNS as a constant?

It centralizes the predictive feature contract for cleaning, validation, and splitting.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/preprocessing.py:8`

### Q246. Why define TARGET_COLUMN?

It avoids hardcoding the target name throughout preprocessing.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/preprocessing.py:18`

### Q247. Why keep QI NUMERIC_COLUMNS separate from PM columns?

Quality inspection uses geometric defect features rather than machine sensor features.

**File reference:** `app/backend/src/app/ml/quality_inspection/preprocessing.py:8`

### Q248. What happens if lag windows are too large?

Too many early rows are dropped and less data remains for training.

**File reference:** `app/backend/src/app/ml/demand_forecasting/features.py:10`

### Q249. What happens if rolling windows are too short?

The model may learn noisy local patterns instead of stable trends.

**File reference:** `app/backend/src/app/ml/demand_forecasting/features.py:11`

### Q250. Why can rolling std help inventory?

Demand volatility influences safety stock and stockout risk.

**File reference:** `ml/inventory_optimization/features.py:29`

### Q251. Why log model_version?

It gives a human-readable release marker for training runs.

**File reference:** `app/backend/src/app/ml/demand_forecasting/model_store.py:42`

### Q252. Why log dataset name?

Metrics only make sense relative to the dataset used.

**File reference:** `app/backend/src/app/ml/demand_forecasting/model_store.py:43`

### Q253. Why log feature_columns?

They document model input schema for reproducible inference.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/pipeline.py:93`

### Q254. Why log class_balance?

It explains metric choice and helps compare runs with different label distributions.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/pipeline.py:94`

### Q255. Why is .h5 persistence imperfect?

It works, but newer Keras formats may preserve metadata more cleanly.

**File reference:** `app/backend/src/app/ml/demand_forecasting/model_store.py:79`

### Q256. What is a risk of joblib pickle artifacts?

They are dependency-sensitive and should not be loaded from untrusted sources.

**File reference:** `app/backend/src/app/ml/demand_forecasting/model_store.py:86`

### Q257. What does SVM C=1.0 control?

C controls regularization strength; 1.0 is a balanced default.

**File reference:** `app/backend/src/app/ml/quality_inspection/train.py:80`

### Q258. Why use XGBoost verbosity=0 in demand?

It keeps automated training logs clean.

**File reference:** `app/backend/src/app/ml/demand_forecasting/train.py:65`

### Q259. Why use n_jobs=-1?

It uses all CPU cores where supported to reduce training time.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/train.py:97`

### Q260. Why train neural nets with verbose=0?

It keeps pipeline logs concise during automated runs.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/train.py:137`

### Q261. Why log len(history.epoch)?

It shows how many epochs were actually trained before early stopping.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/train.py:139`

### Q262. What can go wrong with int(0.2*n_train)?

Small datasets can produce an empty validation split.

**File reference:** `app/backend/src/app/ml/quality_inspection/pipeline.py:78`

### Q263. What can go wrong if test data is shorter than lookback?

The LSTM sequence generator returns no test sequences.

**File reference:** `app/backend/src/app/ml/demand_forecasting/features.py:145`

### Q264. Why raise if inventory df and csv_path are both missing?

The pipeline needs a data source and should fail clearly without one.

**File reference:** `ml/inventory_optimization/pipeline.py:17`

### Q265. Why raise if no inventory grouping columns exist?

Aggregation cannot define SKU/warehouse/date granularity without grouping fields.

**File reference:** `ml/inventory_optimization/preprocessing.py:26`

### Q266. Why track API errors?

Error counters help monitor endpoint reliability.

**File reference:** `app/backend/metrics.py:16`

### Q267. Why use a singleton PredictionService?

It avoids recreating service state repeatedly, though production may use stronger dependency management.

**File reference:** `app/backend/services.py:98`

### Q268. Why use conlist for demand history?

It enforces minimum history length at schema validation time.

**File reference:** `app/backend/schemas.py:47`

### Q269. Why use conint for horizon?

It rejects zero, negative, or too-large forecast horizons.

**File reference:** `app/backend/schemas.py:48`

## Practical Viva Scenarios

### Q270. How would you test feature order stability? (applied follow-up 1)

Assert get_feature_columns exactly matches the columns used for model fit and inference. For this follow-up, also explain what code you would modify and how you would verify the change.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/features.py:59`

### Q271. How would you improve PM class imbalance? (applied follow-up 1)

Use class weights, threshold tuning, resampling, and PR-AUC analysis. For this follow-up, also explain what code you would modify and how you would verify the change.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/preprocessing.py:50`

### Q272. How would you choose maintenance recall versus precision? (applied follow-up 1)

Use business costs: missed failures favor recall; costly false alarms favor precision. For this follow-up, also explain what code you would modify and how you would verify the change.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/evaluate.py:26`

### Q273. How would you make ANN results more reproducible? (applied follow-up 1)

Set Python, NumPy, and TensorFlow seeds and document nondeterministic hardware behavior. For this follow-up, also explain what code you would modify and how you would verify the change.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/train.py:20`

### Q274. How would you tune XGBoost? (applied follow-up 1)

Search n_estimators, max_depth, learning_rate, subsample, colsample_bytree, and regularization. For this follow-up, also explain what code you would modify and how you would verify the change.

**File reference:** `app/backend/src/app/ml/demand_forecasting/train.py:53`

### Q275. How would you tune Random Forest? (applied follow-up 1)

Tune n_estimators, max_depth, min_samples_split, min_samples_leaf, and max_features. For this follow-up, also explain what code you would modify and how you would verify the change.

**File reference:** `app/backend/src/app/ml/demand_forecasting/train.py:33`

### Q276. How would you tune ANN architecture? (applied follow-up 1)

Tune layer sizes, dropout rates, learning rate, batch size, patience, and epochs. For this follow-up, also explain what code you would modify and how you would verify the change.

**File reference:** `app/backend/src/app/ml/quality_inspection/train.py:20`

### Q277. How would you prove MLflow logging works? (applied follow-up 1)

Run a pipeline and show metrics, params, artifacts, and comparison JSON in MLflow UI. For this follow-up, also explain what code you would modify and how you would verify the change.

**File reference:** `app/backend/src/app/ml/demand_forecasting/model_store.py:41`

### Q278. How would you connect PM training to API inference? (applied follow-up 1)

Load the persisted model, reconstruct features, apply saved feature parameters, and call predict_proba. For this follow-up, also explain what code you would modify and how you would verify the change.

**File reference:** `app/backend/services.py:20`

### Q279. How would you avoid overclaiming deep learning? (applied follow-up 1)

Say ANN/LSTM are candidate models and final selection depends on evidence, not model hype. For this follow-up, also explain what code you would modify and how you would verify the change.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/evaluate.py:75`

### Q280. How would you explain why accuracy is misleading? (applied follow-up 1)

A rare-failure dataset can have high accuracy by always predicting no failure. For this follow-up, also explain what code you would modify and how you would verify the change.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/evaluate.py:25`

### Q281. How would you handle drift? (applied follow-up 1)

Monitor feature distributions and live performance, then retrain when drift is detected. For this follow-up, also explain what code you would modify and how you would verify the change.

**File reference:** `architecture.md:174`

### Q282. How would you add explainability? (applied follow-up 1)

Use feature importance and SHAP to show which inputs drive predictions. For this follow-up, also explain what code you would modify and how you would verify the change.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/train.py:76`

### Q283. How would you validate demand forecasts visually? (applied follow-up 1)

Plot actual versus predicted demand and inspect residuals by date, store, and item. For this follow-up, also explain what code you would modify and how you would verify the change.

**File reference:** `app/backend/src/app/ml/demand_forecasting/evaluate.py:94`

### Q284. How would you validate quality classifier errors? (applied follow-up 1)

Use a confusion matrix and class-wise recall to inspect confused defect classes. For this follow-up, also explain what code you would modify and how you would verify the change.

**File reference:** `app/backend/src/app/ml/quality_inspection/evaluate.py:29`

### Q285. How would you choose the PM probability threshold? (applied follow-up 1)

Use validation probabilities and a cost matrix for downtime, inspection cost, and missed failures. For this follow-up, also explain what code you would modify and how you would verify the change.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/evaluate.py:41`

### Q286. How would you handle missing sensor readings in production? (applied follow-up 1)

Validate requests, reject critical missing fields, or use justified imputation. For this follow-up, also explain what code you would modify and how you would verify the change.

**File reference:** `app/backend/schemas.py:7`

### Q287. How would you make inventory recommendations safer? (applied follow-up 1)

Add uncertainty, lead time, service-level targets, and safety stock logic. For this follow-up, also explain what code you would modify and how you would verify the change.

**File reference:** `app/backend/services.py:81`

### Q288. How would you make demand validation stronger? (applied follow-up 1)

Use backtesting across multiple rolling forecast origins. For this follow-up, also explain what code you would modify and how you would verify the change.

**File reference:** `app/backend/src/app/ml/demand_forecasting/preprocessing.py:57`

### Q289. How would you make model selection fairer? (applied follow-up 1)

Use the same train/test partitions and compare models on metrics aligned to business cost. For this follow-up, also explain what code you would modify and how you would verify the change.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/evaluate.py:48`

### Q290. How would you test feature order stability? (applied follow-up 2)

Assert get_feature_columns exactly matches the columns used for model fit and inference. For this follow-up, also explain what code you would modify and how you would verify the change.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/features.py:59`

### Q291. How would you improve PM class imbalance? (applied follow-up 2)

Use class weights, threshold tuning, resampling, and PR-AUC analysis. For this follow-up, also explain what code you would modify and how you would verify the change.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/preprocessing.py:50`

### Q292. How would you choose maintenance recall versus precision? (applied follow-up 2)

Use business costs: missed failures favor recall; costly false alarms favor precision. For this follow-up, also explain what code you would modify and how you would verify the change.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/evaluate.py:26`

### Q293. How would you make ANN results more reproducible? (applied follow-up 2)

Set Python, NumPy, and TensorFlow seeds and document nondeterministic hardware behavior. For this follow-up, also explain what code you would modify and how you would verify the change.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/train.py:20`

### Q294. How would you tune XGBoost? (applied follow-up 2)

Search n_estimators, max_depth, learning_rate, subsample, colsample_bytree, and regularization. For this follow-up, also explain what code you would modify and how you would verify the change.

**File reference:** `app/backend/src/app/ml/demand_forecasting/train.py:53`

### Q295. How would you tune Random Forest? (applied follow-up 2)

Tune n_estimators, max_depth, min_samples_split, min_samples_leaf, and max_features. For this follow-up, also explain what code you would modify and how you would verify the change.

**File reference:** `app/backend/src/app/ml/demand_forecasting/train.py:33`

### Q296. How would you tune ANN architecture? (applied follow-up 2)

Tune layer sizes, dropout rates, learning rate, batch size, patience, and epochs. For this follow-up, also explain what code you would modify and how you would verify the change.

**File reference:** `app/backend/src/app/ml/quality_inspection/train.py:20`

### Q297. How would you prove MLflow logging works? (applied follow-up 2)

Run a pipeline and show metrics, params, artifacts, and comparison JSON in MLflow UI. For this follow-up, also explain what code you would modify and how you would verify the change.

**File reference:** `app/backend/src/app/ml/demand_forecasting/model_store.py:41`

### Q298. How would you connect PM training to API inference? (applied follow-up 2)

Load the persisted model, reconstruct features, apply saved feature parameters, and call predict_proba. For this follow-up, also explain what code you would modify and how you would verify the change.

**File reference:** `app/backend/services.py:20`

### Q299. How would you avoid overclaiming deep learning? (applied follow-up 2)

Say ANN/LSTM are candidate models and final selection depends on evidence, not model hype. For this follow-up, also explain what code you would modify and how you would verify the change.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/evaluate.py:75`

### Q300. How would you explain why accuracy is misleading? (applied follow-up 2)

A rare-failure dataset can have high accuracy by always predicting no failure. For this follow-up, also explain what code you would modify and how you would verify the change.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/evaluate.py:25`

### Q301. How would you handle drift? (applied follow-up 2)

Monitor feature distributions and live performance, then retrain when drift is detected. For this follow-up, also explain what code you would modify and how you would verify the change.

**File reference:** `architecture.md:174`

### Q302. How would you add explainability? (applied follow-up 2)

Use feature importance and SHAP to show which inputs drive predictions. For this follow-up, also explain what code you would modify and how you would verify the change.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/train.py:76`

### Q303. How would you validate demand forecasts visually? (applied follow-up 2)

Plot actual versus predicted demand and inspect residuals by date, store, and item. For this follow-up, also explain what code you would modify and how you would verify the change.

**File reference:** `app/backend/src/app/ml/demand_forecasting/evaluate.py:94`

### Q304. How would you validate quality classifier errors? (applied follow-up 2)

Use a confusion matrix and class-wise recall to inspect confused defect classes. For this follow-up, also explain what code you would modify and how you would verify the change.

**File reference:** `app/backend/src/app/ml/quality_inspection/evaluate.py:29`

### Q305. How would you choose the PM probability threshold? (applied follow-up 2)

Use validation probabilities and a cost matrix for downtime, inspection cost, and missed failures. For this follow-up, also explain what code you would modify and how you would verify the change.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/evaluate.py:41`

### Q306. How would you handle missing sensor readings in production? (applied follow-up 2)

Validate requests, reject critical missing fields, or use justified imputation. For this follow-up, also explain what code you would modify and how you would verify the change.

**File reference:** `app/backend/schemas.py:7`

### Q307. How would you make inventory recommendations safer? (applied follow-up 2)

Add uncertainty, lead time, service-level targets, and safety stock logic. For this follow-up, also explain what code you would modify and how you would verify the change.

**File reference:** `app/backend/services.py:81`

### Q308. How would you make demand validation stronger? (applied follow-up 2)

Use backtesting across multiple rolling forecast origins. For this follow-up, also explain what code you would modify and how you would verify the change.

**File reference:** `app/backend/src/app/ml/demand_forecasting/preprocessing.py:57`

### Q309. How would you make model selection fairer? (applied follow-up 2)

Use the same train/test partitions and compare models on metrics aligned to business cost. For this follow-up, also explain what code you would modify and how you would verify the change.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/evaluate.py:48`

### Q310. How would you test feature order stability? (applied follow-up 3)

Assert get_feature_columns exactly matches the columns used for model fit and inference. For this follow-up, also explain what code you would modify and how you would verify the change.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/features.py:59`

### Q311. How would you improve PM class imbalance? (applied follow-up 3)

Use class weights, threshold tuning, resampling, and PR-AUC analysis. For this follow-up, also explain what code you would modify and how you would verify the change.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/preprocessing.py:50`

### Q312. How would you choose maintenance recall versus precision? (applied follow-up 3)

Use business costs: missed failures favor recall; costly false alarms favor precision. For this follow-up, also explain what code you would modify and how you would verify the change.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/evaluate.py:26`

### Q313. How would you make ANN results more reproducible? (applied follow-up 3)

Set Python, NumPy, and TensorFlow seeds and document nondeterministic hardware behavior. For this follow-up, also explain what code you would modify and how you would verify the change.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/train.py:20`

### Q314. How would you tune XGBoost? (applied follow-up 3)

Search n_estimators, max_depth, learning_rate, subsample, colsample_bytree, and regularization. For this follow-up, also explain what code you would modify and how you would verify the change.

**File reference:** `app/backend/src/app/ml/demand_forecasting/train.py:53`

### Q315. How would you tune Random Forest? (applied follow-up 3)

Tune n_estimators, max_depth, min_samples_split, min_samples_leaf, and max_features. For this follow-up, also explain what code you would modify and how you would verify the change.

**File reference:** `app/backend/src/app/ml/demand_forecasting/train.py:33`

### Q316. How would you tune ANN architecture? (applied follow-up 3)

Tune layer sizes, dropout rates, learning rate, batch size, patience, and epochs. For this follow-up, also explain what code you would modify and how you would verify the change.

**File reference:** `app/backend/src/app/ml/quality_inspection/train.py:20`

### Q317. How would you prove MLflow logging works? (applied follow-up 3)

Run a pipeline and show metrics, params, artifacts, and comparison JSON in MLflow UI. For this follow-up, also explain what code you would modify and how you would verify the change.

**File reference:** `app/backend/src/app/ml/demand_forecasting/model_store.py:41`

### Q318. How would you connect PM training to API inference? (applied follow-up 3)

Load the persisted model, reconstruct features, apply saved feature parameters, and call predict_proba. For this follow-up, also explain what code you would modify and how you would verify the change.

**File reference:** `app/backend/services.py:20`

### Q319. How would you avoid overclaiming deep learning? (applied follow-up 3)

Say ANN/LSTM are candidate models and final selection depends on evidence, not model hype. For this follow-up, also explain what code you would modify and how you would verify the change.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/evaluate.py:75`

### Q320. How would you explain why accuracy is misleading? (applied follow-up 3)

A rare-failure dataset can have high accuracy by always predicting no failure. For this follow-up, also explain what code you would modify and how you would verify the change.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/evaluate.py:25`

### Q321. How would you handle drift? (applied follow-up 3)

Monitor feature distributions and live performance, then retrain when drift is detected. For this follow-up, also explain what code you would modify and how you would verify the change.

**File reference:** `architecture.md:174`

### Q322. How would you add explainability? (applied follow-up 3)

Use feature importance and SHAP to show which inputs drive predictions. For this follow-up, also explain what code you would modify and how you would verify the change.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/train.py:76`

### Q323. How would you validate demand forecasts visually? (applied follow-up 3)

Plot actual versus predicted demand and inspect residuals by date, store, and item. For this follow-up, also explain what code you would modify and how you would verify the change.

**File reference:** `app/backend/src/app/ml/demand_forecasting/evaluate.py:94`

### Q324. How would you validate quality classifier errors? (applied follow-up 3)

Use a confusion matrix and class-wise recall to inspect confused defect classes. For this follow-up, also explain what code you would modify and how you would verify the change.

**File reference:** `app/backend/src/app/ml/quality_inspection/evaluate.py:29`

### Q325. How would you choose the PM probability threshold? (applied follow-up 3)

Use validation probabilities and a cost matrix for downtime, inspection cost, and missed failures. For this follow-up, also explain what code you would modify and how you would verify the change.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/evaluate.py:41`

### Q326. How would you handle missing sensor readings in production? (applied follow-up 3)

Validate requests, reject critical missing fields, or use justified imputation. For this follow-up, also explain what code you would modify and how you would verify the change.

**File reference:** `app/backend/schemas.py:7`

### Q327. How would you make inventory recommendations safer? (applied follow-up 3)

Add uncertainty, lead time, service-level targets, and safety stock logic. For this follow-up, also explain what code you would modify and how you would verify the change.

**File reference:** `app/backend/services.py:81`

### Q328. How would you make demand validation stronger? (applied follow-up 3)

Use backtesting across multiple rolling forecast origins. For this follow-up, also explain what code you would modify and how you would verify the change.

**File reference:** `app/backend/src/app/ml/demand_forecasting/preprocessing.py:57`

### Q329. How would you make model selection fairer? (applied follow-up 3)

Use the same train/test partitions and compare models on metrics aligned to business cost. For this follow-up, also explain what code you would modify and how you would verify the change.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/evaluate.py:48`

### Q330. How would you test feature order stability? (applied follow-up 4)

Assert get_feature_columns exactly matches the columns used for model fit and inference. For this follow-up, also explain what code you would modify and how you would verify the change.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/features.py:59`

### Q331. How would you improve PM class imbalance? (applied follow-up 4)

Use class weights, threshold tuning, resampling, and PR-AUC analysis. For this follow-up, also explain what code you would modify and how you would verify the change.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/preprocessing.py:50`

### Q332. How would you choose maintenance recall versus precision? (applied follow-up 4)

Use business costs: missed failures favor recall; costly false alarms favor precision. For this follow-up, also explain what code you would modify and how you would verify the change.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/evaluate.py:26`

### Q333. How would you make ANN results more reproducible? (applied follow-up 4)

Set Python, NumPy, and TensorFlow seeds and document nondeterministic hardware behavior. For this follow-up, also explain what code you would modify and how you would verify the change.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/train.py:20`

### Q334. How would you tune XGBoost? (applied follow-up 4)

Search n_estimators, max_depth, learning_rate, subsample, colsample_bytree, and regularization. For this follow-up, also explain what code you would modify and how you would verify the change.

**File reference:** `app/backend/src/app/ml/demand_forecasting/train.py:53`

### Q335. How would you tune Random Forest? (applied follow-up 4)

Tune n_estimators, max_depth, min_samples_split, min_samples_leaf, and max_features. For this follow-up, also explain what code you would modify and how you would verify the change.

**File reference:** `app/backend/src/app/ml/demand_forecasting/train.py:33`

### Q336. How would you tune ANN architecture? (applied follow-up 4)

Tune layer sizes, dropout rates, learning rate, batch size, patience, and epochs. For this follow-up, also explain what code you would modify and how you would verify the change.

**File reference:** `app/backend/src/app/ml/quality_inspection/train.py:20`

### Q337. How would you prove MLflow logging works? (applied follow-up 4)

Run a pipeline and show metrics, params, artifacts, and comparison JSON in MLflow UI. For this follow-up, also explain what code you would modify and how you would verify the change.

**File reference:** `app/backend/src/app/ml/demand_forecasting/model_store.py:41`

### Q338. How would you connect PM training to API inference? (applied follow-up 4)

Load the persisted model, reconstruct features, apply saved feature parameters, and call predict_proba. For this follow-up, also explain what code you would modify and how you would verify the change.

**File reference:** `app/backend/services.py:20`

### Q339. How would you avoid overclaiming deep learning? (applied follow-up 4)

Say ANN/LSTM are candidate models and final selection depends on evidence, not model hype. For this follow-up, also explain what code you would modify and how you would verify the change.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/evaluate.py:75`

### Q340. How would you explain why accuracy is misleading? (applied follow-up 4)

A rare-failure dataset can have high accuracy by always predicting no failure. For this follow-up, also explain what code you would modify and how you would verify the change.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/evaluate.py:25`

### Q341. How would you handle drift? (applied follow-up 4)

Monitor feature distributions and live performance, then retrain when drift is detected. For this follow-up, also explain what code you would modify and how you would verify the change.

**File reference:** `architecture.md:174`

### Q342. How would you add explainability? (applied follow-up 4)

Use feature importance and SHAP to show which inputs drive predictions. For this follow-up, also explain what code you would modify and how you would verify the change.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/train.py:76`

### Q343. How would you validate demand forecasts visually? (applied follow-up 4)

Plot actual versus predicted demand and inspect residuals by date, store, and item. For this follow-up, also explain what code you would modify and how you would verify the change.

**File reference:** `app/backend/src/app/ml/demand_forecasting/evaluate.py:94`

### Q344. How would you validate quality classifier errors? (applied follow-up 4)

Use a confusion matrix and class-wise recall to inspect confused defect classes. For this follow-up, also explain what code you would modify and how you would verify the change.

**File reference:** `app/backend/src/app/ml/quality_inspection/evaluate.py:29`

### Q345. How would you choose the PM probability threshold? (applied follow-up 4)

Use validation probabilities and a cost matrix for downtime, inspection cost, and missed failures. For this follow-up, also explain what code you would modify and how you would verify the change.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/evaluate.py:41`

### Q346. How would you handle missing sensor readings in production? (applied follow-up 4)

Validate requests, reject critical missing fields, or use justified imputation. For this follow-up, also explain what code you would modify and how you would verify the change.

**File reference:** `app/backend/schemas.py:7`

### Q347. How would you make inventory recommendations safer? (applied follow-up 4)

Add uncertainty, lead time, service-level targets, and safety stock logic. For this follow-up, also explain what code you would modify and how you would verify the change.

**File reference:** `app/backend/services.py:81`

### Q348. How would you make demand validation stronger? (applied follow-up 4)

Use backtesting across multiple rolling forecast origins. For this follow-up, also explain what code you would modify and how you would verify the change.

**File reference:** `app/backend/src/app/ml/demand_forecasting/preprocessing.py:57`

### Q349. How would you make model selection fairer? (applied follow-up 4)

Use the same train/test partitions and compare models on metrics aligned to business cost. For this follow-up, also explain what code you would modify and how you would verify the change.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/evaluate.py:48`

### Q350. How would you test feature order stability? (applied follow-up 5)

Assert get_feature_columns exactly matches the columns used for model fit and inference. For this follow-up, also explain what code you would modify and how you would verify the change.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/features.py:59`

### Q351. How would you improve PM class imbalance? (applied follow-up 5)

Use class weights, threshold tuning, resampling, and PR-AUC analysis. For this follow-up, also explain what code you would modify and how you would verify the change.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/preprocessing.py:50`

### Q352. How would you choose maintenance recall versus precision? (applied follow-up 5)

Use business costs: missed failures favor recall; costly false alarms favor precision. For this follow-up, also explain what code you would modify and how you would verify the change.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/evaluate.py:26`

### Q353. How would you make ANN results more reproducible? (applied follow-up 5)

Set Python, NumPy, and TensorFlow seeds and document nondeterministic hardware behavior. For this follow-up, also explain what code you would modify and how you would verify the change.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/train.py:20`

### Q354. How would you tune XGBoost? (applied follow-up 5)

Search n_estimators, max_depth, learning_rate, subsample, colsample_bytree, and regularization. For this follow-up, also explain what code you would modify and how you would verify the change.

**File reference:** `app/backend/src/app/ml/demand_forecasting/train.py:53`

### Q355. How would you tune Random Forest? (applied follow-up 5)

Tune n_estimators, max_depth, min_samples_split, min_samples_leaf, and max_features. For this follow-up, also explain what code you would modify and how you would verify the change.

**File reference:** `app/backend/src/app/ml/demand_forecasting/train.py:33`

### Q356. How would you tune ANN architecture? (applied follow-up 5)

Tune layer sizes, dropout rates, learning rate, batch size, patience, and epochs. For this follow-up, also explain what code you would modify and how you would verify the change.

**File reference:** `app/backend/src/app/ml/quality_inspection/train.py:20`

### Q357. How would you prove MLflow logging works? (applied follow-up 5)

Run a pipeline and show metrics, params, artifacts, and comparison JSON in MLflow UI. For this follow-up, also explain what code you would modify and how you would verify the change.

**File reference:** `app/backend/src/app/ml/demand_forecasting/model_store.py:41`

### Q358. How would you connect PM training to API inference? (applied follow-up 5)

Load the persisted model, reconstruct features, apply saved feature parameters, and call predict_proba. For this follow-up, also explain what code you would modify and how you would verify the change.

**File reference:** `app/backend/services.py:20`

### Q359. How would you avoid overclaiming deep learning? (applied follow-up 5)

Say ANN/LSTM are candidate models and final selection depends on evidence, not model hype. For this follow-up, also explain what code you would modify and how you would verify the change.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/evaluate.py:75`

### Q360. How would you explain why accuracy is misleading? (applied follow-up 5)

A rare-failure dataset can have high accuracy by always predicting no failure. For this follow-up, also explain what code you would modify and how you would verify the change.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/evaluate.py:25`

### Q361. How would you handle drift? (applied follow-up 5)

Monitor feature distributions and live performance, then retrain when drift is detected. For this follow-up, also explain what code you would modify and how you would verify the change.

**File reference:** `architecture.md:174`

### Q362. How would you add explainability? (applied follow-up 5)

Use feature importance and SHAP to show which inputs drive predictions. For this follow-up, also explain what code you would modify and how you would verify the change.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/train.py:76`

### Q363. How would you validate demand forecasts visually? (applied follow-up 5)

Plot actual versus predicted demand and inspect residuals by date, store, and item. For this follow-up, also explain what code you would modify and how you would verify the change.

**File reference:** `app/backend/src/app/ml/demand_forecasting/evaluate.py:94`

### Q364. How would you validate quality classifier errors? (applied follow-up 5)

Use a confusion matrix and class-wise recall to inspect confused defect classes. For this follow-up, also explain what code you would modify and how you would verify the change.

**File reference:** `app/backend/src/app/ml/quality_inspection/evaluate.py:29`

### Q365. How would you choose the PM probability threshold? (applied follow-up 5)

Use validation probabilities and a cost matrix for downtime, inspection cost, and missed failures. For this follow-up, also explain what code you would modify and how you would verify the change.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/evaluate.py:41`

### Q366. How would you handle missing sensor readings in production? (applied follow-up 5)

Validate requests, reject critical missing fields, or use justified imputation. For this follow-up, also explain what code you would modify and how you would verify the change.

**File reference:** `app/backend/schemas.py:7`

### Q367. How would you make inventory recommendations safer? (applied follow-up 5)

Add uncertainty, lead time, service-level targets, and safety stock logic. For this follow-up, also explain what code you would modify and how you would verify the change.

**File reference:** `app/backend/services.py:81`

### Q368. How would you make demand validation stronger? (applied follow-up 5)

Use backtesting across multiple rolling forecast origins. For this follow-up, also explain what code you would modify and how you would verify the change.

**File reference:** `app/backend/src/app/ml/demand_forecasting/preprocessing.py:57`

### Q369. How would you make model selection fairer? (applied follow-up 5)

Use the same train/test partitions and compare models on metrics aligned to business cost. For this follow-up, also explain what code you would modify and how you would verify the change.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/evaluate.py:48`

### Q370. How would you test feature order stability? (applied follow-up 6)

Assert get_feature_columns exactly matches the columns used for model fit and inference. For this follow-up, also explain what code you would modify and how you would verify the change.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/features.py:59`

### Q371. How would you improve PM class imbalance? (applied follow-up 6)

Use class weights, threshold tuning, resampling, and PR-AUC analysis. For this follow-up, also explain what code you would modify and how you would verify the change.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/preprocessing.py:50`

### Q372. How would you choose maintenance recall versus precision? (applied follow-up 6)

Use business costs: missed failures favor recall; costly false alarms favor precision. For this follow-up, also explain what code you would modify and how you would verify the change.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/evaluate.py:26`

### Q373. How would you make ANN results more reproducible? (applied follow-up 6)

Set Python, NumPy, and TensorFlow seeds and document nondeterministic hardware behavior. For this follow-up, also explain what code you would modify and how you would verify the change.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/train.py:20`

### Q374. How would you tune XGBoost? (applied follow-up 6)

Search n_estimators, max_depth, learning_rate, subsample, colsample_bytree, and regularization. For this follow-up, also explain what code you would modify and how you would verify the change.

**File reference:** `app/backend/src/app/ml/demand_forecasting/train.py:53`

### Q375. How would you tune Random Forest? (applied follow-up 6)

Tune n_estimators, max_depth, min_samples_split, min_samples_leaf, and max_features. For this follow-up, also explain what code you would modify and how you would verify the change.

**File reference:** `app/backend/src/app/ml/demand_forecasting/train.py:33`

### Q376. How would you tune ANN architecture? (applied follow-up 6)

Tune layer sizes, dropout rates, learning rate, batch size, patience, and epochs. For this follow-up, also explain what code you would modify and how you would verify the change.

**File reference:** `app/backend/src/app/ml/quality_inspection/train.py:20`

### Q377. How would you prove MLflow logging works? (applied follow-up 6)

Run a pipeline and show metrics, params, artifacts, and comparison JSON in MLflow UI. For this follow-up, also explain what code you would modify and how you would verify the change.

**File reference:** `app/backend/src/app/ml/demand_forecasting/model_store.py:41`

### Q378. How would you connect PM training to API inference? (applied follow-up 6)

Load the persisted model, reconstruct features, apply saved feature parameters, and call predict_proba. For this follow-up, also explain what code you would modify and how you would verify the change.

**File reference:** `app/backend/services.py:20`

### Q379. How would you avoid overclaiming deep learning? (applied follow-up 6)

Say ANN/LSTM are candidate models and final selection depends on evidence, not model hype. For this follow-up, also explain what code you would modify and how you would verify the change.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/evaluate.py:75`

### Q380. How would you explain why accuracy is misleading? (applied follow-up 6)

A rare-failure dataset can have high accuracy by always predicting no failure. For this follow-up, also explain what code you would modify and how you would verify the change.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/evaluate.py:25`

### Q381. How would you handle drift? (applied follow-up 6)

Monitor feature distributions and live performance, then retrain when drift is detected. For this follow-up, also explain what code you would modify and how you would verify the change.

**File reference:** `architecture.md:174`

### Q382. How would you add explainability? (applied follow-up 6)

Use feature importance and SHAP to show which inputs drive predictions. For this follow-up, also explain what code you would modify and how you would verify the change.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/train.py:76`

### Q383. How would you validate demand forecasts visually? (applied follow-up 6)

Plot actual versus predicted demand and inspect residuals by date, store, and item. For this follow-up, also explain what code you would modify and how you would verify the change.

**File reference:** `app/backend/src/app/ml/demand_forecasting/evaluate.py:94`

### Q384. How would you validate quality classifier errors? (applied follow-up 6)

Use a confusion matrix and class-wise recall to inspect confused defect classes. For this follow-up, also explain what code you would modify and how you would verify the change.

**File reference:** `app/backend/src/app/ml/quality_inspection/evaluate.py:29`

### Q385. How would you choose the PM probability threshold? (applied follow-up 6)

Use validation probabilities and a cost matrix for downtime, inspection cost, and missed failures. For this follow-up, also explain what code you would modify and how you would verify the change.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/evaluate.py:41`

### Q386. How would you handle missing sensor readings in production? (applied follow-up 6)

Validate requests, reject critical missing fields, or use justified imputation. For this follow-up, also explain what code you would modify and how you would verify the change.

**File reference:** `app/backend/schemas.py:7`

### Q387. How would you make inventory recommendations safer? (applied follow-up 6)

Add uncertainty, lead time, service-level targets, and safety stock logic. For this follow-up, also explain what code you would modify and how you would verify the change.

**File reference:** `app/backend/services.py:81`

### Q388. How would you make demand validation stronger? (applied follow-up 6)

Use backtesting across multiple rolling forecast origins. For this follow-up, also explain what code you would modify and how you would verify the change.

**File reference:** `app/backend/src/app/ml/demand_forecasting/preprocessing.py:57`

### Q389. How would you make model selection fairer? (applied follow-up 6)

Use the same train/test partitions and compare models on metrics aligned to business cost. For this follow-up, also explain what code you would modify and how you would verify the change.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/evaluate.py:48`

### Q390. How would you test feature order stability? (applied follow-up 7)

Assert get_feature_columns exactly matches the columns used for model fit and inference. For this follow-up, also explain what code you would modify and how you would verify the change.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/features.py:59`

### Q391. How would you improve PM class imbalance? (applied follow-up 7)

Use class weights, threshold tuning, resampling, and PR-AUC analysis. For this follow-up, also explain what code you would modify and how you would verify the change.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/preprocessing.py:50`

### Q392. How would you choose maintenance recall versus precision? (applied follow-up 7)

Use business costs: missed failures favor recall; costly false alarms favor precision. For this follow-up, also explain what code you would modify and how you would verify the change.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/evaluate.py:26`

### Q393. How would you make ANN results more reproducible? (applied follow-up 7)

Set Python, NumPy, and TensorFlow seeds and document nondeterministic hardware behavior. For this follow-up, also explain what code you would modify and how you would verify the change.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/train.py:20`

### Q394. How would you tune XGBoost? (applied follow-up 7)

Search n_estimators, max_depth, learning_rate, subsample, colsample_bytree, and regularization. For this follow-up, also explain what code you would modify and how you would verify the change.

**File reference:** `app/backend/src/app/ml/demand_forecasting/train.py:53`

### Q395. How would you tune Random Forest? (applied follow-up 7)

Tune n_estimators, max_depth, min_samples_split, min_samples_leaf, and max_features. For this follow-up, also explain what code you would modify and how you would verify the change.

**File reference:** `app/backend/src/app/ml/demand_forecasting/train.py:33`

### Q396. How would you tune ANN architecture? (applied follow-up 7)

Tune layer sizes, dropout rates, learning rate, batch size, patience, and epochs. For this follow-up, also explain what code you would modify and how you would verify the change.

**File reference:** `app/backend/src/app/ml/quality_inspection/train.py:20`

### Q397. How would you prove MLflow logging works? (applied follow-up 7)

Run a pipeline and show metrics, params, artifacts, and comparison JSON in MLflow UI. For this follow-up, also explain what code you would modify and how you would verify the change.

**File reference:** `app/backend/src/app/ml/demand_forecasting/model_store.py:41`

### Q398. How would you connect PM training to API inference? (applied follow-up 7)

Load the persisted model, reconstruct features, apply saved feature parameters, and call predict_proba. For this follow-up, also explain what code you would modify and how you would verify the change.

**File reference:** `app/backend/services.py:20`

### Q399. How would you avoid overclaiming deep learning? (applied follow-up 7)

Say ANN/LSTM are candidate models and final selection depends on evidence, not model hype. For this follow-up, also explain what code you would modify and how you would verify the change.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/evaluate.py:75`

### Q400. How would you explain why accuracy is misleading? (applied follow-up 7)

A rare-failure dataset can have high accuracy by always predicting no failure. For this follow-up, also explain what code you would modify and how you would verify the change.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/evaluate.py:25`

### Q401. How would you handle drift? (applied follow-up 7)

Monitor feature distributions and live performance, then retrain when drift is detected. For this follow-up, also explain what code you would modify and how you would verify the change.

**File reference:** `architecture.md:174`

### Q402. How would you add explainability? (applied follow-up 7)

Use feature importance and SHAP to show which inputs drive predictions. For this follow-up, also explain what code you would modify and how you would verify the change.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/train.py:76`

### Q403. How would you validate demand forecasts visually? (applied follow-up 7)

Plot actual versus predicted demand and inspect residuals by date, store, and item. For this follow-up, also explain what code you would modify and how you would verify the change.

**File reference:** `app/backend/src/app/ml/demand_forecasting/evaluate.py:94`

### Q404. How would you validate quality classifier errors? (applied follow-up 7)

Use a confusion matrix and class-wise recall to inspect confused defect classes. For this follow-up, also explain what code you would modify and how you would verify the change.

**File reference:** `app/backend/src/app/ml/quality_inspection/evaluate.py:29`

### Q405. How would you choose the PM probability threshold? (applied follow-up 7)

Use validation probabilities and a cost matrix for downtime, inspection cost, and missed failures. For this follow-up, also explain what code you would modify and how you would verify the change.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/evaluate.py:41`

### Q406. How would you handle missing sensor readings in production? (applied follow-up 7)

Validate requests, reject critical missing fields, or use justified imputation. For this follow-up, also explain what code you would modify and how you would verify the change.

**File reference:** `app/backend/schemas.py:7`

### Q407. How would you make inventory recommendations safer? (applied follow-up 7)

Add uncertainty, lead time, service-level targets, and safety stock logic. For this follow-up, also explain what code you would modify and how you would verify the change.

**File reference:** `app/backend/services.py:81`

### Q408. How would you make demand validation stronger? (applied follow-up 7)

Use backtesting across multiple rolling forecast origins. For this follow-up, also explain what code you would modify and how you would verify the change.

**File reference:** `app/backend/src/app/ml/demand_forecasting/preprocessing.py:57`

### Q409. How would you make model selection fairer? (applied follow-up 7)

Use the same train/test partitions and compare models on metrics aligned to business cost. For this follow-up, also explain what code you would modify and how you would verify the change.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/evaluate.py:48`

### Q410. How would you test feature order stability? (applied follow-up 8)

Assert get_feature_columns exactly matches the columns used for model fit and inference. For this follow-up, also explain what code you would modify and how you would verify the change.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/features.py:59`

### Q411. How would you improve PM class imbalance? (applied follow-up 8)

Use class weights, threshold tuning, resampling, and PR-AUC analysis. For this follow-up, also explain what code you would modify and how you would verify the change.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/preprocessing.py:50`

### Q412. How would you choose maintenance recall versus precision? (applied follow-up 8)

Use business costs: missed failures favor recall; costly false alarms favor precision. For this follow-up, also explain what code you would modify and how you would verify the change.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/evaluate.py:26`

### Q413. How would you make ANN results more reproducible? (applied follow-up 8)

Set Python, NumPy, and TensorFlow seeds and document nondeterministic hardware behavior. For this follow-up, also explain what code you would modify and how you would verify the change.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/train.py:20`

### Q414. How would you tune XGBoost? (applied follow-up 8)

Search n_estimators, max_depth, learning_rate, subsample, colsample_bytree, and regularization. For this follow-up, also explain what code you would modify and how you would verify the change.

**File reference:** `app/backend/src/app/ml/demand_forecasting/train.py:53`

### Q415. How would you tune Random Forest? (applied follow-up 8)

Tune n_estimators, max_depth, min_samples_split, min_samples_leaf, and max_features. For this follow-up, also explain what code you would modify and how you would verify the change.

**File reference:** `app/backend/src/app/ml/demand_forecasting/train.py:33`

### Q416. How would you tune ANN architecture? (applied follow-up 8)

Tune layer sizes, dropout rates, learning rate, batch size, patience, and epochs. For this follow-up, also explain what code you would modify and how you would verify the change.

**File reference:** `app/backend/src/app/ml/quality_inspection/train.py:20`

### Q417. How would you prove MLflow logging works? (applied follow-up 8)

Run a pipeline and show metrics, params, artifacts, and comparison JSON in MLflow UI. For this follow-up, also explain what code you would modify and how you would verify the change.

**File reference:** `app/backend/src/app/ml/demand_forecasting/model_store.py:41`

### Q418. How would you connect PM training to API inference? (applied follow-up 8)

Load the persisted model, reconstruct features, apply saved feature parameters, and call predict_proba. For this follow-up, also explain what code you would modify and how you would verify the change.

**File reference:** `app/backend/services.py:20`

### Q419. How would you avoid overclaiming deep learning? (applied follow-up 8)

Say ANN/LSTM are candidate models and final selection depends on evidence, not model hype. For this follow-up, also explain what code you would modify and how you would verify the change.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/evaluate.py:75`

### Q420. How would you explain why accuracy is misleading? (applied follow-up 8)

A rare-failure dataset can have high accuracy by always predicting no failure. For this follow-up, also explain what code you would modify and how you would verify the change.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/evaluate.py:25`

### Q421. How would you handle drift? (applied follow-up 8)

Monitor feature distributions and live performance, then retrain when drift is detected. For this follow-up, also explain what code you would modify and how you would verify the change.

**File reference:** `architecture.md:174`

### Q422. How would you add explainability? (applied follow-up 8)

Use feature importance and SHAP to show which inputs drive predictions. For this follow-up, also explain what code you would modify and how you would verify the change.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/train.py:76`

### Q423. How would you validate demand forecasts visually? (applied follow-up 8)

Plot actual versus predicted demand and inspect residuals by date, store, and item. For this follow-up, also explain what code you would modify and how you would verify the change.

**File reference:** `app/backend/src/app/ml/demand_forecasting/evaluate.py:94`

### Q424. How would you validate quality classifier errors? (applied follow-up 8)

Use a confusion matrix and class-wise recall to inspect confused defect classes. For this follow-up, also explain what code you would modify and how you would verify the change.

**File reference:** `app/backend/src/app/ml/quality_inspection/evaluate.py:29`

### Q425. How would you choose the PM probability threshold? (applied follow-up 8)

Use validation probabilities and a cost matrix for downtime, inspection cost, and missed failures. For this follow-up, also explain what code you would modify and how you would verify the change.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/evaluate.py:41`

### Q426. How would you handle missing sensor readings in production? (applied follow-up 8)

Validate requests, reject critical missing fields, or use justified imputation. For this follow-up, also explain what code you would modify and how you would verify the change.

**File reference:** `app/backend/schemas.py:7`

### Q427. How would you make inventory recommendations safer? (applied follow-up 8)

Add uncertainty, lead time, service-level targets, and safety stock logic. For this follow-up, also explain what code you would modify and how you would verify the change.

**File reference:** `app/backend/services.py:81`

### Q428. How would you make demand validation stronger? (applied follow-up 8)

Use backtesting across multiple rolling forecast origins. For this follow-up, also explain what code you would modify and how you would verify the change.

**File reference:** `app/backend/src/app/ml/demand_forecasting/preprocessing.py:57`

### Q429. How would you make model selection fairer? (applied follow-up 8)

Use the same train/test partitions and compare models on metrics aligned to business cost. For this follow-up, also explain what code you would modify and how you would verify the change.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/evaluate.py:48`

### Q430. How would you test feature order stability? (applied follow-up 9)

Assert get_feature_columns exactly matches the columns used for model fit and inference. For this follow-up, also explain what code you would modify and how you would verify the change.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/features.py:59`

### Q431. How would you improve PM class imbalance? (applied follow-up 9)

Use class weights, threshold tuning, resampling, and PR-AUC analysis. For this follow-up, also explain what code you would modify and how you would verify the change.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/preprocessing.py:50`

### Q432. How would you choose maintenance recall versus precision? (applied follow-up 9)

Use business costs: missed failures favor recall; costly false alarms favor precision. For this follow-up, also explain what code you would modify and how you would verify the change.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/evaluate.py:26`

### Q433. How would you make ANN results more reproducible? (applied follow-up 9)

Set Python, NumPy, and TensorFlow seeds and document nondeterministic hardware behavior. For this follow-up, also explain what code you would modify and how you would verify the change.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/train.py:20`

### Q434. How would you tune XGBoost? (applied follow-up 9)

Search n_estimators, max_depth, learning_rate, subsample, colsample_bytree, and regularization. For this follow-up, also explain what code you would modify and how you would verify the change.

**File reference:** `app/backend/src/app/ml/demand_forecasting/train.py:53`

### Q435. How would you tune Random Forest? (applied follow-up 9)

Tune n_estimators, max_depth, min_samples_split, min_samples_leaf, and max_features. For this follow-up, also explain what code you would modify and how you would verify the change.

**File reference:** `app/backend/src/app/ml/demand_forecasting/train.py:33`

### Q436. How would you tune ANN architecture? (applied follow-up 9)

Tune layer sizes, dropout rates, learning rate, batch size, patience, and epochs. For this follow-up, also explain what code you would modify and how you would verify the change.

**File reference:** `app/backend/src/app/ml/quality_inspection/train.py:20`

### Q437. How would you prove MLflow logging works? (applied follow-up 9)

Run a pipeline and show metrics, params, artifacts, and comparison JSON in MLflow UI. For this follow-up, also explain what code you would modify and how you would verify the change.

**File reference:** `app/backend/src/app/ml/demand_forecasting/model_store.py:41`

### Q438. How would you connect PM training to API inference? (applied follow-up 9)

Load the persisted model, reconstruct features, apply saved feature parameters, and call predict_proba. For this follow-up, also explain what code you would modify and how you would verify the change.

**File reference:** `app/backend/services.py:20`

### Q439. How would you avoid overclaiming deep learning? (applied follow-up 9)

Say ANN/LSTM are candidate models and final selection depends on evidence, not model hype. For this follow-up, also explain what code you would modify and how you would verify the change.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/evaluate.py:75`

### Q440. How would you explain why accuracy is misleading? (applied follow-up 9)

A rare-failure dataset can have high accuracy by always predicting no failure. For this follow-up, also explain what code you would modify and how you would verify the change.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/evaluate.py:25`

### Q441. How would you handle drift? (applied follow-up 9)

Monitor feature distributions and live performance, then retrain when drift is detected. For this follow-up, also explain what code you would modify and how you would verify the change.

**File reference:** `architecture.md:174`

### Q442. How would you add explainability? (applied follow-up 9)

Use feature importance and SHAP to show which inputs drive predictions. For this follow-up, also explain what code you would modify and how you would verify the change.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/train.py:76`

### Q443. How would you validate demand forecasts visually? (applied follow-up 9)

Plot actual versus predicted demand and inspect residuals by date, store, and item. For this follow-up, also explain what code you would modify and how you would verify the change.

**File reference:** `app/backend/src/app/ml/demand_forecasting/evaluate.py:94`

### Q444. How would you validate quality classifier errors? (applied follow-up 9)

Use a confusion matrix and class-wise recall to inspect confused defect classes. For this follow-up, also explain what code you would modify and how you would verify the change.

**File reference:** `app/backend/src/app/ml/quality_inspection/evaluate.py:29`

### Q445. How would you choose the PM probability threshold? (applied follow-up 9)

Use validation probabilities and a cost matrix for downtime, inspection cost, and missed failures. For this follow-up, also explain what code you would modify and how you would verify the change.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/evaluate.py:41`

### Q446. How would you handle missing sensor readings in production? (applied follow-up 9)

Validate requests, reject critical missing fields, or use justified imputation. For this follow-up, also explain what code you would modify and how you would verify the change.

**File reference:** `app/backend/schemas.py:7`

### Q447. How would you make inventory recommendations safer? (applied follow-up 9)

Add uncertainty, lead time, service-level targets, and safety stock logic. For this follow-up, also explain what code you would modify and how you would verify the change.

**File reference:** `app/backend/services.py:81`

### Q448. How would you make demand validation stronger? (applied follow-up 9)

Use backtesting across multiple rolling forecast origins. For this follow-up, also explain what code you would modify and how you would verify the change.

**File reference:** `app/backend/src/app/ml/demand_forecasting/preprocessing.py:57`

### Q449. How would you make model selection fairer? (applied follow-up 9)

Use the same train/test partitions and compare models on metrics aligned to business cost. For this follow-up, also explain what code you would modify and how you would verify the change.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/evaluate.py:48`

### Q450. How would you test feature order stability? (applied follow-up 10)

Assert get_feature_columns exactly matches the columns used for model fit and inference. For this follow-up, also explain what code you would modify and how you would verify the change.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/features.py:59`

### Q451. How would you improve PM class imbalance? (applied follow-up 10)

Use class weights, threshold tuning, resampling, and PR-AUC analysis. For this follow-up, also explain what code you would modify and how you would verify the change.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/preprocessing.py:50`

### Q452. How would you choose maintenance recall versus precision? (applied follow-up 10)

Use business costs: missed failures favor recall; costly false alarms favor precision. For this follow-up, also explain what code you would modify and how you would verify the change.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/evaluate.py:26`

### Q453. How would you make ANN results more reproducible? (applied follow-up 10)

Set Python, NumPy, and TensorFlow seeds and document nondeterministic hardware behavior. For this follow-up, also explain what code you would modify and how you would verify the change.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/train.py:20`

### Q454. How would you tune XGBoost? (applied follow-up 10)

Search n_estimators, max_depth, learning_rate, subsample, colsample_bytree, and regularization. For this follow-up, also explain what code you would modify and how you would verify the change.

**File reference:** `app/backend/src/app/ml/demand_forecasting/train.py:53`

### Q455. How would you tune Random Forest? (applied follow-up 10)

Tune n_estimators, max_depth, min_samples_split, min_samples_leaf, and max_features. For this follow-up, also explain what code you would modify and how you would verify the change.

**File reference:** `app/backend/src/app/ml/demand_forecasting/train.py:33`

### Q456. How would you tune ANN architecture? (applied follow-up 10)

Tune layer sizes, dropout rates, learning rate, batch size, patience, and epochs. For this follow-up, also explain what code you would modify and how you would verify the change.

**File reference:** `app/backend/src/app/ml/quality_inspection/train.py:20`

### Q457. How would you prove MLflow logging works? (applied follow-up 10)

Run a pipeline and show metrics, params, artifacts, and comparison JSON in MLflow UI. For this follow-up, also explain what code you would modify and how you would verify the change.

**File reference:** `app/backend/src/app/ml/demand_forecasting/model_store.py:41`

### Q458. How would you connect PM training to API inference? (applied follow-up 10)

Load the persisted model, reconstruct features, apply saved feature parameters, and call predict_proba. For this follow-up, also explain what code you would modify and how you would verify the change.

**File reference:** `app/backend/services.py:20`

### Q459. How would you avoid overclaiming deep learning? (applied follow-up 10)

Say ANN/LSTM are candidate models and final selection depends on evidence, not model hype. For this follow-up, also explain what code you would modify and how you would verify the change.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/evaluate.py:75`

### Q460. How would you explain why accuracy is misleading? (applied follow-up 10)

A rare-failure dataset can have high accuracy by always predicting no failure. For this follow-up, also explain what code you would modify and how you would verify the change.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/evaluate.py:25`

### Q461. How would you handle drift? (applied follow-up 10)

Monitor feature distributions and live performance, then retrain when drift is detected. For this follow-up, also explain what code you would modify and how you would verify the change.

**File reference:** `architecture.md:174`

### Q462. How would you add explainability? (applied follow-up 10)

Use feature importance and SHAP to show which inputs drive predictions. For this follow-up, also explain what code you would modify and how you would verify the change.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/train.py:76`

### Q463. How would you validate demand forecasts visually? (applied follow-up 10)

Plot actual versus predicted demand and inspect residuals by date, store, and item. For this follow-up, also explain what code you would modify and how you would verify the change.

**File reference:** `app/backend/src/app/ml/demand_forecasting/evaluate.py:94`

### Q464. How would you validate quality classifier errors? (applied follow-up 10)

Use a confusion matrix and class-wise recall to inspect confused defect classes. For this follow-up, also explain what code you would modify and how you would verify the change.

**File reference:** `app/backend/src/app/ml/quality_inspection/evaluate.py:29`

### Q465. How would you choose the PM probability threshold? (applied follow-up 10)

Use validation probabilities and a cost matrix for downtime, inspection cost, and missed failures. For this follow-up, also explain what code you would modify and how you would verify the change.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/evaluate.py:41`

### Q466. How would you handle missing sensor readings in production? (applied follow-up 10)

Validate requests, reject critical missing fields, or use justified imputation. For this follow-up, also explain what code you would modify and how you would verify the change.

**File reference:** `app/backend/schemas.py:7`

### Q467. How would you make inventory recommendations safer? (applied follow-up 10)

Add uncertainty, lead time, service-level targets, and safety stock logic. For this follow-up, also explain what code you would modify and how you would verify the change.

**File reference:** `app/backend/services.py:81`

### Q468. How would you make demand validation stronger? (applied follow-up 10)

Use backtesting across multiple rolling forecast origins. For this follow-up, also explain what code you would modify and how you would verify the change.

**File reference:** `app/backend/src/app/ml/demand_forecasting/preprocessing.py:57`

### Q469. How would you make model selection fairer? (applied follow-up 10)

Use the same train/test partitions and compare models on metrics aligned to business cost. For this follow-up, also explain what code you would modify and how you would verify the change.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/evaluate.py:48`

### Q470. How would you test feature order stability? (applied follow-up 11)

Assert get_feature_columns exactly matches the columns used for model fit and inference. For this follow-up, also explain what code you would modify and how you would verify the change.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/features.py:59`

### Q471. How would you improve PM class imbalance? (applied follow-up 11)

Use class weights, threshold tuning, resampling, and PR-AUC analysis. For this follow-up, also explain what code you would modify and how you would verify the change.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/preprocessing.py:50`

### Q472. How would you choose maintenance recall versus precision? (applied follow-up 11)

Use business costs: missed failures favor recall; costly false alarms favor precision. For this follow-up, also explain what code you would modify and how you would verify the change.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/evaluate.py:26`

### Q473. How would you make ANN results more reproducible? (applied follow-up 11)

Set Python, NumPy, and TensorFlow seeds and document nondeterministic hardware behavior. For this follow-up, also explain what code you would modify and how you would verify the change.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/train.py:20`

### Q474. How would you tune XGBoost? (applied follow-up 11)

Search n_estimators, max_depth, learning_rate, subsample, colsample_bytree, and regularization. For this follow-up, also explain what code you would modify and how you would verify the change.

**File reference:** `app/backend/src/app/ml/demand_forecasting/train.py:53`

### Q475. How would you tune Random Forest? (applied follow-up 11)

Tune n_estimators, max_depth, min_samples_split, min_samples_leaf, and max_features. For this follow-up, also explain what code you would modify and how you would verify the change.

**File reference:** `app/backend/src/app/ml/demand_forecasting/train.py:33`

### Q476. How would you tune ANN architecture? (applied follow-up 11)

Tune layer sizes, dropout rates, learning rate, batch size, patience, and epochs. For this follow-up, also explain what code you would modify and how you would verify the change.

**File reference:** `app/backend/src/app/ml/quality_inspection/train.py:20`

### Q477. How would you prove MLflow logging works? (applied follow-up 11)

Run a pipeline and show metrics, params, artifacts, and comparison JSON in MLflow UI. For this follow-up, also explain what code you would modify and how you would verify the change.

**File reference:** `app/backend/src/app/ml/demand_forecasting/model_store.py:41`

### Q478. How would you connect PM training to API inference? (applied follow-up 11)

Load the persisted model, reconstruct features, apply saved feature parameters, and call predict_proba. For this follow-up, also explain what code you would modify and how you would verify the change.

**File reference:** `app/backend/services.py:20`

### Q479. How would you avoid overclaiming deep learning? (applied follow-up 11)

Say ANN/LSTM are candidate models and final selection depends on evidence, not model hype. For this follow-up, also explain what code you would modify and how you would verify the change.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/evaluate.py:75`

### Q480. How would you explain why accuracy is misleading? (applied follow-up 11)

A rare-failure dataset can have high accuracy by always predicting no failure. For this follow-up, also explain what code you would modify and how you would verify the change.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/evaluate.py:25`

### Q481. How would you handle drift? (applied follow-up 11)

Monitor feature distributions and live performance, then retrain when drift is detected. For this follow-up, also explain what code you would modify and how you would verify the change.

**File reference:** `architecture.md:174`

### Q482. How would you add explainability? (applied follow-up 11)

Use feature importance and SHAP to show which inputs drive predictions. For this follow-up, also explain what code you would modify and how you would verify the change.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/train.py:76`

### Q483. How would you validate demand forecasts visually? (applied follow-up 11)

Plot actual versus predicted demand and inspect residuals by date, store, and item. For this follow-up, also explain what code you would modify and how you would verify the change.

**File reference:** `app/backend/src/app/ml/demand_forecasting/evaluate.py:94`

### Q484. How would you validate quality classifier errors? (applied follow-up 11)

Use a confusion matrix and class-wise recall to inspect confused defect classes. For this follow-up, also explain what code you would modify and how you would verify the change.

**File reference:** `app/backend/src/app/ml/quality_inspection/evaluate.py:29`

### Q485. How would you choose the PM probability threshold? (applied follow-up 11)

Use validation probabilities and a cost matrix for downtime, inspection cost, and missed failures. For this follow-up, also explain what code you would modify and how you would verify the change.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/evaluate.py:41`

### Q486. How would you handle missing sensor readings in production? (applied follow-up 11)

Validate requests, reject critical missing fields, or use justified imputation. For this follow-up, also explain what code you would modify and how you would verify the change.

**File reference:** `app/backend/schemas.py:7`

### Q487. How would you make inventory recommendations safer? (applied follow-up 11)

Add uncertainty, lead time, service-level targets, and safety stock logic. For this follow-up, also explain what code you would modify and how you would verify the change.

**File reference:** `app/backend/services.py:81`

### Q488. How would you make demand validation stronger? (applied follow-up 11)

Use backtesting across multiple rolling forecast origins. For this follow-up, also explain what code you would modify and how you would verify the change.

**File reference:** `app/backend/src/app/ml/demand_forecasting/preprocessing.py:57`

### Q489. How would you make model selection fairer? (applied follow-up 11)

Use the same train/test partitions and compare models on metrics aligned to business cost. For this follow-up, also explain what code you would modify and how you would verify the change.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/evaluate.py:48`

### Q490. How would you test feature order stability? (applied follow-up 12)

Assert get_feature_columns exactly matches the columns used for model fit and inference. For this follow-up, also explain what code you would modify and how you would verify the change.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/features.py:59`

### Q491. How would you improve PM class imbalance? (applied follow-up 12)

Use class weights, threshold tuning, resampling, and PR-AUC analysis. For this follow-up, also explain what code you would modify and how you would verify the change.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/preprocessing.py:50`

### Q492. How would you choose maintenance recall versus precision? (applied follow-up 12)

Use business costs: missed failures favor recall; costly false alarms favor precision. For this follow-up, also explain what code you would modify and how you would verify the change.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/evaluate.py:26`

### Q493. How would you make ANN results more reproducible? (applied follow-up 12)

Set Python, NumPy, and TensorFlow seeds and document nondeterministic hardware behavior. For this follow-up, also explain what code you would modify and how you would verify the change.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/train.py:20`

### Q494. How would you tune XGBoost? (applied follow-up 12)

Search n_estimators, max_depth, learning_rate, subsample, colsample_bytree, and regularization. For this follow-up, also explain what code you would modify and how you would verify the change.

**File reference:** `app/backend/src/app/ml/demand_forecasting/train.py:53`

### Q495. How would you tune Random Forest? (applied follow-up 12)

Tune n_estimators, max_depth, min_samples_split, min_samples_leaf, and max_features. For this follow-up, also explain what code you would modify and how you would verify the change.

**File reference:** `app/backend/src/app/ml/demand_forecasting/train.py:33`

### Q496. How would you tune ANN architecture? (applied follow-up 12)

Tune layer sizes, dropout rates, learning rate, batch size, patience, and epochs. For this follow-up, also explain what code you would modify and how you would verify the change.

**File reference:** `app/backend/src/app/ml/quality_inspection/train.py:20`

### Q497. How would you prove MLflow logging works? (applied follow-up 12)

Run a pipeline and show metrics, params, artifacts, and comparison JSON in MLflow UI. For this follow-up, also explain what code you would modify and how you would verify the change.

**File reference:** `app/backend/src/app/ml/demand_forecasting/model_store.py:41`

### Q498. How would you connect PM training to API inference? (applied follow-up 12)

Load the persisted model, reconstruct features, apply saved feature parameters, and call predict_proba. For this follow-up, also explain what code you would modify and how you would verify the change.

**File reference:** `app/backend/services.py:20`

### Q499. How would you avoid overclaiming deep learning? (applied follow-up 12)

Say ANN/LSTM are candidate models and final selection depends on evidence, not model hype. For this follow-up, also explain what code you would modify and how you would verify the change.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/evaluate.py:75`

### Q500. How would you explain why accuracy is misleading? (applied follow-up 12)

A rare-failure dataset can have high accuracy by always predicting no failure. For this follow-up, also explain what code you would modify and how you would verify the change.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/evaluate.py:25`

### Q501. How would you handle drift? (applied follow-up 12)

Monitor feature distributions and live performance, then retrain when drift is detected. For this follow-up, also explain what code you would modify and how you would verify the change.

**File reference:** `architecture.md:174`

### Q502. How would you add explainability? (applied follow-up 12)

Use feature importance and SHAP to show which inputs drive predictions. For this follow-up, also explain what code you would modify and how you would verify the change.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/train.py:76`

### Q503. How would you validate demand forecasts visually? (applied follow-up 12)

Plot actual versus predicted demand and inspect residuals by date, store, and item. For this follow-up, also explain what code you would modify and how you would verify the change.

**File reference:** `app/backend/src/app/ml/demand_forecasting/evaluate.py:94`

### Q504. How would you validate quality classifier errors? (applied follow-up 12)

Use a confusion matrix and class-wise recall to inspect confused defect classes. For this follow-up, also explain what code you would modify and how you would verify the change.

**File reference:** `app/backend/src/app/ml/quality_inspection/evaluate.py:29`

### Q505. How would you choose the PM probability threshold? (applied follow-up 12)

Use validation probabilities and a cost matrix for downtime, inspection cost, and missed failures. For this follow-up, also explain what code you would modify and how you would verify the change.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/evaluate.py:41`

## Count

Total questions: 505
