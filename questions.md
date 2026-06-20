# Smart Factory Command Center Viva Questions (500)

## 1) ML Fundamentals (Q001-Q020)
1. What is machine learning, and how is it different from traditional rule-based programming?
2. What are the main categories of machine learning (supervised, unsupervised, reinforcement)?
3. What is the difference between a feature, a label, and an instance?
4. What is inductive bias, and why is it necessary for learning?
5. How do you define training, validation, and test datasets?
6. What is overfitting, and how can you identify it?
7. What is underfitting, and what are common causes?
8. What is the bias-variance tradeoff?
9. What does generalization mean in ML systems?
10. Why is data quality often more important than model complexity?
11. What is the role of domain knowledge in feature design?
12. Why are baselines important before trying complex models?
13. What is a loss function, and how is it different from an evaluation metric?
14. Why does random seed control matter for reproducible ML?
15. What are deterministic vs non-deterministic model training behaviors?
16. How would you explain model interpretability to a non-technical stakeholder?
17. What is data leakage, and why is it dangerous?
18. What is concept drift, and how does it differ from data drift?
19. How do you decide whether to solve a problem with regression or classification?
20. What are key assumptions to validate before selecting an ML approach?

## 2) Linear Algebra for ML (Q021-Q040)
21. Why are vectors and matrices fundamental to ML models?
22. What is the geometric meaning of a dot product in ML?
23. How does matrix multiplication relate to neural network layers?
24. What is a tensor, and how is it used in deep learning frameworks?
25. What is rank deficiency, and why can it affect model training?
26. Why is matrix inversion often avoided in numerical optimization?
27. What are eigenvalues and eigenvectors, and where are they used in ML?
28. How does PCA use linear algebra to reduce dimensionality?
29. What is orthogonality, and why is it useful in feature spaces?
30. What is condition number, and how does it impact numerical stability?
31. Why do we normalize vectors in cosine similarity problems?
32. How does SVD help with compression and latent factor modeling?
33. What is a projection of a vector onto a subspace?
34. Why does high dimensionality make distance metrics less meaningful?
35. What is the difference between L1 and L2 norms geometrically?
36. How are gradients represented in vector/matrix form?
37. Why do Jacobian and Hessian matrices matter in optimization?
38. What is broadcasting in tensor operations?
39. How can tensor shape mismatch cause runtime errors in ANN/CNN models?
40. Why is understanding tensor dimensions critical in convolution operations?

## 3) Probability and Statistics (Q041-Q060)
41. What is the difference between probability and likelihood?
42. How does Bayes theorem apply to classification problems?
43. What are prior, posterior, and evidence in Bayesian inference?
44. What is the difference between population and sample statistics?
45. Why is standard deviation important in feature scaling?
46. What is covariance, and how is it different from correlation?
47. How do outliers affect mean, median, and variance?
48. What is a confidence interval, and how is it interpreted?
49. What is a p-value, and what are common misconceptions about it?
50. What is Type I vs Type II error in hypothesis testing?
51. Why is class imbalance a statistical issue for ML evaluation?
52. What is a distribution shift, and how can you detect it statistically?
53. What is KL divergence and where is it useful?
54. What is entropy in information theory and ML?
55. How does cross-entropy relate to classification loss?
56. Why does Gaussian assumption matter in some models?
57. What is heteroscedasticity in regression?
58. How do you test whether two datasets come from the same distribution?
59. What is bootstrapping and why is it useful for uncertainty estimation?
60. How are statistical assumptions validated in production ML pipelines?

