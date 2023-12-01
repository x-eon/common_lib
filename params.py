import os
from dataclasses import dataclass


@dataclass
class Params:   
    """parameters class"""
    work_dir: str = os.getcwd()
    #--- DB --- 
    nameDB: str = 'db_name.db'
    nameTab: str = 'name_tab' 
    #--- chart ---
    title: str = ''
    xlabel: str = 'X' 
    ylabel: str = 'Y'