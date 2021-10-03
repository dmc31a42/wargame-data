import pandas as pd
import argparse
import types

parser = argparse.ArgumentParser(description="""
Parse an intermediate Wargame: Red Dragon data file into a finished product.
""")
parser.add_argument("path", help="A filepath to the folder containing XML dumps to be processed (e.g. "
                                 "C:\\Users\\Alex\\Desktop\\wargame-analysis\\raws).")
parser.add_argument("version", help="The version of Wargame: Red Dragon to be processed (e.g. 510049986). Should be a "
                                    "subfolder of the filepath above.")
parser.add_argument("wargame", help="Pass")

units = pd.read_csv(parser.parse_args().wargame + "/" + parser.parse_args().version + "/final_data.csv",
                        encoding="utf-8",
                        index_col=0)
df = pd.DataFrame(units)
def dfApplymap(v):
  if pd.isnull(v):
    return ""
  vType = type(v)
  if vType == float:
    if int(v) == v:
      return str(int(v))
    else:
      return str(v)
  elif vType == int:
    return str(int(v))
  elif vType == bool:
    if v == True:
      return "TRUE"
    else:
      return "FALSE"
  else:
    return str(v)

df = df.applymap(dfApplymap)
print(df)

df.to_json(parser.parse_args().wargame + "/" + parser.parse_args().version + '/final_data.json', orient="records")
