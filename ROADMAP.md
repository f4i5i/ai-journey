# AI Journey — Full Roadmap

> Learn → Code → Sketchnote → Ship. Every topic gets: working code in this repo, a short `notes.md`, and (for the ★ topics) a sketchnote post.
> Complexity escalates inside each phase; each phase ends with a **milestone project** that gets deployed, not just committed.

**Format per topic folder:** `code/lesson.ipynb` (worked examples, run every cell) + `code/drills.ipynb` (exercises with self-checks — make them all pass) · `notes.md` (what I learned, in my own words) · `sketchnote/` (prompt + final image, if ★)

---

## Phase 0 — Foundations (Week 1–2)

| # | Topic | Code exercise | ★ |
|---|-------|---------------|---|
| 0.1 | Python for ML: NumPy vectors & matrices | implement dot product, broadcasting drills | |
| 0.2 | Pandas: loading, cleaning, groupby, joins | clean a messy real CSV end-to-end | |
| 0.3 | Visualization: matplotlib/seaborn | explore + plot one dataset, find 3 insights | |
| 0.4 | Math essentials 1: linear algebra (vectors, matrices, dot products) | code the math by hand in NumPy | ★ "The math you actually need for ML" |
| 0.5 | Math essentials 2: derivatives & gradients | numerically estimate a gradient | |
| 0.6 | Math essentials 3: probability & statistics (distributions, Bayes, mean/variance) | simulate coin flips → central limit theorem | ★ |

**Milestone 0:** Exploratory Data Analysis report on one messy public dataset, pushed with clean commit history.

---

## Phase 1 — Classical Machine Learning (Week 3–8)

| # | Topic | Code exercise | ★ |
|---|-------|---------------|---|
| 1.1 | What IS machine learning: supervised vs unsupervised vs RL | none — concept post | ★ "Types of ML" |
| 1.2 | Linear regression + loss functions + gradient descent | implement from scratch in NumPy, then sklearn | ★ "How a model learns" |
| 1.3 | Logistic regression & classification | from scratch + sklearn | |
| 1.4 | Evaluation metrics: accuracy, precision, recall, F1, ROC-AUC, confusion matrix | build a metrics report function | ★ "Accuracy is a lie" |
| 1.5 | Train/validation/test split, cross-validation | k-fold CV by hand | |
| 1.6 | Overfitting & bias-variance trade-off | plot learning curves, force overfit then fix it | ★ |
| 1.7 | Regularization: L1, L2 | ridge vs lasso comparison | |
| 1.8 | Feature engineering & preprocessing pipelines | sklearn Pipeline + ColumnTransformer | ★ "Features beat models" |
| 1.9 | Decision trees | train, visualize the tree | |
| 1.10 | Ensembles: random forest, gradient boosting (XGBoost/LightGBM) | compare all on one dataset | ★ "Why XGBoost wins tabular" |
| 1.11 | KNN, Naive Bayes, SVM | quick comparison notebook | |
| 1.12 | Class imbalance: SMOTE, class weights, threshold tuning | fix an imbalanced problem properly | |
| 1.13 | Hyperparameter tuning: grid, random, Optuna | tune the milestone model | |
| 1.14 | Unsupervised: k-means, DBSCAN, hierarchical | cluster customers, interpret clusters | ★ |
| 1.15 | Dimensionality reduction: PCA, t-SNE/UMAP | visualize high-dim data in 2D | |
| 1.16 | **Error analysis & model debugging**: slice-based analysis, leakage detection, "why is my model wrong?" | take a mediocre model, find the 3 worst slices, fix the biggest one | ★ "Debug the data, not the model" |

**Milestone 1 (small):** Titanic/housing baseline — full pipeline, honest evaluation.
**Milestone 1 (real):** **Churn prediction service** — messy dataset, feature pipeline, XGBoost, FastAPI endpoint, Docker, deployed, with an ADR (why these choices).

---

## Phase 2 — Deep Learning (Week 9–14)