## 4) Data Preprocessing (Q061-Q080)
61. Why is missing value treatment critical before model training?
62. Compare mean, median, and model-based imputation techniques.
63. When should rows with missing values be dropped instead of imputed?
64. How do duplicate records impact model behavior?
65. Why is timestamp parsing and timezone handling important in industrial data?
66. What is the impact of inconsistent units across sensors?
67. How do you handle categorical variables in tree-based vs linear models?
68. Why do we scale features for ANN and distance-based models?
69. Compare StandardScaler and MinMaxScaler with practical use cases.
70. What is target leakage during preprocessing?
71. How can train-test contamination happen during scaling?
72. Why should preprocessing steps be fitted only on training data?
73. What is the role of pipelines in preventing preprocessing mistakes?
74. How do you validate schema consistency in ingestion pipelines?
75. What are common preprocessing checks for sensor data quality?
76. How do you detect and handle impossible values (e.g., negative stock)?
77. Why are domain constraints important in preprocessing?
78. What are robust methods for outlier capping in production?
79. How do you design preprocessing for streaming vs batch data?
80. What preprocessing metadata should be versioned for reproducibility?

## 5) Feature Engineering (Q081-Q100)
81. Why is feature engineering often the highest-leverage ML activity?
82. What is the fit-transform pattern and why does it reduce leakage risk?
83. How do lag features capture temporal dependencies?
84. What are rolling-window features and when do they help?
85. Why are cyclical encodings useful for time-based features?
86. What is feature interaction and when should it be explicitly added?
87. How does one-hot encoding impact feature dimensionality?
88. What is target encoding and what leakage risks does it carry?
89. How do you evaluate whether a feature is predictive or redundant?
90. What is multicollinearity and why does it matter for linear models?
91. How can permutation importance validate feature utility?
92. How do domain-driven features improve model trust?
93. What is a feature store and why is it useful in MLOps?
94. Why should feature definitions be shared between training and inference?
95. How do you engineer features for predictive maintenance from sensor streams?
96. How do you engineer features for demand forecasting from sales history?
97. How do you engineer features for inventory risk scoring?
98. How do you engineer features for image-based quality inspection?
99. What feature drift indicators should be monitored in production?
100. How do you retire stale features without breaking downstream models?

## 6) Regression Models (Q101-Q120)
101. What are key assumptions of linear regression?
102. How do you interpret regression coefficients?
103. What is regularization in regression and why is it needed?
104. Compare Ridge, Lasso, and ElasticNet.
105. What does R-squared measure, and when can it be misleading?
106. Why is RMSE sensitive to outliers?
107. When is MAE preferred over RMSE?
108. How does multicollinearity affect regression stability?
109. What is residual analysis and why is it important?
110. How do you detect non-linearity in regression residuals?
111. What is weighted least squares and when is it useful?
112. What is quantile regression and how can it support risk-aware planning?
113. How do you produce prediction intervals in regression tasks?
114. How does feature scaling affect linear regression optimization?
115. Why can simple linear models outperform complex models in production?
116. What is the effect of outliers on fitted regression parameters?
117. How do you evaluate regression performance over time segments?
118. How can regression be used for demand forecasting baselines?
119. How would you explain regression model confidence to operations teams?
120. What safeguards are needed before deploying a regression model?

## 7) Classification Models (Q121-Q140)
121. What is the difference between binary, multiclass, and multilabel classification?
122. How does logistic regression differ from linear regression?
123. Why is sigmoid output interpreted as probability in logistic regression?
124. What is decision threshold and how does it impact precision/recall?
125. What is ROC-AUC and when is PR-AUC more informative?
126. What is confusion matrix and how do you interpret it for quality inspection?
127. Why is F1-score useful in imbalanced datasets?
128. What is class weighting and when should it be used?
129. How does oversampling differ from undersampling?
130. What is SMOTE and what are its limitations?
131. Why is calibration important for probabilistic classifiers?
132. What is log loss and why is it sensitive to confident errors?
133. How do cost-sensitive errors apply to predictive maintenance alerts?
134. What is false positive vs false negative tradeoff in fault detection?
135. How do you select optimal threshold for business objectives?
136. Why should thresholds differ across plants or product lines?
137. What are one-vs-rest and one-vs-one multiclass strategies?
138. How do you monitor classifier drift in production?
139. What type of explainability is needed for classification decisions?
140. What post-deployment checks are required for classification services?

