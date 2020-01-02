import re
import string

class ModelUtil:
    """
    The main objective of this class is to preprocess the textual document into a numerical format
    """

    def __init__(self):
        
        self.total_char = string.printable
        self.int2char = dict(enumerate(self.total_char))
        self.char2int = {ch:idx for idx,ch in self.int2char.items()}


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

    def encode_text(self,data_list):
        """This function encode character into a numerical value
            
                Arguments:
                     {list} -- list of padded character sequence 
                Returns:
                    list --  list of encoded value
                """
        
        encoded_data=[]
        for item in data_list:
            encoded_data.append([self.char2int[char] for char in item])

        return encoded_data


    


#---------------------------Test Case--------------------------------------
# utils = ModelUtil()
# data = "hjgsjslfjklsajfsdfaskjhd sdfhkjhklj"
# print(data)
# processed_data = utils.preprocessing_text(data) 
# print(processed_data)
# processed_data = list(processed_data)
# print(processed_data)
# encoded_data = utils.encode_text(list(processed_data))
# print(encoded_data)

