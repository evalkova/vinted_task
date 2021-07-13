import pandas as pd
import numpy as np
import glob, os, json, logging
from IPython.display import display

logging.getLogger().setLevel(logging.INFO)


class Extractor(object):

    def __init__(self, data_sources):
        self.data_sources = data_sources

    def load_json_files_to_df(self, path):

        #getting a list with the absolute JSON files
        json_pattern = os.path.join(path, '*.json')
        file_list = glob.glob(json_pattern)

        dfs = []
        for file in file_list:
            try:
                with open(file) as f:
                    json_data = pd.read_json(f, convert_dates=True, lines=True)
                    # json_data['original_file'] = file.rsplit("\\", 1)[-1] #to trace which row is coming from each file - might help potential debigging
            except (PermissionError, IOError, ValueError):
                logging.error('The following files cound not be extracted into a dataframe: ' +
                              ','.join(file for file in file_list))
            dfs.append(json_data)
        df = pd.concat(dfs) #ValueError: No objects to concatenate
        # drop duplicated rows just in case
        df = df.drop_duplicates()
        df.replace('', np.nan, inplace=True)
        # print(df.head(10))
        return df

# function to add file to allow running metrics continuously

if __name__ == '__main__':
    datasources = json.load(open('config/data_source_config.json'))
    path = '../data/product_package_types/'
    extractor = Extractor(datasources)
    extractor.load_json_files_to_df(path)
