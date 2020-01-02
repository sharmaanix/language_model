import re

class ModelUtil:
    """
    The main objective of this class is to preprocess the textual document into a numerical format
    """

    def __init__(self):
        pass

    def preprocessing_text(self,raw_text):
        """This function remove numerals, convert it into lowercase and remove multiple spaces
            
                Arguments:
                    raw_text {str} -- text 
                Returns:
                    str --  processed text
                """
    
        # remove numerals
        temp_text = re.sub(r'[0-9]+','', raw_text)

        # convert to lower_case
        temp_text = "".join(list(map(lambda x : x.lower(), temp_text)))

        # remove multiple spaces
        return re.sub(' +', ' ', temp_text)


#---------------------------Test Case--------------------------------------
# utils = ModelUtil()
# data ="HJGSJslfjklsajf56sdfaskjhd              sdfhkjHKLJ"
# print(data)
# print(utils.preprocessing_text(data))