| # | Topic | Code exercise | ★ |
|---|-------|---------------|---|
| 2.1 | The neuron & multi-layer perceptron | forward pass in NumPy | ★ "What a neural net actually is" |
| 2.2 | Backpropagation & autograd | train a tiny net from scratch, then PyTorch autograd | ★ "How backprop works" |
| 2.3 | PyTorch fundamentals: tensors, Dataset, DataLoader, nn.Module | rebuild 2.1 in PyTorch | |
| 2.4 | Activations, losses, optimizers (SGD → Adam) | compare optimizers on same task | |
| 2.5 | The training loop: batching, LR schedules, early stopping | write a reusable train loop | |
| 2.6 | Regularization in DL: dropout, batch norm, weight decay | ablation experiment | |
| 2.7 | CNNs: convolutions, pooling, architectures | train CNN on CIFAR-10 | ★ "How CNNs see" |
| 2.8 | Transfer learning | fine-tune ResNet on a small custom dataset | ★ "Never train from scratch" |
| 2.9 | RNN / LSTM / GRU | character-level text generator | |
| 2.10 | Attention & the Transformer | implement single-head attention; read "Attention Is All You Need" | ★ "The transformer, drawn" |
| 2.11 | Experiment tracking: MLflow or W&B | instrument the training loop | |
| 2.12 | **Debugging neural nets**: loss-curve reading, overfit-one-batch test, gradient checks, LR sweeps | break a training run 5 ways, diagnose each from the curves alone | ★ "Read the loss curve like a doctor" |

**Milestone 2:** Image classifier on a self-collected dataset (photos you take/scrape), fine-tuned, tracked experiments, deployed behind an API with a simple UI.

---

## Phase 3 — Computer Vision (Week 15–19)

| # | Topic | Code exercise | ★ |
|---|-------|---------------|---|
| 3.1 | Images as data; OpenCV basics | filters, edges, transforms | |
| 3.2 | Data augmentation | augmentation pipeline + effect on accuracy | |
| 3.3 | Object detection: YOLO family | fine-tune YOLO on custom objects | ★ "Classification vs detection vs segmentation" |
| 3.4 | Segmentation (semantic vs instance) | run SAM / train U-Net on small task | |
| 3.5 | OCR | extract text from receipts/documents | |
| 3.6 | Vision transformers & CLIP | zero-shot classification with CLIP | ★ |

**Milestone 3:** Custom object-detection app (pick a local, real problem — e.g. traffic/retail shelf/document), labeled own data, deployed with live inference.

---

## Phase 4 — NLP (Week 20–24)

| # | Topic | Code exercise | ★ |
|---|-------|---------------|---|
| 4.1 | Text preprocessing & tokenization (BPE!) | build a tiny BPE tokenizer | ★ "How LLMs read" |
| 4.2 | Classical NLP: bag-of-words, TF-IDF + linear model | spam/sentiment classifier | |
| 4.3 | Word embeddings: word2vec, GloVe | train word2vec, explore analogies | ★ "King − man + woman" |
| 4.4 | HuggingFace ecosystem | pipeline → tokenizer → model, fine-tune workflow | |
| 4.5 | Fine-tune BERT for classification | beat the TF-IDF baseline | |
| 4.6 | Named Entity Recognition | fine-tune for NER on domain data | |
| 4.7 | Small model vs LLM API showdown | same task: fine-tuned small model vs LLM — cost, latency, accuracy table | ★ "When NOT to use an LLM" |

**Milestone 4:** Text-classification/NER microservice with the cost-accuracy comparison written up as an ADR. (This one IS architecture judgment, documented.)

---

## Phase 5 — Specialized Domains (Week 25–28)

| # | Topic | Code exercise | ★ |
|---|-------|---------------|---|
| 5.1 | Time-series: stationarity, baselines, backtesting | naive vs ARIMA vs gradient boosting | ★ "Forecasting done honestly" |
| 5.2 | Forecasting with ML | sales/demand forecast with proper backtest | |
| 5.3 | Recommenders: collaborative filtering, matrix factorization | build a movie/product recommender | ★ |
| 5.4 | Recommenders: two-tower / embeddings-based | upgrade 5.3 with embeddings | |
| 5.5 | Speech: Whisper STT + a TTS model | transcription pipeline | |

**Milestone 5:** One deployed forecasting OR recommender system on real data.

---

## Phase 6 — MLOps & Production (Week 29–32, overlaps everything)

