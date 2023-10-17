import os
from pathlib import Path
import logging

## logging string

logging.basicConfig(level=logging.INFO,format='[%(asctime)s]:[%(message)s]:')
 
project_name = 'CNNClassifier'
 
file_list = [
 ".github/workflow/.gitkeep",
  f"src/{project_name}/__init__.py",
  f"src/{project_name}/components/__init__.py",
  f"src/{project_name}/utils/__init__.py",
  f"src/{project_name}/config/__init__.py",
  f"src/{project_name}/config/configuration/__init__.py",
  f"src/{project_name}/pipeline/__init__.py",
  f"src/{project_name}/entity/__init__.py",
  f"src/{project_name}/constant/__init__.py",
  "config/config.yaml",
  "dvc.yaml",
  "params.yaml",
  "requirment.txt",
  "setup.py",
  "reserch/trials.ipynb",
  "templates/index.html"
  
]


for filepath in file_list:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)
     
    if filedir !="":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"creatinf file directory;{(filedir)} for the file{filename}")

    if(not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w" ) as f:
            logging.info(f"creating a empty file{filepath}")
        
    else:
         logging.info(f"{filepath} alredy exists")