## 8) Tree-Based and Ensemble Methods (Q141-Q160)
141. How does a decision tree split data, and what is impurity reduction?
142. Compare Gini impurity and entropy.
143. Why do decision trees overfit without constraints?
144. How do max depth and min samples affect tree bias/variance?
145. What is bagging and how does Random Forest use it?
146. Why are Random Forests robust to noisy features?
147. What is feature importance in Random Forest and its pitfalls?
148. How does boosting differ from bagging?
149. What is gradient boosting in simple terms?
150. Why is XGBoost often strong on tabular data?
151. What is the role of learning rate in boosted trees?
152. How do `n_estimators` and `max_depth` interact in XGBoost?
153. What is early stopping and why is it useful in boosting?
154. How do you prevent overfitting in XGBoost?
155. Why does XGBoost handle non-linear interactions well?
156. What are common hyperparameters to tune for Random Forest?
157. How do you compare tree-based models with linear baselines fairly?
158. When can tree ensembles fail in time series tasks?
159. How do you serve tree models efficiently in microservices?
160. What monitoring metrics matter specifically for boosted tree models?

## 9) Model Selection and Tuning (Q161-Q180)
161. Why is cross-validation important for model selection?
162. What is the difference between random split and time-based split?
163. Why is random CV invalid for many forecasting problems?
164. What is nested cross-validation and when is it needed?
165. Compare grid search, random search, and Bayesian optimization.
166. What is hyperparameter overfitting to validation data?
167. How do you define a fair model comparison protocol?
168. Why should preprocessing be included inside CV folds?
169. What are practical stopping criteria in hyperparameter tuning?
170. How do you choose evaluation metric aligned to business cost?
171. What is champion-challenger evaluation in MLOps?
172. How do you compare models across multiple plants and SKUs?
173. Why should confidence intervals be reported with performance metrics?
174. How do you evaluate model stability across random seeds?
175. What is Pareto tradeoff between accuracy and latency?
176. How do you tune models under strict inference SLAs?
177. How do you avoid data snooping in iterative model development?
178. When should you stop model complexity escalation?
179. How do you document model selection decisions for audits?
180. What reproducibility artifacts must be saved after tuning?

## 10) ANN Foundations (Q181-Q200)
181. What is an artificial neuron and how does it compute output?
182. What is the role of activation functions in ANN?
183. Why are non-linear activations essential in deep networks?
184. Compare ReLU, Leaky ReLU, tanh, and sigmoid.
185. What is forward propagation?
186. What is backpropagation and why does chain rule matter?
187. What is gradient descent in neural network training?
188. Compare batch, mini-batch, and stochastic gradient descent.
189. Why does learning rate strongly affect ANN convergence?
190. What is vanishing gradient and where does it occur?
191. What is exploding gradient and how do you mitigate it?
192. What is weight initialization and why is it important?
193. Compare Xavier and He initialization.
194. What is the role of bias terms in ANN layers?
195. Why is normalization useful in ANN training?
196. What does an epoch represent in deep learning?
197. What are trainable parameters and how do you count them?
198. Why can deeper networks represent complex functions better?
199. What is universal approximation theorem and its practical limitation?
200. How do ANN models differ from tree models on tabular industrial data?

## 11) ANN Architectures and Regularization (Q201-Q220)
201. How do you choose the number of hidden layers and neurons?
202. What is dropout and how does it reduce overfitting?
203. What is L2 regularization in neural networks?
204. What is batch normalization and why does it speed up training?
205. What is early stopping and when should it be triggered?
206. How does optimizer choice (SGD, Adam, RMSProp) impact training?
207. What are Adam advantages and potential pitfalls?
208. Why does ANN on small datasets often overfit quickly?
209. What is model capacity and how is it controlled?
210. How do you perform ANN hyperparameter tuning efficiently?
211. What is the difference between training loss and validation loss trends?
212. How do you diagnose ANN underfitting from learning curves?
213. How do you diagnose ANN overfitting from learning curves?
214. What is label smoothing and when is it useful?
215. What is gradient clipping and why can it stabilize training?
216. How do mixed precision and GPU acceleration affect ANN training?
217. Why is deterministic ANN training difficult across hardware?
218. How do you export ANN models for production inference?
219. What ANN-specific monitoring should be done in production?
220. When is ANN not the right choice for a manufacturing use case?

