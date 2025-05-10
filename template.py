import os 
from pathlib import Path 
import logging 
logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: - %(levelname)s - %(message)s')

project_name = "ProdPipeline"
list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py", ## local package 5
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/data/data_prep.py",
    f"src/{project_name}/training/train.py",
    f"src/{project_name}/evaluation/evaluate.py",
    f"src/{project_name}/deployment/deploy_model.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/pipeline/pipeline.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/helpers.py",
    f"src/{project_name}/test/test_pipeline.py",
    f"src/{project_name}/logging/__init__.py",
    f"requirements.txt",
    f"setup.py",
    f"run_pipeline.py",
    f"config/config.yaml",
    f"Dockerfile",
    f"Reseach/trial.ipynb"
]

for file in list_of_files:
    filepath = Path(file)
    filedir, filename = os.path.split(filepath)
    if filedir:
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating {filedir} directory")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
        with open(filepath, 'w') as f:
           pass 
        logging.info(f"Creating {filename} file")
    else:
        logging.info(f"{filename} already exists")
              