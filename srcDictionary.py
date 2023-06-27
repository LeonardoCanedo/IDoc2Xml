import pandas as pd
import lxml.etree as ET
# creates DataFrame with source excel file
df = pd.read_excel('ExcelReferenciaSourceTarget.xlsx', engine='openpyxl')
# parse the XML file
tree = ET.parse('source.xml')
# get the root element
root = tree.getroot()
# get all source tags excluding any empty cells or cells with missing data,
# tags are put in an array based on the column
sourceTags = df['Source'].dropna().values
# Dictonary that will be filled with all the tags and their paths
srcTagsDict = {}


def findElementsByTag(tag):
    # find the element with the specific TAG
    tag_to_find = tag
    for element in root.findall('.//' + tag_to_find):
        # we can print element properties by using element.tag, element.attrib, element.text
        return element
        # currently returning only one tag, even if there are more of the same in the document


def findElementPath(element):
    elementPath = ''
    # gets all element's ancestors as a etree element object
    elementAncestors = element.xpath('ancestor::*')
    # concatenates each ancestor's tag to the path variable and creates path
    for ancestor in elementAncestors:
        elementPath += ancestor.tag + '/'
    elementPath += element.tag
    return elementPath


def appendTagsInDictonary(sourceTags):
    # gets all the path for all the tags in the array and appends it in the dictonary
    # e.g tagsDict = {tag: tagPath}
    for tag in sourceTags:
        tagPath = findElementPath(findElementsByTag(tag))
        srcTagsDict[tag] = tagPath
    return srcTagsDict


appendTagsInDictonary(sourceTags)


# current output based on example source file:
# {'MAKTX': 'ZCFLA_MAT/IDOC/E1MARAM/E1MAKTM/MAKTX',
#  'MSGFN': 'ZCFLA_MAT/IDOC/E1MARAM/MSGFN',
#  'MATNR': 'ZCFLA_MAT/IDOC/E1MARAM/MATNR',
#  'ERSDA': 'ZCFLA_MAT/IDOC/E1MARAM/ERSDA',
#  'ERNAM': 'ZCFLA_MAT/IDOC/E1MARAM/ERNAM',
#  'AENAM': 'ZCFLA_MAT/IDOC/E1MARAM/AENAM',
#  'PSTAT': 'ZCFLA_MAT/IDOC/E1MARAM/PSTAT',
#  'MTART': 'ZCFLA_MAT/IDOC/E1MARAM/MTART',
#  'MBRSH': 'ZCFLA_MAT/IDOC/E1MARAM/MBRSH',
#  'MATKL': 'ZCFLA_MAT/IDOC/E1MARAM/MATKL',
#  'BISMT': 'ZCFLA_MAT/IDOC/E1MARAM/BISMT',
#  'MEINS': 'ZCFLA_MAT/IDOC/E1MARAM/MEINS',
#  'BLANZ': 'ZCFLA_MAT/IDOC/E1MARAM/BLANZ'}
