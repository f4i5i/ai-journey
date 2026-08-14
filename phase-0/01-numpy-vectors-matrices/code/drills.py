"""
Topic 0.1 — DRILLS. Your job: replace every `TODO` until all checks pass.

Run me:  ../../../.venv/bin/python drills.py

Rules:
  - drill 1 must use a plain Python loop (prove you know what dot IS)
  - every other drill: NumPy only, NO loops
  - don't change the checks
"""
import numpy as np

TODO = None  # sentinel — replace TODO with your answer in each drill


# ---------------------------------------------------------------- drill 1
def dot_by_hand(a, b):
    """Compute the dot product with a plain Python loop (no np.dot, no @)."""
    result = TODO
    return result


# ---------------------------------------------------------------- drill 2
def predict(X, w, b):
    """Linear model predictions for ALL samples at once, no loops.
    X: (n_samples, n_features), w: (n_features,), b: scalar
    Returns: (n_samples,) — each sample's  w . x + b
    """
    return TODO


# ---------------------------------------------------------------- drill 3
def valid_shape(shape_a, shape_b):
    """Return the resulting shape of  A @ B  as a tuple, or None if invalid.
    No NumPy needed — pure shape reasoning: (a, b) @ (b, c) -> (a, c).
    """
    return TODO


# ---------------------------------------------------------------- drill 4
def center_columns(X):
    """Subtract each COLUMN's mean from that column (dataset centering)."""
    return TODO


# ---------------------------------------------------------------- drill 5
def normalize_rows(X):
    """Scale each ROW to sum to 1. Watch your shapes (keepdims!)."""
    return TODO


# ---------------------------------------------------------------- drill 6
def standardize(X):
    """The z-score: (X - column mean) / column std.
    THE most common ML preprocessing step. One expression, no loops.
    """
    return TODO


# ---------------------------------------------------------------- drill 7
def pairwise_diff(a, b):
    """Given a (n,) and b (m,), return the (n, m) matrix D where D[i, j] = a[i] - b[j].
    Hint: reshape a to a column with a[:, None], then broadcast.
    """
    return TODO


# ================================================================ checks
def main():
    rng = np.random.default_rng(0)
    results = []

    def check(name, fn):
        try:
            fn()
            results.append((name, "PASS", ""))
        except Exception as e:  # noqa: BLE001
            kind = "todo" if TODO is None and "NoneType" in str(e) else "FAIL"
            results.append((name, "FAIL", f"{type(e).__name__}: {e}"))

    def c1():
        a, b = rng.random(50), rng.random(50)
        assert np.isclose(dot_by_hand(a, b), a @ b)

    def c2():
        X, w, b = rng.random((100, 3)), rng.random(3), 0.5
        assert predict(X, w, b).shape == (100,)
        assert np.allclose(predict(X, w, b), X @ w + b)

    def c3():
        assert valid_shape((4, 3), (3, 5)) == (4, 5)
        assert valid_shape((2, 7), (7, 1)) == (2, 1)
        assert valid_shape((4, 3), (4, 5)) is None

    def c4():
        X = rng.random((30, 4))
        out = center_columns(X)
        assert out.shape == X.shape
        assert np.allclose(out.mean(axis=0), 0)

    def c5():
        X = rng.random((10, 6))
        assert np.allclose(normalize_rows(X).sum(axis=1), 1)

    def c6():
        X = rng.random((200, 5)) * 100 + 7
        out = standardize(X)
        assert np.allclose(out.mean(axis=0), 0, atol=1e-9)
        assert np.allclose(out.std(axis=0), 1)

    def c7():
        a, b = np.array([1.0, 2.0, 3.0]), np.array([10.0, 20.0])
        expected = np.array([[-9.0, -19.0], [-8.0, -18.0], [-7.0, -17.0]])
        assert pairwise_diff(a, b).shape == (3, 2)
        assert np.allclose(pairwise_diff(a, b), expected)

    check("1 dot_by_hand    (dot product with a loop)", c1)
    check("2 predict        (whole-dataset linear model)", c2)
    check("3 valid_shape    (matmul shape rules)", c3)
    check("4 center_columns (broadcasting, axis=0)", c4)
    check("5 normalize_rows (keepdims gotcha)", c5)
    check("6 standardize    (z-score)", c6)
    check("7 pairwise_diff  (2-D broadcasting)", c7)

    print()
    passed = 0
    for name, status, err in results:
        mark = "✅" if status == "PASS" else "❌"
        print(f"  {mark}  drill {name}")
        if err and "NoneType" not in err:
            print(f"        {err}")
        passed += status == "PASS"
    print(f"\n  {passed}/7 passed", "— topic complete! 🎉" if passed == 7 else "— keep going.")


if __name__ == "__main__":
    main()
