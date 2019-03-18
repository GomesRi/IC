import os
import csv
import pandas as pd
from tabula import read_pdf

for i in range(0, 141):
    if i == 117:
        df117 = read_pdf("2008.pdf", pages=117, output_format="dataframe", java_options="-Dfile.encoding=UTF8", pandas_options={'header':None})
        df118 = read_pdf("2008.pdf", pages=118, output_format="dataframe", java_options="-Dfile.encoding=UTF8", pandas_options={'header':None})
        df119 = read_pdf("2008.pdf", pages=119, output_format="dataframe", java_options="-Dfile.encoding=UTF8", pandas_options={'header':None})
        df120 = read_pdf("2008.pdf", pages=120, output_format="dataframe", java_options="-Dfile.encoding=UTF8", pandas_options={'header':None})

        df119.at[0, 24] = 1

        df117.to_csv('DF117bad.csv')

        create_txt = open('DF117good.txt', "w")
        create_txt.close()

        csv_file = open('DF117bad.csv', "r")
        txt_file = open('DF117good.txt', "r+")

        [txt_file.write(" ".join(row) + '\n') for row in csv.reader(csv_file)]

        csv_file.close()

        filedata = txt_file.read()

        newdata = filedata.replace(" ", ";")

        txt_file.write(newdata)

        txt_file.close()

        lercol = []
        nomecol = []

        for i in range(1, 32):
            lercol.append(i)
            nomecol.append(i-1)

        df117fix = pd.read_csv('DF117good.txt', sep=" ", header=None, skiprows=[0, 1, 2], usecols=lercol, names=nomecol)

        frames = [df117fix, df118, df119, df120]
        result = pd.concat(frames)

        with pd.ExcelWriter('Apendice 2.xlsx') as writer:
            result.to_excel(writer)

        os.remove('DF117bad.csv')
        os.remove('DF117good.txt')

    if i == 121:
        df_table = read_pdf("2008.pdf", pages=121, output_format="dataframe", java_options="-Dfile.encoding=UTF8")

        df_aux = pd.DataFrame(df_table)

        df121_1 = pd.DataFrame(df_aux.loc[:, ['NR', 'SAÍDA', 'COD']])
        df121_2 = pd.DataFrame(df_aux.loc[:, ['NR.1', 'SAÍDA.1', 'COD.1']])

        df121_2.columns = ['NR', 'SAÍDA', 'COD']
        new_index = [x for x in range(df121_1.shape[0], 2*df121_1.shape[0])]
        df121_2.index = new_index

        df121 = [df121_1, df121_2]
        result = pd.concat(df121)

        with pd.ExcelWriter('Apendice 3.xlsx') as writer:
            result.to_excel(writer)
