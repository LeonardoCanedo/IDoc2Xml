import pandas as pd
import lxml.etree as ET
# imports the file that creates the tag dictionary, tagsDict is the name of the dictionary that we'll use
import srcDictionary as srcDictionary
# creates DataFrame with source excel file
df = pd.read_excel('ExcelReferenciaSourceTarget.xlsx', engine='openpyxl')
# parse the XML file
tree = ET.parse('source.xml')
# get the root element
root = tree.getroot()
# target column tags in an array
targetTags = df['Target'].dropna().values
# dictionary that will be filled with the targets tags and their paths based on the source tags/file
targetWithPathDict = {}

# getting the xsl commands on variables, they must be concatenated with the 
xslValueOf = '<xsl:value-of select="' 
xslForEach = '<xsl:for-each select="'
# use case: xslValueOf+srcDictionary.tagsDict[tag/key]+'">'

def valueOfConstructorTag(key):
    tag = xslValueOf+srcDictionary.srcTagsDict[key]+'">'
    return tag


def appendTargetAndPathToDictionary():
    i = 0
    for path in srcDictionary.srcTagsDict.values():
        targetWithPathDict[targetTags[i]] = path
        i = i + 1
    print(targetWithPathDict)
    return targetWithPathDict


appendTargetAndPathToDictionary()

# current output based on example files:
#   {'Name': 'ZCFLA_MAT/IDOC/E1MARAM/E1MAKTM/MAKTX',
#    'PRICAT13825': 'ZCFLA_MAT/IDOC/E1MARAM/MSGFN',
#    'PRICAT13762': 'ZCFLA_MAT/IDOC/E1MARAM/MATNR',
#    'INNOVACION13572': 'ZCFLA_MAT/IDOC/E1MARAM/ERSDA',
#    'PUM13832': 'ZCFLA_MAT/IDOC/E1MARAM/ERNAM',
#    'NOVAVENTA_ATRIBUTO13700': 'ZCFLA_MAT/IDOC/E1MARAM/AENAM',
#    'PRICAT13729': 'ZCFLA_MAT/IDOC/E1MARAM/PSTAT',
#    'INNOVACION13612': 'ZCFLA_MAT/IDOC/E1MARAM/MTART',
#    'INNOVACION13575': 'ZCFLA_MAT/IDOC/E1MARAM/MBRSH',
#    'INNOVACION13573': 'ZCFLA_MAT/IDOC/E1MARAM/MATKL',
#    'PUM13831': 'ZCFLA_MAT/IDOC/E1MARAM/BISMT',
#    'INNOVACION13571': 'ZCFLA_MAT/IDOC/E1MARAM/MEINS',
#    'ATRIBLEGALESPERU13597': 'ZCFLA_MAT/IDOC/E1MARAM/BLANZ'}



