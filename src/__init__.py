from pathlib import Path


def get_project_summary():
    """Return a lightweight summary of the repository workflow."""
    return {
        "project_name": "realistic-heterogeneity-intermittent-connectivity",
        "workflow": "VS Code for editing and Git; Google Colab for training and evaluation",
        "notebooks": [
            "01_environment.ipynb",
            "02_dataset.ipynb",
            "03_non_iid.ipynb",
            "04_fedavg.ipynb",
            "05_meta_learning.ipynb",
            "06_dp.ipynb",
            "07_connectivity.ipynb",
            "08_results.ipynb",
        ],
        "root": str(Path(__file__).resolve().parents[1]),
    }
