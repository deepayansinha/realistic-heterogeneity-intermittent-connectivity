# realistic-heterogeneity-intermittent-connectivity

Federated Meta-Learning with Differential Privacy for Non-IID Edge Devices combines federated learning, meta-learning (MAML-style fast adaptation), differential privacy budgets, and communication-efficient gradient compression under realistic edge-device heterogeneity and intermittent connectivity.

## Workflow

This project is now structured around a Colab-first execution model:

- VS Code is used for editing, Git, documentation, and repository management.
- Google Colab is used for training, evaluation, and experiment runs.
- The repository code under src is designed to be imported from notebooks in Colab.

## Repository layout

- notebooks/: Colab notebooks for environment setup, datasets, non-IID partitions, FedAvg, meta-learning, differential privacy, connectivity, and results.
- src/: reusable Python modules for datasets, models, federated learning, privacy, simulation, and utilities.
- configs/: configuration files for experiments.
- results/: checkpoints, logs, metrics, and plots.

## Getting started

1. Clone the repository and open it in VS Code.
2. Use the notebooks in the notebooks/ directory as the main experiment entry points.
3. In Colab, mount the repository and run the notebooks from the project root.
