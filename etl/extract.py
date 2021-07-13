import pandas as pd
import numpy as np
import glob, os, json, logging

# logging.getLogger().setLevel(logging.INFO)


class Extractor(object):

    def __init__(self, datasources_config):
        self.datasources_config = datasources_config

    def load_json_files_to_df(self, type_of_data):

        open_datasources = json.load(open(self.datasources_config))
        path = open_datasources['data_sources']['folders_with_json_files'][type_of_data]
        #getting a list with the absolute JSON files
        json_pattern = os.path.join(path, '*.json')
        file_list = glob.glob(json_pattern)

        dfs = []
        for file in file_list:
            try:
                with open(file) as f:
                    json_data = pd.read_json(f, convert_dates=True, lines=True)
                    # json_data['original_file'] = file.rsplit("\\", 1)[-1] #can be added o trace which row is coming from each file - might help potential debigging
            except (PermissionError, IOError, ValueError):
                logging.error('The following files cound not be extracted into a dataframe: ' +
                              ','.join(file for file in file_list))
            dfs.append(json_data)
        df = pd.concat(dfs)

        # it would be best fot this basic transformation to be moved in a separate function
        # drop duplicated rows just in case
        df = df.drop_duplicates()
        # TODO: log how many were dropped
        df.replace('', np.nan, inplace=True)
        # TODO: log how many were replaced
        # print(df.head(10)) # Used for local testing
        return df

# TODO: function to add file to allow running metrics continuously

# Used for local testing
if __name__ == '__main__':
    datasources_config = 'config/data_source_config.json'
    extractor = Extractor(datasources_config)
    extractor.load_json_files_to_df("product_invoices")
