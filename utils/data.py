import os, pandas as pd
from pathlib import Path

def load_csv_files_to_df_dict(directory):
    return {
        os.path.splitext(file)[0]: pd.read_csv(os.path.join(directory, file))
        for file in os.listdir(directory) if file.endswith('.csv')
    }

def rename_keys_to_suffix(input_dict):
    # Replace keys of the form "a_b" with "b" in :input_dict:.
    return {key.split('_')[-1]: value for key, value in input_dict.items()}

def get_sp500_df():
    current_dir = Path(os.path.dirname(os.path.abspath(__file__)));
    data_dir = current_dir.parent.absolute();
    data_dir = os.path.join(data_dir,'data','sp500')
    df_dict = load_csv_files_to_df_dict(data_dir)
    df_dict = rename_keys_to_suffix(df_dict)
    return df_dict