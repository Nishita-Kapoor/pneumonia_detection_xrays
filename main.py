# Main file to run
# Author: Nishita Kapoor

# Package Imports
import yaml
import argparse
from data.explore_data import data_analysis
from scripts.train import train
from scripts.evaluate import evaluate, predict
import os


# Main function
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", help="Path of config file, e.g. configs/config_resnet50.yaml", default="configs/final/config_resnet50.yaml",
                        type=str)
    args = parser.parse_args()

    # Read config file
    with open(str(args.config), "r") as ymlfile:
        cfg = yaml.safe_load(ymlfile)
        print("Config params: " + str(cfg) + "\n")

    os.environ["CUDA_VISIBLE_DEVICES"] = cfg["gpus"]

    # Which script to run, as per config setting
    task_map = {"EDA": data_analysis, "train": train,
                "evaluate": evaluate, "predict": predict}

    for task in cfg["tasks"]:
        task_map[task](**cfg)

# How to run:
# python main.py --config configs/config_resnet50.yaml
if __name__ == '__main__':
    main()