| # | Topic | Code exercise | ★ |
|---|-------|---------------|---|
| 6.1 | Model serving patterns: batch vs online, FastAPI, model registry | standardize serving across past projects | |
| 6.2 | Docker & docker-compose for ML | containerize every milestone | |
| 6.3 | CI/CD for models: tests, GitHub Actions | auto-test + build on push | ★ "MLOps in one picture" |
| 6.4 | Monitoring & drift detection | add drift alerts to the churn service | ★ |
| 6.5 | Kubernetes basics + GPU serving, quantization, vLLM | self-host an open LLM with vLLM | ★ "Self-hosting an LLM" |
| 6.6 | Build an MCP server | working MCP server, published | ★ |

**Milestone 6 (capstone):** One end-to-end platform combining pieces: e.g. churn model + recommender + LLM explanation layer, monitored, documented with ADRs.

> GenAI/LLM theory track (RAG, agents) is covered by the content series — this repo holds its CODE: the RAG pipeline with evals (series finale link) and the agent + MCP builds.

---

## Phase 7 — LLM Engineering: Evaluation, Fine-tuning, Optimization (Week 33–40)

> The differentiator phase. Anyone can call an LLM API — this is the "one step ahead of just building" layer: measure it, tune it, make it cheaper and faster, debug it, attack it.

| # | Topic | Code exercise | ★ |
|---|-------|---------------|---|
| 7.1 | LLM evaluation fundamentals: benchmarks vs YOUR task, building a golden eval set | hand-build a 50-case eval set for one real task | ★ "Benchmarks lie about your use case" |
| 7.2 | Eval harnesses & LLM-as-judge: pairwise vs rubric scoring, judge bias, human agreement check | build a reusable eval harness; measure judge-vs-human agreement | ★ |
| 7.3 | Prompt engineering as ENGINEERING: versioned prompts, regression tests, A/B prompts | put prompts under test — a prompt change must pass evals before merge | ★ "Prompts are code" |
| 7.4 | Structured outputs & guardrails: JSON schemas, validators, retry-on-invalid | constrained-output pipeline with failure handling | |
| 7.5 | Fine-tuning 1: dataset curation + SFT with LoRA/QLoRA | fine-tune a small open model on a custom dataset | ★ "Fine-tuning on one GPU" |
| 7.6 | Fine-tuning 2: preference tuning (DPO) + the decision framework — fine-tune vs prompt vs RAG | DPO pass on 7.5's model; write the decision ADR | ★ |
| 7.7 | Quantization & distillation: GGUF/AWQ, quality-vs-size curves, teacher→student | quantize 7.5's model at 3 levels, plot quality vs size vs speed | ★ "Shrink the model, keep the brain" |
| 7.8 | Token & cost optimization: prompt compression, context budgeting, semantic caching, model routing | cut a real pipeline's cost 5-10x, before/after dashboard | ★ "Same quality, 1/10th the bill" |
| 7.9 | Inference internals: KV cache, continuous batching, speculative decoding | benchmark vLLM vs naive serving, explain WHY it wins | ★ |
| 7.10 | LLM observability: tracing, token/latency/cost per request (Langfuse or OTel) | instrument an LLM app end-to-end | |
| 7.11 | Debugging LLM apps: failure taxonomy, error analysis loop, retrieval-vs-generation diagnosis | take a failing RAG app, classify 50 failures, fix the top class, re-eval | ★ "Debug LLM apps like a scientist" |
| 7.12 | LLM security testing: prompt-injection red-teaming, jailbreak evals, output filtering | red-team your own app with an attack suite; fix what breaks | ★ |

**Milestone 7 (the standout):** **Fine-tune → prove → ship.** Fine-tune a small model on a custom dataset, *beat the base model on your own eval harness*, quantize it, serve it with vLLM, and publish the full writeup: eval numbers, cost-per-1k-requests vs the API model, and the ADR. This single project demonstrates evaluation + fine-tuning + optimization + serving in one artifact.

---

## Journey rules

1. **Code before content** — the sketchnote for a topic is only made after the code runs.
2. **Commit per topic** — small commits, real messages; the git history IS the journey.
3. **notes.md in my own words** — if I can't explain it simply, I don't know it yet.
4. **Every milestone gets deployed** — a URL or it didn't happen.
5. **Every milestone gets an ADR** — what I chose, what I rejected, why.
6. **From scratch first, library second** — implement the core idea in NumPy once, then use the real tool forever.
7. **Every library call gets explained** — any lesson line that uses a library method (`np.mean`, `train_test_split`, `nn.Module`, …) carries a short inline comment saying what that method does and why it's used here. If a line can't be explained in one comment, it doesn't go in the lesson.
