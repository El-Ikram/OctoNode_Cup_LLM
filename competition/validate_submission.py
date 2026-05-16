# competition/validate_submission.py

import pandas as pd
import sys


REQUIRED_COLUMNS = {"id", "ml_target"}


def main(pred_path, test_nodes_path):
    preds = pd.read_csv(pred_path)
    test_nodes = pd.read_csv(test_nodes_path)

    # Required columns
    if not REQUIRED_COLUMNS.issubset(preds.columns):
        raise ValueError("Submission must contain columns: id, ml_target")

    # Duplicate IDs
    if preds["id"].duplicated().any():
        raise ValueError("Duplicate IDs found in submission")

    # No NaNs
    if preds["ml_target"].isna().any():
        raise ValueError("NaN values found in predictions")

    # Strict binary check (0 or 1 only)
    if not set(preds["ml_target"].unique()).issubset({0, 1}):
        raise ValueError("Predictions must be binary: 0 or 1")

    # Exact ID match
    if set(preds["id"]) != set(test_nodes["id"]):
        raise ValueError("Submission IDs do not match required test IDs")

    print("VALID_SUBMISSION")


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
