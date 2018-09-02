import logging
import os


import nltk
from nltk.corpus import state_union
from nltk.tokenize import PunktSentenceTokenizer



def process_content():
    try:
        for i in tokenized[:5]:
            words = nltk.word_tokenize(i)
            tagged = nltk.pos_tag(words)
            print(tagged)

    except Exception as e:
        print(str(e))

#Reads and returns the list of files from a directory
def read_directory(mypath):
    current_list_of_files = []

    while True:
        for (_, _, filenames) in os.walk(mypath):
            current_list_of_files = filenames
        logging.info("Reading the directory for the list of file names")
        return current_list_of_files


# Function you will be working with
def create_knowledge_graph(contents_of_input_file, name_of_input_file):
    # Through this function you have to use the contents of each file to create a knowledge graph
    # The output has to be saved in the data/output folder with the same name as data/input file
    # Note the writing to file has to be handled by you.
    custom_sent_tokenizer = PunktSentenceTokenizer(contents_of_input_file)
    tokenized = custom_sent_tokenizer.tokenize(sample_text)
    contents_of_output_file=process_content()
    path=os.path.dirname(os.path.abspath(__file__))
    file = open(path+'/data/output/'+name_of_input_file,'w')
    file = contents_of_output_file
    file.close()




#Main function
if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, format='%(asctime)s:%(levelname)s:%(message)s')

    #Folder where the input files are present
    mypath = "data//input"
    list_of_input_files = read_directory(mypath)
    logging.debug(list_of_input_files)
    for each_file in list_of_input_files:
        with open(os.path.join(mypath,each_file), "r") as f:
            file_contents = f.read()

            create_knowledge_graph(file_contents, each_file)
            # end of code