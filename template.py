import logging
import os
from pathlib import Path

logging.basicConfig(level=logging.INFO, format='%(asctime)s:%(message)s:')

package_name = "Advance_house_price_prediction"

list_of_files = [
    f"src/{package_name}/__init__.py",
    f"src/{package_name}/components/__init__.py",
    f"src/{package_name}/utils/__init__.py",
    f"src/{package_name}/config/__init__.py",
    f"src/{package_name}/config/configuration.py",
    f"src/{package_name}/pipeline/__init__.py",
    f"src/{package_name}/entity/__init__.py",
    f"src/{package_name}/constants/__init__.py",
    f"src/{package_name}/exception/__init__.py",
    f"src/{package_name}/logger/__init__.py",
    "tests/__init__.py",
    "test/unit/__init__.py",
    "tests/integration/__init__.py",
    "configs/__init__.py",
    "configs/config.yaml",
    "configs/schema.yaml",
    "configs/model.yaml",
    "dvc.yaml",
    "params.yaml",
    "init_setup.sh",
    "requirements.txt",
    "requirements_dev.txt",
    "setup.py",
    'setup.cfg',
    "pyproject.toml",
    "tox.ini",
    "notebook/01-exploratory-data-analysis.ipynb",
    "notebook/02-feature-engineering.ipynb",
    "notebook/03-model-training.ipynb",
    "notebook/04-model-evaluation.ipynb",
    ]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory : {filedir} for file: {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass  # create an empty file
            logging.info(f"Creating empty file: {filepath}")
    else:
        logging.info(f"{filename} already exists")