## 12) CNN Fundamentals (Q221-Q240)
221. What is a convolution operation in CNNs?
222. What are kernels/filters and how do they learn features?
223. What is stride and how does it affect output resolution?
224. What is padding and why do we use it?
225. What is receptive field in CNN architecture?
226. How does pooling reduce dimensionality?
227. Compare max pooling and average pooling.
228. Why are CNNs translation-invariant to an extent?
229. What are feature maps in a CNN layer?
230. Why do early CNN layers learn edges and textures?
231. Why do deeper CNN layers learn semantic patterns?
232. What is the role of flattening before dense layers?
233. Why is parameter sharing beneficial in CNNs?
234. What is the difference between convolution and cross-correlation?
235. What is depthwise separable convolution?
236. How do 1x1 convolutions help network design?
237. What is dilated convolution and where is it useful?
238. How do CNNs handle grayscale vs RGB industrial images?
239. What preprocessing is required before CNN inference?
240. What are common causes of poor CNN generalization?

## 13) CNN Architectures and Training (Q241-Q260)
241. Compare LeNet, AlexNet, VGG, ResNet, and EfficientNet briefly.
242. What problem do residual connections solve?
243. How do skip connections improve gradient flow?
244. What is transfer learning and why is it useful in quality inspection?
245. What is fine-tuning vs feature extraction in pretrained CNNs?
246. How do you choose layers to freeze during transfer learning?
247. What data augmentation techniques are useful for defect images?
248. How does class imbalance affect defect detection CNNs?
249. What are focal loss and weighted loss functions?
250. What is IoU and where is it used in vision tasks?
251. What is mAP and how is it interpreted?
252. How do you evaluate CNN false negatives in safety-critical QA?
253. What is Grad-CAM and why is it useful for explainability?
254. How do you detect data leakage in image datasets?
255. Why can background artifacts cause shortcut learning in CNNs?
256. How do you design a robust train/val/test split for image data?
257. What are practical GPU memory optimization techniques for CNN training?
258. How do you benchmark CNN inference latency in production?
259. What compression methods (quantization/pruning) apply to CNN deployment?
260. How do you monitor CNN performance drift after deployment?

## 14) Time Series and LSTM (Q261-Q280)
261. Why do time series problems require order-aware data splitting?
262. What are stationarity and seasonality in time series?
263. How do lag and rolling features compare with sequence models?
264. What is a sliding window and why is it used for LSTM input?
265. How does an LSTM cell differ from a simple RNN cell?
266. What are input, forget, and output gates in LSTM?
267. Why do LSTMs mitigate vanishing gradients better than vanilla RNNs?
268. How do you choose lookback window size for LSTM forecasting?
269. What is teacher forcing and when is it relevant?
270. How do you handle multi-step forecasting in LSTM?
271. Why must sequence scaling be consistent between training and inference?
272. What are sequence-to-one vs sequence-to-sequence forecasting setups?
273. How do you evaluate forecasting models with rolling-origin backtesting?
274. What is MAPE and when can it be misleading?
275. Why should naive forecasts be included as benchmarks?
276. How do exogenous variables improve demand forecasting?
277. How do you prevent leakage in calendar/event features?
278. How do you detect forecast drift after deployment?
279. How do you estimate uncertainty in LSTM forecasts?
280. When are tree-based time-series features better than LSTM?

