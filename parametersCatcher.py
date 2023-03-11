import lxml.etree as ET

tree = ET.parse('target.xml')
root = tree.getroot()

# finding the Product element
product = root.find('./Products/Product')
# creating array that will be filled with the tag parameter
parametersArray = []
# finding all the Value elements with AttributeID attribute/parameter
values = product.findall('./Values/Value[@AttributeID]')


def appendInParametersArray():
    for value in values:
        attr_id = value.get('AttributeID')
        parametersArray.append(attr_id)
    print(parametersArray)
    return parametersArray


appendInParametersArray()
