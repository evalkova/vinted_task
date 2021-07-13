import logging
import re
import math

# logging.getLogger().setLevel(logging.INFO)


class Transformer(object):

    def __init__(self):
        pass

    def check_if_unique_id(self, df, id):
        try:
            isTransIdUnique = df[id].is_unique
            logging.info(id + " is Unique: " + str(isTransIdUnique) + '\n')
        except (KeyError, NameError, TypeError, AttributeError):
            logging.error('Could not perform check for the provided df '
                          'object and id ' + str(id) +'. Please provide different values')
            return
        return isTransIdUnique

    # The function needs to be improved to return booleans so it is more usable.
    def check_missing_values(self, df):
        try:
            values = df.isnull().sum()
            logging.info('Number of missing values for: ' + '\n' + str(values))
        except (KeyError, NameError, TypeError, AttributeError):
            logging.error('Could not perform check. Please provide a different value')

    def cleanup_description(self, entry):
    # Handle the check of if it is nan properly, not by only checking the type of parameter
        if not isinstance(entry, str):
            return 0
        else:
            # Regular expressions used to leave only the kg value
            foundEntries = re.findall(r"(([0-9]+|(0\.[0-9]+))\s*kg|Kg|KG)", entry)
            if(len(foundEntries) > 1 or not foundEntries) :
                return 0
            return re.sub('[a-zA-Z\\s]+','', foundEntries[0][0])
