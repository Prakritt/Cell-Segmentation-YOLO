import os 
from pathlib import Path
import logging # to check if the files are being created or not 

logging.basicConfig(level=logging.INFO,format='[%(asctime)s]: %(message)s: ')

project_name = "cellSegmentation"

lost_of_files = [
    ".github/workflows/.gitkeep",#For CICD deplyent, gitkeep to commit empty folder
    "data/.gitkeep",#User uploaded Image will be saved in this folder 
    f"{project_name}/__init__.py",
    f"{project_name}/components/__init__.py",
    f"{project_name}/components/data_ingestion.py",
    f"{project_name}/components/data_validation.py",
    f"{project_name}/components/model_trainer.py",
    f"{project_name}/constant/__init__.py",
    f"{project_name}/constant/training_pipeline/__init__.py",
    f"{project_name}/constant/application.py",
    f"{project_name}/entity/config_entity.py",
    f"{project_name}/entity/artifacts_entity.py"
    f"{project_name}/exception/__init__.py"
    f"{project_name}/logger/__init__.py",
    f"{project_name}/pipeline/__init__.py"
    f"{project_name}/pipeline/training_pipeline.py",
    f"{project_name}/utils/__init__.py",
    f"{project_name}/utils/main_utils.py",
    "research/trails.ipynb",
    "templates/index.html",
    "app.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py"#Will help for local package installation

]

for filepath in lost_of_files:
    filepath = Path(filepath)

    filedir, filename = os.path.split(filepath)

    if filedir!="":
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"Creating directory: {filedir} for file {filename}")
    if(not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
        with open(filepath,"w") as f:
            pass
            logging.info(f"Creating empty file {filename }")
    
    else:
        logging.info(f"{filename} already exists..")