import pandas as pd
# imports the file that creates the tag dictionary, tagsDict is the name of the dictionary that we'll use
import srcDictionary as srcDictionary
# creates DataFrame with source excel file
df = pd.read_excel('ExcelReferenciaSourceTarget.xlsx', engine='openpyxl')
# target column tags in an array
targetTags = df['Target'].dropna().values
# dictionary that will be filled with the targets tags and their paths based on the source tags/file
targetWithPathDict = {}


def appendTargetAndPathToDictionary():
    i = 0
    for path in srcDictionary.srcTagsDict.values():
        targetWithPathDict[targetTags[i]] = path
        i = i + 1
    # print(targetWithPathDict)
    return targetWithPathDict


appendTargetAndPathToDictionary()