## 15) Demand Forecasting Module Viva (Q281-Q300)
281. Why aggregate demand by store-item-date before modeling?
282. What business decisions depend on accurate demand forecasts?
283. Why were lag windows like 7, 14, and 30 chosen?
284. How do rolling mean and rolling std improve model signal?
285. Why include day-of-week and month in forecasting features?
286. How do promotions/holidays affect forecast quality?
287. Why use a train/val/test temporal split of 70/15/15?
288. How do you compare Linear Regression, Random Forest, XGBoost, and LSTM fairly?
289. Why can LSTM have a different effective test size after windowing?
290. How do you ensure SKU-level forecasts remain coherent with total demand?
291. What risks arise when using synthetic data for notebook validation?
292. How do you handle cold-start SKUs with little history?
293. What retraining cadence is suitable for demand models?
294. What forecast horizon is optimal for procurement planning?
295. How do you evaluate forecasts across high-volume and low-volume SKUs?
296. How is forecast output integrated into inventory risk scoring?
297. Which model interpretability techniques help planners trust forecasts?
298. How do you set alert thresholds for forecast degradation?
299. What runtime SLAs are needed for forecast API endpoints?
300. What fallback logic should be used when model inference fails?

## 16) Predictive Maintenance Module Viva (Q301-Q320)
301. What is predictive maintenance and how is it different from preventive maintenance?
302. What labels are typically used in maintenance prediction tasks?
303. How do sensor sampling rates impact feature design?
304. What features indicate imminent equipment failure?
305. How do you model remaining useful life (RUL)?
306. What are challenges of rare failure events in model training?
307. How do false negatives impact maintenance risk?
308. How do false positives impact operations cost?
309. What threshold strategy is used for maintenance alerting?
310. Why are temporal validation strategies critical in maintenance data?
311. How do you deal with sensor drift and recalibration events?
312. What role do operating regimes play in model performance?
313. How do you capture machine-specific behavior differences?
314. How do you explain a high-risk score to reliability engineers?
315. What actions should follow a model-generated maintenance alert?
316. How do you monitor maintenance model precision over time?
317. What data governance controls are required for machine telemetry?
318. How do you design feedback loops from maintenance outcomes?
319. Which metrics are most important for maintenance model success?
320. How do you run safe canary deployment for maintenance models?

## 17) Quality Inspection Module Viva (Q321-Q340)
321. What is the target variable in a typical quality inspection model?
322. How do vision and tabular quality models complement each other?
323. How do you define defect taxonomy consistently across plants?
324. Why is annotation quality crucial for CNN defect models?
325. How do you handle class imbalance between normal and defective samples?
326. What is the cost of a false accept vs false reject in QA?
327. How do you set operating thresholds for pass/fail decisions?
328. What explainability methods are acceptable for quality auditors?
329. How do you avoid data leakage from repeated product images?
330. How do you manage domain shift between camera setups?
331. What preprocessing is required for illumination variation?
332. How do you monitor defect-type-specific performance drift?
333. Why might precision be prioritized over recall (or vice versa) in QA?
334. How do you integrate quality predictions with MES systems?
335. How do you validate robustness under noisy production conditions?
336. What retraining triggers should be used for quality models?
337. How do you version quality datasets and annotation guidelines?
338. What is a human-in-the-loop workflow for uncertain predictions?
339. How do you estimate throughput impact from model inference latency?
340. How do you test quality model rollback procedures?

## 18) Inventory Optimization Viva (Q341-Q360)
341. How does inventory optimization depend on demand forecasts?
342. What is reorder point and how is it calculated?
343. What is safety stock and how is uncertainty incorporated?
344. How do lead time and service level affect optimal stock?
345. What is stockout risk and how is it quantified?
346. How do you balance holding cost vs stockout penalty?
347. Why aggregate inventory data by warehouse-SKU-date?
348. Which features are most predictive for inventory risk scoring?
349. How can seasonality distort reorder recommendations?
350. How do you incorporate supplier reliability in risk models?
351. What KPI should validate inventory model effectiveness?
352. How do you evaluate model recommendations against EOQ baselines?
353. What constraints must be considered in real reorder decisions?
354. How do you avoid over-ordering due to forecast bias?
355. How should inventory model outputs be surfaced in dashboards?
356. How do you detect drift in stock and demand distributions?
357. What failure modes exist if inventory APIs are unavailable?
358. How do you prioritize SKUs for model rollout?
359. How do you A/B test inventory policies safely?
360. How do you audit inventory recommendation decisions?

