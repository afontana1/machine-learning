"""Fill Unit 7 graded notebooks from their adjacent completed companions.

Only cells carrying a Coursera UNQ_* exercise identifier are updated.  Markdown,
setup cells, and notebook metadata remain untouched.
"""

from __future__ import annotations

import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1] / "Unit 7 - NLP"
EXERCISE_ID = re.compile(r"\bUNQ_[A-Z]?\d+\b")


def source(cell: dict) -> str:
    return "".join(cell.get("source", []))


def exercise_id(cell: dict) -> str | None:
    match = EXERCISE_ID.search(source(cell))
    return match.group(0) if match else None


def clean_hmm_tagger() -> int:
    """Remove dead placeholder raises and correct the bigram counting exercise."""
    path = ROOT / "NLP-with-Python" / "HMM Tagger.ipynb"
    notebook = json.loads(path.read_text(encoding="utf-8"))
    changed = 0

    for cell in notebook.get("cells", []):
        if cell.get("cell_type") != "code":
            continue
        text = source(cell)
        updated = text.replace("\n    raise NotImplementedError\n", "\n")

        if "def bigram_counts(sequences):" in updated:
            start = updated.index("def bigram_counts(sequences):")
            end = updated.index("\n# TODO: call bigram_counts", start)
            replacement = '''def bigram_counts(sequences):
    """Count adjacent value pairs within each input sequence."""
    counts = Counter()
    for sequence in sequences:
        counts.update(zip(sequence, sequence[1:]))
    return counts
'''
            updated = updated[:start] + replacement + updated[end:]
            updated = re.sub(
                r"tags = \[tag for i, \(word, tag\) in enumerate\(data\.stream\(\)\)\]\n"
                r"o = \[\(tags\[i\],tags\[i\+1\]\) for i in range\(0,len\(tags\)-2,2\)\]\n"
                r"tag_bigrams = bigram_counts\(o\)",
                "tag_bigrams = bigram_counts(data.training_set.Y)",
                updated,
            )

        if updated != text:
            cell["source"] = updated.splitlines(keepends=True)
            cell["execution_count"] = None
            cell["outputs"] = []
            changed += 1

    if changed:
        path.write_text(
            json.dumps(notebook, ensure_ascii=False, indent=1) + "\n",
            encoding="utf-8",
        )
        print(path.relative_to(ROOT))
    return changed


def repair_sentiment_lab() -> int:
    """Fix completed TODOs that used the training matrix in place of test data."""
    path = ROOT / "NLP-with-Python" / "sentiment_analysis.ipynb"
    notebook = json.loads(path.read_text(encoding="utf-8"))
    replacements = {
        "from sklearn.externals import joblib": "import joblib",
        "features_test = vectorizer.fit_transform(words_train).toarray()":
            "features_test = vectorizer.transform(words_test).toarray()",
        "clf.score(features_train, labels_train)": "clf.score(X_train, y_train)",
        "clf.score(features_test, labels_test)": "clf.score(X_test, y_test)",
        "my_eview_features=pr.normalize(my_review_features)":
            "my_review_features = pr.normalize(my_review_features)",
    }
    changed = 0
    for cell in notebook.get("cells", []):
        if cell.get("cell_type") != "code":
            continue
        text = source(cell)
        updated = text
        for old, new in replacements.items():
            updated = updated.replace(old, new)
        if updated != text:
            cell["source"] = updated.splitlines(keepends=True)
            cell["execution_count"] = None
            cell["outputs"] = []
            changed += 1
    if changed:
        path.write_text(
            json.dumps(notebook, ensure_ascii=False, indent=1) + "\n",
            encoding="utf-8",
        )
        print(path.relative_to(ROOT))
    return changed


def main() -> None:
    changed_notebooks = 0
    changed_cells = 0

    for assignment_path in sorted(ROOT.rglob("*_Assignment.ipynb")):
        if assignment_path.stem.endswith("_Solution"):
            continue

        solution_path = assignment_path.with_name(
            f"{assignment_path.stem}_Solution.ipynb"
        )
        if not solution_path.exists():
            continue

        assignment = json.loads(assignment_path.read_text(encoding="utf-8"))
        solution = json.loads(solution_path.read_text(encoding="utf-8"))
        completed = {
            key: cell
            for cell in solution.get("cells", [])
            if cell.get("cell_type") == "code" and (key := exercise_id(cell))
        }

        notebook_changed = False
        for cell in assignment.get("cells", []):
            if cell.get("cell_type") != "code":
                continue
            key = exercise_id(cell)
            if not key or key not in completed:
                continue
            completed_source = completed[key].get("source", [])
            if cell.get("source", []) == completed_source:
                continue
            cell["source"] = completed_source
            cell["execution_count"] = None
            cell["outputs"] = []
            changed_cells += 1
            notebook_changed = True

        if notebook_changed:
            assignment_path.write_text(
                json.dumps(assignment, ensure_ascii=False, indent=1) + "\n",
                encoding="utf-8",
            )
            changed_notebooks += 1
            print(assignment_path.relative_to(ROOT))

    hmm_cells = clean_hmm_tagger()
    sentiment_cells = repair_sentiment_lab()
    print(
        f"Updated {changed_cells} exercises in {changed_notebooks} notebooks; "
        f"cleaned {hmm_cells} HMM cells and repaired {sentiment_cells} sentiment cells."
    )


if __name__ == "__main__":
    main()
