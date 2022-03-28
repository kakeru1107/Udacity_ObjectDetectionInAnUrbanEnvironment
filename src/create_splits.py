import argparse
import glob
import os
import random

import numpy as np

from utils import get_module_logger
import shutil


def split(data_dir):
    """
    Create three splits from the processed records. The files should be moved to new folders in the 
    same directory. This folder should be named train, val and test.

    args:
        - data_dir [str]: data directory, /home/workspace/data/waymo
    """
    
    # TODO: Split the data present in `/home/workspace/data/waymo/training_and_validation` into train and val sets.
    # You should move the files rather than copy because of space limitations in the workspace.
    file_paths=glob.glob(os.path.join(data_dir,"training_and_validation/*.tfrecord"))
    np.random.shuffle(file_paths)
    for _dir in ["train","val","test"]:
        dir_path=os.path.join(data_dir,_dir)
        os.makedirs(dir_path,exist_ok=True)
        
    # split out the training part, 0.8
    start=0
    end=start + int(0.8*len( file_paths))
    for file in file_paths[start:end]:
        dir_path=os.path.join(data_dir,"train")
        dest_path=os.path.join(dir_path,os.path.basename(file))
        shutil.move(file,dest_path)
        
    # split out the eval part, 0.1
    start=end
    end=start + int(0.1*len(file_paths))
    for file in file_paths[start:end]:
        dir_path=os.path.join(data_dir,"val")
        dest_path=os.path.join(dir_path,os.path.basename(file))
        shutil.move(file,dest_path)
        
    # split out the final part for testing
    for file in file_paths[end:]:
        dir_path=os.path.join(data_dir,"test")
        dest_path=os.path.join(dir_path,os.path.basename(file))
        shutil.move(file,dest_path)
    return 

if __name__ == "__main__": 
    parser = argparse.ArgumentParser(description='Split data into training / validation / testing')
    parser.add_argument('--data_dir', required=True,
                        help='data directory')
    args = parser.parse_args()

    logger = get_module_logger(__name__)
    logger.info('Creating splits...')
    split(args.data_dir)