## 19) MLflow and MLOps (Q361-Q380)
361. What is the purpose of experiment tracking in MLflow?
362. What artifacts should be logged for reproducible experiments?
363. What are run parameters, metrics, and artifacts in MLflow?
364. How does model registry support governance and traceability?
365. What is model versioning and why is it critical?
366. How do staging and production model stages differ?
367. What checks should gate model promotion to production?
368. How do you compare runs programmatically for selection?
369. How do you maintain lineage from data to model to endpoint?
370. What is a champion-challenger deployment workflow?
371. How do CI/CD pipelines integrate with MLflow registry?
372. What rollback strategy should be used after bad model release?
373. How should feature preprocessing objects be versioned with models?
374. How do you track environment dependencies for reproducibility?
375. What are risks of local artifact storage vs object storage?
376. How do you secure model registry access in enterprise setups?
377. How do you monitor model freshness and staleness?
378. What retraining orchestration options are suitable for this platform?
379. How do you design model approval workflows with audit trails?
380. What MLOps anti-patterns are common in early-stage platforms?

## 20) Backend and API Architecture (Q381-Q400)
381. Why use FastAPI for ML microservices?
382. How do DTOs improve API contract reliability?
383. What validation rules should be enforced at request boundaries?
384. How do dependency injection patterns improve testability?
385. Why is centralized exception handling important?
386. How do you structure APIs for maintenance, quality, forecast, and inventory endpoints?
387. What are sync vs async tradeoffs in inference services?
388. How do you enforce API latency SLAs under load?
389. What retry and timeout strategies should clients use?
390. How do you handle partial failures across microservices?
391. What authentication mechanism fits internal industrial APIs?
392. How do you implement authorization by plant/role?
393. Why is rate limiting important for prediction endpoints?
394. How do you version APIs without breaking clients?
395. What should be included in OpenAPI docs for ML endpoints?
396. How do you design health, readiness, and liveness endpoints?
397. How do you expose model metadata safely via API?
398. How can idempotency be handled in inference requests?
399. What logging context should be captured per request?
400. How do you load models efficiently at startup in FastAPI?

## 21) Frontend and Dashboard Viva (Q401-Q420)
401. Why use Material UI for enterprise dashboards?
402. How do you design responsive dashboard layouts for desktop and mobile?
403. What KPIs should appear on an Executive Dashboard?
404. How should Maintenance Dashboard visualize risk trends?
405. What visuals are most useful for Quality Dashboard insights?
406. How should Forecast Dashboard communicate uncertainty?
407. How should Inventory Dashboard represent reorder risk and priorities?
408. Why are real-time charts useful for operations command centers?
409. How do you avoid misleading chart scaling in KPI dashboards?
410. What caching strategy should frontend use for API calls?
411. How should auth context be handled in React apps?
412. What are secure token storage best practices in browser apps?
413. How do protected routes improve security posture?
414. How do you design error states for failed prediction APIs?
415. What UX patterns improve trust in AI-generated recommendations?
416. How do you show model confidence and caveats in UI?
417. How do you handle stale data indicators in dashboards?
418. How do you make dashboard filtering performant at scale?
419. What accessibility requirements matter for industrial dashboards?
420. How do you test frontend integrations with backend mock services?

## 22) Observability and Monitoring Viva (Q421-Q440)
421. Why is Prometheus suitable for monitoring ML services?
422. What metrics define API latency and how are percentiles used?
423. How do you monitor model latency separately from API latency?
424. What is prediction volume and why track it per model?
425. How do you compute and track error rates per endpoint?
426. What are useful Grafana dashboard panels for this platform?
427. How does OpenTelemetry tracing help root-cause analysis?
428. Why use Jaeger for distributed trace visualization?
429. What tracing spans should be created in inference flows?
430. How do you correlate logs, metrics, and traces in incidents?
431. How do ELK components support centralized logging?
432. What structured log fields are essential for ML services?
433. How do you design alerts for high latency and high error rates?
434. How should alert thresholds differ for batch vs real-time endpoints?
435. What are high-cardinality metric pitfalls in Prometheus?
436. How do you sample traces without losing diagnostic value?
437. What drift detection metrics should be monitored continuously?
438. How do you monitor data freshness and missing data incidents?
439. How do you build SLOs for AI services in manufacturing?
440. What runbooks should accompany observability dashboards?

