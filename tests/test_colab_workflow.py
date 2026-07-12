from pathlib import Path

import src


def test_project_package_and_notebooks_are_scaffolded():
    root = Path(__file__).resolve().parents[1]

    assert hasattr(src, "get_project_summary")

    notebooks_dir = root / "notebooks"
    expected_notebooks = [
        "01_environment.ipynb",
        "02_dataset.ipynb",
        "03_non_iid.ipynb",
        "04_fedavg.ipynb",
        "05_meta_learning.ipynb",
        "06_dp.ipynb",
        "07_connectivity.ipynb",
        "08_results.ipynb",
    ]

    for notebook_name in expected_notebooks:
        assert (notebooks_dir / notebook_name).exists(), f"Missing notebook: {notebook_name}"
