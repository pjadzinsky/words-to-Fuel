"""
Write a module to convert all the words in 'folder' to mfcc features and then
store those mfcc features in a 'fuel' document.

At the end of the day I'd like to be able to say things like: 
    give me all instances of level 'numbers' in French
    give me all instances of words 'cero' and 'cat' in English and French

Therefore each sample will be associated with two features: 'Language' and 'word'

I'm assuming that all words in 'folder' are named like word_#.ext, for example:
    cero_0.wav, cero_1.wav, ..., cero_123.wav, two_0,.wav, ..., cat_0.wav, cat_1.wav, ...

"""
import sys
import os
import os.path
import re
import features
import pdb

if __name__=='__main__':
    '''
    This is what runs when when from bash user types:
        python Speech_Classificaiton/words_to_fuel.py Speech_classification/Spanish_Numbers

    Just loop through all the files in the given folder, converting each one to mfcc and
    storing the mfcc into the hdf5
    '''

    # make sure folder exists
    folder = sys.argv[1]
    
    if not os.path.isdir(folder):
        raise ValueError("Folder '{folder}' does not exist".format(folder=folder))
    print('processing files in {folder}'.format(folder=folder))

    # create a re object to parse word name from number ('uno_0', 'red_23')
    word_number_re = re.compile(r'(?P<word>.*)_(?P<number>[\d]*)')

    # in the loop, I'll only process files with the following extensions
    possible_extenssions = ['wav', 'mp3']

    pdb.set_trace()
    # start looping through every file in the given folder
    for f in os.listdir(folder):
        try:
            # all file names have only 1 '.' separating basename from file extension
            basename_ext = f.split('.')

            basename = basename_ext[0]
            ext = basename_ext[1]

            if ext in possible_extenssions:
                # word and num will be used as features of the mfcc in fuel
                tokens = word_number_re.split(basename)
                word = tokens[1]
                num = tokens[2]
                print("processing word: {word}, instance: {num}".format(word=word, num=num))

                path_to_file = os.path.join(folder, f)
                mfcc = features.mfcc(path_to_file)

        except:
            print('Skipping file: {file}\n something went wrong when processing it'.format(
                file=basename))

        #[f_name, f_ext] = f.split('.')
        #print(f_name, f_ext)