## 23) Drift Detection and Model Governance (Q441-Q460)
441. What is feature drift and how do you detect it statistically?
442. What is label drift and why is it harder to detect in real time?
443. What is prediction drift and what does it indicate?
444. How can PSI (Population Stability Index) be used for drift monitoring?
445. How do KS tests help compare training and production distributions?
446. What drift thresholds should trigger investigation vs retraining?
447. How do you prevent alert fatigue in drift monitoring?
448. What governance policy should exist for model retraining approvals?
449. How do you validate new model candidates under drifted data?
450. What is shadow deployment and why is it valuable?
451. What is canary deployment for ML models?
452. How do you measure business impact of model drift?
453. How do delayed labels affect drift response strategies?
454. What rollback criteria should be codified in production?
455. How do you ensure traceability for each prediction decision?
456. How do you handle regulated audit requests for model outcomes?
457. Why is data lineage essential for drift root-cause analysis?
458. How do you document model cards for industrial AI systems?
459. What governance controls are needed for model promotion workflow?
460. How do you enforce separation of duties in MLOps pipelines?

## 24) Security, Reliability, and Scalability (Q461-Q480)
461. What are top security risks for ML APIs in industrial environments?
462. How do you secure model artifacts at rest and in transit?
463. Why is secrets management mandatory in production ML platforms?
464. How do you design RBAC for data scientists, operators, and admins?
465. What is the role of network segmentation in protecting OT/IT systems?
466. How do you mitigate prompt/model extraction attacks on APIs?
467. How do you defend against data poisoning risks in retraining pipelines?
468. What reliability patterns improve inference service uptime?
469. How do circuit breakers and bulkheads help microservice resilience?
470. What autoscaling signals should be used for inference pods?
471. How do you plan capacity for peak prediction traffic?
472. What caching strategies reduce inference latency and cost?
473. How do you guarantee graceful degradation when dependencies fail?
474. What backup and disaster recovery plans are needed for model registry?
475. How do you test chaos scenarios for ML microservices?
476. Why are liveness/readiness probes important in Kubernetes deployment?
477. How do you isolate noisy-neighbor effects in multi-tenant environments?
478. How do you estimate infra cost impact of observability retention?
479. What tradeoffs exist between latency, accuracy, and compute cost?
480. How do you prioritize technical debt under production pressure?

## 25) System Design, Strategy, and Viva Deep-Dive (Q481-Q500)
481. How would you explain end-to-end architecture of this platform to leadership?
482. What design decisions make this platform extensible for new AI modules?
483. Why should training and inference be separated operationally?
484. How do you define production readiness for AI systems?
485. What maturity model would you use for this Smart Factory AI platform?
486. What are the biggest architectural risks in the current implementation?
487. What are the highest-priority improvements before go-live?
488. How would you phase rollout across plants safely?
489. How would you benchmark ROI of each AI module?
490. Which KPIs indicate success for predictive maintenance deployment?
491. Which KPIs indicate success for quality inspection deployment?
492. Which KPIs indicate success for demand forecasting deployment?
493. Which KPIs indicate success for inventory optimization deployment?
494. How would you present model uncertainty to non-technical stakeholders?
495. What governance board decisions are required for model promotion?
496. How would you audit fairness and consistency across plants and product lines?
497. What is your strategy for continuous learning and retraining?
498. How do you future-proof the platform for edge AI use cases?
499. If one module fails, how should the overall command center continue operating?
500. What would your 90-day production hardening roadmap include?
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
