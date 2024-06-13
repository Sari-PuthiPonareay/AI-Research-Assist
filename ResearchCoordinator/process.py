import os
import pandas as pd


def process(src, dest):

    all_files = os.listdir(src)
    df = {"filename": []}
    for file in all_files: 
        df["filename"].append(file)
    
    pd.DataFrame(df).to_csv(dest + "photo.csv")




if __name__ == '__main__': 
    src = os.path.join(os.getcwd() + "/Photos")
    dest = ""
    print(os.getcwd())
    process(src, dest)