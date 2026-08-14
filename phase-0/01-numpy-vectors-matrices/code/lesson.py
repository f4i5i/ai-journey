"""
Topic 0.1 — NumPy vectors & matrices: the LESSON.

Run me:  ../../../.venv/bin/python lesson.py  (or activate the venv first)

Read each section, run the file, and match the printed output to the code.
Then go earn your checkmarks in drills.py.
"""
import time

import numpy as np

rng = np.random.default_rng(seed=42)

print("=" * 60)
print("1. A vector is just an array with a shape")
print("=" * 60)

v = np.array([2.0, -1.0, 3.0])
M = np.array([[1.0, 2.0, 3.0],
              [4.0, 5.0, 6.0]])

print(f"v         = {v},  shape={v.shape}")   # (3,)   1-D: a vector
print(f"M shape   = {M.shape}")               # (2, 3) 2-D: a matrix
# In ML, EVERYTHING is one of these:
#   one data sample  -> a vector of features        shape (n_features,)
#   a whole dataset  -> a matrix, one row per sample shape (n_samples, n_features)
#   model weights    -> a vector (or matrix)

print()
print("=" * 60)
print("2. The dot product — the single most-used operation in ML")
print("=" * 60)

# Dot product: multiply elementwise, then sum. That's it.
a = np.array([1.0, 2.0, 3.0])
b = np.array([4.0, 5.0, 6.0])

manual = 0.0
for i in range(len(a)):
    manual += a[i] * b[i]

print(f"by loop : {manual}")            # 1*4 + 2*5 + 3*6 = 32
print(f"np.dot  : {np.dot(a, b)}")
print(f"a @ b   : {a @ b}   (@ is the same thing)")
# Why care? A linear model's prediction IS a dot product:
#   prediction = weights . features + bias

print()
print("=" * 60)
print("3. Why we vectorize: loops are slow, NumPy is fast")
print("=" * 60)

big_a = rng.random(1_000_000)
big_b = rng.random(1_000_000)

t0 = time.perf_counter()
s = 0.0
for i in range(len(big_a)):
    s += big_a[i] * big_b[i]
loop_ms = (time.perf_counter() - t0) * 1000

t0 = time.perf_counter()
s2 = big_a @ big_b
numpy_ms = (time.perf_counter() - t0) * 1000

print(f"python loop: {loop_ms:8.1f} ms")
print(f"numpy @    : {numpy_ms:8.2f} ms   -> ~{loop_ms / numpy_ms:.0f}x faster")
# This is THE reason ML code looks the way it does: no loops over samples,
# ever. One matrix expression handles the whole dataset at once.

print()
print("=" * 60)
print("4. Matrix multiplication = many dot products at once")
print("=" * 60)

# (2,3) @ (3,) -> (2,)  : each ROW of M dotted with v
print(f"M @ v = {M @ v}")
print(f"  row0 . v = {M[0] @ v},  row1 . v = {M[1] @ v}  (same numbers!)")

# The shape rule: (a, b) @ (b, c) -> (a, c). Inner dims must MATCH.
A = rng.random((4, 3))
B = rng.random((3, 5))
print(f"(4,3) @ (3,5) -> {(A @ B).shape}")
# ML translation: X (100 samples, 3 features) @ w (3 weights) -> 100 predictions
# in ONE line. That's section 3's speedup applied to a whole model.

print()
print("=" * 60)
print("5. Broadcasting — NumPy stretches shapes for you")
print("=" * 60)

X = np.array([[1.0, 2.0],
              [3.0, 4.0],
              [5.0, 6.0]])          # (3, 2): 3 samples, 2 features

print(f"X * 10 :\n{X * 10}")         # scalar stretches to every element
col_means = X.mean(axis=0)           # (2,) - mean of each COLUMN (axis 0 collapses rows)
print(f"col_means = {col_means}")
print(f"X - col_means :\n{X - col_means}")   # (3,2) - (2,) : the (2,) row is
# "broadcast" (repeated) across all 3 rows. This one line CENTERS a dataset —
# a preprocessing step you'll use in nearly every ML pipeline.

# The rule: compare shapes right-to-left; dims are compatible if equal or 1.
#   (3, 2) vs (2,)   -> (2,) acts like (1, 2) -> stretched to (3, 2). OK!
#   (3, 2) vs (3,)   -> ERROR: 2 vs 3 mismatch on the last axis.
# Gotcha: to broadcast per-ROW you need a column shape, e.g. (3, 1):
row_sums = X.sum(axis=1, keepdims=True)    # (3, 1) instead of (3,)
print(f"X / row_sums (normalize each row):\n{X / row_sums}")

print()
print("Lesson done. Now open drills.py and make every check pass.")
