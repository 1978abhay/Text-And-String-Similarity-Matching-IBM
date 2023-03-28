import pandas as pd
import re
import math
import os

# To Use: 
# Move data files into folder called Data. Data should be contained within the same folder as dataGarbageRemover.py and regex.txt.
# Write all regexes into regex.txt.
# Run Program. Copies of the data files will be written to a folder called output, with all text patterns matching any regex 
# removed for all listed columns for that file. If a raw column is listed, then a non-raw column is added to the copy instead.
if __name__ == "__main__":
    fileColumns = (("Data//bbc_news_list_uk.json",("title","content","short_description")),
                   ("Data//cnbc_news_datase.csv",("title","short_description","description")),
                   ("Data//cnn_data copy.json",("title","short_description","content")),
                 ("Data//crypto_news_dataset.csv",("title","raw_content")),
                   ("Data//data_world_example.json",("title","content","news_sub_header")),
                   ("Data//huffpost_news_data.csv",("headline","description")))

    regexes = []
    with open("regex.txt", "r") as f:
        for regex in f:
            regexes.append(regex.strip("\n"))

    for file, columns in fileColumns:

        if file.endswith("json"):
            df = pd.read_json(file)
        elif file.endswith("csv"):
            df = pd.read_csv(file)
        else:
            raise ValueError("This file type is not supported")

        for column in columns:
                
            dfNewContent = list(df[column])

            for regex in regexes:

                for i in range(len(dfNewContent)):

                    # ie if not nan (nan = empty cell, type float)
                    if type(dfNewContent[i]) == str:
                        # removes text in cell that matches regex
                        dfNewContent[i] = re.sub(regex, '', dfNewContent[i])

            if "raw" in column:     # if operating on a raw col, assume no processed col exists; add the processed column
                newColumn = column.replace("raw","").strip("_")
                df[newColumn] = dfNewContent
            else:
                df[column] = df[column].replace(list(df[column]),dfNewContent)
                            #df[column].replace([1st old, 2nd old, ...], [1st new, 2nd new, ...])
                            # is the correct way to overwrite column with respective values

        # easier to be able to assume all files are json in future

        splitFile = file.split("//")
        splitFile[-1] = "clean_"+splitFile[-1].replace("csv","json")
        newFile = "output//"+"//".join(splitFile[1:])

        if not os.path.exists("output"):
            os.makedirs("output")
            
        df.to_json(newFile)
