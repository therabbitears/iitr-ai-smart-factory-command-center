# Capstone Predictive Maintenance Questions and Answers

This file contains implementation-specific viva/interview questions for the IIT Roorkee AI Smart Factory Command Center capstone.

## Formula Sheet
- StandardScaler: z=(x-mean)/std.
- Sigmoid: p=1/(1+exp(-(w dot x+b))).
- Dense layer: output=activation(input dot kernel+bias).
- ReLU: max(0,x).
- Binary crossentropy: -mean(y log(p)+(1-y)log(1-p)).
- Dropout: drop activations with probability rate and scale remaining activations by 1/(1-rate).
- Precision=TP/(TP+FP), Recall=TP/(TP+FN), F1=2PR/(P+R), Accuracy=(TP+TN)/N.
- temp_delta=process_temperature-air_temperature.
- wear_rate=tool_wear/rotational_speed_min.
- torque_ratio=torque/rotational_speed_min.
- temperature_ratio=process_temperature/air_temp_min.

## Sources Consulted
- [sklearn LogisticRegression](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html)
- [sklearn RandomForestClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html)
- [sklearn StandardScaler](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.StandardScaler.html)
- [sklearn train_test_split](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html)
- [sklearn metrics](https://scikit-learn.org/stable/modules/model_evaluation.html)
- [XGBoost params](https://xgboost.readthedocs.io/en/stable/parameter.html)
- [Keras Dense](https://keras.io/2/api/layers/core_layers/dense/)
- [Keras Dropout](https://keras.io/api/layers/regularization_layers/dropout/)
- [Keras EarlyStopping](https://keras.io/api/callbacks/early_stopping/)
- [TensorFlow Adam](https://www.tensorflow.org/api_docs/python/tf/keras/optimizers/Adam)
- [TensorFlow binary_crossentropy](https://www.tensorflow.org/api_docs/python/tf/keras/losses/binary_crossentropy)
- [Pandera](https://pandera.readthedocs.io/en/stable/)
- [MLflow](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.html)
- [Pandas to_datetime](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.to_datetime.html)

## Questions


## Data Validation

### Q1. Why is `machine_id` important from the schema type perspective?

`machine_id` is treated as str because it represents asset identity. In this implementation the Pandera schema checks this before training, so invalid factory records are rejected early instead of silently corrupting the feature matrix, target labels, or audit trail.

**File reference:** `app/backend/src/app/data/loaders.py:128`

### Q2. Why is `machine_id` important from the missing value risk perspective?

`machine_id` is treated as str because it represents asset identity. In this implementation the Pandera schema checks this before training, so invalid factory records are rejected early instead of silently corrupting the feature matrix, target labels, or audit trail.

**File reference:** `app/backend/src/app/data/loaders.py:128`

### Q3. Why is `machine_id` important from the business meaning perspective?

`machine_id` is treated as str because it represents asset identity. In this implementation the Pandera schema checks this before training, so invalid factory records are rejected early instead of silently corrupting the feature matrix, target labels, or audit trail.

**File reference:** `app/backend/src/app/data/loaders.py:128`

### Q4. Why is `machine_id` important from the model impact perspective?

`machine_id` is treated as str because it represents asset identity. In this implementation the Pandera schema checks this before training, so invalid factory records are rejected early instead of silently corrupting the feature matrix, target labels, or audit trail.

**File reference:** `app/backend/src/app/data/loaders.py:128`

### Q5. Why is `machine_id` important from the validation defense perspective?

`machine_id` is treated as str because it represents asset identity. In this implementation the Pandera schema checks this before training, so invalid factory records are rejected early instead of silently corrupting the feature matrix, target labels, or audit trail.

**File reference:** `app/backend/src/app/data/loaders.py:128`

### Q6. Why is `timestamp` important from the schema type perspective?

`timestamp` is treated as datetime because it represents sensor event time. In this implementation the Pandera schema checks this before training, so invalid factory records are rejected early instead of silently corrupting the feature matrix, target labels, or audit trail.

**File reference:** `app/backend/src/app/data/loaders.py:129`

### Q7. Why is `timestamp` important from the missing value risk perspective?

`timestamp` is treated as datetime because it represents sensor event time. In this implementation the Pandera schema checks this before training, so invalid factory records are rejected early instead of silently corrupting the feature matrix, target labels, or audit trail.

**File reference:** `app/backend/src/app/data/loaders.py:129`

### Q8. Why is `timestamp` important from the business meaning perspective?

`timestamp` is treated as datetime because it represents sensor event time. In this implementation the Pandera schema checks this before training, so invalid factory records are rejected early instead of silently corrupting the feature matrix, target labels, or audit trail.

**File reference:** `app/backend/src/app/data/loaders.py:129`

### Q9. Why is `timestamp` important from the model impact perspective?

`timestamp` is treated as datetime because it represents sensor event time. In this implementation the Pandera schema checks this before training, so invalid factory records are rejected early instead of silently corrupting the feature matrix, target labels, or audit trail.

**File reference:** `app/backend/src/app/data/loaders.py:129`

### Q10. Why is `timestamp` important from the validation defense perspective?

`timestamp` is treated as datetime because it represents sensor event time. In this implementation the Pandera schema checks this before training, so invalid factory records are rejected early instead of silently corrupting the feature matrix, target labels, or audit trail.

**File reference:** `app/backend/src/app/data/loaders.py:129`

### Q11. Why is `air_temperature` important from the schema type perspective?

`air_temperature` is treated as float 0..100 because it represents ambient heat. In this implementation the Pandera schema checks this before training, so invalid factory records are rejected early instead of silently corrupting the feature matrix, target labels, or audit trail.

**File reference:** `app/backend/src/app/data/loaders.py:130`; `app/backend/src/app/ml/predictive_maintenance/features.py:10`

### Q12. Why is `air_temperature` important from the missing value risk perspective?

`air_temperature` is treated as float 0..100 because it represents ambient heat. In this implementation the Pandera schema checks this before training, so invalid factory records are rejected early instead of silently corrupting the feature matrix, target labels, or audit trail.

**File reference:** `app/backend/src/app/data/loaders.py:130`; `app/backend/src/app/ml/predictive_maintenance/features.py:10`

### Q13. Why is `air_temperature` important from the business meaning perspective?

`air_temperature` is treated as float 0..100 because it represents ambient heat. In this implementation the Pandera schema checks this before training, so invalid factory records are rejected early instead of silently corrupting the feature matrix, target labels, or audit trail.

**File reference:** `app/backend/src/app/data/loaders.py:130`; `app/backend/src/app/ml/predictive_maintenance/features.py:10`

### Q14. Why is `air_temperature` important from the model impact perspective?

`air_temperature` is treated as float 0..100 because it represents ambient heat. In this implementation the Pandera schema checks this before training, so invalid factory records are rejected early instead of silently corrupting the feature matrix, target labels, or audit trail.

**File reference:** `app/backend/src/app/data/loaders.py:130`; `app/backend/src/app/ml/predictive_maintenance/features.py:10`

### Q15. Why is `air_temperature` important from the validation defense perspective?

`air_temperature` is treated as float 0..100 because it represents ambient heat. In this implementation the Pandera schema checks this before training, so invalid factory records are rejected early instead of silently corrupting the feature matrix, target labels, or audit trail.

**File reference:** `app/backend/src/app/data/loaders.py:130`; `app/backend/src/app/ml/predictive_maintenance/features.py:10`

### Q16. Why is `process_temperature` important from the schema type perspective?

`process_temperature` is treated as float 0..200 because it represents process heat. In this implementation the Pandera schema checks this before training, so invalid factory records are rejected early instead of silently corrupting the feature matrix, target labels, or audit trail.

**File reference:** `app/backend/src/app/data/loaders.py:131`; `app/backend/src/app/ml/predictive_maintenance/features.py:11`

### Q17. Why is `process_temperature` important from the missing value risk perspective?

`process_temperature` is treated as float 0..200 because it represents process heat. In this implementation the Pandera schema checks this before training, so invalid factory records are rejected early instead of silently corrupting the feature matrix, target labels, or audit trail.

**File reference:** `app/backend/src/app/data/loaders.py:131`; `app/backend/src/app/ml/predictive_maintenance/features.py:11`

### Q18. Why is `process_temperature` important from the business meaning perspective?

`process_temperature` is treated as float 0..200 because it represents process heat. In this implementation the Pandera schema checks this before training, so invalid factory records are rejected early instead of silently corrupting the feature matrix, target labels, or audit trail.

**File reference:** `app/backend/src/app/data/loaders.py:131`; `app/backend/src/app/ml/predictive_maintenance/features.py:11`

### Q19. Why is `process_temperature` important from the model impact perspective?

`process_temperature` is treated as float 0..200 because it represents process heat. In this implementation the Pandera schema checks this before training, so invalid factory records are rejected early instead of silently corrupting the feature matrix, target labels, or audit trail.

**File reference:** `app/backend/src/app/data/loaders.py:131`; `app/backend/src/app/ml/predictive_maintenance/features.py:11`

### Q20. Why is `process_temperature` important from the validation defense perspective?

`process_temperature` is treated as float 0..200 because it represents process heat. In this implementation the Pandera schema checks this before training, so invalid factory records are rejected early instead of silently corrupting the feature matrix, target labels, or audit trail.

**File reference:** `app/backend/src/app/data/loaders.py:131`; `app/backend/src/app/ml/predictive_maintenance/features.py:11`

### Q21. Why is `rotational_speed` important from the schema type perspective?

`rotational_speed` is treated as float >=0 because it represents shaft speed. In this implementation the Pandera schema checks this before training, so invalid factory records are rejected early instead of silently corrupting the feature matrix, target labels, or audit trail.

**File reference:** `app/backend/src/app/data/loaders.py:132`; `app/backend/src/app/ml/predictive_maintenance/features.py:12`

### Q22. Why is `rotational_speed` important from the missing value risk perspective?

`rotational_speed` is treated as float >=0 because it represents shaft speed. In this implementation the Pandera schema checks this before training, so invalid factory records are rejected early instead of silently corrupting the feature matrix, target labels, or audit trail.

**File reference:** `app/backend/src/app/data/loaders.py:132`; `app/backend/src/app/ml/predictive_maintenance/features.py:12`

### Q23. Why is `rotational_speed` important from the business meaning perspective?

`rotational_speed` is treated as float >=0 because it represents shaft speed. In this implementation the Pandera schema checks this before training, so invalid factory records are rejected early instead of silently corrupting the feature matrix, target labels, or audit trail.

**File reference:** `app/backend/src/app/data/loaders.py:132`; `app/backend/src/app/ml/predictive_maintenance/features.py:12`

### Q24. Why is `rotational_speed` important from the model impact perspective?

`rotational_speed` is treated as float >=0 because it represents shaft speed. In this implementation the Pandera schema checks this before training, so invalid factory records are rejected early instead of silently corrupting the feature matrix, target labels, or audit trail.

**File reference:** `app/backend/src/app/data/loaders.py:132`; `app/backend/src/app/ml/predictive_maintenance/features.py:12`

### Q25. Why is `rotational_speed` important from the validation defense perspective?

`rotational_speed` is treated as float >=0 because it represents shaft speed. In this implementation the Pandera schema checks this before training, so invalid factory records are rejected early instead of silently corrupting the feature matrix, target labels, or audit trail.

**File reference:** `app/backend/src/app/data/loaders.py:132`; `app/backend/src/app/ml/predictive_maintenance/features.py:12`

### Q26. Why is `torque` important from the schema type perspective?

`torque` is treated as float >=0 because it represents rotational force. In this implementation the Pandera schema checks this before training, so invalid factory records are rejected early instead of silently corrupting the feature matrix, target labels, or audit trail.

**File reference:** `app/backend/src/app/data/loaders.py:133`; `app/backend/src/app/ml/predictive_maintenance/features.py:13`

### Q27. Why is `torque` important from the missing value risk perspective?

`torque` is treated as float >=0 because it represents rotational force. In this implementation the Pandera schema checks this before training, so invalid factory records are rejected early instead of silently corrupting the feature matrix, target labels, or audit trail.

**File reference:** `app/backend/src/app/data/loaders.py:133`; `app/backend/src/app/ml/predictive_maintenance/features.py:13`

### Q28. Why is `torque` important from the business meaning perspective?

`torque` is treated as float >=0 because it represents rotational force. In this implementation the Pandera schema checks this before training, so invalid factory records are rejected early instead of silently corrupting the feature matrix, target labels, or audit trail.

**File reference:** `app/backend/src/app/data/loaders.py:133`; `app/backend/src/app/ml/predictive_maintenance/features.py:13`

### Q29. Why is `torque` important from the model impact perspective?

`torque` is treated as float >=0 because it represents rotational force. In this implementation the Pandera schema checks this before training, so invalid factory records are rejected early instead of silently corrupting the feature matrix, target labels, or audit trail.

**File reference:** `app/backend/src/app/data/loaders.py:133`; `app/backend/src/app/ml/predictive_maintenance/features.py:13`

### Q30. Why is `torque` important from the validation defense perspective?

`torque` is treated as float >=0 because it represents rotational force. In this implementation the Pandera schema checks this before training, so invalid factory records are rejected early instead of silently corrupting the feature matrix, target labels, or audit trail.

**File reference:** `app/backend/src/app/data/loaders.py:133`; `app/backend/src/app/ml/predictive_maintenance/features.py:13`

### Q31. Why is `tool_wear` important from the schema type perspective?

`tool_wear` is treated as float 0..100 because it represents wear level. In this implementation the Pandera schema checks this before training, so invalid factory records are rejected early instead of silently corrupting the feature matrix, target labels, or audit trail.

**File reference:** `app/backend/src/app/data/loaders.py:134`; `app/backend/src/app/ml/predictive_maintenance/features.py:14`

### Q32. Why is `tool_wear` important from the missing value risk perspective?

`tool_wear` is treated as float 0..100 because it represents wear level. In this implementation the Pandera schema checks this before training, so invalid factory records are rejected early instead of silently corrupting the feature matrix, target labels, or audit trail.

**File reference:** `app/backend/src/app/data/loaders.py:134`; `app/backend/src/app/ml/predictive_maintenance/features.py:14`

### Q33. Why is `tool_wear` important from the business meaning perspective?

`tool_wear` is treated as float 0..100 because it represents wear level. In this implementation the Pandera schema checks this before training, so invalid factory records are rejected early instead of silently corrupting the feature matrix, target labels, or audit trail.

**File reference:** `app/backend/src/app/data/loaders.py:134`; `app/backend/src/app/ml/predictive_maintenance/features.py:14`

### Q34. Why is `tool_wear` important from the model impact perspective?

`tool_wear` is treated as float 0..100 because it represents wear level. In this implementation the Pandera schema checks this before training, so invalid factory records are rejected early instead of silently corrupting the feature matrix, target labels, or audit trail.

**File reference:** `app/backend/src/app/data/loaders.py:134`; `app/backend/src/app/ml/predictive_maintenance/features.py:14`

### Q35. Why is `tool_wear` important from the validation defense perspective?

`tool_wear` is treated as float 0..100 because it represents wear level. In this implementation the Pandera schema checks this before training, so invalid factory records are rejected early instead of silently corrupting the feature matrix, target labels, or audit trail.

**File reference:** `app/backend/src/app/data/loaders.py:134`; `app/backend/src/app/ml/predictive_maintenance/features.py:14`

### Q36. Why is `machine_failure` important from the schema type perspective?

`machine_failure` is treated as int in {0,1} because it represents binary target. In this implementation the Pandera schema checks this before training, so invalid factory records are rejected early instead of silently corrupting the feature matrix, target labels, or audit trail.

**File reference:** `app/backend/src/app/data/loaders.py:135`; `app/backend/src/app/ml/predictive_maintenance/preprocessing.py:18`

### Q37. Why is `machine_failure` important from the missing value risk perspective?

`machine_failure` is treated as int in {0,1} because it represents binary target. In this implementation the Pandera schema checks this before training, so invalid factory records are rejected early instead of silently corrupting the feature matrix, target labels, or audit trail.

**File reference:** `app/backend/src/app/data/loaders.py:135`; `app/backend/src/app/ml/predictive_maintenance/preprocessing.py:18`

### Q38. Why is `machine_failure` important from the business meaning perspective?

`machine_failure` is treated as int in {0,1} because it represents binary target. In this implementation the Pandera schema checks this before training, so invalid factory records are rejected early instead of silently corrupting the feature matrix, target labels, or audit trail.

**File reference:** `app/backend/src/app/data/loaders.py:135`; `app/backend/src/app/ml/predictive_maintenance/preprocessing.py:18`

### Q39. Why is `machine_failure` important from the model impact perspective?

`machine_failure` is treated as int in {0,1} because it represents binary target. In this implementation the Pandera schema checks this before training, so invalid factory records are rejected early instead of silently corrupting the feature matrix, target labels, or audit trail.

**File reference:** `app/backend/src/app/data/loaders.py:135`; `app/backend/src/app/ml/predictive_maintenance/preprocessing.py:18`

### Q40. Why is `machine_failure` important from the validation defense perspective?

`machine_failure` is treated as int in {0,1} because it represents binary target. In this implementation the Pandera schema checks this before training, so invalid factory records are rejected early instead of silently corrupting the feature matrix, target labels, or audit trail.

**File reference:** `app/backend/src/app/data/loaders.py:135`; `app/backend/src/app/ml/predictive_maintenance/preprocessing.py:18`

### Q41. Why is `failure_type` important from the schema type perspective?

`failure_type` is treated as str because it represents failure category. In this implementation the Pandera schema checks this before training, so invalid factory records are rejected early instead of silently corrupting the feature matrix, target labels, or audit trail.

**File reference:** `app/backend/src/app/data/loaders.py:136`

### Q42. Why is `failure_type` important from the missing value risk perspective?

`failure_type` is treated as str because it represents failure category. In this implementation the Pandera schema checks this before training, so invalid factory records are rejected early instead of silently corrupting the feature matrix, target labels, or audit trail.

**File reference:** `app/backend/src/app/data/loaders.py:136`

### Q43. Why is `failure_type` important from the business meaning perspective?

`failure_type` is treated as str because it represents failure category. In this implementation the Pandera schema checks this before training, so invalid factory records are rejected early instead of silently corrupting the feature matrix, target labels, or audit trail.

**File reference:** `app/backend/src/app/data/loaders.py:136`

### Q44. Why is `failure_type` important from the model impact perspective?

`failure_type` is treated as str because it represents failure category. In this implementation the Pandera schema checks this before training, so invalid factory records are rejected early instead of silently corrupting the feature matrix, target labels, or audit trail.

**File reference:** `app/backend/src/app/data/loaders.py:136`

### Q45. Why is `failure_type` important from the validation defense perspective?

`failure_type` is treated as str because it represents failure category. In this implementation the Pandera schema checks this before training, so invalid factory records are rejected early instead of silently corrupting the feature matrix, target labels, or audit trail.

**File reference:** `app/backend/src/app/data/loaders.py:136`

## Validation Engine

### Q46. why used: `DataFrameSchema`?

`DataFrameSchema` is used for table contract. It makes data quality explicit, reproducible, and explainable. If removed, the pipeline may train on malformed data or fail later with weaker diagnostic information.

**File reference:** `app/backend/src/app/data/loaders.py:126`

### Q47. what risk reduced: `DataFrameSchema`?

`DataFrameSchema` is used for table contract. It makes data quality explicit, reproducible, and explainable. If removed, the pipeline may train on malformed data or fail later with weaker diagnostic information.

**File reference:** `app/backend/src/app/data/loaders.py:126`

### Q48. how to defend: `DataFrameSchema`?

`DataFrameSchema` is used for table contract. It makes data quality explicit, reproducible, and explainable. If removed, the pipeline may train on malformed data or fail later with weaker diagnostic information.

**File reference:** `app/backend/src/app/data/loaders.py:126`

### Q49. what happens if removed: `DataFrameSchema`?

`DataFrameSchema` is used for table contract. It makes data quality explicit, reproducible, and explainable. If removed, the pipeline may train on malformed data or fail later with weaker diagnostic information.

**File reference:** `app/backend/src/app/data/loaders.py:126`

### Q50. why used: `Column`?

`Column` is used for column contract. It makes data quality explicit, reproducible, and explainable. If removed, the pipeline may train on malformed data or fail later with weaker diagnostic information.

**File reference:** `app/backend/src/app/data/loaders.py:128`

### Q51. what risk reduced: `Column`?

`Column` is used for column contract. It makes data quality explicit, reproducible, and explainable. If removed, the pipeline may train on malformed data or fail later with weaker diagnostic information.

**File reference:** `app/backend/src/app/data/loaders.py:128`

### Q52. how to defend: `Column`?

`Column` is used for column contract. It makes data quality explicit, reproducible, and explainable. If removed, the pipeline may train on malformed data or fail later with weaker diagnostic information.

**File reference:** `app/backend/src/app/data/loaders.py:128`

### Q53. what happens if removed: `Column`?

`Column` is used for column contract. It makes data quality explicit, reproducible, and explainable. If removed, the pipeline may train on malformed data or fail later with weaker diagnostic information.

**File reference:** `app/backend/src/app/data/loaders.py:128`

### Q54. why used: `nullable=False`?

`nullable=False` is used for no missing core values. It makes data quality explicit, reproducible, and explainable. If removed, the pipeline may train on malformed data or fail later with weaker diagnostic information.

**File reference:** `app/backend/src/app/data/loaders.py:128`

### Q55. what risk reduced: `nullable=False`?

`nullable=False` is used for no missing core values. It makes data quality explicit, reproducible, and explainable. If removed, the pipeline may train on malformed data or fail later with weaker diagnostic information.

**File reference:** `app/backend/src/app/data/loaders.py:128`

### Q56. how to defend: `nullable=False`?

`nullable=False` is used for no missing core values. It makes data quality explicit, reproducible, and explainable. If removed, the pipeline may train on malformed data or fail later with weaker diagnostic information.

**File reference:** `app/backend/src/app/data/loaders.py:128`

### Q57. what happens if removed: `nullable=False`?

`nullable=False` is used for no missing core values. It makes data quality explicit, reproducible, and explainable. If removed, the pipeline may train on malformed data or fail later with weaker diagnostic information.

**File reference:** `app/backend/src/app/data/loaders.py:128`

### Q58. why used: `Check.in_range`?

`Check.in_range` is used for physical bounds. It makes data quality explicit, reproducible, and explainable. If removed, the pipeline may train on malformed data or fail later with weaker diagnostic information.

**File reference:** `app/backend/src/app/data/loaders.py:130`

### Q59. what risk reduced: `Check.in_range`?

`Check.in_range` is used for physical bounds. It makes data quality explicit, reproducible, and explainable. If removed, the pipeline may train on malformed data or fail later with weaker diagnostic information.

**File reference:** `app/backend/src/app/data/loaders.py:130`

### Q60. how to defend: `Check.in_range`?

`Check.in_range` is used for physical bounds. It makes data quality explicit, reproducible, and explainable. If removed, the pipeline may train on malformed data or fail later with weaker diagnostic information.

**File reference:** `app/backend/src/app/data/loaders.py:130`

### Q61. what happens if removed: `Check.in_range`?

`Check.in_range` is used for physical bounds. It makes data quality explicit, reproducible, and explainable. If removed, the pipeline may train on malformed data or fail later with weaker diagnostic information.

**File reference:** `app/backend/src/app/data/loaders.py:130`

### Q62. why used: `Check.ge(0)`?

`Check.ge(0)` is used for non-negative physical quantities. It makes data quality explicit, reproducible, and explainable. If removed, the pipeline may train on malformed data or fail later with weaker diagnostic information.

**File reference:** `app/backend/src/app/data/loaders.py:132`

### Q63. what risk reduced: `Check.ge(0)`?

`Check.ge(0)` is used for non-negative physical quantities. It makes data quality explicit, reproducible, and explainable. If removed, the pipeline may train on malformed data or fail later with weaker diagnostic information.

**File reference:** `app/backend/src/app/data/loaders.py:132`

### Q64. how to defend: `Check.ge(0)`?

`Check.ge(0)` is used for non-negative physical quantities. It makes data quality explicit, reproducible, and explainable. If removed, the pipeline may train on malformed data or fail later with weaker diagnostic information.

**File reference:** `app/backend/src/app/data/loaders.py:132`

### Q65. what happens if removed: `Check.ge(0)`?

`Check.ge(0)` is used for non-negative physical quantities. It makes data quality explicit, reproducible, and explainable. If removed, the pipeline may train on malformed data or fail later with weaker diagnostic information.

**File reference:** `app/backend/src/app/data/loaders.py:132`

### Q66. why used: `Check.isin([0,1])`?

`Check.isin([0,1])` is used for binary labels. It makes data quality explicit, reproducible, and explainable. If removed, the pipeline may train on malformed data or fail later with weaker diagnostic information.

**File reference:** `app/backend/src/app/data/loaders.py:135`

### Q67. what risk reduced: `Check.isin([0,1])`?

`Check.isin([0,1])` is used for binary labels. It makes data quality explicit, reproducible, and explainable. If removed, the pipeline may train on malformed data or fail later with weaker diagnostic information.

**File reference:** `app/backend/src/app/data/loaders.py:135`

### Q68. how to defend: `Check.isin([0,1])`?

`Check.isin([0,1])` is used for binary labels. It makes data quality explicit, reproducible, and explainable. If removed, the pipeline may train on malformed data or fail later with weaker diagnostic information.

**File reference:** `app/backend/src/app/data/loaders.py:135`

### Q69. what happens if removed: `Check.isin([0,1])`?

`Check.isin([0,1])` is used for binary labels. It makes data quality explicit, reproducible, and explainable. If removed, the pipeline may train on malformed data or fail later with weaker diagnostic information.

**File reference:** `app/backend/src/app/data/loaders.py:135`

### Q70. why used: `strict=True`?

`strict=True` is used for no unexpected columns or leakage. It makes data quality explicit, reproducible, and explainable. If removed, the pipeline may train on malformed data or fail later with weaker diagnostic information.

**File reference:** `app/backend/src/app/data/loaders.py:138`

### Q71. what risk reduced: `strict=True`?

`strict=True` is used for no unexpected columns or leakage. It makes data quality explicit, reproducible, and explainable. If removed, the pipeline may train on malformed data or fail later with weaker diagnostic information.

**File reference:** `app/backend/src/app/data/loaders.py:138`

### Q72. how to defend: `strict=True`?

`strict=True` is used for no unexpected columns or leakage. It makes data quality explicit, reproducible, and explainable. If removed, the pipeline may train on malformed data or fail later with weaker diagnostic information.

**File reference:** `app/backend/src/app/data/loaders.py:138`

### Q73. what happens if removed: `strict=True`?

`strict=True` is used for no unexpected columns or leakage. It makes data quality explicit, reproducible, and explainable. If removed, the pipeline may train on malformed data or fail later with weaker diagnostic information.

**File reference:** `app/backend/src/app/data/loaders.py:138`

### Q74. why used: `lazy=True`?

`lazy=True` is used for collect many errors. It makes data quality explicit, reproducible, and explainable. If removed, the pipeline may train on malformed data or fail later with weaker diagnostic information.

**File reference:** `app/backend/src/app/data/validation.py:16`

### Q75. what risk reduced: `lazy=True`?

`lazy=True` is used for collect many errors. It makes data quality explicit, reproducible, and explainable. If removed, the pipeline may train on malformed data or fail later with weaker diagnostic information.

**File reference:** `app/backend/src/app/data/validation.py:16`

### Q76. how to defend: `lazy=True`?

`lazy=True` is used for collect many errors. It makes data quality explicit, reproducible, and explainable. If removed, the pipeline may train on malformed data or fail later with weaker diagnostic information.

**File reference:** `app/backend/src/app/data/validation.py:16`

### Q77. what happens if removed: `lazy=True`?

`lazy=True` is used for collect many errors. It makes data quality explicit, reproducible, and explainable. If removed, the pipeline may train on malformed data or fail later with weaker diagnostic information.

**File reference:** `app/backend/src/app/data/validation.py:16`

### Q78. why used: `SchemaError`?

`SchemaError` is used for structured exception. It makes data quality explicit, reproducible, and explainable. If removed, the pipeline may train on malformed data or fail later with weaker diagnostic information.

**File reference:** `app/backend/src/app/data/validation.py:5`

### Q79. what risk reduced: `SchemaError`?

`SchemaError` is used for structured exception. It makes data quality explicit, reproducible, and explainable. If removed, the pipeline may train on malformed data or fail later with weaker diagnostic information.

**File reference:** `app/backend/src/app/data/validation.py:5`

### Q80. how to defend: `SchemaError`?

`SchemaError` is used for structured exception. It makes data quality explicit, reproducible, and explainable. If removed, the pipeline may train on malformed data or fail later with weaker diagnostic information.

**File reference:** `app/backend/src/app/data/validation.py:5`

### Q81. what happens if removed: `SchemaError`?

`SchemaError` is used for structured exception. It makes data quality explicit, reproducible, and explainable. If removed, the pipeline may train on malformed data or fail later with weaker diagnostic information.

**File reference:** `app/backend/src/app/data/validation.py:5`

### Q82. why used: `failure_cases`?

`failure_cases` is used for debuggable bad rows. It makes data quality explicit, reproducible, and explainable. If removed, the pipeline may train on malformed data or fail later with weaker diagnostic information.

**File reference:** `app/backend/src/app/data/validation.py:19`

### Q83. what risk reduced: `failure_cases`?

`failure_cases` is used for debuggable bad rows. It makes data quality explicit, reproducible, and explainable. If removed, the pipeline may train on malformed data or fail later with weaker diagnostic information.

**File reference:** `app/backend/src/app/data/validation.py:19`

### Q84. how to defend: `failure_cases`?

`failure_cases` is used for debuggable bad rows. It makes data quality explicit, reproducible, and explainable. If removed, the pipeline may train on malformed data or fail later with weaker diagnostic information.

**File reference:** `app/backend/src/app/data/validation.py:19`

### Q85. what happens if removed: `failure_cases`?

`failure_cases` is used for debuggable bad rows. It makes data quality explicit, reproducible, and explainable. If removed, the pipeline may train on malformed data or fail later with weaker diagnostic information.

**File reference:** `app/backend/src/app/data/validation.py:19`

## Loading and Cleaning

### Q86. What is the purpose of `Path(source_path)`?

`Path(source_path)` normalizes dataset path. This matters because ML quality depends heavily on reliable preprocessing; clean data prevents biased training, hidden runtime errors, and misleading metrics.

**File reference:** `app/backend/src/app/data/loaders.py:17`

### Q87. What is the failure mode of `Path(source_path)`?

`Path(source_path)` normalizes dataset path. This matters because ML quality depends heavily on reliable preprocessing; clean data prevents biased training, hidden runtime errors, and misleading metrics.

**File reference:** `app/backend/src/app/data/loaders.py:17`

### Q88. What is the capstone reasoning of `Path(source_path)`?

`Path(source_path)` normalizes dataset path. This matters because ML quality depends heavily on reliable preprocessing; clean data prevents biased training, hidden runtime errors, and misleading metrics.

**File reference:** `app/backend/src/app/data/loaders.py:17`

### Q89. What is the production reasoning of `Path(source_path)`?

`Path(source_path)` normalizes dataset path. This matters because ML quality depends heavily on reliable preprocessing; clean data prevents biased training, hidden runtime errors, and misleading metrics.

**File reference:** `app/backend/src/app/data/loaders.py:17`

### Q90. What is the purpose of `exists check`?

`exists check` fails fast for missing data. This matters because ML quality depends heavily on reliable preprocessing; clean data prevents biased training, hidden runtime errors, and misleading metrics.

**File reference:** `app/backend/src/app/data/loaders.py:38`

### Q91. What is the failure mode of `exists check`?

`exists check` fails fast for missing data. This matters because ML quality depends heavily on reliable preprocessing; clean data prevents biased training, hidden runtime errors, and misleading metrics.

**File reference:** `app/backend/src/app/data/loaders.py:38`

### Q92. What is the capstone reasoning of `exists check`?

`exists check` fails fast for missing data. This matters because ML quality depends heavily on reliable preprocessing; clean data prevents biased training, hidden runtime errors, and misleading metrics.

**File reference:** `app/backend/src/app/data/loaders.py:38`

### Q93. What is the production reasoning of `exists check`?

`exists check` fails fast for missing data. This matters because ML quality depends heavily on reliable preprocessing; clean data prevents biased training, hidden runtime errors, and misleading metrics.

**File reference:** `app/backend/src/app/data/loaders.py:38`

### Q94. What is the purpose of `.csv branch`?

`.csv branch` loads Kaggle CSV. This matters because ML quality depends heavily on reliable preprocessing; clean data prevents biased training, hidden runtime errors, and misleading metrics.

**File reference:** `app/backend/src/app/data/loaders.py:41`

### Q95. What is the failure mode of `.csv branch`?

`.csv branch` loads Kaggle CSV. This matters because ML quality depends heavily on reliable preprocessing; clean data prevents biased training, hidden runtime errors, and misleading metrics.

**File reference:** `app/backend/src/app/data/loaders.py:41`

### Q96. What is the capstone reasoning of `.csv branch`?

`.csv branch` loads Kaggle CSV. This matters because ML quality depends heavily on reliable preprocessing; clean data prevents biased training, hidden runtime errors, and misleading metrics.

**File reference:** `app/backend/src/app/data/loaders.py:41`

### Q97. What is the production reasoning of `.csv branch`?

`.csv branch` loads Kaggle CSV. This matters because ML quality depends heavily on reliable preprocessing; clean data prevents biased training, hidden runtime errors, and misleading metrics.

**File reference:** `app/backend/src/app/data/loaders.py:41`

### Q98. What is the purpose of `.parquet branch`?

`.parquet branch` supports efficient columnar files. This matters because ML quality depends heavily on reliable preprocessing; clean data prevents biased training, hidden runtime errors, and misleading metrics.

**File reference:** `app/backend/src/app/data/loaders.py:43`

### Q99. What is the failure mode of `.parquet branch`?

`.parquet branch` supports efficient columnar files. This matters because ML quality depends heavily on reliable preprocessing; clean data prevents biased training, hidden runtime errors, and misleading metrics.

**File reference:** `app/backend/src/app/data/loaders.py:43`

### Q100. What is the capstone reasoning of `.parquet branch`?

`.parquet branch` supports efficient columnar files. This matters because ML quality depends heavily on reliable preprocessing; clean data prevents biased training, hidden runtime errors, and misleading metrics.

**File reference:** `app/backend/src/app/data/loaders.py:43`

### Q101. What is the production reasoning of `.parquet branch`?

`.parquet branch` supports efficient columnar files. This matters because ML quality depends heavily on reliable preprocessing; clean data prevents biased training, hidden runtime errors, and misleading metrics.

**File reference:** `app/backend/src/app/data/loaders.py:43`

### Q102. What is the purpose of `parse_dates`?

`parse_dates` handles timestamp columns. This matters because ML quality depends heavily on reliable preprocessing; clean data prevents biased training, hidden runtime errors, and misleading metrics.

**File reference:** `app/backend/src/app/data/loaders.py:41`

### Q103. What is the failure mode of `parse_dates`?

`parse_dates` handles timestamp columns. This matters because ML quality depends heavily on reliable preprocessing; clean data prevents biased training, hidden runtime errors, and misleading metrics.

**File reference:** `app/backend/src/app/data/loaders.py:41`

### Q104. What is the capstone reasoning of `parse_dates`?

`parse_dates` handles timestamp columns. This matters because ML quality depends heavily on reliable preprocessing; clean data prevents biased training, hidden runtime errors, and misleading metrics.

**File reference:** `app/backend/src/app/data/loaders.py:41`

### Q105. What is the production reasoning of `parse_dates`?

`parse_dates` handles timestamp columns. This matters because ML quality depends heavily on reliable preprocessing; clean data prevents biased training, hidden runtime errors, and misleading metrics.

**File reference:** `app/backend/src/app/data/loaders.py:41`

### Q106. What is the purpose of `_normalize_columns`?

`_normalize_columns` strips header whitespace. This matters because ML quality depends heavily on reliable preprocessing; clean data prevents biased training, hidden runtime errors, and misleading metrics.

**File reference:** `app/backend/src/app/data/loaders.py:49`

### Q107. What is the failure mode of `_normalize_columns`?

`_normalize_columns` strips header whitespace. This matters because ML quality depends heavily on reliable preprocessing; clean data prevents biased training, hidden runtime errors, and misleading metrics.

**File reference:** `app/backend/src/app/data/loaders.py:49`

### Q108. What is the capstone reasoning of `_normalize_columns`?

`_normalize_columns` strips header whitespace. This matters because ML quality depends heavily on reliable preprocessing; clean data prevents biased training, hidden runtime errors, and misleading metrics.

**File reference:** `app/backend/src/app/data/loaders.py:49`

### Q109. What is the production reasoning of `_normalize_columns`?

`_normalize_columns` strips header whitespace. This matters because ML quality depends heavily on reliable preprocessing; clean data prevents biased training, hidden runtime errors, and misleading metrics.

**File reference:** `app/backend/src/app/data/loaders.py:49`

### Q110. What is the purpose of `df.copy()`?

`df.copy()` avoids mutating caller data. This matters because ML quality depends heavily on reliable preprocessing; clean data prevents biased training, hidden runtime errors, and misleading metrics.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/preprocessing.py:22`

### Q111. What is the failure mode of `df.copy()`?

`df.copy()` avoids mutating caller data. This matters because ML quality depends heavily on reliable preprocessing; clean data prevents biased training, hidden runtime errors, and misleading metrics.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/preprocessing.py:22`

### Q112. What is the capstone reasoning of `df.copy()`?

`df.copy()` avoids mutating caller data. This matters because ML quality depends heavily on reliable preprocessing; clean data prevents biased training, hidden runtime errors, and misleading metrics.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/preprocessing.py:22`

### Q113. What is the production reasoning of `df.copy()`?

`df.copy()` avoids mutating caller data. This matters because ML quality depends heavily on reliable preprocessing; clean data prevents biased training, hidden runtime errors, and misleading metrics.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/preprocessing.py:22`

### Q114. What is the purpose of `drop_duplicates()`?

`drop_duplicates()` removes repeated records. This matters because ML quality depends heavily on reliable preprocessing; clean data prevents biased training, hidden runtime errors, and misleading metrics.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/preprocessing.py:25`

### Q115. What is the failure mode of `drop_duplicates()`?

`drop_duplicates()` removes repeated records. This matters because ML quality depends heavily on reliable preprocessing; clean data prevents biased training, hidden runtime errors, and misleading metrics.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/preprocessing.py:25`

### Q116. What is the capstone reasoning of `drop_duplicates()`?

`drop_duplicates()` removes repeated records. This matters because ML quality depends heavily on reliable preprocessing; clean data prevents biased training, hidden runtime errors, and misleading metrics.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/preprocessing.py:25`

### Q117. What is the production reasoning of `drop_duplicates()`?

`drop_duplicates()` removes repeated records. This matters because ML quality depends heavily on reliable preprocessing; clean data prevents biased training, hidden runtime errors, and misleading metrics.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/preprocessing.py:25`

### Q118. What is the purpose of `pd.to_datetime(...,utc=True)`?

`pd.to_datetime(...,utc=True)` standardizes timestamps. This matters because ML quality depends heavily on reliable preprocessing; clean data prevents biased training, hidden runtime errors, and misleading metrics.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/preprocessing.py:28`

### Q119. What is the failure mode of `pd.to_datetime(...,utc=True)`?

`pd.to_datetime(...,utc=True)` standardizes timestamps. This matters because ML quality depends heavily on reliable preprocessing; clean data prevents biased training, hidden runtime errors, and misleading metrics.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/preprocessing.py:28`

### Q120. What is the capstone reasoning of `pd.to_datetime(...,utc=True)`?

`pd.to_datetime(...,utc=True)` standardizes timestamps. This matters because ML quality depends heavily on reliable preprocessing; clean data prevents biased training, hidden runtime errors, and misleading metrics.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/preprocessing.py:28`

### Q121. What is the production reasoning of `pd.to_datetime(...,utc=True)`?

`pd.to_datetime(...,utc=True)` standardizes timestamps. This matters because ML quality depends heavily on reliable preprocessing; clean data prevents biased training, hidden runtime errors, and misleading metrics.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/preprocessing.py:28`

### Q122. What is the purpose of `dropna(subset=features+target)`?

`dropna(subset=features+target)` keeps complete training rows. This matters because ML quality depends heavily on reliable preprocessing; clean data prevents biased training, hidden runtime errors, and misleading metrics.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/preprocessing.py:30`

### Q123. What is the failure mode of `dropna(subset=features+target)`?

`dropna(subset=features+target)` keeps complete training rows. This matters because ML quality depends heavily on reliable preprocessing; clean data prevents biased training, hidden runtime errors, and misleading metrics.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/preprocessing.py:30`

### Q124. What is the capstone reasoning of `dropna(subset=features+target)`?

`dropna(subset=features+target)` keeps complete training rows. This matters because ML quality depends heavily on reliable preprocessing; clean data prevents biased training, hidden runtime errors, and misleading metrics.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/preprocessing.py:30`

### Q125. What is the production reasoning of `dropna(subset=features+target)`?

`dropna(subset=features+target)` keeps complete training rows. This matters because ML quality depends heavily on reliable preprocessing; clean data prevents biased training, hidden runtime errors, and misleading metrics.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/preprocessing.py:30`

### Q126. What is the purpose of `astype(int)`?

`astype(int)` makes labels class integers. This matters because ML quality depends heavily on reliable preprocessing; clean data prevents biased training, hidden runtime errors, and misleading metrics.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/preprocessing.py:72`

### Q127. What is the failure mode of `astype(int)`?

`astype(int)` makes labels class integers. This matters because ML quality depends heavily on reliable preprocessing; clean data prevents biased training, hidden runtime errors, and misleading metrics.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/preprocessing.py:72`

### Q128. What is the capstone reasoning of `astype(int)`?

`astype(int)` makes labels class integers. This matters because ML quality depends heavily on reliable preprocessing; clean data prevents biased training, hidden runtime errors, and misleading metrics.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/preprocessing.py:72`

### Q129. What is the production reasoning of `astype(int)`?

`astype(int)` makes labels class integers. This matters because ML quality depends heavily on reliable preprocessing; clean data prevents biased training, hidden runtime errors, and misleading metrics.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/preprocessing.py:72`

### Q130. What is the purpose of `validate_numeric_columns`?

`validate_numeric_columns` ensures model-ready numeric input. This matters because ML quality depends heavily on reliable preprocessing; clean data prevents biased training, hidden runtime errors, and misleading metrics.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/preprocessing.py:34`

### Q131. What is the failure mode of `validate_numeric_columns`?

`validate_numeric_columns` ensures model-ready numeric input. This matters because ML quality depends heavily on reliable preprocessing; clean data prevents biased training, hidden runtime errors, and misleading metrics.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/preprocessing.py:34`

### Q132. What is the capstone reasoning of `validate_numeric_columns`?

`validate_numeric_columns` ensures model-ready numeric input. This matters because ML quality depends heavily on reliable preprocessing; clean data prevents biased training, hidden runtime errors, and misleading metrics.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/preprocessing.py:34`

### Q133. What is the production reasoning of `validate_numeric_columns`?

`validate_numeric_columns` ensures model-ready numeric input. This matters because ML quality depends heavily on reliable preprocessing; clean data prevents biased training, hidden runtime errors, and misleading metrics.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/preprocessing.py:34`

## Feature Engineering

### Q134. formula: `temp_delta`?

`temp_delta` uses `process_temperature-air_temperature` and captures thermal stress. It is fitted after train/test split where needed, so test-set information does not influence training transformations.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/features.py:18`; `app/backend/src/app/ml/predictive_maintenance/features.py:49`

### Q135. why useful: `temp_delta`?

`temp_delta` uses `process_temperature-air_temperature` and captures thermal stress. It is fitted after train/test split where needed, so test-set information does not influence training transformations.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/features.py:18`; `app/backend/src/app/ml/predictive_maintenance/features.py:49`

### Q136. leakage prevention: `temp_delta`?

`temp_delta` uses `process_temperature-air_temperature` and captures thermal stress. It is fitted after train/test split where needed, so test-set information does not influence training transformations.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/features.py:18`; `app/backend/src/app/ml/predictive_maintenance/features.py:49`

### Q137. what if removed: `temp_delta`?

`temp_delta` uses `process_temperature-air_temperature` and captures thermal stress. It is fitted after train/test split where needed, so test-set information does not influence training transformations.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/features.py:18`; `app/backend/src/app/ml/predictive_maintenance/features.py:49`

### Q138. defense answer: `temp_delta`?

`temp_delta` uses `process_temperature-air_temperature` and captures thermal stress. It is fitted after train/test split where needed, so test-set information does not influence training transformations.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/features.py:18`; `app/backend/src/app/ml/predictive_maintenance/features.py:49`

### Q139. formula: `wear_rate`?

`wear_rate` uses `tool_wear/rotational_speed_min` and captures wear normalized by speed baseline. It is fitted after train/test split where needed, so test-set information does not influence training transformations.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/features.py:19`; `app/backend/src/app/ml/predictive_maintenance/features.py:50`

### Q140. why useful: `wear_rate`?

`wear_rate` uses `tool_wear/rotational_speed_min` and captures wear normalized by speed baseline. It is fitted after train/test split where needed, so test-set information does not influence training transformations.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/features.py:19`; `app/backend/src/app/ml/predictive_maintenance/features.py:50`

### Q141. leakage prevention: `wear_rate`?

`wear_rate` uses `tool_wear/rotational_speed_min` and captures wear normalized by speed baseline. It is fitted after train/test split where needed, so test-set information does not influence training transformations.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/features.py:19`; `app/backend/src/app/ml/predictive_maintenance/features.py:50`

### Q142. what if removed: `wear_rate`?

`wear_rate` uses `tool_wear/rotational_speed_min` and captures wear normalized by speed baseline. It is fitted after train/test split where needed, so test-set information does not influence training transformations.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/features.py:19`; `app/backend/src/app/ml/predictive_maintenance/features.py:50`

### Q143. defense answer: `wear_rate`?

`wear_rate` uses `tool_wear/rotational_speed_min` and captures wear normalized by speed baseline. It is fitted after train/test split where needed, so test-set information does not influence training transformations.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/features.py:19`; `app/backend/src/app/ml/predictive_maintenance/features.py:50`

### Q144. formula: `torque_ratio`?

`torque_ratio` uses `torque/rotational_speed_min` and captures load relative to speed baseline. It is fitted after train/test split where needed, so test-set information does not influence training transformations.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/features.py:20`; `app/backend/src/app/ml/predictive_maintenance/features.py:51`

### Q145. why useful: `torque_ratio`?

`torque_ratio` uses `torque/rotational_speed_min` and captures load relative to speed baseline. It is fitted after train/test split where needed, so test-set information does not influence training transformations.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/features.py:20`; `app/backend/src/app/ml/predictive_maintenance/features.py:51`

### Q146. leakage prevention: `torque_ratio`?

`torque_ratio` uses `torque/rotational_speed_min` and captures load relative to speed baseline. It is fitted after train/test split where needed, so test-set information does not influence training transformations.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/features.py:20`; `app/backend/src/app/ml/predictive_maintenance/features.py:51`

### Q147. what if removed: `torque_ratio`?

`torque_ratio` uses `torque/rotational_speed_min` and captures load relative to speed baseline. It is fitted after train/test split where needed, so test-set information does not influence training transformations.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/features.py:20`; `app/backend/src/app/ml/predictive_maintenance/features.py:51`

### Q148. defense answer: `torque_ratio`?

`torque_ratio` uses `torque/rotational_speed_min` and captures load relative to speed baseline. It is fitted after train/test split where needed, so test-set information does not influence training transformations.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/features.py:20`; `app/backend/src/app/ml/predictive_maintenance/features.py:51`

### Q149. formula: `temperature_ratio`?

`temperature_ratio` uses `process_temperature/air_temp_min` and captures process heat relative to ambient baseline. It is fitted after train/test split where needed, so test-set information does not influence training transformations.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/features.py:21`; `app/backend/src/app/ml/predictive_maintenance/features.py:52`

### Q150. why useful: `temperature_ratio`?

`temperature_ratio` uses `process_temperature/air_temp_min` and captures process heat relative to ambient baseline. It is fitted after train/test split where needed, so test-set information does not influence training transformations.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/features.py:21`; `app/backend/src/app/ml/predictive_maintenance/features.py:52`

### Q151. leakage prevention: `temperature_ratio`?

`temperature_ratio` uses `process_temperature/air_temp_min` and captures process heat relative to ambient baseline. It is fitted after train/test split where needed, so test-set information does not influence training transformations.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/features.py:21`; `app/backend/src/app/ml/predictive_maintenance/features.py:52`

### Q152. what if removed: `temperature_ratio`?

`temperature_ratio` uses `process_temperature/air_temp_min` and captures process heat relative to ambient baseline. It is fitted after train/test split where needed, so test-set information does not influence training transformations.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/features.py:21`; `app/backend/src/app/ml/predictive_maintenance/features.py:52`

### Q153. defense answer: `temperature_ratio`?

`temperature_ratio` uses `process_temperature/air_temp_min` and captures process heat relative to ambient baseline. It is fitted after train/test split where needed, so test-set information does not influence training transformations.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/features.py:21`; `app/backend/src/app/ml/predictive_maintenance/features.py:52`

### Q154. formula: `rotational_speed_min`?

`rotational_speed_min` uses `max(train min,1.0)` and captures safe denominator learned only from train. It is fitted after train/test split where needed, so test-set information does not influence training transformations.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/features.py:31`; `app/backend/src/app/ml/predictive_maintenance/features.py:37`

### Q155. why useful: `rotational_speed_min`?

`rotational_speed_min` uses `max(train min,1.0)` and captures safe denominator learned only from train. It is fitted after train/test split where needed, so test-set information does not influence training transformations.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/features.py:31`; `app/backend/src/app/ml/predictive_maintenance/features.py:37`

### Q156. leakage prevention: `rotational_speed_min`?

`rotational_speed_min` uses `max(train min,1.0)` and captures safe denominator learned only from train. It is fitted after train/test split where needed, so test-set information does not influence training transformations.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/features.py:31`; `app/backend/src/app/ml/predictive_maintenance/features.py:37`

### Q157. what if removed: `rotational_speed_min`?

`rotational_speed_min` uses `max(train min,1.0)` and captures safe denominator learned only from train. It is fitted after train/test split where needed, so test-set information does not influence training transformations.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/features.py:31`; `app/backend/src/app/ml/predictive_maintenance/features.py:37`

### Q158. defense answer: `rotational_speed_min`?

`rotational_speed_min` uses `max(train min,1.0)` and captures safe denominator learned only from train. It is fitted after train/test split where needed, so test-set information does not influence training transformations.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/features.py:31`; `app/backend/src/app/ml/predictive_maintenance/features.py:37`

### Q159. formula: `air_temp_min`?

`air_temp_min` uses `max(train min,1.0)` and captures safe denominator learned only from train. It is fitted after train/test split where needed, so test-set information does not influence training transformations.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/features.py:32`; `app/backend/src/app/ml/predictive_maintenance/features.py:38`

### Q160. why useful: `air_temp_min`?

`air_temp_min` uses `max(train min,1.0)` and captures safe denominator learned only from train. It is fitted after train/test split where needed, so test-set information does not influence training transformations.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/features.py:32`; `app/backend/src/app/ml/predictive_maintenance/features.py:38`

### Q161. leakage prevention: `air_temp_min`?

`air_temp_min` uses `max(train min,1.0)` and captures safe denominator learned only from train. It is fitted after train/test split where needed, so test-set information does not influence training transformations.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/features.py:32`; `app/backend/src/app/ml/predictive_maintenance/features.py:38`

### Q162. what if removed: `air_temp_min`?

`air_temp_min` uses `max(train min,1.0)` and captures safe denominator learned only from train. It is fitted after train/test split where needed, so test-set information does not influence training transformations.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/features.py:32`; `app/backend/src/app/ml/predictive_maintenance/features.py:38`

### Q163. defense answer: `air_temp_min`?

`air_temp_min` uses `max(train min,1.0)` and captures safe denominator learned only from train. It is fitted after train/test split where needed, so test-set information does not influence training transformations.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/features.py:32`; `app/backend/src/app/ml/predictive_maintenance/features.py:38`

### Q164. formula: `_is_fitted`?

`_is_fitted` uses `boolean guard` and captures prevents transform before fit. It is fitted after train/test split where needed, so test-set information does not influence training transformations.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/features.py:33`; `app/backend/src/app/ml/predictive_maintenance/features.py:46`

### Q165. why useful: `_is_fitted`?

`_is_fitted` uses `boolean guard` and captures prevents transform before fit. It is fitted after train/test split where needed, so test-set information does not influence training transformations.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/features.py:33`; `app/backend/src/app/ml/predictive_maintenance/features.py:46`

### Q166. leakage prevention: `_is_fitted`?

`_is_fitted` uses `boolean guard` and captures prevents transform before fit. It is fitted after train/test split where needed, so test-set information does not influence training transformations.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/features.py:33`; `app/backend/src/app/ml/predictive_maintenance/features.py:46`

### Q167. what if removed: `_is_fitted`?

`_is_fitted` uses `boolean guard` and captures prevents transform before fit. It is fitted after train/test split where needed, so test-set information does not influence training transformations.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/features.py:33`; `app/backend/src/app/ml/predictive_maintenance/features.py:46`

### Q168. defense answer: `_is_fitted`?

`_is_fitted` uses `boolean guard` and captures prevents transform before fit. It is fitted after train/test split where needed, so test-set information does not influence training transformations.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/features.py:33`; `app/backend/src/app/ml/predictive_maintenance/features.py:46`

### Q169. formula: `fit_transform`?

`fit_transform` uses `fit then transform` and captures convenience for training. It is fitted after train/test split where needed, so test-set information does not influence training transformations.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/features.py:55`

### Q170. why useful: `fit_transform`?

`fit_transform` uses `fit then transform` and captures convenience for training. It is fitted after train/test split where needed, so test-set information does not influence training transformations.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/features.py:55`

### Q171. leakage prevention: `fit_transform`?

`fit_transform` uses `fit then transform` and captures convenience for training. It is fitted after train/test split where needed, so test-set information does not influence training transformations.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/features.py:55`

### Q172. what if removed: `fit_transform`?

`fit_transform` uses `fit then transform` and captures convenience for training. It is fitted after train/test split where needed, so test-set information does not influence training transformations.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/features.py:55`

### Q173. defense answer: `fit_transform`?

`fit_transform` uses `fit then transform` and captures convenience for training. It is fitted after train/test split where needed, so test-set information does not influence training transformations.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/features.py:55`

## Splitting and Balance

### Q174. why chosen: `test_size=0.2`?

`test_size=0.2` gives 20 percent held-out test data. Predictive maintenance labels are often imbalanced, so the split must be reproducible and representative before evaluating F1, recall, precision, and ROC-AUC.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/preprocessing.py:67`; `app/backend/src/app/ml/predictive_maintenance/preprocessing.py:75`

### Q175. risk without it: `test_size=0.2`?

`test_size=0.2` gives 20 percent held-out test data. Predictive maintenance labels are often imbalanced, so the split must be reproducible and representative before evaluating F1, recall, precision, and ROC-AUC.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/preprocessing.py:67`; `app/backend/src/app/ml/predictive_maintenance/preprocessing.py:75`

### Q176. metric impact: `test_size=0.2`?

`test_size=0.2` gives 20 percent held-out test data. Predictive maintenance labels are often imbalanced, so the split must be reproducible and representative before evaluating F1, recall, precision, and ROC-AUC.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/preprocessing.py:67`; `app/backend/src/app/ml/predictive_maintenance/preprocessing.py:75`

### Q177. defense answer: `test_size=0.2`?

`test_size=0.2` gives 20 percent held-out test data. Predictive maintenance labels are often imbalanced, so the split must be reproducible and representative before evaluating F1, recall, precision, and ROC-AUC.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/preprocessing.py:67`; `app/backend/src/app/ml/predictive_maintenance/preprocessing.py:75`

### Q178. why chosen: `random_state=42`?

`random_state=42` gives reproducible split. Predictive maintenance labels are often imbalanced, so the split must be reproducible and representative before evaluating F1, recall, precision, and ROC-AUC.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/preprocessing.py:68`; `app/backend/src/app/ml/predictive_maintenance/train.py:47`

### Q179. risk without it: `random_state=42`?

`random_state=42` gives reproducible split. Predictive maintenance labels are often imbalanced, so the split must be reproducible and representative before evaluating F1, recall, precision, and ROC-AUC.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/preprocessing.py:68`; `app/backend/src/app/ml/predictive_maintenance/train.py:47`

### Q180. metric impact: `random_state=42`?

`random_state=42` gives reproducible split. Predictive maintenance labels are often imbalanced, so the split must be reproducible and representative before evaluating F1, recall, precision, and ROC-AUC.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/preprocessing.py:68`; `app/backend/src/app/ml/predictive_maintenance/train.py:47`

### Q181. defense answer: `random_state=42`?

`random_state=42` gives reproducible split. Predictive maintenance labels are often imbalanced, so the split must be reproducible and representative before evaluating F1, recall, precision, and ROC-AUC.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/preprocessing.py:68`; `app/backend/src/app/ml/predictive_maintenance/train.py:47`

### Q182. why chosen: `stratify=y`?

`stratify=y` gives class proportions preserved. Predictive maintenance labels are often imbalanced, so the split must be reproducible and representative before evaluating F1, recall, precision, and ROC-AUC.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/preprocessing.py:75`

### Q183. risk without it: `stratify=y`?

`stratify=y` gives class proportions preserved. Predictive maintenance labels are often imbalanced, so the split must be reproducible and representative before evaluating F1, recall, precision, and ROC-AUC.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/preprocessing.py:75`

### Q184. metric impact: `stratify=y`?

`stratify=y` gives class proportions preserved. Predictive maintenance labels are often imbalanced, so the split must be reproducible and representative before evaluating F1, recall, precision, and ROC-AUC.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/preprocessing.py:75`

### Q185. defense answer: `stratify=y`?

`stratify=y` gives class proportions preserved. Predictive maintenance labels are often imbalanced, so the split must be reproducible and representative before evaluating F1, recall, precision, and ROC-AUC.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/preprocessing.py:75`

### Q186. why chosen: `val_size=0.2`?

`val_size=0.2` gives ANN validation subset. Predictive maintenance labels are often imbalanced, so the split must be reproducible and representative before evaluating F1, recall, precision, and ROC-AUC.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/pipeline.py:151`; `app/backend/src/app/ml/predictive_maintenance/pipeline.py:156`

### Q187. risk without it: `val_size=0.2`?

`val_size=0.2` gives ANN validation subset. Predictive maintenance labels are often imbalanced, so the split must be reproducible and representative before evaluating F1, recall, precision, and ROC-AUC.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/pipeline.py:151`; `app/backend/src/app/ml/predictive_maintenance/pipeline.py:156`

### Q188. metric impact: `val_size=0.2`?

`val_size=0.2` gives ANN validation subset. Predictive maintenance labels are often imbalanced, so the split must be reproducible and representative before evaluating F1, recall, precision, and ROC-AUC.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/pipeline.py:151`; `app/backend/src/app/ml/predictive_maintenance/pipeline.py:156`

### Q189. defense answer: `val_size=0.2`?

`val_size=0.2` gives ANN validation subset. Predictive maintenance labels are often imbalanced, so the split must be reproducible and representative before evaluating F1, recall, precision, and ROC-AUC.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/pipeline.py:151`; `app/backend/src/app/ml/predictive_maintenance/pipeline.py:156`

### Q190. why chosen: `imbalance_ratio`?

`imbalance_ratio` gives failure rarity summary. Predictive maintenance labels are often imbalanced, so the split must be reproducible and representative before evaluating F1, recall, precision, and ROC-AUC.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/preprocessing.py:52`

### Q191. risk without it: `imbalance_ratio`?

`imbalance_ratio` gives failure rarity summary. Predictive maintenance labels are often imbalanced, so the split must be reproducible and representative before evaluating F1, recall, precision, and ROC-AUC.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/preprocessing.py:52`

### Q192. metric impact: `imbalance_ratio`?

`imbalance_ratio` gives failure rarity summary. Predictive maintenance labels are often imbalanced, so the split must be reproducible and representative before evaluating F1, recall, precision, and ROC-AUC.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/preprocessing.py:52`

### Q193. defense answer: `imbalance_ratio`?

`imbalance_ratio` gives failure rarity summary. Predictive maintenance labels are often imbalanced, so the split must be reproducible and representative before evaluating F1, recall, precision, and ROC-AUC.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/preprocessing.py:52`

### Q194. why chosen: `warning if >10`?

`warning if >10` gives flags severe imbalance. Predictive maintenance labels are often imbalanced, so the split must be reproducible and representative before evaluating F1, recall, precision, and ROC-AUC.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/pipeline.py:51`

### Q195. risk without it: `warning if >10`?

`warning if >10` gives flags severe imbalance. Predictive maintenance labels are often imbalanced, so the split must be reproducible and representative before evaluating F1, recall, precision, and ROC-AUC.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/pipeline.py:51`

### Q196. metric impact: `warning if >10`?

`warning if >10` gives flags severe imbalance. Predictive maintenance labels are often imbalanced, so the split must be reproducible and representative before evaluating F1, recall, precision, and ROC-AUC.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/pipeline.py:51`

### Q197. defense answer: `warning if >10`?

`warning if >10` gives flags severe imbalance. Predictive maintenance labels are often imbalanced, so the split must be reproducible and representative before evaluating F1, recall, precision, and ROC-AUC.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/pipeline.py:51`

### Q198. why chosen: `train_test_split`?

`train_test_split` gives standard partition function. Predictive maintenance labels are often imbalanced, so the split must be reproducible and representative before evaluating F1, recall, precision, and ROC-AUC.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/preprocessing.py:6`; `app/backend/src/app/ml/predictive_maintenance/preprocessing.py:74`

### Q199. risk without it: `train_test_split`?

`train_test_split` gives standard partition function. Predictive maintenance labels are often imbalanced, so the split must be reproducible and representative before evaluating F1, recall, precision, and ROC-AUC.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/preprocessing.py:6`; `app/backend/src/app/ml/predictive_maintenance/preprocessing.py:74`

### Q200. metric impact: `train_test_split`?

`train_test_split` gives standard partition function. Predictive maintenance labels are often imbalanced, so the split must be reproducible and representative before evaluating F1, recall, precision, and ROC-AUC.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/preprocessing.py:6`; `app/backend/src/app/ml/predictive_maintenance/preprocessing.py:74`

### Q201. defense answer: `train_test_split`?

`train_test_split` gives standard partition function. Predictive maintenance labels are often imbalanced, so the split must be reproducible and representative before evaluating F1, recall, precision, and ROC-AUC.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/preprocessing.py:6`; `app/backend/src/app/ml/predictive_maintenance/preprocessing.py:74`

## StandardScaler

### Q202. why used: `StandardScaler`?

`StandardScaler` standardizes features. It is crucial for gradient/linear models because large-scale features can dominate optimization. Tree models need it less, but the common pipeline keeps comparison consistent.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/train.py:10`; `app/backend/src/app/ml/predictive_maintenance/train.py:59`

### Q203. formula link: `StandardScaler`?

`StandardScaler` standardizes features. It is crucial for gradient/linear models because large-scale features can dominate optimization. Tree models need it less, but the common pipeline keeps comparison consistent.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/train.py:10`; `app/backend/src/app/ml/predictive_maintenance/train.py:59`

### Q204. effect on Logistic Regression: `StandardScaler`?

`StandardScaler` standardizes features. It is crucial for gradient/linear models because large-scale features can dominate optimization. Tree models need it less, but the common pipeline keeps comparison consistent.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/train.py:10`; `app/backend/src/app/ml/predictive_maintenance/train.py:59`

### Q205. effect on ANN: `StandardScaler`?

`StandardScaler` standardizes features. It is crucial for gradient/linear models because large-scale features can dominate optimization. Tree models need it less, but the common pipeline keeps comparison consistent.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/train.py:10`; `app/backend/src/app/ml/predictive_maintenance/train.py:59`

### Q206. effect on trees: `StandardScaler`?

`StandardScaler` standardizes features. It is crucial for gradient/linear models because large-scale features can dominate optimization. Tree models need it less, but the common pipeline keeps comparison consistent.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/train.py:10`; `app/backend/src/app/ml/predictive_maintenance/train.py:59`

### Q207. why used: `with_mean=True default`?

`with_mean=True default` subtracts mean. It is crucial for gradient/linear models because large-scale features can dominate optimization. Tree models need it less, but the common pipeline keeps comparison consistent.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/train.py:59`

### Q208. formula link: `with_mean=True default`?

`with_mean=True default` subtracts mean. It is crucial for gradient/linear models because large-scale features can dominate optimization. Tree models need it less, but the common pipeline keeps comparison consistent.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/train.py:59`

### Q209. effect on Logistic Regression: `with_mean=True default`?

`with_mean=True default` subtracts mean. It is crucial for gradient/linear models because large-scale features can dominate optimization. Tree models need it less, but the common pipeline keeps comparison consistent.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/train.py:59`

### Q210. effect on ANN: `with_mean=True default`?

`with_mean=True default` subtracts mean. It is crucial for gradient/linear models because large-scale features can dominate optimization. Tree models need it less, but the common pipeline keeps comparison consistent.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/train.py:59`

### Q211. effect on trees: `with_mean=True default`?

`with_mean=True default` subtracts mean. It is crucial for gradient/linear models because large-scale features can dominate optimization. Tree models need it less, but the common pipeline keeps comparison consistent.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/train.py:59`

### Q212. why used: `with_std=True default`?

`with_std=True default` divides by std. It is crucial for gradient/linear models because large-scale features can dominate optimization. Tree models need it less, but the common pipeline keeps comparison consistent.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/train.py:59`

### Q213. formula link: `with_std=True default`?

`with_std=True default` divides by std. It is crucial for gradient/linear models because large-scale features can dominate optimization. Tree models need it less, but the common pipeline keeps comparison consistent.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/train.py:59`

### Q214. effect on Logistic Regression: `with_std=True default`?

`with_std=True default` divides by std. It is crucial for gradient/linear models because large-scale features can dominate optimization. Tree models need it less, but the common pipeline keeps comparison consistent.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/train.py:59`

### Q215. effect on ANN: `with_std=True default`?

`with_std=True default` divides by std. It is crucial for gradient/linear models because large-scale features can dominate optimization. Tree models need it less, but the common pipeline keeps comparison consistent.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/train.py:59`

### Q216. effect on trees: `with_std=True default`?

`with_std=True default` divides by std. It is crucial for gradient/linear models because large-scale features can dominate optimization. Tree models need it less, but the common pipeline keeps comparison consistent.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/train.py:59`

### Q217. why used: `Pipeline scaler step`?

`Pipeline scaler step` binds preprocessing to estimator. It is crucial for gradient/linear models because large-scale features can dominate optimization. Tree models need it less, but the common pipeline keeps comparison consistent.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/train.py:57`; `app/backend/src/app/ml/predictive_maintenance/train.py:59`

### Q218. formula link: `Pipeline scaler step`?

`Pipeline scaler step` binds preprocessing to estimator. It is crucial for gradient/linear models because large-scale features can dominate optimization. Tree models need it less, but the common pipeline keeps comparison consistent.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/train.py:57`; `app/backend/src/app/ml/predictive_maintenance/train.py:59`

### Q219. effect on Logistic Regression: `Pipeline scaler step`?

`Pipeline scaler step` binds preprocessing to estimator. It is crucial for gradient/linear models because large-scale features can dominate optimization. Tree models need it less, but the common pipeline keeps comparison consistent.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/train.py:57`; `app/backend/src/app/ml/predictive_maintenance/train.py:59`

### Q220. effect on ANN: `Pipeline scaler step`?

`Pipeline scaler step` binds preprocessing to estimator. It is crucial for gradient/linear models because large-scale features can dominate optimization. Tree models need it less, but the common pipeline keeps comparison consistent.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/train.py:57`; `app/backend/src/app/ml/predictive_maintenance/train.py:59`

### Q221. effect on trees: `Pipeline scaler step`?

`Pipeline scaler step` binds preprocessing to estimator. It is crucial for gradient/linear models because large-scale features can dominate optimization. Tree models need it less, but the common pipeline keeps comparison consistent.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/train.py:57`; `app/backend/src/app/ml/predictive_maintenance/train.py:59`

### Q222. why used: `z=(x-mean)/std`?

`z=(x-mean)/std` scaling formula. It is crucial for gradient/linear models because large-scale features can dominate optimization. Tree models need it less, but the common pipeline keeps comparison consistent.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/train.py:59`

### Q223. formula link: `z=(x-mean)/std`?

`z=(x-mean)/std` scaling formula. It is crucial for gradient/linear models because large-scale features can dominate optimization. Tree models need it less, but the common pipeline keeps comparison consistent.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/train.py:59`

### Q224. effect on Logistic Regression: `z=(x-mean)/std`?

`z=(x-mean)/std` scaling formula. It is crucial for gradient/linear models because large-scale features can dominate optimization. Tree models need it less, but the common pipeline keeps comparison consistent.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/train.py:59`

### Q225. effect on ANN: `z=(x-mean)/std`?

`z=(x-mean)/std` scaling formula. It is crucial for gradient/linear models because large-scale features can dominate optimization. Tree models need it less, but the common pipeline keeps comparison consistent.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/train.py:59`

### Q226. effect on trees: `z=(x-mean)/std`?

`z=(x-mean)/std` scaling formula. It is crucial for gradient/linear models because large-scale features can dominate optimization. Tree models need it less, but the common pipeline keeps comparison consistent.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/train.py:59`

## Logistic Regression

### Q227. why used: `solver=liblinear`?

In Logistic Regression, `solver=liblinear` means small/medium binary solver. The choice is a conservative tabular-ML default for this predictive maintenance dataset. It connects to the model principle: probability estimation for Logistic Regression/ANN, ensemble voting for Random Forest, and sequential loss minimization for XGBoost.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/train.py:63`

### Q228. algorithm formula: `solver=liblinear`?

In Logistic Regression, `solver=liblinear` means small/medium binary solver. The choice is a conservative tabular-ML default for this predictive maintenance dataset. It connects to the model principle: probability estimation for Logistic Regression/ANN, ensemble voting for Random Forest, and sequential loss minimization for XGBoost.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/train.py:63`

### Q229. chosen value reasoning: `solver=liblinear`?

In Logistic Regression, `solver=liblinear` means small/medium binary solver. The choice is a conservative tabular-ML default for this predictive maintenance dataset. It connects to the model principle: probability estimation for Logistic Regression/ANN, ensemble voting for Random Forest, and sequential loss minimization for XGBoost.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/train.py:63`

### Q230. overfitting impact: `solver=liblinear`?

In Logistic Regression, `solver=liblinear` means small/medium binary solver. The choice is a conservative tabular-ML default for this predictive maintenance dataset. It connects to the model principle: probability estimation for Logistic Regression/ANN, ensemble voting for Random Forest, and sequential loss minimization for XGBoost.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/train.py:63`

### Q231. what to tune: `solver=liblinear`?

In Logistic Regression, `solver=liblinear` means small/medium binary solver. The choice is a conservative tabular-ML default for this predictive maintenance dataset. It connects to the model principle: probability estimation for Logistic Regression/ANN, ensemble voting for Random Forest, and sequential loss minimization for XGBoost.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/train.py:63`

### Q232. viva defense: `solver=liblinear`?

In Logistic Regression, `solver=liblinear` means small/medium binary solver. The choice is a conservative tabular-ML default for this predictive maintenance dataset. It connects to the model principle: probability estimation for Logistic Regression/ANN, ensemble voting for Random Forest, and sequential loss minimization for XGBoost.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/train.py:63`

### Q233. why used: `penalty=l2`?

In Logistic Regression, `penalty=l2` means weight shrinkage. The choice is a conservative tabular-ML default for this predictive maintenance dataset. It connects to the model principle: probability estimation for Logistic Regression/ANN, ensemble voting for Random Forest, and sequential loss minimization for XGBoost.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/train.py:64`

### Q234. algorithm formula: `penalty=l2`?

In Logistic Regression, `penalty=l2` means weight shrinkage. The choice is a conservative tabular-ML default for this predictive maintenance dataset. It connects to the model principle: probability estimation for Logistic Regression/ANN, ensemble voting for Random Forest, and sequential loss minimization for XGBoost.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/train.py:64`

### Q235. chosen value reasoning: `penalty=l2`?

In Logistic Regression, `penalty=l2` means weight shrinkage. The choice is a conservative tabular-ML default for this predictive maintenance dataset. It connects to the model principle: probability estimation for Logistic Regression/ANN, ensemble voting for Random Forest, and sequential loss minimization for XGBoost.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/train.py:64`

### Q236. overfitting impact: `penalty=l2`?

In Logistic Regression, `penalty=l2` means weight shrinkage. The choice is a conservative tabular-ML default for this predictive maintenance dataset. It connects to the model principle: probability estimation for Logistic Regression/ANN, ensemble voting for Random Forest, and sequential loss minimization for XGBoost.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/train.py:64`

### Q237. what to tune: `penalty=l2`?

In Logistic Regression, `penalty=l2` means weight shrinkage. The choice is a conservative tabular-ML default for this predictive maintenance dataset. It connects to the model principle: probability estimation for Logistic Regression/ANN, ensemble voting for Random Forest, and sequential loss minimization for XGBoost.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/train.py:64`

### Q238. viva defense: `penalty=l2`?

In Logistic Regression, `penalty=l2` means weight shrinkage. The choice is a conservative tabular-ML default for this predictive maintenance dataset. It connects to the model principle: probability estimation for Logistic Regression/ANN, ensemble voting for Random Forest, and sequential loss minimization for XGBoost.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/train.py:64`

### Q239. why used: `max_iter=1000`?

In Logistic Regression, `max_iter=1000` means more convergence iterations. The choice is a conservative tabular-ML default for this predictive maintenance dataset. It connects to the model principle: probability estimation for Logistic Regression/ANN, ensemble voting for Random Forest, and sequential loss minimization for XGBoost.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/train.py:66`

### Q240. algorithm formula: `max_iter=1000`?

In Logistic Regression, `max_iter=1000` means more convergence iterations. The choice is a conservative tabular-ML default for this predictive maintenance dataset. It connects to the model principle: probability estimation for Logistic Regression/ANN, ensemble voting for Random Forest, and sequential loss minimization for XGBoost.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/train.py:66`

### Q241. chosen value reasoning: `max_iter=1000`?

In Logistic Regression, `max_iter=1000` means more convergence iterations. The choice is a conservative tabular-ML default for this predictive maintenance dataset. It connects to the model principle: probability estimation for Logistic Regression/ANN, ensemble voting for Random Forest, and sequential loss minimization for XGBoost.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/train.py:66`

### Q242. overfitting impact: `max_iter=1000`?

In Logistic Regression, `max_iter=1000` means more convergence iterations. The choice is a conservative tabular-ML default for this predictive maintenance dataset. It connects to the model principle: probability estimation for Logistic Regression/ANN, ensemble voting for Random Forest, and sequential loss minimization for XGBoost.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/train.py:66`

### Q243. what to tune: `max_iter=1000`?

In Logistic Regression, `max_iter=1000` means more convergence iterations. The choice is a conservative tabular-ML default for this predictive maintenance dataset. It connects to the model principle: probability estimation for Logistic Regression/ANN, ensemble voting for Random Forest, and sequential loss minimization for XGBoost.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/train.py:66`

### Q244. viva defense: `max_iter=1000`?

In Logistic Regression, `max_iter=1000` means more convergence iterations. The choice is a conservative tabular-ML default for this predictive maintenance dataset. It connects to the model principle: probability estimation for Logistic Regression/ANN, ensemble voting for Random Forest, and sequential loss minimization for XGBoost.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/train.py:66`

### Q245. why used: `random_state=42`?

In Logistic Regression, `random_state=42` means reproducibility. The choice is a conservative tabular-ML default for this predictive maintenance dataset. It connects to the model principle: probability estimation for Logistic Regression/ANN, ensemble voting for Random Forest, and sequential loss minimization for XGBoost.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/preprocessing.py:68`; `app/backend/src/app/ml/predictive_maintenance/train.py:47`

### Q246. algorithm formula: `random_state=42`?

In Logistic Regression, `random_state=42` means reproducibility. The choice is a conservative tabular-ML default for this predictive maintenance dataset. It connects to the model principle: probability estimation for Logistic Regression/ANN, ensemble voting for Random Forest, and sequential loss minimization for XGBoost.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/preprocessing.py:68`; `app/backend/src/app/ml/predictive_maintenance/train.py:47`

### Q247. chosen value reasoning: `random_state=42`?

In Logistic Regression, `random_state=42` means reproducibility. The choice is a conservative tabular-ML default for this predictive maintenance dataset. It connects to the model principle: probability estimation for Logistic Regression/ANN, ensemble voting for Random Forest, and sequential loss minimization for XGBoost.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/preprocessing.py:68`; `app/backend/src/app/ml/predictive_maintenance/train.py:47`

### Q248. overfitting impact: `random_state=42`?

In Logistic Regression, `random_state=42` means reproducibility. The choice is a conservative tabular-ML default for this predictive maintenance dataset. It connects to the model principle: probability estimation for Logistic Regression/ANN, ensemble voting for Random Forest, and sequential loss minimization for XGBoost.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/preprocessing.py:68`; `app/backend/src/app/ml/predictive_maintenance/train.py:47`

### Q249. what to tune: `random_state=42`?

In Logistic Regression, `random_state=42` means reproducibility. The choice is a conservative tabular-ML default for this predictive maintenance dataset. It connects to the model principle: probability estimation for Logistic Regression/ANN, ensemble voting for Random Forest, and sequential loss minimization for XGBoost.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/preprocessing.py:68`; `app/backend/src/app/ml/predictive_maintenance/train.py:47`

### Q250. viva defense: `random_state=42`?

In Logistic Regression, `random_state=42` means reproducibility. The choice is a conservative tabular-ML default for this predictive maintenance dataset. It connects to the model principle: probability estimation for Logistic Regression/ANN, ensemble voting for Random Forest, and sequential loss minimization for XGBoost.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/preprocessing.py:68`; `app/backend/src/app/ml/predictive_maintenance/train.py:47`

### Q251. why used: `sigmoid`?

In Logistic Regression, `sigmoid` means probability mapping. The choice is a conservative tabular-ML default for this predictive maintenance dataset. It connects to the model principle: probability estimation for Logistic Regression/ANN, ensemble voting for Random Forest, and sequential loss minimization for XGBoost.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/train.py:35`

### Q252. algorithm formula: `sigmoid`?

In Logistic Regression, `sigmoid` means probability mapping. The choice is a conservative tabular-ML default for this predictive maintenance dataset. It connects to the model principle: probability estimation for Logistic Regression/ANN, ensemble voting for Random Forest, and sequential loss minimization for XGBoost.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/train.py:35`

### Q253. chosen value reasoning: `sigmoid`?

In Logistic Regression, `sigmoid` means probability mapping. The choice is a conservative tabular-ML default for this predictive maintenance dataset. It connects to the model principle: probability estimation for Logistic Regression/ANN, ensemble voting for Random Forest, and sequential loss minimization for XGBoost.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/train.py:35`

### Q254. overfitting impact: `sigmoid`?

In Logistic Regression, `sigmoid` means probability mapping. The choice is a conservative tabular-ML default for this predictive maintenance dataset. It connects to the model principle: probability estimation for Logistic Regression/ANN, ensemble voting for Random Forest, and sequential loss minimization for XGBoost.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/train.py:35`

### Q255. what to tune: `sigmoid`?

In Logistic Regression, `sigmoid` means probability mapping. The choice is a conservative tabular-ML default for this predictive maintenance dataset. It connects to the model principle: probability estimation for Logistic Regression/ANN, ensemble voting for Random Forest, and sequential loss minimization for XGBoost.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/train.py:35`

### Q256. viva defense: `sigmoid`?

In Logistic Regression, `sigmoid` means probability mapping. The choice is a conservative tabular-ML default for this predictive maintenance dataset. It connects to the model principle: probability estimation for Logistic Regression/ANN, ensemble voting for Random Forest, and sequential loss minimization for XGBoost.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/train.py:35`

### Q257. why used: `baseline`?

In Logistic Regression, `baseline` means interpretable benchmark. The choice is a conservative tabular-ML default for this predictive maintenance dataset. It connects to the model principle: probability estimation for Logistic Regression/ANN, ensemble voting for Random Forest, and sequential loss minimization for XGBoost.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/train.py:56`

### Q258. algorithm formula: `baseline`?

In Logistic Regression, `baseline` means interpretable benchmark. The choice is a conservative tabular-ML default for this predictive maintenance dataset. It connects to the model principle: probability estimation for Logistic Regression/ANN, ensemble voting for Random Forest, and sequential loss minimization for XGBoost.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/train.py:56`

### Q259. chosen value reasoning: `baseline`?

In Logistic Regression, `baseline` means interpretable benchmark. The choice is a conservative tabular-ML default for this predictive maintenance dataset. It connects to the model principle: probability estimation for Logistic Regression/ANN, ensemble voting for Random Forest, and sequential loss minimization for XGBoost.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/train.py:56`

### Q260. overfitting impact: `baseline`?

In Logistic Regression, `baseline` means interpretable benchmark. The choice is a conservative tabular-ML default for this predictive maintenance dataset. It connects to the model principle: probability estimation for Logistic Regression/ANN, ensemble voting for Random Forest, and sequential loss minimization for XGBoost.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/train.py:56`

### Q261. what to tune: `baseline`?

In Logistic Regression, `baseline` means interpretable benchmark. The choice is a conservative tabular-ML default for this predictive maintenance dataset. It connects to the model principle: probability estimation for Logistic Regression/ANN, ensemble voting for Random Forest, and sequential loss minimization for XGBoost.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/train.py:56`

### Q262. viva defense: `baseline`?

In Logistic Regression, `baseline` means interpretable benchmark. The choice is a conservative tabular-ML default for this predictive maintenance dataset. It connects to the model principle: probability estimation for Logistic Regression/ANN, ensemble voting for Random Forest, and sequential loss minimization for XGBoost.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/train.py:56`

## Random Forest

### Q263. why used: `n_estimators=200`?

In Random Forest, `n_estimators=200` means stable tree averaging. The choice is a conservative tabular-ML default for this predictive maintenance dataset. It connects to the model principle: probability estimation for Logistic Regression/ANN, ensemble voting for Random Forest, and sequential loss minimization for XGBoost.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/train.py:77`; `app/backend/src/app/ml/predictive_maintenance/train.py:91`

### Q264. algorithm formula: `n_estimators=200`?

In Random Forest, `n_estimators=200` means stable tree averaging. The choice is a conservative tabular-ML default for this predictive maintenance dataset. It connects to the model principle: probability estimation for Logistic Regression/ANN, ensemble voting for Random Forest, and sequential loss minimization for XGBoost.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/train.py:77`; `app/backend/src/app/ml/predictive_maintenance/train.py:91`

### Q265. chosen value reasoning: `n_estimators=200`?

In Random Forest, `n_estimators=200` means stable tree averaging. The choice is a conservative tabular-ML default for this predictive maintenance dataset. It connects to the model principle: probability estimation for Logistic Regression/ANN, ensemble voting for Random Forest, and sequential loss minimization for XGBoost.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/train.py:77`; `app/backend/src/app/ml/predictive_maintenance/train.py:91`

### Q266. overfitting impact: `n_estimators=200`?

In Random Forest, `n_estimators=200` means stable tree averaging. The choice is a conservative tabular-ML default for this predictive maintenance dataset. It connects to the model principle: probability estimation for Logistic Regression/ANN, ensemble voting for Random Forest, and sequential loss minimization for XGBoost.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/train.py:77`; `app/backend/src/app/ml/predictive_maintenance/train.py:91`

### Q267. what to tune: `n_estimators=200`?

In Random Forest, `n_estimators=200` means stable tree averaging. The choice is a conservative tabular-ML default for this predictive maintenance dataset. It connects to the model principle: probability estimation for Logistic Regression/ANN, ensemble voting for Random Forest, and sequential loss minimization for XGBoost.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/train.py:77`; `app/backend/src/app/ml/predictive_maintenance/train.py:91`

### Q268. viva defense: `n_estimators=200`?

In Random Forest, `n_estimators=200` means stable tree averaging. The choice is a conservative tabular-ML default for this predictive maintenance dataset. It connects to the model principle: probability estimation for Logistic Regression/ANN, ensemble voting for Random Forest, and sequential loss minimization for XGBoost.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/train.py:77`; `app/backend/src/app/ml/predictive_maintenance/train.py:91`

### Q269. why used: `max_depth=12`?

In Random Forest, `max_depth=12` means limits overfitting. The choice is a conservative tabular-ML default for this predictive maintenance dataset. It connects to the model principle: probability estimation for Logistic Regression/ANN, ensemble voting for Random Forest, and sequential loss minimization for XGBoost.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/train.py:78`

### Q270. algorithm formula: `max_depth=12`?

In Random Forest, `max_depth=12` means limits overfitting. The choice is a conservative tabular-ML default for this predictive maintenance dataset. It connects to the model principle: probability estimation for Logistic Regression/ANN, ensemble voting for Random Forest, and sequential loss minimization for XGBoost.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/train.py:78`

### Q271. chosen value reasoning: `max_depth=12`?

In Random Forest, `max_depth=12` means limits overfitting. The choice is a conservative tabular-ML default for this predictive maintenance dataset. It connects to the model principle: probability estimation for Logistic Regression/ANN, ensemble voting for Random Forest, and sequential loss minimization for XGBoost.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/train.py:78`

### Q272. overfitting impact: `max_depth=12`?

In Random Forest, `max_depth=12` means limits overfitting. The choice is a conservative tabular-ML default for this predictive maintenance dataset. It connects to the model principle: probability estimation for Logistic Regression/ANN, ensemble voting for Random Forest, and sequential loss minimization for XGBoost.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/train.py:78`

### Q273. what to tune: `max_depth=12`?

In Random Forest, `max_depth=12` means limits overfitting. The choice is a conservative tabular-ML default for this predictive maintenance dataset. It connects to the model principle: probability estimation for Logistic Regression/ANN, ensemble voting for Random Forest, and sequential loss minimization for XGBoost.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/train.py:78`

### Q274. viva defense: `max_depth=12`?

In Random Forest, `max_depth=12` means limits overfitting. The choice is a conservative tabular-ML default for this predictive maintenance dataset. It connects to the model principle: probability estimation for Logistic Regression/ANN, ensemble voting for Random Forest, and sequential loss minimization for XGBoost.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/train.py:78`

### Q275. why used: `random_state=42`?

In Random Forest, `random_state=42` means reproducible randomness. The choice is a conservative tabular-ML default for this predictive maintenance dataset. It connects to the model principle: probability estimation for Logistic Regression/ANN, ensemble voting for Random Forest, and sequential loss minimization for XGBoost.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/preprocessing.py:68`; `app/backend/src/app/ml/predictive_maintenance/train.py:47`

### Q276. algorithm formula: `random_state=42`?

In Random Forest, `random_state=42` means reproducible randomness. The choice is a conservative tabular-ML default for this predictive maintenance dataset. It connects to the model principle: probability estimation for Logistic Regression/ANN, ensemble voting for Random Forest, and sequential loss minimization for XGBoost.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/preprocessing.py:68`; `app/backend/src/app/ml/predictive_maintenance/train.py:47`

### Q277. chosen value reasoning: `random_state=42`?

In Random Forest, `random_state=42` means reproducible randomness. The choice is a conservative tabular-ML default for this predictive maintenance dataset. It connects to the model principle: probability estimation for Logistic Regression/ANN, ensemble voting for Random Forest, and sequential loss minimization for XGBoost.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/preprocessing.py:68`; `app/backend/src/app/ml/predictive_maintenance/train.py:47`

### Q278. overfitting impact: `random_state=42`?

In Random Forest, `random_state=42` means reproducible randomness. The choice is a conservative tabular-ML default for this predictive maintenance dataset. It connects to the model principle: probability estimation for Logistic Regression/ANN, ensemble voting for Random Forest, and sequential loss minimization for XGBoost.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/preprocessing.py:68`; `app/backend/src/app/ml/predictive_maintenance/train.py:47`

### Q279. what to tune: `random_state=42`?

In Random Forest, `random_state=42` means reproducible randomness. The choice is a conservative tabular-ML default for this predictive maintenance dataset. It connects to the model principle: probability estimation for Logistic Regression/ANN, ensemble voting for Random Forest, and sequential loss minimization for XGBoost.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/preprocessing.py:68`; `app/backend/src/app/ml/predictive_maintenance/train.py:47`

### Q280. viva defense: `random_state=42`?

In Random Forest, `random_state=42` means reproducible randomness. The choice is a conservative tabular-ML default for this predictive maintenance dataset. It connects to the model principle: probability estimation for Logistic Regression/ANN, ensemble voting for Random Forest, and sequential loss minimization for XGBoost.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/preprocessing.py:68`; `app/backend/src/app/ml/predictive_maintenance/train.py:47`

### Q281. why used: `n_jobs=-1`?

In Random Forest, `n_jobs=-1` means all CPU cores. The choice is a conservative tabular-ML default for this predictive maintenance dataset. It connects to the model principle: probability estimation for Logistic Regression/ANN, ensemble voting for Random Forest, and sequential loss minimization for XGBoost.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/train.py:80`; `app/backend/src/app/ml/predictive_maintenance/train.py:97`

### Q282. algorithm formula: `n_jobs=-1`?

In Random Forest, `n_jobs=-1` means all CPU cores. The choice is a conservative tabular-ML default for this predictive maintenance dataset. It connects to the model principle: probability estimation for Logistic Regression/ANN, ensemble voting for Random Forest, and sequential loss minimization for XGBoost.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/train.py:80`; `app/backend/src/app/ml/predictive_maintenance/train.py:97`

### Q283. chosen value reasoning: `n_jobs=-1`?

In Random Forest, `n_jobs=-1` means all CPU cores. The choice is a conservative tabular-ML default for this predictive maintenance dataset. It connects to the model principle: probability estimation for Logistic Regression/ANN, ensemble voting for Random Forest, and sequential loss minimization for XGBoost.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/train.py:80`; `app/backend/src/app/ml/predictive_maintenance/train.py:97`

### Q284. overfitting impact: `n_jobs=-1`?

In Random Forest, `n_jobs=-1` means all CPU cores. The choice is a conservative tabular-ML default for this predictive maintenance dataset. It connects to the model principle: probability estimation for Logistic Regression/ANN, ensemble voting for Random Forest, and sequential loss minimization for XGBoost.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/train.py:80`; `app/backend/src/app/ml/predictive_maintenance/train.py:97`

### Q285. what to tune: `n_jobs=-1`?

In Random Forest, `n_jobs=-1` means all CPU cores. The choice is a conservative tabular-ML default for this predictive maintenance dataset. It connects to the model principle: probability estimation for Logistic Regression/ANN, ensemble voting for Random Forest, and sequential loss minimization for XGBoost.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/train.py:80`; `app/backend/src/app/ml/predictive_maintenance/train.py:97`

### Q286. viva defense: `n_jobs=-1`?

In Random Forest, `n_jobs=-1` means all CPU cores. The choice is a conservative tabular-ML default for this predictive maintenance dataset. It connects to the model principle: probability estimation for Logistic Regression/ANN, ensemble voting for Random Forest, and sequential loss minimization for XGBoost.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/train.py:80`; `app/backend/src/app/ml/predictive_maintenance/train.py:97`

### Q287. why used: `bootstrap default`?

In Random Forest, `bootstrap default` means tree diversity. The choice is a conservative tabular-ML default for this predictive maintenance dataset. It connects to the model principle: probability estimation for Logistic Regression/ANN, ensemble voting for Random Forest, and sequential loss minimization for XGBoost.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/train.py:76`

### Q288. algorithm formula: `bootstrap default`?

In Random Forest, `bootstrap default` means tree diversity. The choice is a conservative tabular-ML default for this predictive maintenance dataset. It connects to the model principle: probability estimation for Logistic Regression/ANN, ensemble voting for Random Forest, and sequential loss minimization for XGBoost.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/train.py:76`

### Q289. chosen value reasoning: `bootstrap default`?

In Random Forest, `bootstrap default` means tree diversity. The choice is a conservative tabular-ML default for this predictive maintenance dataset. It connects to the model principle: probability estimation for Logistic Regression/ANN, ensemble voting for Random Forest, and sequential loss minimization for XGBoost.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/train.py:76`

### Q290. overfitting impact: `bootstrap default`?

In Random Forest, `bootstrap default` means tree diversity. The choice is a conservative tabular-ML default for this predictive maintenance dataset. It connects to the model principle: probability estimation for Logistic Regression/ANN, ensemble voting for Random Forest, and sequential loss minimization for XGBoost.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/train.py:76`

### Q291. what to tune: `bootstrap default`?

In Random Forest, `bootstrap default` means tree diversity. The choice is a conservative tabular-ML default for this predictive maintenance dataset. It connects to the model principle: probability estimation for Logistic Regression/ANN, ensemble voting for Random Forest, and sequential loss minimization for XGBoost.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/train.py:76`

### Q292. viva defense: `bootstrap default`?

In Random Forest, `bootstrap default` means tree diversity. The choice is a conservative tabular-ML default for this predictive maintenance dataset. It connects to the model principle: probability estimation for Logistic Regression/ANN, ensemble voting for Random Forest, and sequential loss minimization for XGBoost.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/train.py:76`

### Q293. why used: `Gini default`?

In Random Forest, `Gini default` means split impurity. The choice is a conservative tabular-ML default for this predictive maintenance dataset. It connects to the model principle: probability estimation for Logistic Regression/ANN, ensemble voting for Random Forest, and sequential loss minimization for XGBoost.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/train.py:76`

### Q294. algorithm formula: `Gini default`?

In Random Forest, `Gini default` means split impurity. The choice is a conservative tabular-ML default for this predictive maintenance dataset. It connects to the model principle: probability estimation for Logistic Regression/ANN, ensemble voting for Random Forest, and sequential loss minimization for XGBoost.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/train.py:76`

### Q295. chosen value reasoning: `Gini default`?

In Random Forest, `Gini default` means split impurity. The choice is a conservative tabular-ML default for this predictive maintenance dataset. It connects to the model principle: probability estimation for Logistic Regression/ANN, ensemble voting for Random Forest, and sequential loss minimization for XGBoost.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/train.py:76`

### Q296. overfitting impact: `Gini default`?

In Random Forest, `Gini default` means split impurity. The choice is a conservative tabular-ML default for this predictive maintenance dataset. It connects to the model principle: probability estimation for Logistic Regression/ANN, ensemble voting for Random Forest, and sequential loss minimization for XGBoost.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/train.py:76`

### Q297. what to tune: `Gini default`?

In Random Forest, `Gini default` means split impurity. The choice is a conservative tabular-ML default for this predictive maintenance dataset. It connects to the model principle: probability estimation for Logistic Regression/ANN, ensemble voting for Random Forest, and sequential loss minimization for XGBoost.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/train.py:76`

### Q298. viva defense: `Gini default`?

In Random Forest, `Gini default` means split impurity. The choice is a conservative tabular-ML default for this predictive maintenance dataset. It connects to the model principle: probability estimation for Logistic Regression/ANN, ensemble voting for Random Forest, and sequential loss minimization for XGBoost.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/train.py:76`

### Q299. why used: `predict_proba`?

In Random Forest, `predict_proba` means probability from trees. The choice is a conservative tabular-ML default for this predictive maintenance dataset. It connects to the model principle: probability estimation for Logistic Regression/ANN, ensemble voting for Random Forest, and sequential loss minimization for XGBoost.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/evaluate.py:39`

### Q300. algorithm formula: `predict_proba`?

In Random Forest, `predict_proba` means probability from trees. The choice is a conservative tabular-ML default for this predictive maintenance dataset. It connects to the model principle: probability estimation for Logistic Regression/ANN, ensemble voting for Random Forest, and sequential loss minimization for XGBoost.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/evaluate.py:39`

### Q301. chosen value reasoning: `predict_proba`?

In Random Forest, `predict_proba` means probability from trees. The choice is a conservative tabular-ML default for this predictive maintenance dataset. It connects to the model principle: probability estimation for Logistic Regression/ANN, ensemble voting for Random Forest, and sequential loss minimization for XGBoost.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/evaluate.py:39`

### Q302. overfitting impact: `predict_proba`?

In Random Forest, `predict_proba` means probability from trees. The choice is a conservative tabular-ML default for this predictive maintenance dataset. It connects to the model principle: probability estimation for Logistic Regression/ANN, ensemble voting for Random Forest, and sequential loss minimization for XGBoost.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/evaluate.py:39`

### Q303. what to tune: `predict_proba`?

In Random Forest, `predict_proba` means probability from trees. The choice is a conservative tabular-ML default for this predictive maintenance dataset. It connects to the model principle: probability estimation for Logistic Regression/ANN, ensemble voting for Random Forest, and sequential loss minimization for XGBoost.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/evaluate.py:39`

### Q304. viva defense: `predict_proba`?

In Random Forest, `predict_proba` means probability from trees. The choice is a conservative tabular-ML default for this predictive maintenance dataset. It connects to the model principle: probability estimation for Logistic Regression/ANN, ensemble voting for Random Forest, and sequential loss minimization for XGBoost.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/evaluate.py:39`

## XGBoost

### Q305. why used: `n_estimators=200`?

In XGBoost, `n_estimators=200` means 200 boosting rounds. The choice is a conservative tabular-ML default for this predictive maintenance dataset. It connects to the model principle: probability estimation for Logistic Regression/ANN, ensemble voting for Random Forest, and sequential loss minimization for XGBoost.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/train.py:77`; `app/backend/src/app/ml/predictive_maintenance/train.py:91`

### Q306. algorithm formula: `n_estimators=200`?

In XGBoost, `n_estimators=200` means 200 boosting rounds. The choice is a conservative tabular-ML default for this predictive maintenance dataset. It connects to the model principle: probability estimation for Logistic Regression/ANN, ensemble voting for Random Forest, and sequential loss minimization for XGBoost.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/train.py:77`; `app/backend/src/app/ml/predictive_maintenance/train.py:91`

### Q307. chosen value reasoning: `n_estimators=200`?

In XGBoost, `n_estimators=200` means 200 boosting rounds. The choice is a conservative tabular-ML default for this predictive maintenance dataset. It connects to the model principle: probability estimation for Logistic Regression/ANN, ensemble voting for Random Forest, and sequential loss minimization for XGBoost.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/train.py:77`; `app/backend/src/app/ml/predictive_maintenance/train.py:91`

### Q308. overfitting impact: `n_estimators=200`?

In XGBoost, `n_estimators=200` means 200 boosting rounds. The choice is a conservative tabular-ML default for this predictive maintenance dataset. It connects to the model principle: probability estimation for Logistic Regression/ANN, ensemble voting for Random Forest, and sequential loss minimization for XGBoost.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/train.py:77`; `app/backend/src/app/ml/predictive_maintenance/train.py:91`

### Q309. what to tune: `n_estimators=200`?

In XGBoost, `n_estimators=200` means 200 boosting rounds. The choice is a conservative tabular-ML default for this predictive maintenance dataset. It connects to the model principle: probability estimation for Logistic Regression/ANN, ensemble voting for Random Forest, and sequential loss minimization for XGBoost.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/train.py:77`; `app/backend/src/app/ml/predictive_maintenance/train.py:91`

### Q310. viva defense: `n_estimators=200`?

In XGBoost, `n_estimators=200` means 200 boosting rounds. The choice is a conservative tabular-ML default for this predictive maintenance dataset. It connects to the model principle: probability estimation for Logistic Regression/ANN, ensemble voting for Random Forest, and sequential loss minimization for XGBoost.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/train.py:77`; `app/backend/src/app/ml/predictive_maintenance/train.py:91`

### Q311. why used: `max_depth=6`?

In XGBoost, `max_depth=6` means moderate tree complexity. The choice is a conservative tabular-ML default for this predictive maintenance dataset. It connects to the model principle: probability estimation for Logistic Regression/ANN, ensemble voting for Random Forest, and sequential loss minimization for XGBoost.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/train.py:92`

### Q312. algorithm formula: `max_depth=6`?

In XGBoost, `max_depth=6` means moderate tree complexity. The choice is a conservative tabular-ML default for this predictive maintenance dataset. It connects to the model principle: probability estimation for Logistic Regression/ANN, ensemble voting for Random Forest, and sequential loss minimization for XGBoost.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/train.py:92`

### Q313. chosen value reasoning: `max_depth=6`?

In XGBoost, `max_depth=6` means moderate tree complexity. The choice is a conservative tabular-ML default for this predictive maintenance dataset. It connects to the model principle: probability estimation for Logistic Regression/ANN, ensemble voting for Random Forest, and sequential loss minimization for XGBoost.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/train.py:92`

### Q314. overfitting impact: `max_depth=6`?

In XGBoost, `max_depth=6` means moderate tree complexity. The choice is a conservative tabular-ML default for this predictive maintenance dataset. It connects to the model principle: probability estimation for Logistic Regression/ANN, ensemble voting for Random Forest, and sequential loss minimization for XGBoost.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/train.py:92`

### Q315. what to tune: `max_depth=6`?

In XGBoost, `max_depth=6` means moderate tree complexity. The choice is a conservative tabular-ML default for this predictive maintenance dataset. It connects to the model principle: probability estimation for Logistic Regression/ANN, ensemble voting for Random Forest, and sequential loss minimization for XGBoost.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/train.py:92`

### Q316. viva defense: `max_depth=6`?

In XGBoost, `max_depth=6` means moderate tree complexity. The choice is a conservative tabular-ML default for this predictive maintenance dataset. It connects to the model principle: probability estimation for Logistic Regression/ANN, ensemble voting for Random Forest, and sequential loss minimization for XGBoost.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/train.py:92`

### Q317. why used: `learning_rate=0.1`?

In XGBoost, `learning_rate=0.1` means shrinkage/eta. The choice is a conservative tabular-ML default for this predictive maintenance dataset. It connects to the model principle: probability estimation for Logistic Regression/ANN, ensemble voting for Random Forest, and sequential loss minimization for XGBoost.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/train.py:93`

### Q318. algorithm formula: `learning_rate=0.1`?

In XGBoost, `learning_rate=0.1` means shrinkage/eta. The choice is a conservative tabular-ML default for this predictive maintenance dataset. It connects to the model principle: probability estimation for Logistic Regression/ANN, ensemble voting for Random Forest, and sequential loss minimization for XGBoost.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/train.py:93`

### Q319. chosen value reasoning: `learning_rate=0.1`?

In XGBoost, `learning_rate=0.1` means shrinkage/eta. The choice is a conservative tabular-ML default for this predictive maintenance dataset. It connects to the model principle: probability estimation for Logistic Regression/ANN, ensemble voting for Random Forest, and sequential loss minimization for XGBoost.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/train.py:93`

### Q320. overfitting impact: `learning_rate=0.1`?

In XGBoost, `learning_rate=0.1` means shrinkage/eta. The choice is a conservative tabular-ML default for this predictive maintenance dataset. It connects to the model principle: probability estimation for Logistic Regression/ANN, ensemble voting for Random Forest, and sequential loss minimization for XGBoost.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/train.py:93`

### Q321. what to tune: `learning_rate=0.1`?

In XGBoost, `learning_rate=0.1` means shrinkage/eta. The choice is a conservative tabular-ML default for this predictive maintenance dataset. It connects to the model principle: probability estimation for Logistic Regression/ANN, ensemble voting for Random Forest, and sequential loss minimization for XGBoost.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/train.py:93`

### Q322. viva defense: `learning_rate=0.1`?

In XGBoost, `learning_rate=0.1` means shrinkage/eta. The choice is a conservative tabular-ML default for this predictive maintenance dataset. It connects to the model principle: probability estimation for Logistic Regression/ANN, ensemble voting for Random Forest, and sequential loss minimization for XGBoost.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/train.py:93`

### Q323. why used: `eval_metric=logloss`?

In XGBoost, `eval_metric=logloss` means probability loss. The choice is a conservative tabular-ML default for this predictive maintenance dataset. It connects to the model principle: probability estimation for Logistic Regression/ANN, ensemble voting for Random Forest, and sequential loss minimization for XGBoost.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/train.py:95`

### Q324. algorithm formula: `eval_metric=logloss`?

In XGBoost, `eval_metric=logloss` means probability loss. The choice is a conservative tabular-ML default for this predictive maintenance dataset. It connects to the model principle: probability estimation for Logistic Regression/ANN, ensemble voting for Random Forest, and sequential loss minimization for XGBoost.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/train.py:95`

### Q325. chosen value reasoning: `eval_metric=logloss`?

In XGBoost, `eval_metric=logloss` means probability loss. The choice is a conservative tabular-ML default for this predictive maintenance dataset. It connects to the model principle: probability estimation for Logistic Regression/ANN, ensemble voting for Random Forest, and sequential loss minimization for XGBoost.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/train.py:95`

### Q326. overfitting impact: `eval_metric=logloss`?

In XGBoost, `eval_metric=logloss` means probability loss. The choice is a conservative tabular-ML default for this predictive maintenance dataset. It connects to the model principle: probability estimation for Logistic Regression/ANN, ensemble voting for Random Forest, and sequential loss minimization for XGBoost.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/train.py:95`

### Q327. what to tune: `eval_metric=logloss`?

In XGBoost, `eval_metric=logloss` means probability loss. The choice is a conservative tabular-ML default for this predictive maintenance dataset. It connects to the model principle: probability estimation for Logistic Regression/ANN, ensemble voting for Random Forest, and sequential loss minimization for XGBoost.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/train.py:95`

### Q328. viva defense: `eval_metric=logloss`?

In XGBoost, `eval_metric=logloss` means probability loss. The choice is a conservative tabular-ML default for this predictive maintenance dataset. It connects to the model principle: probability estimation for Logistic Regression/ANN, ensemble voting for Random Forest, and sequential loss minimization for XGBoost.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/train.py:95`

### Q329. why used: `use_label_encoder=False`?

In XGBoost, `use_label_encoder=False` means avoid deprecated encoder. The choice is a conservative tabular-ML default for this predictive maintenance dataset. It connects to the model principle: probability estimation for Logistic Regression/ANN, ensemble voting for Random Forest, and sequential loss minimization for XGBoost.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/train.py:94`

### Q330. algorithm formula: `use_label_encoder=False`?

In XGBoost, `use_label_encoder=False` means avoid deprecated encoder. The choice is a conservative tabular-ML default for this predictive maintenance dataset. It connects to the model principle: probability estimation for Logistic Regression/ANN, ensemble voting for Random Forest, and sequential loss minimization for XGBoost.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/train.py:94`

### Q331. chosen value reasoning: `use_label_encoder=False`?

In XGBoost, `use_label_encoder=False` means avoid deprecated encoder. The choice is a conservative tabular-ML default for this predictive maintenance dataset. It connects to the model principle: probability estimation for Logistic Regression/ANN, ensemble voting for Random Forest, and sequential loss minimization for XGBoost.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/train.py:94`

### Q332. overfitting impact: `use_label_encoder=False`?

In XGBoost, `use_label_encoder=False` means avoid deprecated encoder. The choice is a conservative tabular-ML default for this predictive maintenance dataset. It connects to the model principle: probability estimation for Logistic Regression/ANN, ensemble voting for Random Forest, and sequential loss minimization for XGBoost.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/train.py:94`

### Q333. what to tune: `use_label_encoder=False`?

In XGBoost, `use_label_encoder=False` means avoid deprecated encoder. The choice is a conservative tabular-ML default for this predictive maintenance dataset. It connects to the model principle: probability estimation for Logistic Regression/ANN, ensemble voting for Random Forest, and sequential loss minimization for XGBoost.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/train.py:94`

### Q334. viva defense: `use_label_encoder=False`?

In XGBoost, `use_label_encoder=False` means avoid deprecated encoder. The choice is a conservative tabular-ML default for this predictive maintenance dataset. It connects to the model principle: probability estimation for Logistic Regression/ANN, ensemble voting for Random Forest, and sequential loss minimization for XGBoost.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/train.py:94`

### Q335. why used: `random_state=42`?

In XGBoost, `random_state=42` means reproducible. The choice is a conservative tabular-ML default for this predictive maintenance dataset. It connects to the model principle: probability estimation for Logistic Regression/ANN, ensemble voting for Random Forest, and sequential loss minimization for XGBoost.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/preprocessing.py:68`; `app/backend/src/app/ml/predictive_maintenance/train.py:47`

### Q336. algorithm formula: `random_state=42`?

In XGBoost, `random_state=42` means reproducible. The choice is a conservative tabular-ML default for this predictive maintenance dataset. It connects to the model principle: probability estimation for Logistic Regression/ANN, ensemble voting for Random Forest, and sequential loss minimization for XGBoost.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/preprocessing.py:68`; `app/backend/src/app/ml/predictive_maintenance/train.py:47`

### Q337. chosen value reasoning: `random_state=42`?

In XGBoost, `random_state=42` means reproducible. The choice is a conservative tabular-ML default for this predictive maintenance dataset. It connects to the model principle: probability estimation for Logistic Regression/ANN, ensemble voting for Random Forest, and sequential loss minimization for XGBoost.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/preprocessing.py:68`; `app/backend/src/app/ml/predictive_maintenance/train.py:47`

### Q338. overfitting impact: `random_state=42`?

In XGBoost, `random_state=42` means reproducible. The choice is a conservative tabular-ML default for this predictive maintenance dataset. It connects to the model principle: probability estimation for Logistic Regression/ANN, ensemble voting for Random Forest, and sequential loss minimization for XGBoost.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/preprocessing.py:68`; `app/backend/src/app/ml/predictive_maintenance/train.py:47`

### Q339. what to tune: `random_state=42`?

In XGBoost, `random_state=42` means reproducible. The choice is a conservative tabular-ML default for this predictive maintenance dataset. It connects to the model principle: probability estimation for Logistic Regression/ANN, ensemble voting for Random Forest, and sequential loss minimization for XGBoost.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/preprocessing.py:68`; `app/backend/src/app/ml/predictive_maintenance/train.py:47`

### Q340. viva defense: `random_state=42`?

In XGBoost, `random_state=42` means reproducible. The choice is a conservative tabular-ML default for this predictive maintenance dataset. It connects to the model principle: probability estimation for Logistic Regression/ANN, ensemble voting for Random Forest, and sequential loss minimization for XGBoost.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/preprocessing.py:68`; `app/backend/src/app/ml/predictive_maintenance/train.py:47`

### Q341. why used: `n_jobs=-1`?

In XGBoost, `n_jobs=-1` means parallelism. The choice is a conservative tabular-ML default for this predictive maintenance dataset. It connects to the model principle: probability estimation for Logistic Regression/ANN, ensemble voting for Random Forest, and sequential loss minimization for XGBoost.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/train.py:80`; `app/backend/src/app/ml/predictive_maintenance/train.py:97`

### Q342. algorithm formula: `n_jobs=-1`?

In XGBoost, `n_jobs=-1` means parallelism. The choice is a conservative tabular-ML default for this predictive maintenance dataset. It connects to the model principle: probability estimation for Logistic Regression/ANN, ensemble voting for Random Forest, and sequential loss minimization for XGBoost.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/train.py:80`; `app/backend/src/app/ml/predictive_maintenance/train.py:97`

### Q343. chosen value reasoning: `n_jobs=-1`?

In XGBoost, `n_jobs=-1` means parallelism. The choice is a conservative tabular-ML default for this predictive maintenance dataset. It connects to the model principle: probability estimation for Logistic Regression/ANN, ensemble voting for Random Forest, and sequential loss minimization for XGBoost.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/train.py:80`; `app/backend/src/app/ml/predictive_maintenance/train.py:97`

### Q344. overfitting impact: `n_jobs=-1`?

In XGBoost, `n_jobs=-1` means parallelism. The choice is a conservative tabular-ML default for this predictive maintenance dataset. It connects to the model principle: probability estimation for Logistic Regression/ANN, ensemble voting for Random Forest, and sequential loss minimization for XGBoost.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/train.py:80`; `app/backend/src/app/ml/predictive_maintenance/train.py:97`

### Q345. what to tune: `n_jobs=-1`?

In XGBoost, `n_jobs=-1` means parallelism. The choice is a conservative tabular-ML default for this predictive maintenance dataset. It connects to the model principle: probability estimation for Logistic Regression/ANN, ensemble voting for Random Forest, and sequential loss minimization for XGBoost.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/train.py:80`; `app/backend/src/app/ml/predictive_maintenance/train.py:97`

### Q346. viva defense: `n_jobs=-1`?

In XGBoost, `n_jobs=-1` means parallelism. The choice is a conservative tabular-ML default for this predictive maintenance dataset. It connects to the model principle: probability estimation for Logistic Regression/ANN, ensemble voting for Random Forest, and sequential loss minimization for XGBoost.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/train.py:80`; `app/backend/src/app/ml/predictive_maintenance/train.py:97`

### Q347. why used: `regularized objective`?

In XGBoost, `regularized objective` means loss plus complexity. The choice is a conservative tabular-ML default for this predictive maintenance dataset. It connects to the model principle: probability estimation for Logistic Regression/ANN, ensemble voting for Random Forest, and sequential loss minimization for XGBoost.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/train.py:90`

### Q348. algorithm formula: `regularized objective`?

In XGBoost, `regularized objective` means loss plus complexity. The choice is a conservative tabular-ML default for this predictive maintenance dataset. It connects to the model principle: probability estimation for Logistic Regression/ANN, ensemble voting for Random Forest, and sequential loss minimization for XGBoost.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/train.py:90`

### Q349. chosen value reasoning: `regularized objective`?

In XGBoost, `regularized objective` means loss plus complexity. The choice is a conservative tabular-ML default for this predictive maintenance dataset. It connects to the model principle: probability estimation for Logistic Regression/ANN, ensemble voting for Random Forest, and sequential loss minimization for XGBoost.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/train.py:90`

### Q350. overfitting impact: `regularized objective`?

In XGBoost, `regularized objective` means loss plus complexity. The choice is a conservative tabular-ML default for this predictive maintenance dataset. It connects to the model principle: probability estimation for Logistic Regression/ANN, ensemble voting for Random Forest, and sequential loss minimization for XGBoost.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/train.py:90`

### Q351. what to tune: `regularized objective`?

In XGBoost, `regularized objective` means loss plus complexity. The choice is a conservative tabular-ML default for this predictive maintenance dataset. It connects to the model principle: probability estimation for Logistic Regression/ANN, ensemble voting for Random Forest, and sequential loss minimization for XGBoost.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/train.py:90`

### Q352. viva defense: `regularized objective`?

In XGBoost, `regularized objective` means loss plus complexity. The choice is a conservative tabular-ML default for this predictive maintenance dataset. It connects to the model principle: probability estimation for Logistic Regression/ANN, ensemble voting for Random Forest, and sequential loss minimization for XGBoost.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/train.py:90`

## ANN

### Q353. why used: `Sequential`?

In ANN, `Sequential` means layer stack. The choice is a conservative tabular-ML default for this predictive maintenance dataset. It connects to the model principle: probability estimation for Logistic Regression/ANN, ensemble voting for Random Forest, and sequential loss minimization for XGBoost.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/train.py:12`; `app/backend/src/app/ml/predictive_maintenance/train.py:24`

### Q354. algorithm formula: `Sequential`?

In ANN, `Sequential` means layer stack. The choice is a conservative tabular-ML default for this predictive maintenance dataset. It connects to the model principle: probability estimation for Logistic Regression/ANN, ensemble voting for Random Forest, and sequential loss minimization for XGBoost.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/train.py:12`; `app/backend/src/app/ml/predictive_maintenance/train.py:24`

### Q355. chosen value reasoning: `Sequential`?

In ANN, `Sequential` means layer stack. The choice is a conservative tabular-ML default for this predictive maintenance dataset. It connects to the model principle: probability estimation for Logistic Regression/ANN, ensemble voting for Random Forest, and sequential loss minimization for XGBoost.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/train.py:12`; `app/backend/src/app/ml/predictive_maintenance/train.py:24`

### Q356. overfitting impact: `Sequential`?

In ANN, `Sequential` means layer stack. The choice is a conservative tabular-ML default for this predictive maintenance dataset. It connects to the model principle: probability estimation for Logistic Regression/ANN, ensemble voting for Random Forest, and sequential loss minimization for XGBoost.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/train.py:12`; `app/backend/src/app/ml/predictive_maintenance/train.py:24`

### Q357. what to tune: `Sequential`?

In ANN, `Sequential` means layer stack. The choice is a conservative tabular-ML default for this predictive maintenance dataset. It connects to the model principle: probability estimation for Logistic Regression/ANN, ensemble voting for Random Forest, and sequential loss minimization for XGBoost.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/train.py:12`; `app/backend/src/app/ml/predictive_maintenance/train.py:24`

### Q358. viva defense: `Sequential`?

In ANN, `Sequential` means layer stack. The choice is a conservative tabular-ML default for this predictive maintenance dataset. It connects to the model principle: probability estimation for Logistic Regression/ANN, ensemble voting for Random Forest, and sequential loss minimization for XGBoost.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/train.py:12`; `app/backend/src/app/ml/predictive_maintenance/train.py:24`

### Q359. why used: `Dense(64)`?

In ANN, `Dense(64)` means first hidden capacity. The choice is a conservative tabular-ML default for this predictive maintenance dataset. It connects to the model principle: probability estimation for Logistic Regression/ANN, ensemble voting for Random Forest, and sequential loss minimization for XGBoost.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/train.py:31`

### Q360. algorithm formula: `Dense(64)`?

In ANN, `Dense(64)` means first hidden capacity. The choice is a conservative tabular-ML default for this predictive maintenance dataset. It connects to the model principle: probability estimation for Logistic Regression/ANN, ensemble voting for Random Forest, and sequential loss minimization for XGBoost.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/train.py:31`

### Q361. chosen value reasoning: `Dense(64)`?

In ANN, `Dense(64)` means first hidden capacity. The choice is a conservative tabular-ML default for this predictive maintenance dataset. It connects to the model principle: probability estimation for Logistic Regression/ANN, ensemble voting for Random Forest, and sequential loss minimization for XGBoost.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/train.py:31`

### Q362. overfitting impact: `Dense(64)`?

In ANN, `Dense(64)` means first hidden capacity. The choice is a conservative tabular-ML default for this predictive maintenance dataset. It connects to the model principle: probability estimation for Logistic Regression/ANN, ensemble voting for Random Forest, and sequential loss minimization for XGBoost.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/train.py:31`

### Q363. what to tune: `Dense(64)`?

In ANN, `Dense(64)` means first hidden capacity. The choice is a conservative tabular-ML default for this predictive maintenance dataset. It connects to the model principle: probability estimation for Logistic Regression/ANN, ensemble voting for Random Forest, and sequential loss minimization for XGBoost.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/train.py:31`

### Q364. viva defense: `Dense(64)`?

In ANN, `Dense(64)` means first hidden capacity. The choice is a conservative tabular-ML default for this predictive maintenance dataset. It connects to the model principle: probability estimation for Logistic Regression/ANN, ensemble voting for Random Forest, and sequential loss minimization for XGBoost.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/train.py:31`

### Q365. why used: `relu`?

In ANN, `relu` means nonlinear activation. The choice is a conservative tabular-ML default for this predictive maintenance dataset. It connects to the model principle: probability estimation for Logistic Regression/ANN, ensemble voting for Random Forest, and sequential loss minimization for XGBoost.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/train.py:31`; `app/backend/src/app/ml/predictive_maintenance/train.py:33`

### Q366. algorithm formula: `relu`?

In ANN, `relu` means nonlinear activation. The choice is a conservative tabular-ML default for this predictive maintenance dataset. It connects to the model principle: probability estimation for Logistic Regression/ANN, ensemble voting for Random Forest, and sequential loss minimization for XGBoost.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/train.py:31`; `app/backend/src/app/ml/predictive_maintenance/train.py:33`

### Q367. chosen value reasoning: `relu`?

In ANN, `relu` means nonlinear activation. The choice is a conservative tabular-ML default for this predictive maintenance dataset. It connects to the model principle: probability estimation for Logistic Regression/ANN, ensemble voting for Random Forest, and sequential loss minimization for XGBoost.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/train.py:31`; `app/backend/src/app/ml/predictive_maintenance/train.py:33`

### Q368. overfitting impact: `relu`?

In ANN, `relu` means nonlinear activation. The choice is a conservative tabular-ML default for this predictive maintenance dataset. It connects to the model principle: probability estimation for Logistic Regression/ANN, ensemble voting for Random Forest, and sequential loss minimization for XGBoost.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/train.py:31`; `app/backend/src/app/ml/predictive_maintenance/train.py:33`

### Q369. what to tune: `relu`?

In ANN, `relu` means nonlinear activation. The choice is a conservative tabular-ML default for this predictive maintenance dataset. It connects to the model principle: probability estimation for Logistic Regression/ANN, ensemble voting for Random Forest, and sequential loss minimization for XGBoost.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/train.py:31`; `app/backend/src/app/ml/predictive_maintenance/train.py:33`

### Q370. viva defense: `relu`?

In ANN, `relu` means nonlinear activation. The choice is a conservative tabular-ML default for this predictive maintenance dataset. It connects to the model principle: probability estimation for Logistic Regression/ANN, ensemble voting for Random Forest, and sequential loss minimization for XGBoost.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/train.py:31`; `app/backend/src/app/ml/predictive_maintenance/train.py:33`

### Q371. why used: `input_shape=(n_features,)`?

In ANN, `input_shape=(n_features,)` means feature dimension. The choice is a conservative tabular-ML default for this predictive maintenance dataset. It connects to the model principle: probability estimation for Logistic Regression/ANN, ensemble voting for Random Forest, and sequential loss minimization for XGBoost.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/train.py:31`

### Q372. algorithm formula: `input_shape=(n_features,)`?

In ANN, `input_shape=(n_features,)` means feature dimension. The choice is a conservative tabular-ML default for this predictive maintenance dataset. It connects to the model principle: probability estimation for Logistic Regression/ANN, ensemble voting for Random Forest, and sequential loss minimization for XGBoost.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/train.py:31`

### Q373. chosen value reasoning: `input_shape=(n_features,)`?

In ANN, `input_shape=(n_features,)` means feature dimension. The choice is a conservative tabular-ML default for this predictive maintenance dataset. It connects to the model principle: probability estimation for Logistic Regression/ANN, ensemble voting for Random Forest, and sequential loss minimization for XGBoost.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/train.py:31`

### Q374. overfitting impact: `input_shape=(n_features,)`?

In ANN, `input_shape=(n_features,)` means feature dimension. The choice is a conservative tabular-ML default for this predictive maintenance dataset. It connects to the model principle: probability estimation for Logistic Regression/ANN, ensemble voting for Random Forest, and sequential loss minimization for XGBoost.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/train.py:31`

### Q375. what to tune: `input_shape=(n_features,)`?

In ANN, `input_shape=(n_features,)` means feature dimension. The choice is a conservative tabular-ML default for this predictive maintenance dataset. It connects to the model principle: probability estimation for Logistic Regression/ANN, ensemble voting for Random Forest, and sequential loss minimization for XGBoost.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/train.py:31`

### Q376. viva defense: `input_shape=(n_features,)`?

In ANN, `input_shape=(n_features,)` means feature dimension. The choice is a conservative tabular-ML default for this predictive maintenance dataset. It connects to the model principle: probability estimation for Logistic Regression/ANN, ensemble voting for Random Forest, and sequential loss minimization for XGBoost.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/train.py:31`

### Q377. why used: `Dropout(0.2)`?

In ANN, `Dropout(0.2)` means 20 percent regularization. The choice is a conservative tabular-ML default for this predictive maintenance dataset. It connects to the model principle: probability estimation for Logistic Regression/ANN, ensemble voting for Random Forest, and sequential loss minimization for XGBoost.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/train.py:32`

### Q378. algorithm formula: `Dropout(0.2)`?

In ANN, `Dropout(0.2)` means 20 percent regularization. The choice is a conservative tabular-ML default for this predictive maintenance dataset. It connects to the model principle: probability estimation for Logistic Regression/ANN, ensemble voting for Random Forest, and sequential loss minimization for XGBoost.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/train.py:32`

### Q379. chosen value reasoning: `Dropout(0.2)`?

In ANN, `Dropout(0.2)` means 20 percent regularization. The choice is a conservative tabular-ML default for this predictive maintenance dataset. It connects to the model principle: probability estimation for Logistic Regression/ANN, ensemble voting for Random Forest, and sequential loss minimization for XGBoost.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/train.py:32`

### Q380. overfitting impact: `Dropout(0.2)`?

In ANN, `Dropout(0.2)` means 20 percent regularization. The choice is a conservative tabular-ML default for this predictive maintenance dataset. It connects to the model principle: probability estimation for Logistic Regression/ANN, ensemble voting for Random Forest, and sequential loss minimization for XGBoost.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/train.py:32`

### Q381. what to tune: `Dropout(0.2)`?

In ANN, `Dropout(0.2)` means 20 percent regularization. The choice is a conservative tabular-ML default for this predictive maintenance dataset. It connects to the model principle: probability estimation for Logistic Regression/ANN, ensemble voting for Random Forest, and sequential loss minimization for XGBoost.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/train.py:32`

### Q382. viva defense: `Dropout(0.2)`?

In ANN, `Dropout(0.2)` means 20 percent regularization. The choice is a conservative tabular-ML default for this predictive maintenance dataset. It connects to the model principle: probability estimation for Logistic Regression/ANN, ensemble voting for Random Forest, and sequential loss minimization for XGBoost.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/train.py:32`

### Q383. why used: `Dense(32)`?

In ANN, `Dense(32)` means compressed hidden layer. The choice is a conservative tabular-ML default for this predictive maintenance dataset. It connects to the model principle: probability estimation for Logistic Regression/ANN, ensemble voting for Random Forest, and sequential loss minimization for XGBoost.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/train.py:33`

### Q384. algorithm formula: `Dense(32)`?

In ANN, `Dense(32)` means compressed hidden layer. The choice is a conservative tabular-ML default for this predictive maintenance dataset. It connects to the model principle: probability estimation for Logistic Regression/ANN, ensemble voting for Random Forest, and sequential loss minimization for XGBoost.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/train.py:33`

### Q385. chosen value reasoning: `Dense(32)`?

In ANN, `Dense(32)` means compressed hidden layer. The choice is a conservative tabular-ML default for this predictive maintenance dataset. It connects to the model principle: probability estimation for Logistic Regression/ANN, ensemble voting for Random Forest, and sequential loss minimization for XGBoost.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/train.py:33`

### Q386. overfitting impact: `Dense(32)`?

In ANN, `Dense(32)` means compressed hidden layer. The choice is a conservative tabular-ML default for this predictive maintenance dataset. It connects to the model principle: probability estimation for Logistic Regression/ANN, ensemble voting for Random Forest, and sequential loss minimization for XGBoost.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/train.py:33`

### Q387. what to tune: `Dense(32)`?

In ANN, `Dense(32)` means compressed hidden layer. The choice is a conservative tabular-ML default for this predictive maintenance dataset. It connects to the model principle: probability estimation for Logistic Regression/ANN, ensemble voting for Random Forest, and sequential loss minimization for XGBoost.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/train.py:33`

### Q388. viva defense: `Dense(32)`?

In ANN, `Dense(32)` means compressed hidden layer. The choice is a conservative tabular-ML default for this predictive maintenance dataset. It connects to the model principle: probability estimation for Logistic Regression/ANN, ensemble voting for Random Forest, and sequential loss minimization for XGBoost.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/train.py:33`

### Q389. why used: `Dropout(0.1)`?

In ANN, `Dropout(0.1)` means lighter regularization. The choice is a conservative tabular-ML default for this predictive maintenance dataset. It connects to the model principle: probability estimation for Logistic Regression/ANN, ensemble voting for Random Forest, and sequential loss minimization for XGBoost.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/train.py:34`

### Q390. algorithm formula: `Dropout(0.1)`?

In ANN, `Dropout(0.1)` means lighter regularization. The choice is a conservative tabular-ML default for this predictive maintenance dataset. It connects to the model principle: probability estimation for Logistic Regression/ANN, ensemble voting for Random Forest, and sequential loss minimization for XGBoost.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/train.py:34`

### Q391. chosen value reasoning: `Dropout(0.1)`?

In ANN, `Dropout(0.1)` means lighter regularization. The choice is a conservative tabular-ML default for this predictive maintenance dataset. It connects to the model principle: probability estimation for Logistic Regression/ANN, ensemble voting for Random Forest, and sequential loss minimization for XGBoost.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/train.py:34`

### Q392. overfitting impact: `Dropout(0.1)`?

In ANN, `Dropout(0.1)` means lighter regularization. The choice is a conservative tabular-ML default for this predictive maintenance dataset. It connects to the model principle: probability estimation for Logistic Regression/ANN, ensemble voting for Random Forest, and sequential loss minimization for XGBoost.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/train.py:34`

### Q393. what to tune: `Dropout(0.1)`?

In ANN, `Dropout(0.1)` means lighter regularization. The choice is a conservative tabular-ML default for this predictive maintenance dataset. It connects to the model principle: probability estimation for Logistic Regression/ANN, ensemble voting for Random Forest, and sequential loss minimization for XGBoost.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/train.py:34`

### Q394. viva defense: `Dropout(0.1)`?

In ANN, `Dropout(0.1)` means lighter regularization. The choice is a conservative tabular-ML default for this predictive maintenance dataset. It connects to the model principle: probability estimation for Logistic Regression/ANN, ensemble voting for Random Forest, and sequential loss minimization for XGBoost.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/train.py:34`

### Q395. why used: `Dense(1)`?

In ANN, `Dense(1)` means binary output. The choice is a conservative tabular-ML default for this predictive maintenance dataset. It connects to the model principle: probability estimation for Logistic Regression/ANN, ensemble voting for Random Forest, and sequential loss minimization for XGBoost.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/train.py:35`

### Q396. algorithm formula: `Dense(1)`?

In ANN, `Dense(1)` means binary output. The choice is a conservative tabular-ML default for this predictive maintenance dataset. It connects to the model principle: probability estimation for Logistic Regression/ANN, ensemble voting for Random Forest, and sequential loss minimization for XGBoost.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/train.py:35`

### Q397. chosen value reasoning: `Dense(1)`?

In ANN, `Dense(1)` means binary output. The choice is a conservative tabular-ML default for this predictive maintenance dataset. It connects to the model principle: probability estimation for Logistic Regression/ANN, ensemble voting for Random Forest, and sequential loss minimization for XGBoost.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/train.py:35`

### Q398. overfitting impact: `Dense(1)`?

In ANN, `Dense(1)` means binary output. The choice is a conservative tabular-ML default for this predictive maintenance dataset. It connects to the model principle: probability estimation for Logistic Regression/ANN, ensemble voting for Random Forest, and sequential loss minimization for XGBoost.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/train.py:35`

### Q399. what to tune: `Dense(1)`?

In ANN, `Dense(1)` means binary output. The choice is a conservative tabular-ML default for this predictive maintenance dataset. It connects to the model principle: probability estimation for Logistic Regression/ANN, ensemble voting for Random Forest, and sequential loss minimization for XGBoost.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/train.py:35`

### Q400. viva defense: `Dense(1)`?

In ANN, `Dense(1)` means binary output. The choice is a conservative tabular-ML default for this predictive maintenance dataset. It connects to the model principle: probability estimation for Logistic Regression/ANN, ensemble voting for Random Forest, and sequential loss minimization for XGBoost.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/train.py:35`

### Q401. why used: `sigmoid`?

In ANN, `sigmoid` means probability output. The choice is a conservative tabular-ML default for this predictive maintenance dataset. It connects to the model principle: probability estimation for Logistic Regression/ANN, ensemble voting for Random Forest, and sequential loss minimization for XGBoost.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/train.py:35`

### Q402. algorithm formula: `sigmoid`?

In ANN, `sigmoid` means probability output. The choice is a conservative tabular-ML default for this predictive maintenance dataset. It connects to the model principle: probability estimation for Logistic Regression/ANN, ensemble voting for Random Forest, and sequential loss minimization for XGBoost.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/train.py:35`

### Q403. chosen value reasoning: `sigmoid`?

In ANN, `sigmoid` means probability output. The choice is a conservative tabular-ML default for this predictive maintenance dataset. It connects to the model principle: probability estimation for Logistic Regression/ANN, ensemble voting for Random Forest, and sequential loss minimization for XGBoost.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/train.py:35`

### Q404. overfitting impact: `sigmoid`?

In ANN, `sigmoid` means probability output. The choice is a conservative tabular-ML default for this predictive maintenance dataset. It connects to the model principle: probability estimation for Logistic Regression/ANN, ensemble voting for Random Forest, and sequential loss minimization for XGBoost.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/train.py:35`

### Q405. what to tune: `sigmoid`?

In ANN, `sigmoid` means probability output. The choice is a conservative tabular-ML default for this predictive maintenance dataset. It connects to the model principle: probability estimation for Logistic Regression/ANN, ensemble voting for Random Forest, and sequential loss minimization for XGBoost.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/train.py:35`

### Q406. viva defense: `sigmoid`?

In ANN, `sigmoid` means probability output. The choice is a conservative tabular-ML default for this predictive maintenance dataset. It connects to the model principle: probability estimation for Logistic Regression/ANN, ensemble voting for Random Forest, and sequential loss minimization for XGBoost.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/train.py:35`

### Q407. why used: `Adam lr=0.001`?

In ANN, `Adam lr=0.001` means adaptive optimizer. The choice is a conservative tabular-ML default for this predictive maintenance dataset. It connects to the model principle: probability estimation for Logistic Regression/ANN, ensemble voting for Random Forest, and sequential loss minimization for XGBoost.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/train.py:39`

### Q408. algorithm formula: `Adam lr=0.001`?

In ANN, `Adam lr=0.001` means adaptive optimizer. The choice is a conservative tabular-ML default for this predictive maintenance dataset. It connects to the model principle: probability estimation for Logistic Regression/ANN, ensemble voting for Random Forest, and sequential loss minimization for XGBoost.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/train.py:39`

### Q409. chosen value reasoning: `Adam lr=0.001`?

In ANN, `Adam lr=0.001` means adaptive optimizer. The choice is a conservative tabular-ML default for this predictive maintenance dataset. It connects to the model principle: probability estimation for Logistic Regression/ANN, ensemble voting for Random Forest, and sequential loss minimization for XGBoost.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/train.py:39`

### Q410. overfitting impact: `Adam lr=0.001`?

In ANN, `Adam lr=0.001` means adaptive optimizer. The choice is a conservative tabular-ML default for this predictive maintenance dataset. It connects to the model principle: probability estimation for Logistic Regression/ANN, ensemble voting for Random Forest, and sequential loss minimization for XGBoost.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/train.py:39`

### Q411. what to tune: `Adam lr=0.001`?

In ANN, `Adam lr=0.001` means adaptive optimizer. The choice is a conservative tabular-ML default for this predictive maintenance dataset. It connects to the model principle: probability estimation for Logistic Regression/ANN, ensemble voting for Random Forest, and sequential loss minimization for XGBoost.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/train.py:39`

### Q412. viva defense: `Adam lr=0.001`?

In ANN, `Adam lr=0.001` means adaptive optimizer. The choice is a conservative tabular-ML default for this predictive maintenance dataset. It connects to the model principle: probability estimation for Logistic Regression/ANN, ensemble voting for Random Forest, and sequential loss minimization for XGBoost.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/train.py:39`

### Q413. why used: `binary_crossentropy`?

In ANN, `binary_crossentropy` means binary loss. The choice is a conservative tabular-ML default for this predictive maintenance dataset. It connects to the model principle: probability estimation for Logistic Regression/ANN, ensemble voting for Random Forest, and sequential loss minimization for XGBoost.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/train.py:40`

### Q414. algorithm formula: `binary_crossentropy`?

In ANN, `binary_crossentropy` means binary loss. The choice is a conservative tabular-ML default for this predictive maintenance dataset. It connects to the model principle: probability estimation for Logistic Regression/ANN, ensemble voting for Random Forest, and sequential loss minimization for XGBoost.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/train.py:40`

### Q415. chosen value reasoning: `binary_crossentropy`?

In ANN, `binary_crossentropy` means binary loss. The choice is a conservative tabular-ML default for this predictive maintenance dataset. It connects to the model principle: probability estimation for Logistic Regression/ANN, ensemble voting for Random Forest, and sequential loss minimization for XGBoost.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/train.py:40`

### Q416. overfitting impact: `binary_crossentropy`?

In ANN, `binary_crossentropy` means binary loss. The choice is a conservative tabular-ML default for this predictive maintenance dataset. It connects to the model principle: probability estimation for Logistic Regression/ANN, ensemble voting for Random Forest, and sequential loss minimization for XGBoost.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/train.py:40`

### Q417. what to tune: `binary_crossentropy`?

In ANN, `binary_crossentropy` means binary loss. The choice is a conservative tabular-ML default for this predictive maintenance dataset. It connects to the model principle: probability estimation for Logistic Regression/ANN, ensemble voting for Random Forest, and sequential loss minimization for XGBoost.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/train.py:40`

### Q418. viva defense: `binary_crossentropy`?

In ANN, `binary_crossentropy` means binary loss. The choice is a conservative tabular-ML default for this predictive maintenance dataset. It connects to the model principle: probability estimation for Logistic Regression/ANN, ensemble voting for Random Forest, and sequential loss minimization for XGBoost.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/train.py:40`

### Q419. why used: `accuracy metric`?

In ANN, `accuracy metric` means training monitor. The choice is a conservative tabular-ML default for this predictive maintenance dataset. It connects to the model principle: probability estimation for Logistic Regression/ANN, ensemble voting for Random Forest, and sequential loss minimization for XGBoost.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/train.py:41`

### Q420. algorithm formula: `accuracy metric`?

In ANN, `accuracy metric` means training monitor. The choice is a conservative tabular-ML default for this predictive maintenance dataset. It connects to the model principle: probability estimation for Logistic Regression/ANN, ensemble voting for Random Forest, and sequential loss minimization for XGBoost.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/train.py:41`

### Q421. chosen value reasoning: `accuracy metric`?

In ANN, `accuracy metric` means training monitor. The choice is a conservative tabular-ML default for this predictive maintenance dataset. It connects to the model principle: probability estimation for Logistic Regression/ANN, ensemble voting for Random Forest, and sequential loss minimization for XGBoost.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/train.py:41`

### Q422. overfitting impact: `accuracy metric`?

In ANN, `accuracy metric` means training monitor. The choice is a conservative tabular-ML default for this predictive maintenance dataset. It connects to the model principle: probability estimation for Logistic Regression/ANN, ensemble voting for Random Forest, and sequential loss minimization for XGBoost.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/train.py:41`

### Q423. what to tune: `accuracy metric`?

In ANN, `accuracy metric` means training monitor. The choice is a conservative tabular-ML default for this predictive maintenance dataset. It connects to the model principle: probability estimation for Logistic Regression/ANN, ensemble voting for Random Forest, and sequential loss minimization for XGBoost.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/train.py:41`

### Q424. viva defense: `accuracy metric`?

In ANN, `accuracy metric` means training monitor. The choice is a conservative tabular-ML default for this predictive maintenance dataset. It connects to the model principle: probability estimation for Logistic Regression/ANN, ensemble voting for Random Forest, and sequential loss minimization for XGBoost.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/train.py:41`

### Q425. why used: `epochs=50`?

In ANN, `epochs=50` means max epochs. The choice is a conservative tabular-ML default for this predictive maintenance dataset. It connects to the model principle: probability estimation for Logistic Regression/ANN, ensemble voting for Random Forest, and sequential loss minimization for XGBoost.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/train.py:113`; `app/backend/src/app/ml/predictive_maintenance/train.py:133`

### Q426. algorithm formula: `epochs=50`?

In ANN, `epochs=50` means max epochs. The choice is a conservative tabular-ML default for this predictive maintenance dataset. It connects to the model principle: probability estimation for Logistic Regression/ANN, ensemble voting for Random Forest, and sequential loss minimization for XGBoost.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/train.py:113`; `app/backend/src/app/ml/predictive_maintenance/train.py:133`

### Q427. chosen value reasoning: `epochs=50`?

In ANN, `epochs=50` means max epochs. The choice is a conservative tabular-ML default for this predictive maintenance dataset. It connects to the model principle: probability estimation for Logistic Regression/ANN, ensemble voting for Random Forest, and sequential loss minimization for XGBoost.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/train.py:113`; `app/backend/src/app/ml/predictive_maintenance/train.py:133`

### Q428. overfitting impact: `epochs=50`?

In ANN, `epochs=50` means max epochs. The choice is a conservative tabular-ML default for this predictive maintenance dataset. It connects to the model principle: probability estimation for Logistic Regression/ANN, ensemble voting for Random Forest, and sequential loss minimization for XGBoost.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/train.py:113`; `app/backend/src/app/ml/predictive_maintenance/train.py:133`

### Q429. what to tune: `epochs=50`?

In ANN, `epochs=50` means max epochs. The choice is a conservative tabular-ML default for this predictive maintenance dataset. It connects to the model principle: probability estimation for Logistic Regression/ANN, ensemble voting for Random Forest, and sequential loss minimization for XGBoost.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/train.py:113`; `app/backend/src/app/ml/predictive_maintenance/train.py:133`

### Q430. viva defense: `epochs=50`?

In ANN, `epochs=50` means max epochs. The choice is a conservative tabular-ML default for this predictive maintenance dataset. It connects to the model principle: probability estimation for Logistic Regression/ANN, ensemble voting for Random Forest, and sequential loss minimization for XGBoost.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/train.py:113`; `app/backend/src/app/ml/predictive_maintenance/train.py:133`

### Q431. why used: `batch_size=32`?

In ANN, `batch_size=32` means samples per update. The choice is a conservative tabular-ML default for this predictive maintenance dataset. It connects to the model principle: probability estimation for Logistic Regression/ANN, ensemble voting for Random Forest, and sequential loss minimization for XGBoost.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/train.py:114`; `app/backend/src/app/ml/predictive_maintenance/train.py:134`

### Q432. algorithm formula: `batch_size=32`?

In ANN, `batch_size=32` means samples per update. The choice is a conservative tabular-ML default for this predictive maintenance dataset. It connects to the model principle: probability estimation for Logistic Regression/ANN, ensemble voting for Random Forest, and sequential loss minimization for XGBoost.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/train.py:114`; `app/backend/src/app/ml/predictive_maintenance/train.py:134`

### Q433. chosen value reasoning: `batch_size=32`?

In ANN, `batch_size=32` means samples per update. The choice is a conservative tabular-ML default for this predictive maintenance dataset. It connects to the model principle: probability estimation for Logistic Regression/ANN, ensemble voting for Random Forest, and sequential loss minimization for XGBoost.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/train.py:114`; `app/backend/src/app/ml/predictive_maintenance/train.py:134`

### Q434. overfitting impact: `batch_size=32`?

In ANN, `batch_size=32` means samples per update. The choice is a conservative tabular-ML default for this predictive maintenance dataset. It connects to the model principle: probability estimation for Logistic Regression/ANN, ensemble voting for Random Forest, and sequential loss minimization for XGBoost.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/train.py:114`; `app/backend/src/app/ml/predictive_maintenance/train.py:134`

### Q435. what to tune: `batch_size=32`?

In ANN, `batch_size=32` means samples per update. The choice is a conservative tabular-ML default for this predictive maintenance dataset. It connects to the model principle: probability estimation for Logistic Regression/ANN, ensemble voting for Random Forest, and sequential loss minimization for XGBoost.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/train.py:114`; `app/backend/src/app/ml/predictive_maintenance/train.py:134`

### Q436. viva defense: `batch_size=32`?

In ANN, `batch_size=32` means samples per update. The choice is a conservative tabular-ML default for this predictive maintenance dataset. It connects to the model principle: probability estimation for Logistic Regression/ANN, ensemble voting for Random Forest, and sequential loss minimization for XGBoost.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/train.py:114`; `app/backend/src/app/ml/predictive_maintenance/train.py:134`

### Q437. why used: `verbose=0`?

In ANN, `verbose=0` means quiet automation. The choice is a conservative tabular-ML default for this predictive maintenance dataset. It connects to the model principle: probability estimation for Logistic Regression/ANN, ensemble voting for Random Forest, and sequential loss minimization for XGBoost.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/train.py:137`

### Q438. algorithm formula: `verbose=0`?

In ANN, `verbose=0` means quiet automation. The choice is a conservative tabular-ML default for this predictive maintenance dataset. It connects to the model principle: probability estimation for Logistic Regression/ANN, ensemble voting for Random Forest, and sequential loss minimization for XGBoost.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/train.py:137`

### Q439. chosen value reasoning: `verbose=0`?

In ANN, `verbose=0` means quiet automation. The choice is a conservative tabular-ML default for this predictive maintenance dataset. It connects to the model principle: probability estimation for Logistic Regression/ANN, ensemble voting for Random Forest, and sequential loss minimization for XGBoost.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/train.py:137`

### Q440. overfitting impact: `verbose=0`?

In ANN, `verbose=0` means quiet automation. The choice is a conservative tabular-ML default for this predictive maintenance dataset. It connects to the model principle: probability estimation for Logistic Regression/ANN, ensemble voting for Random Forest, and sequential loss minimization for XGBoost.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/train.py:137`

### Q441. what to tune: `verbose=0`?

In ANN, `verbose=0` means quiet automation. The choice is a conservative tabular-ML default for this predictive maintenance dataset. It connects to the model principle: probability estimation for Logistic Regression/ANN, ensemble voting for Random Forest, and sequential loss minimization for XGBoost.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/train.py:137`

### Q442. viva defense: `verbose=0`?

In ANN, `verbose=0` means quiet automation. The choice is a conservative tabular-ML default for this predictive maintenance dataset. It connects to the model principle: probability estimation for Logistic Regression/ANN, ensemble voting for Random Forest, and sequential loss minimization for XGBoost.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/train.py:137`

## ANN Training

### Q443. purpose: `EarlyStopping`?

`EarlyStopping` stops when validation stops improving. It helps the neural network stop at a model that generalizes, not merely one that keeps improving on training samples.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/train.py:13`; `app/backend/src/app/ml/predictive_maintenance/train.py:127`

### Q444. overfitting control: `EarlyStopping`?

`EarlyStopping` stops when validation stops improving. It helps the neural network stop at a model that generalizes, not merely one that keeps improving on training samples.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/train.py:13`; `app/backend/src/app/ml/predictive_maintenance/train.py:127`

### Q445. why value: `EarlyStopping`?

`EarlyStopping` stops when validation stops improving. It helps the neural network stop at a model that generalizes, not merely one that keeps improving on training samples.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/train.py:13`; `app/backend/src/app/ml/predictive_maintenance/train.py:127`

### Q446. what if removed: `EarlyStopping`?

`EarlyStopping` stops when validation stops improving. It helps the neural network stop at a model that generalizes, not merely one that keeps improving on training samples.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/train.py:13`; `app/backend/src/app/ml/predictive_maintenance/train.py:127`

### Q447. defense answer: `EarlyStopping`?

`EarlyStopping` stops when validation stops improving. It helps the neural network stop at a model that generalizes, not merely one that keeps improving on training samples.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/train.py:13`; `app/backend/src/app/ml/predictive_maintenance/train.py:127`

### Q448. purpose: `monitor=val_loss`?

`monitor=val_loss` tracks generalization loss. It helps the neural network stop at a model that generalizes, not merely one that keeps improving on training samples.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/train.py:127`

### Q449. overfitting control: `monitor=val_loss`?

`monitor=val_loss` tracks generalization loss. It helps the neural network stop at a model that generalizes, not merely one that keeps improving on training samples.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/train.py:127`

### Q450. why value: `monitor=val_loss`?

`monitor=val_loss` tracks generalization loss. It helps the neural network stop at a model that generalizes, not merely one that keeps improving on training samples.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/train.py:127`

### Q451. what if removed: `monitor=val_loss`?

`monitor=val_loss` tracks generalization loss. It helps the neural network stop at a model that generalizes, not merely one that keeps improving on training samples.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/train.py:127`

### Q452. defense answer: `monitor=val_loss`?

`monitor=val_loss` tracks generalization loss. It helps the neural network stop at a model that generalizes, not merely one that keeps improving on training samples.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/train.py:127`

### Q453. purpose: `patience=5`?

`patience=5` waits 5 epochs. It helps the neural network stop at a model that generalizes, not merely one that keeps improving on training samples.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/train.py:127`

### Q454. overfitting control: `patience=5`?

`patience=5` waits 5 epochs. It helps the neural network stop at a model that generalizes, not merely one that keeps improving on training samples.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/train.py:127`

### Q455. why value: `patience=5`?

`patience=5` waits 5 epochs. It helps the neural network stop at a model that generalizes, not merely one that keeps improving on training samples.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/train.py:127`

### Q456. what if removed: `patience=5`?

`patience=5` waits 5 epochs. It helps the neural network stop at a model that generalizes, not merely one that keeps improving on training samples.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/train.py:127`

### Q457. defense answer: `patience=5`?

`patience=5` waits 5 epochs. It helps the neural network stop at a model that generalizes, not merely one that keeps improving on training samples.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/train.py:127`

### Q458. purpose: `restore_best_weights=True`?

`restore_best_weights=True` keeps best epoch. It helps the neural network stop at a model that generalizes, not merely one that keeps improving on training samples.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/train.py:127`

### Q459. overfitting control: `restore_best_weights=True`?

`restore_best_weights=True` keeps best epoch. It helps the neural network stop at a model that generalizes, not merely one that keeps improving on training samples.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/train.py:127`

### Q460. why value: `restore_best_weights=True`?

`restore_best_weights=True` keeps best epoch. It helps the neural network stop at a model that generalizes, not merely one that keeps improving on training samples.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/train.py:127`

### Q461. what if removed: `restore_best_weights=True`?

`restore_best_weights=True` keeps best epoch. It helps the neural network stop at a model that generalizes, not merely one that keeps improving on training samples.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/train.py:127`

### Q462. defense answer: `restore_best_weights=True`?

`restore_best_weights=True` keeps best epoch. It helps the neural network stop at a model that generalizes, not merely one that keeps improving on training samples.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/train.py:127`

### Q463. purpose: `validation_data`?

`validation_data` unseen training split for ANN. It helps the neural network stop at a model that generalizes, not merely one that keeps improving on training samples.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/train.py:131`

### Q464. overfitting control: `validation_data`?

`validation_data` unseen training split for ANN. It helps the neural network stop at a model that generalizes, not merely one that keeps improving on training samples.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/train.py:131`

### Q465. why value: `validation_data`?

`validation_data` unseen training split for ANN. It helps the neural network stop at a model that generalizes, not merely one that keeps improving on training samples.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/train.py:131`

### Q466. what if removed: `validation_data`?

`validation_data` unseen training split for ANN. It helps the neural network stop at a model that generalizes, not merely one that keeps improving on training samples.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/train.py:131`

### Q467. defense answer: `validation_data`?

`validation_data` unseen training split for ANN. It helps the neural network stop at a model that generalizes, not merely one that keeps improving on training samples.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/train.py:131`

### Q468. purpose: `callbacks=[callback]`?

`callbacks=[callback]` injects stopping logic. It helps the neural network stop at a model that generalizes, not merely one that keeps improving on training samples.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/train.py:136`

### Q469. overfitting control: `callbacks=[callback]`?

`callbacks=[callback]` injects stopping logic. It helps the neural network stop at a model that generalizes, not merely one that keeps improving on training samples.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/train.py:136`

### Q470. why value: `callbacks=[callback]`?

`callbacks=[callback]` injects stopping logic. It helps the neural network stop at a model that generalizes, not merely one that keeps improving on training samples.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/train.py:136`

### Q471. what if removed: `callbacks=[callback]`?

`callbacks=[callback]` injects stopping logic. It helps the neural network stop at a model that generalizes, not merely one that keeps improving on training samples.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/train.py:136`

### Q472. defense answer: `callbacks=[callback]`?

`callbacks=[callback]` injects stopping logic. It helps the neural network stop at a model that generalizes, not merely one that keeps improving on training samples.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/train.py:136`

### Q473. purpose: `history.epoch`?

`history.epoch` actual epochs trained. It helps the neural network stop at a model that generalizes, not merely one that keeps improving on training samples.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/train.py:139`

### Q474. overfitting control: `history.epoch`?

`history.epoch` actual epochs trained. It helps the neural network stop at a model that generalizes, not merely one that keeps improving on training samples.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/train.py:139`

### Q475. why value: `history.epoch`?

`history.epoch` actual epochs trained. It helps the neural network stop at a model that generalizes, not merely one that keeps improving on training samples.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/train.py:139`

### Q476. what if removed: `history.epoch`?

`history.epoch` actual epochs trained. It helps the neural network stop at a model that generalizes, not merely one that keeps improving on training samples.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/train.py:139`

### Q477. defense answer: `history.epoch`?

`history.epoch` actual epochs trained. It helps the neural network stop at a model that generalizes, not merely one that keeps improving on training samples.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/train.py:139`

### Q478. purpose: `model.fit`?

`model.fit` gradient training loop. It helps the neural network stop at a model that generalizes, not merely one that keeps improving on training samples.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/train.py:128`

### Q479. overfitting control: `model.fit`?

`model.fit` gradient training loop. It helps the neural network stop at a model that generalizes, not merely one that keeps improving on training samples.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/train.py:128`

### Q480. why value: `model.fit`?

`model.fit` gradient training loop. It helps the neural network stop at a model that generalizes, not merely one that keeps improving on training samples.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/train.py:128`

### Q481. what if removed: `model.fit`?

`model.fit` gradient training loop. It helps the neural network stop at a model that generalizes, not merely one that keeps improving on training samples.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/train.py:128`

### Q482. defense answer: `model.fit`?

`model.fit` gradient training loop. It helps the neural network stop at a model that generalizes, not merely one that keeps improving on training samples.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/train.py:128`

## Evaluation Metrics

### Q483. definition: `accuracy`?

`accuracy` measures overall correctness. Formula/concept: `(TP+TN)/N`. It is reported because predictive maintenance has asymmetric costs: missed failures and false alarms both matter.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/evaluate.py:25`

### Q484. formula: `accuracy`?

`accuracy` measures overall correctness. Formula/concept: `(TP+TN)/N`. It is reported because predictive maintenance has asymmetric costs: missed failures and false alarms both matter.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/evaluate.py:25`

### Q485. business reason: `accuracy`?

`accuracy` measures overall correctness. Formula/concept: `(TP+TN)/N`. It is reported because predictive maintenance has asymmetric costs: missed failures and false alarms both matter.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/evaluate.py:25`

### Q486. limitation: `accuracy`?

`accuracy` measures overall correctness. Formula/concept: `(TP+TN)/N`. It is reported because predictive maintenance has asymmetric costs: missed failures and false alarms both matter.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/evaluate.py:25`

### Q487. why logged: `accuracy`?

`accuracy` measures overall correctness. Formula/concept: `(TP+TN)/N`. It is reported because predictive maintenance has asymmetric costs: missed failures and false alarms both matter.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/evaluate.py:25`

### Q488. defense answer: `accuracy`?

`accuracy` measures overall correctness. Formula/concept: `(TP+TN)/N`. It is reported because predictive maintenance has asymmetric costs: missed failures and false alarms both matter.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/evaluate.py:25`

### Q489. definition: `precision`?

`precision` measures false alarm control. Formula/concept: `TP/(TP+FP)`. It is reported because predictive maintenance has asymmetric costs: missed failures and false alarms both matter.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/evaluate.py:26`

### Q490. formula: `precision`?

`precision` measures false alarm control. Formula/concept: `TP/(TP+FP)`. It is reported because predictive maintenance has asymmetric costs: missed failures and false alarms both matter.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/evaluate.py:26`

### Q491. business reason: `precision`?

`precision` measures false alarm control. Formula/concept: `TP/(TP+FP)`. It is reported because predictive maintenance has asymmetric costs: missed failures and false alarms both matter.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/evaluate.py:26`

### Q492. limitation: `precision`?

`precision` measures false alarm control. Formula/concept: `TP/(TP+FP)`. It is reported because predictive maintenance has asymmetric costs: missed failures and false alarms both matter.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/evaluate.py:26`

### Q493. why logged: `precision`?

`precision` measures false alarm control. Formula/concept: `TP/(TP+FP)`. It is reported because predictive maintenance has asymmetric costs: missed failures and false alarms both matter.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/evaluate.py:26`

### Q494. defense answer: `precision`?

`precision` measures false alarm control. Formula/concept: `TP/(TP+FP)`. It is reported because predictive maintenance has asymmetric costs: missed failures and false alarms both matter.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/evaluate.py:26`

### Q495. definition: `recall`?

`recall` measures missed failure control. Formula/concept: `TP/(TP+FN)`. It is reported because predictive maintenance has asymmetric costs: missed failures and false alarms both matter.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/evaluate.py:27`

### Q496. formula: `recall`?

`recall` measures missed failure control. Formula/concept: `TP/(TP+FN)`. It is reported because predictive maintenance has asymmetric costs: missed failures and false alarms both matter.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/evaluate.py:27`

### Q497. business reason: `recall`?

`recall` measures missed failure control. Formula/concept: `TP/(TP+FN)`. It is reported because predictive maintenance has asymmetric costs: missed failures and false alarms both matter.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/evaluate.py:27`

### Q498. limitation: `recall`?

`recall` measures missed failure control. Formula/concept: `TP/(TP+FN)`. It is reported because predictive maintenance has asymmetric costs: missed failures and false alarms both matter.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/evaluate.py:27`

### Q499. why logged: `recall`?

`recall` measures missed failure control. Formula/concept: `TP/(TP+FN)`. It is reported because predictive maintenance has asymmetric costs: missed failures and false alarms both matter.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/evaluate.py:27`

### Q500. defense answer: `recall`?

`recall` measures missed failure control. Formula/concept: `TP/(TP+FN)`. It is reported because predictive maintenance has asymmetric costs: missed failures and false alarms both matter.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/evaluate.py:27`

### Q501. definition: `f1_score`?

`f1_score` measures balance precision/recall. Formula/concept: `2PR/(P+R)`. It is reported because predictive maintenance has asymmetric costs: missed failures and false alarms both matter.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/evaluate.py:28`

### Q502. formula: `f1_score`?

`f1_score` measures balance precision/recall. Formula/concept: `2PR/(P+R)`. It is reported because predictive maintenance has asymmetric costs: missed failures and false alarms both matter.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/evaluate.py:28`

### Q503. business reason: `f1_score`?

`f1_score` measures balance precision/recall. Formula/concept: `2PR/(P+R)`. It is reported because predictive maintenance has asymmetric costs: missed failures and false alarms both matter.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/evaluate.py:28`

### Q504. limitation: `f1_score`?

`f1_score` measures balance precision/recall. Formula/concept: `2PR/(P+R)`. It is reported because predictive maintenance has asymmetric costs: missed failures and false alarms both matter.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/evaluate.py:28`

### Q505. why logged: `f1_score`?

`f1_score` measures balance precision/recall. Formula/concept: `2PR/(P+R)`. It is reported because predictive maintenance has asymmetric costs: missed failures and false alarms both matter.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/evaluate.py:28`

### Q506. defense answer: `f1_score`?

`f1_score` measures balance precision/recall. Formula/concept: `2PR/(P+R)`. It is reported because predictive maintenance has asymmetric costs: missed failures and false alarms both matter.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/evaluate.py:28`

### Q507. definition: `roc_auc`?

`roc_auc` measures ranking across thresholds. Formula/concept: `area under ROC`. It is reported because predictive maintenance has asymmetric costs: missed failures and false alarms both matter.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/evaluate.py:29`

### Q508. formula: `roc_auc`?

`roc_auc` measures ranking across thresholds. Formula/concept: `area under ROC`. It is reported because predictive maintenance has asymmetric costs: missed failures and false alarms both matter.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/evaluate.py:29`

### Q509. business reason: `roc_auc`?

`roc_auc` measures ranking across thresholds. Formula/concept: `area under ROC`. It is reported because predictive maintenance has asymmetric costs: missed failures and false alarms both matter.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/evaluate.py:29`

### Q510. limitation: `roc_auc`?

`roc_auc` measures ranking across thresholds. Formula/concept: `area under ROC`. It is reported because predictive maintenance has asymmetric costs: missed failures and false alarms both matter.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/evaluate.py:29`

### Q511. why logged: `roc_auc`?

`roc_auc` measures ranking across thresholds. Formula/concept: `area under ROC`. It is reported because predictive maintenance has asymmetric costs: missed failures and false alarms both matter.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/evaluate.py:29`

### Q512. defense answer: `roc_auc`?

`roc_auc` measures ranking across thresholds. Formula/concept: `area under ROC`. It is reported because predictive maintenance has asymmetric costs: missed failures and false alarms both matter.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/evaluate.py:29`

### Q513. definition: `zero_division=0`?

`zero_division=0` measures prevents crashes. Formula/concept: `safe undefined metric handling`. It is reported because predictive maintenance has asymmetric costs: missed failures and false alarms both matter.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/evaluate.py:26`

### Q514. formula: `zero_division=0`?

`zero_division=0` measures prevents crashes. Formula/concept: `safe undefined metric handling`. It is reported because predictive maintenance has asymmetric costs: missed failures and false alarms both matter.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/evaluate.py:26`

### Q515. business reason: `zero_division=0`?

`zero_division=0` measures prevents crashes. Formula/concept: `safe undefined metric handling`. It is reported because predictive maintenance has asymmetric costs: missed failures and false alarms both matter.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/evaluate.py:26`

### Q516. limitation: `zero_division=0`?

`zero_division=0` measures prevents crashes. Formula/concept: `safe undefined metric handling`. It is reported because predictive maintenance has asymmetric costs: missed failures and false alarms both matter.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/evaluate.py:26`

### Q517. why logged: `zero_division=0`?

`zero_division=0` measures prevents crashes. Formula/concept: `safe undefined metric handling`. It is reported because predictive maintenance has asymmetric costs: missed failures and false alarms both matter.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/evaluate.py:26`

### Q518. defense answer: `zero_division=0`?

`zero_division=0` measures prevents crashes. Formula/concept: `safe undefined metric handling`. It is reported because predictive maintenance has asymmetric costs: missed failures and false alarms both matter.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/evaluate.py:26`

### Q519. definition: `threshold 0.5`?

`threshold 0.5` measures class conversion. Formula/concept: `default probability cutoff`. It is reported because predictive maintenance has asymmetric costs: missed failures and false alarms both matter.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/evaluate.py:41`; `app/backend/src/app/ml/predictive_maintenance/evaluate.py:44`

### Q520. formula: `threshold 0.5`?

`threshold 0.5` measures class conversion. Formula/concept: `default probability cutoff`. It is reported because predictive maintenance has asymmetric costs: missed failures and false alarms both matter.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/evaluate.py:41`; `app/backend/src/app/ml/predictive_maintenance/evaluate.py:44`

### Q521. business reason: `threshold 0.5`?

`threshold 0.5` measures class conversion. Formula/concept: `default probability cutoff`. It is reported because predictive maintenance has asymmetric costs: missed failures and false alarms both matter.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/evaluate.py:41`; `app/backend/src/app/ml/predictive_maintenance/evaluate.py:44`

### Q522. limitation: `threshold 0.5`?

`threshold 0.5` measures class conversion. Formula/concept: `default probability cutoff`. It is reported because predictive maintenance has asymmetric costs: missed failures and false alarms both matter.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/evaluate.py:41`; `app/backend/src/app/ml/predictive_maintenance/evaluate.py:44`

### Q523. why logged: `threshold 0.5`?

`threshold 0.5` measures class conversion. Formula/concept: `default probability cutoff`. It is reported because predictive maintenance has asymmetric costs: missed failures and false alarms both matter.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/evaluate.py:41`; `app/backend/src/app/ml/predictive_maintenance/evaluate.py:44`

### Q524. defense answer: `threshold 0.5`?

`threshold 0.5` measures class conversion. Formula/concept: `default probability cutoff`. It is reported because predictive maintenance has asymmetric costs: missed failures and false alarms both matter.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/evaluate.py:41`; `app/backend/src/app/ml/predictive_maintenance/evaluate.py:44`

### Q525. definition: `sort by f1_score`?

`sort by f1_score` measures imbalance-aware selection. Formula/concept: `best-model rule`. It is reported because predictive maintenance has asymmetric costs: missed failures and false alarms both matter.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/evaluate.py:75`

### Q526. formula: `sort by f1_score`?

`sort by f1_score` measures imbalance-aware selection. Formula/concept: `best-model rule`. It is reported because predictive maintenance has asymmetric costs: missed failures and false alarms both matter.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/evaluate.py:75`

### Q527. business reason: `sort by f1_score`?

`sort by f1_score` measures imbalance-aware selection. Formula/concept: `best-model rule`. It is reported because predictive maintenance has asymmetric costs: missed failures and false alarms both matter.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/evaluate.py:75`

### Q528. limitation: `sort by f1_score`?

`sort by f1_score` measures imbalance-aware selection. Formula/concept: `best-model rule`. It is reported because predictive maintenance has asymmetric costs: missed failures and false alarms both matter.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/evaluate.py:75`

### Q529. why logged: `sort by f1_score`?

`sort by f1_score` measures imbalance-aware selection. Formula/concept: `best-model rule`. It is reported because predictive maintenance has asymmetric costs: missed failures and false alarms both matter.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/evaluate.py:75`

### Q530. defense answer: `sort by f1_score`?

`sort by f1_score` measures imbalance-aware selection. Formula/concept: `best-model rule`. It is reported because predictive maintenance has asymmetric costs: missed failures and false alarms both matter.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/evaluate.py:75`

## MLflow and Persistence

### Q531. why used: `compare_models`?

`compare_models` provides same test-set comparison. It makes the capstone reproducible because the selected model, parameters, metrics, and artifact location can be audited after training.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/evaluate.py:48`; `app/backend/src/app/ml/predictive_maintenance/pipeline.py:69`

### Q532. MLOps value: `compare_models`?

`compare_models` provides same test-set comparison. It makes the capstone reproducible because the selected model, parameters, metrics, and artifact location can be audited after training.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/evaluate.py:48`; `app/backend/src/app/ml/predictive_maintenance/pipeline.py:69`

### Q533. demo explanation: `compare_models`?

`compare_models` provides same test-set comparison. It makes the capstone reproducible because the selected model, parameters, metrics, and artifact location can be audited after training.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/evaluate.py:48`; `app/backend/src/app/ml/predictive_maintenance/pipeline.py:69`

### Q534. risk if missing: `compare_models`?

`compare_models` provides same test-set comparison. It makes the capstone reproducible because the selected model, parameters, metrics, and artifact location can be audited after training.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/evaluate.py:48`; `app/backend/src/app/ml/predictive_maintenance/pipeline.py:69`

### Q535. why used: `best_row=iloc[0]`?

`best_row=iloc[0]` provides top F1 model. It makes the capstone reproducible because the selected model, parameters, metrics, and artifact location can be audited after training.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/pipeline.py:74`

### Q536. MLOps value: `best_row=iloc[0]`?

`best_row=iloc[0]` provides top F1 model. It makes the capstone reproducible because the selected model, parameters, metrics, and artifact location can be audited after training.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/pipeline.py:74`

### Q537. demo explanation: `best_row=iloc[0]`?

`best_row=iloc[0]` provides top F1 model. It makes the capstone reproducible because the selected model, parameters, metrics, and artifact location can be audited after training.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/pipeline.py:74`

### Q538. risk if missing: `best_row=iloc[0]`?

`best_row=iloc[0]` provides top F1 model. It makes the capstone reproducible because the selected model, parameters, metrics, and artifact location can be audited after training.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/pipeline.py:74`

### Q539. why used: `mlflow.set_tracking_uri`?

`mlflow.set_tracking_uri` provides tracking location. It makes the capstone reproducible because the selected model, parameters, metrics, and artifact location can be audited after training.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/model_store.py:17`

### Q540. MLOps value: `mlflow.set_tracking_uri`?

`mlflow.set_tracking_uri` provides tracking location. It makes the capstone reproducible because the selected model, parameters, metrics, and artifact location can be audited after training.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/model_store.py:17`

### Q541. demo explanation: `mlflow.set_tracking_uri`?

`mlflow.set_tracking_uri` provides tracking location. It makes the capstone reproducible because the selected model, parameters, metrics, and artifact location can be audited after training.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/model_store.py:17`

### Q542. risk if missing: `mlflow.set_tracking_uri`?

`mlflow.set_tracking_uri` provides tracking location. It makes the capstone reproducible because the selected model, parameters, metrics, and artifact location can be audited after training.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/model_store.py:17`

### Q543. why used: `mlflow.set_experiment`?

`mlflow.set_experiment` provides experiment grouping. It makes the capstone reproducible because the selected model, parameters, metrics, and artifact location can be audited after training.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/model_store.py:18`

### Q544. MLOps value: `mlflow.set_experiment`?

`mlflow.set_experiment` provides experiment grouping. It makes the capstone reproducible because the selected model, parameters, metrics, and artifact location can be audited after training.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/model_store.py:18`

### Q545. demo explanation: `mlflow.set_experiment`?

`mlflow.set_experiment` provides experiment grouping. It makes the capstone reproducible because the selected model, parameters, metrics, and artifact location can be audited after training.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/model_store.py:18`

### Q546. risk if missing: `mlflow.set_experiment`?

`mlflow.set_experiment` provides experiment grouping. It makes the capstone reproducible because the selected model, parameters, metrics, and artifact location can be audited after training.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/model_store.py:18`

### Q547. why used: `mlflow.start_run`?

`mlflow.start_run` provides run boundary. It makes the capstone reproducible because the selected model, parameters, metrics, and artifact location can be audited after training.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/model_store.py:30`

### Q548. MLOps value: `mlflow.start_run`?

`mlflow.start_run` provides run boundary. It makes the capstone reproducible because the selected model, parameters, metrics, and artifact location can be audited after training.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/model_store.py:30`

### Q549. demo explanation: `mlflow.start_run`?

`mlflow.start_run` provides run boundary. It makes the capstone reproducible because the selected model, parameters, metrics, and artifact location can be audited after training.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/model_store.py:30`

### Q550. risk if missing: `mlflow.start_run`?

`mlflow.start_run` provides run boundary. It makes the capstone reproducible because the selected model, parameters, metrics, and artifact location can be audited after training.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/model_store.py:30`

### Q551. why used: `mlflow.log_params`?

`mlflow.log_params` provides configuration record. It makes the capstone reproducible because the selected model, parameters, metrics, and artifact location can be audited after training.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/model_store.py:31`

### Q552. MLOps value: `mlflow.log_params`?

`mlflow.log_params` provides configuration record. It makes the capstone reproducible because the selected model, parameters, metrics, and artifact location can be audited after training.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/model_store.py:31`

### Q553. demo explanation: `mlflow.log_params`?

`mlflow.log_params` provides configuration record. It makes the capstone reproducible because the selected model, parameters, metrics, and artifact location can be audited after training.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/model_store.py:31`

### Q554. risk if missing: `mlflow.log_params`?

`mlflow.log_params` provides configuration record. It makes the capstone reproducible because the selected model, parameters, metrics, and artifact location can be audited after training.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/model_store.py:31`

### Q555. why used: `mlflow.log_metrics`?

`mlflow.log_metrics` provides metric record. It makes the capstone reproducible because the selected model, parameters, metrics, and artifact location can be audited after training.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/model_store.py:32`

### Q556. MLOps value: `mlflow.log_metrics`?

`mlflow.log_metrics` provides metric record. It makes the capstone reproducible because the selected model, parameters, metrics, and artifact location can be audited after training.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/model_store.py:32`

### Q557. demo explanation: `mlflow.log_metrics`?

`mlflow.log_metrics` provides metric record. It makes the capstone reproducible because the selected model, parameters, metrics, and artifact location can be audited after training.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/model_store.py:32`

### Q558. risk if missing: `mlflow.log_metrics`?

`mlflow.log_metrics` provides metric record. It makes the capstone reproducible because the selected model, parameters, metrics, and artifact location can be audited after training.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/model_store.py:32`

### Q559. why used: `mlflow.keras.log_model`?

`mlflow.keras.log_model` provides ANN artifact. It makes the capstone reproducible because the selected model, parameters, metrics, and artifact location can be audited after training.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/model_store.py:34`

### Q560. MLOps value: `mlflow.keras.log_model`?

`mlflow.keras.log_model` provides ANN artifact. It makes the capstone reproducible because the selected model, parameters, metrics, and artifact location can be audited after training.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/model_store.py:34`

### Q561. demo explanation: `mlflow.keras.log_model`?

`mlflow.keras.log_model` provides ANN artifact. It makes the capstone reproducible because the selected model, parameters, metrics, and artifact location can be audited after training.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/model_store.py:34`

### Q562. risk if missing: `mlflow.keras.log_model`?

`mlflow.keras.log_model` provides ANN artifact. It makes the capstone reproducible because the selected model, parameters, metrics, and artifact location can be audited after training.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/model_store.py:34`

### Q563. why used: `mlflow.sklearn.log_model`?

`mlflow.sklearn.log_model` provides sklearn artifact. It makes the capstone reproducible because the selected model, parameters, metrics, and artifact location can be audited after training.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/model_store.py:36`

### Q564. MLOps value: `mlflow.sklearn.log_model`?

`mlflow.sklearn.log_model` provides sklearn artifact. It makes the capstone reproducible because the selected model, parameters, metrics, and artifact location can be audited after training.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/model_store.py:36`

### Q565. demo explanation: `mlflow.sklearn.log_model`?

`mlflow.sklearn.log_model` provides sklearn artifact. It makes the capstone reproducible because the selected model, parameters, metrics, and artifact location can be audited after training.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/model_store.py:36`

### Q566. risk if missing: `mlflow.sklearn.log_model`?

`mlflow.sklearn.log_model` provides sklearn artifact. It makes the capstone reproducible because the selected model, parameters, metrics, and artifact location can be audited after training.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/model_store.py:36`

### Q567. why used: `persist_best_model`?

`persist_best_model` provides deployable local copy. It makes the capstone reproducible because the selected model, parameters, metrics, and artifact location can be audited after training.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/model_store.py:40`

### Q568. MLOps value: `persist_best_model`?

`persist_best_model` provides deployable local copy. It makes the capstone reproducible because the selected model, parameters, metrics, and artifact location can be audited after training.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/model_store.py:40`

### Q569. demo explanation: `persist_best_model`?

`persist_best_model` provides deployable local copy. It makes the capstone reproducible because the selected model, parameters, metrics, and artifact location can be audited after training.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/model_store.py:40`

### Q570. risk if missing: `persist_best_model`?

`persist_best_model` provides deployable local copy. It makes the capstone reproducible because the selected model, parameters, metrics, and artifact location can be audited after training.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/model_store.py:40`

### Q571. why used: `artifact_path`?

`artifact_path` provides artifact name. It makes the capstone reproducible because the selected model, parameters, metrics, and artifact location can be audited after training.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/model_store.py:27`

### Q572. MLOps value: `artifact_path`?

`artifact_path` provides artifact name. It makes the capstone reproducible because the selected model, parameters, metrics, and artifact location can be audited after training.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/model_store.py:27`

### Q573. demo explanation: `artifact_path`?

`artifact_path` provides artifact name. It makes the capstone reproducible because the selected model, parameters, metrics, and artifact location can be audited after training.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/model_store.py:27`

### Q574. risk if missing: `artifact_path`?

`artifact_path` provides artifact name. It makes the capstone reproducible because the selected model, parameters, metrics, and artifact location can be audited after training.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/model_store.py:27`

### Q575. why used: `model_registry_path`?

`model_registry_path` provides registry root. It makes the capstone reproducible because the selected model, parameters, metrics, and artifact location can be audited after training.

**File reference:** `app/backend/src/app/core/config.py:14`; `app/backend/src/app/ml/predictive_maintenance/model_store.py:19`

### Q576. MLOps value: `model_registry_path`?

`model_registry_path` provides registry root. It makes the capstone reproducible because the selected model, parameters, metrics, and artifact location can be audited after training.

**File reference:** `app/backend/src/app/core/config.py:14`; `app/backend/src/app/ml/predictive_maintenance/model_store.py:19`

### Q577. demo explanation: `model_registry_path`?

`model_registry_path` provides registry root. It makes the capstone reproducible because the selected model, parameters, metrics, and artifact location can be audited after training.

**File reference:** `app/backend/src/app/core/config.py:14`; `app/backend/src/app/ml/predictive_maintenance/model_store.py:19`

### Q578. risk if missing: `model_registry_path`?

`model_registry_path` provides registry root. It makes the capstone reproducible because the selected model, parameters, metrics, and artifact location can be audited after training.

**File reference:** `app/backend/src/app/core/config.py:14`; `app/backend/src/app/ml/predictive_maintenance/model_store.py:19`

## Configuration

### Q579. purpose: `FASTAPI_ENV`?

`FASTAPI_ENV` controls runtime mode. Configuration is separated from code so the same application can run locally, in Docker, or in production with different environment values.

**File reference:** `app/backend/src/app/core/config.py:7`; `app/backend/.env.example:1`

### Q580. deployment value: `FASTAPI_ENV`?

`FASTAPI_ENV` controls runtime mode. Configuration is separated from code so the same application can run locally, in Docker, or in production with different environment values.

**File reference:** `app/backend/src/app/core/config.py:7`; `app/backend/.env.example:1`

### Q581. misconfiguration risk: `FASTAPI_ENV`?

`FASTAPI_ENV` controls runtime mode. Configuration is separated from code so the same application can run locally, in Docker, or in production with different environment values.

**File reference:** `app/backend/src/app/core/config.py:7`; `app/backend/.env.example:1`

### Q582. purpose: `FASTAPI_HOST=0.0.0.0`?

`FASTAPI_HOST=0.0.0.0` controls container-friendly bind. Configuration is separated from code so the same application can run locally, in Docker, or in production with different environment values.

**File reference:** `app/backend/src/app/core/config.py:8`; `app/backend/.env.example:2`

### Q583. deployment value: `FASTAPI_HOST=0.0.0.0`?

`FASTAPI_HOST=0.0.0.0` controls container-friendly bind. Configuration is separated from code so the same application can run locally, in Docker, or in production with different environment values.

**File reference:** `app/backend/src/app/core/config.py:8`; `app/backend/.env.example:2`

### Q584. misconfiguration risk: `FASTAPI_HOST=0.0.0.0`?

`FASTAPI_HOST=0.0.0.0` controls container-friendly bind. Configuration is separated from code so the same application can run locally, in Docker, or in production with different environment values.

**File reference:** `app/backend/src/app/core/config.py:8`; `app/backend/.env.example:2`

### Q585. purpose: `FASTAPI_PORT=8000`?

`FASTAPI_PORT=8000` controls API port. Configuration is separated from code so the same application can run locally, in Docker, or in production with different environment values.

**File reference:** `app/backend/src/app/core/config.py:9`; `app/backend/.env.example:3`

### Q586. deployment value: `FASTAPI_PORT=8000`?

`FASTAPI_PORT=8000` controls API port. Configuration is separated from code so the same application can run locally, in Docker, or in production with different environment values.

**File reference:** `app/backend/src/app/core/config.py:9`; `app/backend/.env.example:3`

### Q587. misconfiguration risk: `FASTAPI_PORT=8000`?

`FASTAPI_PORT=8000` controls API port. Configuration is separated from code so the same application can run locally, in Docker, or in production with different environment values.

**File reference:** `app/backend/src/app/core/config.py:9`; `app/backend/.env.example:3`

### Q588. purpose: `DATABASE_URL`?

`DATABASE_URL` controls PostgreSQL connection. Configuration is separated from code so the same application can run locally, in Docker, or in production with different environment values.

**File reference:** `app/backend/src/app/core/config.py:10`; `app/backend/.env.example:4`

### Q589. deployment value: `DATABASE_URL`?

`DATABASE_URL` controls PostgreSQL connection. Configuration is separated from code so the same application can run locally, in Docker, or in production with different environment values.

**File reference:** `app/backend/src/app/core/config.py:10`; `app/backend/.env.example:4`

### Q590. misconfiguration risk: `DATABASE_URL`?

`DATABASE_URL` controls PostgreSQL connection. Configuration is separated from code so the same application can run locally, in Docker, or in production with different environment values.

**File reference:** `app/backend/src/app/core/config.py:10`; `app/backend/.env.example:4`

### Q591. purpose: `LOG_LEVEL=INFO`?

`LOG_LEVEL=INFO` controls useful logs. Configuration is separated from code so the same application can run locally, in Docker, or in production with different environment values.

**File reference:** `app/backend/src/app/core/config.py:11`; `app/backend/.env.example:5`

### Q592. deployment value: `LOG_LEVEL=INFO`?

`LOG_LEVEL=INFO` controls useful logs. Configuration is separated from code so the same application can run locally, in Docker, or in production with different environment values.

**File reference:** `app/backend/src/app/core/config.py:11`; `app/backend/.env.example:5`

### Q593. misconfiguration risk: `LOG_LEVEL=INFO`?

`LOG_LEVEL=INFO` controls useful logs. Configuration is separated from code so the same application can run locally, in Docker, or in production with different environment values.

**File reference:** `app/backend/src/app/core/config.py:11`; `app/backend/.env.example:5`

### Q594. purpose: `MLFLOW_TRACKING_URI`?

`MLFLOW_TRACKING_URI` controls experiment location. Configuration is separated from code so the same application can run locally, in Docker, or in production with different environment values.

**File reference:** `app/backend/src/app/core/config.py:12`; `app/backend/.env.example:6`

### Q595. deployment value: `MLFLOW_TRACKING_URI`?

`MLFLOW_TRACKING_URI` controls experiment location. Configuration is separated from code so the same application can run locally, in Docker, or in production with different environment values.

**File reference:** `app/backend/src/app/core/config.py:12`; `app/backend/.env.example:6`

### Q596. misconfiguration risk: `MLFLOW_TRACKING_URI`?

`MLFLOW_TRACKING_URI` controls experiment location. Configuration is separated from code so the same application can run locally, in Docker, or in production with different environment values.

**File reference:** `app/backend/src/app/core/config.py:12`; `app/backend/.env.example:6`

### Q597. purpose: `MLFLOW_EXPERIMENT_NAME`?

`MLFLOW_EXPERIMENT_NAME` controls run grouping. Configuration is separated from code so the same application can run locally, in Docker, or in production with different environment values.

**File reference:** `app/backend/src/app/core/config.py:13`; `app/backend/.env.example:7`

### Q598. deployment value: `MLFLOW_EXPERIMENT_NAME`?

`MLFLOW_EXPERIMENT_NAME` controls run grouping. Configuration is separated from code so the same application can run locally, in Docker, or in production with different environment values.

**File reference:** `app/backend/src/app/core/config.py:13`; `app/backend/.env.example:7`

### Q599. misconfiguration risk: `MLFLOW_EXPERIMENT_NAME`?

`MLFLOW_EXPERIMENT_NAME` controls run grouping. Configuration is separated from code so the same application can run locally, in Docker, or in production with different environment values.

**File reference:** `app/backend/src/app/core/config.py:13`; `app/backend/.env.example:7`

### Q600. purpose: `MLFLOW_ARTIFACT_ROOT`?

`MLFLOW_ARTIFACT_ROOT` controls artifact root. Configuration is separated from code so the same application can run locally, in Docker, or in production with different environment values.

**File reference:** `app/backend/src/app/core/config.py:14`; `app/backend/.env.example:8`

### Q601. deployment value: `MLFLOW_ARTIFACT_ROOT`?

`MLFLOW_ARTIFACT_ROOT` controls artifact root. Configuration is separated from code so the same application can run locally, in Docker, or in production with different environment values.

**File reference:** `app/backend/src/app/core/config.py:14`; `app/backend/.env.example:8`

### Q602. misconfiguration risk: `MLFLOW_ARTIFACT_ROOT`?

`MLFLOW_ARTIFACT_ROOT` controls artifact root. Configuration is separated from code so the same application can run locally, in Docker, or in production with different environment values.

**File reference:** `app/backend/src/app/core/config.py:14`; `app/backend/.env.example:8`

### Q603. purpose: `BaseSettings`?

`BaseSettings` controls env loading. Configuration is separated from code so the same application can run locally, in Docker, or in production with different environment values.

**File reference:** `app/backend/src/app/core/config.py:3`; `app/backend/src/app/core/config.py:6`

### Q604. deployment value: `BaseSettings`?

`BaseSettings` controls env loading. Configuration is separated from code so the same application can run locally, in Docker, or in production with different environment values.

**File reference:** `app/backend/src/app/core/config.py:3`; `app/backend/src/app/core/config.py:6`

### Q605. misconfiguration risk: `BaseSettings`?

`BaseSettings` controls env loading. Configuration is separated from code so the same application can run locally, in Docker, or in production with different environment values.

**File reference:** `app/backend/src/app/core/config.py:3`; `app/backend/src/app/core/config.py:6`

### Q606. purpose: `AnyUrl`?

`AnyUrl` controls URL validation. Configuration is separated from code so the same application can run locally, in Docker, or in production with different environment values.

**File reference:** `app/backend/src/app/core/config.py:3`; `app/backend/src/app/core/config.py:10`

### Q607. deployment value: `AnyUrl`?

`AnyUrl` controls URL validation. Configuration is separated from code so the same application can run locally, in Docker, or in production with different environment values.

**File reference:** `app/backend/src/app/core/config.py:3`; `app/backend/src/app/core/config.py:10`

### Q608. misconfiguration risk: `AnyUrl`?

`AnyUrl` controls URL validation. Configuration is separated from code so the same application can run locally, in Docker, or in production with different environment values.

**File reference:** `app/backend/src/app/core/config.py:3`; `app/backend/src/app/core/config.py:10`

## API and Serving

### Q609. why present: `MaintenanceRequest`?

`MaintenanceRequest` represents device and sensors. It connects ML training to an application interface; a future improvement is loading the persisted MLflow model instead of relying on the current lightweight heuristic path.

**File reference:** `app/backend/schemas.py:12`; `app/backend/services.py:20`; `app/backend/api.py:45`

### Q610. real-app connection: `MaintenanceRequest`?

`MaintenanceRequest` represents device and sensors. It connects ML training to an application interface; a future improvement is loading the persisted MLflow model instead of relying on the current lightweight heuristic path.

**File reference:** `app/backend/schemas.py:12`; `app/backend/services.py:20`; `app/backend/api.py:45`

### Q611. future improvement: `MaintenanceRequest`?

`MaintenanceRequest` represents device and sensors. It connects ML training to an application interface; a future improvement is loading the persisted MLflow model instead of relying on the current lightweight heuristic path.

**File reference:** `app/backend/schemas.py:12`; `app/backend/services.py:20`; `app/backend/api.py:45`

### Q612. why present: `MaintenanceSensor`?

`MaintenanceSensor` represents timestamped readings. It connects ML training to an application interface; a future improvement is loading the persisted MLflow model instead of relying on the current lightweight heuristic path.

**File reference:** `app/backend/schemas.py:7`

### Q613. real-app connection: `MaintenanceSensor`?

`MaintenanceSensor` represents timestamped readings. It connects ML training to an application interface; a future improvement is loading the persisted MLflow model instead of relying on the current lightweight heuristic path.

**File reference:** `app/backend/schemas.py:7`

### Q614. future improvement: `MaintenanceSensor`?

`MaintenanceSensor` represents timestamped readings. It connects ML training to an application interface; a future improvement is loading the persisted MLflow model instead of relying on the current lightweight heuristic path.

**File reference:** `app/backend/schemas.py:7`

### Q615. why present: `failure_risk`?

`failure_risk` represents bounded risk score. It connects ML training to an application interface; a future improvement is loading the persisted MLflow model instead of relying on the current lightweight heuristic path.

**File reference:** `app/backend/schemas.py:19`; `app/backend/services.py:36`

### Q616. real-app connection: `failure_risk`?

`failure_risk` represents bounded risk score. It connects ML training to an application interface; a future improvement is loading the persisted MLflow model instead of relying on the current lightweight heuristic path.

**File reference:** `app/backend/schemas.py:19`; `app/backend/services.py:36`

### Q617. future improvement: `failure_risk`?

`failure_risk` represents bounded risk score. It connects ML training to an application interface; a future improvement is loading the persisted MLflow model instead of relying on the current lightweight heuristic path.

**File reference:** `app/backend/schemas.py:19`; `app/backend/services.py:36`

### Q618. why present: `eta_hours`?

`eta_hours` represents maintenance urgency. It connects ML training to an application interface; a future improvement is loading the persisted MLflow model instead of relying on the current lightweight heuristic path.

**File reference:** `app/backend/schemas.py:20`; `app/backend/services.py:27`

### Q619. real-app connection: `eta_hours`?

`eta_hours` represents maintenance urgency. It connects ML training to an application interface; a future improvement is loading the persisted MLflow model instead of relying on the current lightweight heuristic path.

**File reference:** `app/backend/schemas.py:20`; `app/backend/services.py:27`

### Q620. future improvement: `eta_hours`?

`eta_hours` represents maintenance urgency. It connects ML training to an application interface; a future improvement is loading the persisted MLflow model instead of relying on the current lightweight heuristic path.

**File reference:** `app/backend/schemas.py:20`; `app/backend/services.py:27`

### Q621. why present: `explanation`?

`explanation` represents reason/source. It connects ML training to an application interface; a future improvement is loading the persisted MLflow model instead of relying on the current lightweight heuristic path.

**File reference:** `app/backend/schemas.py:21`; `app/backend/services.py:36`

### Q622. real-app connection: `explanation`?

`explanation` represents reason/source. It connects ML training to an application interface; a future improvement is loading the persisted MLflow model instead of relying on the current lightweight heuristic path.

**File reference:** `app/backend/schemas.py:21`; `app/backend/services.py:36`

### Q623. future improvement: `explanation`?

`explanation` represents reason/source. It connects ML training to an application interface; a future improvement is loading the persisted MLflow model instead of relying on the current lightweight heuristic path.

**File reference:** `app/backend/schemas.py:21`; `app/backend/services.py:36`

### Q624. why present: `Field ge/le`?

`Field ge/le` represents output bounds. It connects ML training to an application interface; a future improvement is loading the persisted MLflow model instead of relying on the current lightweight heuristic path.

**File reference:** `app/backend/schemas.py:19`

### Q625. real-app connection: `Field ge/le`?

`Field ge/le` represents output bounds. It connects ML training to an application interface; a future improvement is loading the persisted MLflow model instead of relying on the current lightweight heuristic path.

**File reference:** `app/backend/schemas.py:19`

### Q626. future improvement: `Field ge/le`?

`Field ge/le` represents output bounds. It connects ML training to an application interface; a future improvement is loading the persisted MLflow model instead of relying on the current lightweight heuristic path.

**File reference:** `app/backend/schemas.py:19`

### Q627. why present: `ServiceError`?

`ServiceError` represents controlled API failure. It connects ML training to an application interface; a future improvement is loading the persisted MLflow model instead of relying on the current lightweight heuristic path.

**File reference:** `app/backend/services.py:25`

### Q628. real-app connection: `ServiceError`?

`ServiceError` represents controlled API failure. It connects ML training to an application interface; a future improvement is loading the persisted MLflow model instead of relying on the current lightweight heuristic path.

**File reference:** `app/backend/services.py:25`

### Q629. future improvement: `ServiceError`?

`ServiceError` represents controlled API failure. It connects ML training to an application interface; a future improvement is loading the persisted MLflow model instead of relying on the current lightweight heuristic path.

**File reference:** `app/backend/services.py:25`

### Q630. why present: `latency metric`?

`latency metric` represents inference timing. It connects ML training to an application interface; a future improvement is loading the persisted MLflow model instead of relying on the current lightweight heuristic path.

**File reference:** `app/backend/services.py:33`

### Q631. real-app connection: `latency metric`?

`latency metric` represents inference timing. It connects ML training to an application interface; a future improvement is loading the persisted MLflow model instead of relying on the current lightweight heuristic path.

**File reference:** `app/backend/services.py:33`

### Q632. future improvement: `latency metric`?

`latency metric` represents inference timing. It connects ML training to an application interface; a future improvement is loading the persisted MLflow model instead of relying on the current lightweight heuristic path.

**File reference:** `app/backend/services.py:33`

### Q633. why present: `prediction volume`?

`prediction volume` represents usage monitoring. It connects ML training to an application interface; a future improvement is loading the persisted MLflow model instead of relying on the current lightweight heuristic path.

**File reference:** `app/backend/services.py:34`

### Q634. real-app connection: `prediction volume`?

`prediction volume` represents usage monitoring. It connects ML training to an application interface; a future improvement is loading the persisted MLflow model instead of relying on the current lightweight heuristic path.

**File reference:** `app/backend/services.py:34`

### Q635. future improvement: `prediction volume`?

`prediction volume` represents usage monitoring. It connects ML training to an application interface; a future improvement is loading the persisted MLflow model instead of relying on the current lightweight heuristic path.

**File reference:** `app/backend/services.py:34`

### Q636. why present: `heuristic current service`?

`heuristic current service` represents temporary fallback before real model loading. It connects ML training to an application interface; a future improvement is loading the persisted MLflow model instead of relying on the current lightweight heuristic path.

**File reference:** `app/backend/services.py:20`

### Q637. real-app connection: `heuristic current service`?

`heuristic current service` represents temporary fallback before real model loading. It connects ML training to an application interface; a future improvement is loading the persisted MLflow model instead of relying on the current lightweight heuristic path.

**File reference:** `app/backend/services.py:20`

### Q638. future improvement: `heuristic current service`?

`heuristic current service` represents temporary fallback before real model loading. It connects ML training to an application interface; a future improvement is loading the persisted MLflow model instead of relying on the current lightweight heuristic path.

**File reference:** `app/backend/services.py:20`

## Architecture

### Q639. why included: `React frontend`?

`React frontend` is included to make the project a deployable AI operations platform rather than a notebook. It supports usability, persistence, governance, reproducibility, monitoring, or future scaling.

**File reference:** `architecture.md:36`; `architecture.md:151`

### Q640. capstone defense: `React frontend`?

`React frontend` is included to make the project a deployable AI operations platform rather than a notebook. It supports usability, persistence, governance, reproducibility, monitoring, or future scaling.

**File reference:** `architecture.md:36`; `architecture.md:151`

### Q641. production value: `React frontend`?

`React frontend` is included to make the project a deployable AI operations platform rather than a notebook. It supports usability, persistence, governance, reproducibility, monitoring, or future scaling.

**File reference:** `architecture.md:36`; `architecture.md:151`

### Q642. why included: `FastAPI backend`?

`FastAPI backend` is included to make the project a deployable AI operations platform rather than a notebook. It supports usability, persistence, governance, reproducibility, monitoring, or future scaling.

**File reference:** `architecture.md:37`; `app/backend/src/app/main.py:8`

### Q643. capstone defense: `FastAPI backend`?

`FastAPI backend` is included to make the project a deployable AI operations platform rather than a notebook. It supports usability, persistence, governance, reproducibility, monitoring, or future scaling.

**File reference:** `architecture.md:37`; `app/backend/src/app/main.py:8`

### Q644. production value: `FastAPI backend`?

`FastAPI backend` is included to make the project a deployable AI operations platform rather than a notebook. It supports usability, persistence, governance, reproducibility, monitoring, or future scaling.

**File reference:** `architecture.md:37`; `app/backend/src/app/main.py:8`

### Q645. why included: `PostgreSQL`?

`PostgreSQL` is included to make the project a deployable AI operations platform rather than a notebook. It supports usability, persistence, governance, reproducibility, monitoring, or future scaling.

**File reference:** `architecture.md:39`; `app/backend/.env.example:4`

### Q646. capstone defense: `PostgreSQL`?

`PostgreSQL` is included to make the project a deployable AI operations platform rather than a notebook. It supports usability, persistence, governance, reproducibility, monitoring, or future scaling.

**File reference:** `architecture.md:39`; `app/backend/.env.example:4`

### Q647. production value: `PostgreSQL`?

`PostgreSQL` is included to make the project a deployable AI operations platform rather than a notebook. It supports usability, persistence, governance, reproducibility, monitoring, or future scaling.

**File reference:** `architecture.md:39`; `app/backend/.env.example:4`

### Q648. why included: `MLflow`?

`MLflow` is included to make the project a deployable AI operations platform rather than a notebook. It supports usability, persistence, governance, reproducibility, monitoring, or future scaling.

**File reference:** `architecture.md:40`; `app/backend/src/app/ml/predictive_maintenance/model_store.py:17`

### Q649. capstone defense: `MLflow`?

`MLflow` is included to make the project a deployable AI operations platform rather than a notebook. It supports usability, persistence, governance, reproducibility, monitoring, or future scaling.

**File reference:** `architecture.md:40`; `app/backend/src/app/ml/predictive_maintenance/model_store.py:17`

### Q650. production value: `MLflow`?

`MLflow` is included to make the project a deployable AI operations platform rather than a notebook. It supports usability, persistence, governance, reproducibility, monitoring, or future scaling.

**File reference:** `architecture.md:40`; `app/backend/src/app/ml/predictive_maintenance/model_store.py:17`

### Q651. why included: `Docker Compose`?

`Docker Compose` is included to make the project a deployable AI operations platform rather than a notebook. It supports usability, persistence, governance, reproducibility, monitoring, or future scaling.

**File reference:** `architecture.md:134`

### Q652. capstone defense: `Docker Compose`?

`Docker Compose` is included to make the project a deployable AI operations platform rather than a notebook. It supports usability, persistence, governance, reproducibility, monitoring, or future scaling.

**File reference:** `architecture.md:134`

### Q653. production value: `Docker Compose`?

`Docker Compose` is included to make the project a deployable AI operations platform rather than a notebook. It supports usability, persistence, governance, reproducibility, monitoring, or future scaling.

**File reference:** `architecture.md:134`

### Q654. why included: `structured logs`?

`structured logs` is included to make the project a deployable AI operations platform rather than a notebook. It supports usability, persistence, governance, reproducibility, monitoring, or future scaling.

**File reference:** `architecture.md:178`

### Q655. capstone defense: `structured logs`?

`structured logs` is included to make the project a deployable AI operations platform rather than a notebook. It supports usability, persistence, governance, reproducibility, monitoring, or future scaling.

**File reference:** `architecture.md:178`

### Q656. production value: `structured logs`?

`structured logs` is included to make the project a deployable AI operations platform rather than a notebook. It supports usability, persistence, governance, reproducibility, monitoring, or future scaling.

**File reference:** `architecture.md:178`

### Q657. why included: `correlation IDs`?

`correlation IDs` is included to make the project a deployable AI operations platform rather than a notebook. It supports usability, persistence, governance, reproducibility, monitoring, or future scaling.

**File reference:** `architecture.md:183`

### Q658. capstone defense: `correlation IDs`?

`correlation IDs` is included to make the project a deployable AI operations platform rather than a notebook. It supports usability, persistence, governance, reproducibility, monitoring, or future scaling.

**File reference:** `architecture.md:183`

### Q659. production value: `correlation IDs`?

`correlation IDs` is included to make the project a deployable AI operations platform rather than a notebook. It supports usability, persistence, governance, reproducibility, monitoring, or future scaling.

**File reference:** `architecture.md:183`

### Q660. why included: `model registry`?

`model registry` is included to make the project a deployable AI operations platform rather than a notebook. It supports usability, persistence, governance, reproducibility, monitoring, or future scaling.

**File reference:** `architecture.md:121`

### Q661. capstone defense: `model registry`?

`model registry` is included to make the project a deployable AI operations platform rather than a notebook. It supports usability, persistence, governance, reproducibility, monitoring, or future scaling.

**File reference:** `architecture.md:121`

### Q662. production value: `model registry`?

`model registry` is included to make the project a deployable AI operations platform rather than a notebook. It supports usability, persistence, governance, reproducibility, monitoring, or future scaling.

**File reference:** `architecture.md:121`

### Q663. why included: `validation layer`?

`validation layer` is included to make the project a deployable AI operations platform rather than a notebook. It supports usability, persistence, governance, reproducibility, monitoring, or future scaling.

**File reference:** `architecture.md:196`

### Q664. capstone defense: `validation layer`?

`validation layer` is included to make the project a deployable AI operations platform rather than a notebook. It supports usability, persistence, governance, reproducibility, monitoring, or future scaling.

**File reference:** `architecture.md:196`

### Q665. production value: `validation layer`?

`validation layer` is included to make the project a deployable AI operations platform rather than a notebook. It supports usability, persistence, governance, reproducibility, monitoring, or future scaling.

**File reference:** `architecture.md:196`

### Q666. why included: `operator feedback loop`?

`operator feedback loop` is included to make the project a deployable AI operations platform rather than a notebook. It supports usability, persistence, governance, reproducibility, monitoring, or future scaling.

**File reference:** `architecture.md:101`

### Q667. capstone defense: `operator feedback loop`?

`operator feedback loop` is included to make the project a deployable AI operations platform rather than a notebook. It supports usability, persistence, governance, reproducibility, monitoring, or future scaling.

**File reference:** `architecture.md:101`

### Q668. production value: `operator feedback loop`?

`operator feedback loop` is included to make the project a deployable AI operations platform rather than a notebook. It supports usability, persistence, governance, reproducibility, monitoring, or future scaling.

**File reference:** `architecture.md:101`

## Future Work

### Q669. what is it: `SMOTE/class_weight`?

`SMOTE/class_weight` would improve scientific rigor or production readiness. It is not mandatory for the first version because the current pipeline already proves validation, feature engineering, multi-model training, ANN training, MLflow tracking, and persistence.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/preprocessing.py:50`; `app/backend/src/app/ml/predictive_maintenance/train.py:62`

### Q670. why useful: `SMOTE/class_weight`?

`SMOTE/class_weight` would improve scientific rigor or production readiness. It is not mandatory for the first version because the current pipeline already proves validation, feature engineering, multi-model training, ANN training, MLflow tracking, and persistence.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/preprocessing.py:50`; `app/backend/src/app/ml/predictive_maintenance/train.py:62`

### Q671. why not mandatory now: `SMOTE/class_weight`?

`SMOTE/class_weight` would improve scientific rigor or production readiness. It is not mandatory for the first version because the current pipeline already proves validation, feature engineering, multi-model training, ANN training, MLflow tracking, and persistence.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/preprocessing.py:50`; `app/backend/src/app/ml/predictive_maintenance/train.py:62`

### Q672. what is it: `threshold tuning`?

`threshold tuning` would improve scientific rigor or production readiness. It is not mandatory for the first version because the current pipeline already proves validation, feature engineering, multi-model training, ANN training, MLflow tracking, and persistence.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/evaluate.py:41`

### Q673. why useful: `threshold tuning`?

`threshold tuning` would improve scientific rigor or production readiness. It is not mandatory for the first version because the current pipeline already proves validation, feature engineering, multi-model training, ANN training, MLflow tracking, and persistence.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/evaluate.py:41`

### Q674. why not mandatory now: `threshold tuning`?

`threshold tuning` would improve scientific rigor or production readiness. It is not mandatory for the first version because the current pipeline already proves validation, feature engineering, multi-model training, ANN training, MLflow tracking, and persistence.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/evaluate.py:41`

### Q675. what is it: `cross-validation`?

`cross-validation` would improve scientific rigor or production readiness. It is not mandatory for the first version because the current pipeline already proves validation, feature engineering, multi-model training, ANN training, MLflow tracking, and persistence.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/pipeline.py:69`

### Q676. why useful: `cross-validation`?

`cross-validation` would improve scientific rigor or production readiness. It is not mandatory for the first version because the current pipeline already proves validation, feature engineering, multi-model training, ANN training, MLflow tracking, and persistence.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/pipeline.py:69`

### Q677. why not mandatory now: `cross-validation`?

`cross-validation` would improve scientific rigor or production readiness. It is not mandatory for the first version because the current pipeline already proves validation, feature engineering, multi-model training, ANN training, MLflow tracking, and persistence.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/pipeline.py:69`

### Q678. what is it: `hyperparameter search`?

`hyperparameter search` would improve scientific rigor or production readiness. It is not mandatory for the first version because the current pipeline already proves validation, feature engineering, multi-model training, ANN training, MLflow tracking, and persistence.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/train.py:47`

### Q679. why useful: `hyperparameter search`?

`hyperparameter search` would improve scientific rigor or production readiness. It is not mandatory for the first version because the current pipeline already proves validation, feature engineering, multi-model training, ANN training, MLflow tracking, and persistence.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/train.py:47`

### Q680. why not mandatory now: `hyperparameter search`?

`hyperparameter search` would improve scientific rigor or production readiness. It is not mandatory for the first version because the current pipeline already proves validation, feature engineering, multi-model training, ANN training, MLflow tracking, and persistence.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/train.py:47`

### Q681. what is it: `SHAP`?

`SHAP` would improve scientific rigor or production readiness. It is not mandatory for the first version because the current pipeline already proves validation, feature engineering, multi-model training, ANN training, MLflow tracking, and persistence.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/model_store.py:30`

### Q682. why useful: `SHAP`?

`SHAP` would improve scientific rigor or production readiness. It is not mandatory for the first version because the current pipeline already proves validation, feature engineering, multi-model training, ANN training, MLflow tracking, and persistence.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/model_store.py:30`

### Q683. why not mandatory now: `SHAP`?

`SHAP` would improve scientific rigor or production readiness. It is not mandatory for the first version because the current pipeline already proves validation, feature engineering, multi-model training, ANN training, MLflow tracking, and persistence.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/model_store.py:30`

### Q684. what is it: `real model serving`?

`real model serving` would improve scientific rigor or production readiness. It is not mandatory for the first version because the current pipeline already proves validation, feature engineering, multi-model training, ANN training, MLflow tracking, and persistence.

**File reference:** `app/backend/services.py:15`; `app/backend/src/app/ml/predictive_maintenance/model_store.py:40`

### Q685. why useful: `real model serving`?

`real model serving` would improve scientific rigor or production readiness. It is not mandatory for the first version because the current pipeline already proves validation, feature engineering, multi-model training, ANN training, MLflow tracking, and persistence.

**File reference:** `app/backend/services.py:15`; `app/backend/src/app/ml/predictive_maintenance/model_store.py:40`

### Q686. why not mandatory now: `real model serving`?

`real model serving` would improve scientific rigor or production readiness. It is not mandatory for the first version because the current pipeline already proves validation, feature engineering, multi-model training, ANN training, MLflow tracking, and persistence.

**File reference:** `app/backend/services.py:15`; `app/backend/src/app/ml/predictive_maintenance/model_store.py:40`

### Q687. what is it: `drift monitoring`?

`drift monitoring` would improve scientific rigor or production readiness. It is not mandatory for the first version because the current pipeline already proves validation, feature engineering, multi-model training, ANN training, MLflow tracking, and persistence.

**File reference:** `architecture.md:174`

### Q688. why useful: `drift monitoring`?

`drift monitoring` would improve scientific rigor or production readiness. It is not mandatory for the first version because the current pipeline already proves validation, feature engineering, multi-model training, ANN training, MLflow tracking, and persistence.

**File reference:** `architecture.md:174`

### Q689. why not mandatory now: `drift monitoring`?

`drift monitoring` would improve scientific rigor or production readiness. It is not mandatory for the first version because the current pipeline already proves validation, feature engineering, multi-model training, ANN training, MLflow tracking, and persistence.

**File reference:** `architecture.md:174`

### Q690. what is it: `calibration`?

`calibration` would improve scientific rigor or production readiness. It is not mandatory for the first version because the current pipeline already proves validation, feature engineering, multi-model training, ANN training, MLflow tracking, and persistence.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/evaluate.py:39`

### Q691. why useful: `calibration`?

`calibration` would improve scientific rigor or production readiness. It is not mandatory for the first version because the current pipeline already proves validation, feature engineering, multi-model training, ANN training, MLflow tracking, and persistence.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/evaluate.py:39`

### Q692. why not mandatory now: `calibration`?

`calibration` would improve scientific rigor or production readiness. It is not mandatory for the first version because the current pipeline already proves validation, feature engineering, multi-model training, ANN training, MLflow tracking, and persistence.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/evaluate.py:39`

### Q693. what is it: `confusion matrix`?

`confusion matrix` would improve scientific rigor or production readiness. It is not mandatory for the first version because the current pipeline already proves validation, feature engineering, multi-model training, ANN training, MLflow tracking, and persistence.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/evaluate.py:17`

### Q694. why useful: `confusion matrix`?

`confusion matrix` would improve scientific rigor or production readiness. It is not mandatory for the first version because the current pipeline already proves validation, feature engineering, multi-model training, ANN training, MLflow tracking, and persistence.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/evaluate.py:17`

### Q695. why not mandatory now: `confusion matrix`?

`confusion matrix` would improve scientific rigor or production readiness. It is not mandatory for the first version because the current pipeline already proves validation, feature engineering, multi-model training, ANN training, MLflow tracking, and persistence.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/evaluate.py:17`

### Q696. what is it: `PR-AUC`?

`PR-AUC` would improve scientific rigor or production readiness. It is not mandatory for the first version because the current pipeline already proves validation, feature engineering, multi-model training, ANN training, MLflow tracking, and persistence.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/evaluate.py:17`

### Q697. why useful: `PR-AUC`?

`PR-AUC` would improve scientific rigor or production readiness. It is not mandatory for the first version because the current pipeline already proves validation, feature engineering, multi-model training, ANN training, MLflow tracking, and persistence.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/evaluate.py:17`

### Q698. why not mandatory now: `PR-AUC`?

`PR-AUC` would improve scientific rigor or production readiness. It is not mandatory for the first version because the current pipeline already proves validation, feature engineering, multi-model training, ANN training, MLflow tracking, and persistence.

**File reference:** `app/backend/src/app/ml/predictive_maintenance/evaluate.py:17`

### Q699. what is it: `Kafka streaming`?

`Kafka streaming` would improve scientific rigor or production readiness. It is not mandatory for the first version because the current pipeline already proves validation, feature engineering, multi-model training, ANN training, MLflow tracking, and persistence.

**File reference:** `architecture.md:319`

### Q700. why useful: `Kafka streaming`?

`Kafka streaming` would improve scientific rigor or production readiness. It is not mandatory for the first version because the current pipeline already proves validation, feature engineering, multi-model training, ANN training, MLflow tracking, and persistence.

**File reference:** `architecture.md:319`

### Q701. why not mandatory now: `Kafka streaming`?

`Kafka streaming` would improve scientific rigor or production readiness. It is not mandatory for the first version because the current pipeline already proves validation, feature engineering, multi-model training, ANN training, MLflow tracking, and persistence.

**File reference:** `architecture.md:319`

### Q702. what is it: `Dockerized training`?

`Dockerized training` would improve scientific rigor or production readiness. It is not mandatory for the first version because the current pipeline already proves validation, feature engineering, multi-model training, ANN training, MLflow tracking, and persistence.

**File reference:** `architecture.md:134`

### Q703. why useful: `Dockerized training`?

`Dockerized training` would improve scientific rigor or production readiness. It is not mandatory for the first version because the current pipeline already proves validation, feature engineering, multi-model training, ANN training, MLflow tracking, and persistence.

**File reference:** `architecture.md:134`

### Q704. why not mandatory now: `Dockerized training`?

`Dockerized training` would improve scientific rigor or production readiness. It is not mandatory for the first version because the current pipeline already proves validation, feature engineering, multi-model training, ANN training, MLflow tracking, and persistence.

**File reference:** `architecture.md:134`

## Summary

Total questions: 704. Core defense: validated data, leakage-safe feature engineering, Logistic Regression baseline, Random Forest and XGBoost tabular models, compact ANN, early stopping, F1-led model selection, MLflow tracking, and deployable API architecture.
