import os
import torch
import pandas as pd
import matplotlib.pyplot as plt


def create_directories():
    os.makedirs("results/checkpoints", exist_ok=True)
    os.makedirs("results/metrics", exist_ok=True)
    os.makedirs("results/plots", exist_ok=True)


def save_model(model, filename):
    create_directories()
    torch.save(model.state_dict(),
               f"results/checkpoints/{filename}")


def save_metrics(df, filename):
    create_directories()
    df.to_csv(
        f"results/metrics/{filename}",
        index=False
    )


def save_plot(filename):
    create_directories()
    plt.savefig(
        f"results/plots/{filename}",
        dpi=300,
        bbox_inches="tight"
    )