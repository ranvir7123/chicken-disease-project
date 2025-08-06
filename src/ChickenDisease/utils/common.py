import os
from box.exceptions import BoxValueError
import yaml
from src.ChickenDisease import logger  # Fixed import
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any
import base64

@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """Read YAML file and return ConfigBox object
    
    Args:
        path_to_yaml (Path): Path to YAML file
        
    Returns:
        ConfigBox: ConfigBox type
        
    Raises:
        ValueError: If YAML file is empty
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            if not content:
                raise BoxValueError("YAML file is empty")
            logger.info(f"YAML file loaded: {path_to_yaml}")
            return ConfigBox(content)
    except Exception as e:
        logger.error(f"Error loading YAML file: {e}")
        raise e

@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """Create list of directories
    
    Args:
        path_to_directories (list): List of directory paths
        verbose (bool): Whether to log creation (default: True)
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"Created directory: {path}")

@ensure_annotations
def save_json(path: Path, data: dict):
    """Save data to JSON file
    
    Args:
        path (Path): Path to JSON file
        data (dict): Data to save
    """
    with open(path, "w") as f:
        json.dump(data, f, indent=4)
    logger.info(f"JSON file saved: {path}")

@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    """Load JSON file
    
    Args:
        path (Path): Path to JSON file
        
    Returns:
        ConfigBox: Data as ConfigBox object
    """
    with open(path) as f:
        content = json.load(f)
    logger.info(f"JSON file loaded: {path}")
    return ConfigBox(content)

@ensure_annotations
def save_bin(data: Any, path: Path):
    """Save data as binary file
    
    Args:
        data (Any): Data to save
        path (Path): Path to binary file
    """
    joblib.dump(data, path)
    logger.info(f"Binary file saved: {path}")

@ensure_annotations
def load_bin(path: Path) -> Any:
    """Load binary file
    
    Args:
        path (Path): Path to binary file
        
    Returns:
        Any: Loaded data
    """
    data = joblib.load(path)
    logger.info(f"Binary file loaded: {path}")
    return data

@ensure_annotations
def get_size(path: Path) -> str:
    """Get file size in KB
    
    Args:
        path (Path): Path to file
        
    Returns:
        str: Size in KB
    """
    size_in_kb = round(os.path.getsize(path)/1024)
    return f"~ {size_in_kb} KB"

def decodeImage(imgstring: str, fileName: str) -> None:
    """Decode base64 image and save to file
    
    Args:
        imgstring (str): Base64 encoded image
        fileName (str): Output file path
    """
    imgdata = base64.b64decode(imgstring)
    with open(fileName, 'wb') as f:
        f.write(imgdata)

def encodeImageIntoBase64(croppedImagePath: str) -> bytes:
    """Encode image to base64
    
    Args:
        croppedImagePath (str): Path to image file
        
    Returns:
        bytes: Base64 encoded image
    """
    with open(croppedImagePath, "rb") as f:
        return base64.b64encode(f.read())