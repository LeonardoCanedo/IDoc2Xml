from lxml import etree
import re
import targetDictionary as targetDictionary

data_dict = targetDictionary.targetWithPathDict

xslt_template = '''<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
  <xsl:template match="/">
    <xsl:apply-templates select="*" />
        <Values>
'''

# Closing tags
endingTags = '''  
  </Values>
  </xsl:template>
</xsl:stylesheet>
'''

pathsArray = []

for key, path_value in data_dict.items():
    currentAttributePath = '''
        <Value AttributeID="{currentKeyValue}">
          <xsl:value-of select="{currentPathValue}" />
        </Value>
        '''.format(currentKeyValue=key, currentPathValue=path_value)
    pathsArray.append(currentAttributePath)

for path in pathsArray:
    xslt_template = xslt_template + path

xslt_template = xslt_template + endingTags

# Load XML file
xml_file_path = 'source.xml'  # Replace with your XML file path
xml_tree = etree.parse(xml_file_path)

xslt_file_content = xslt_template.format()

# Save the XSLT file
with open('output.xslt', 'w') as f:
    f.write(xslt_file_content)

# Get XSLT file created
xslt_file = "output.xslt"

# Build up transformer for XML and XSLT
transformer = etree.XSLT(etree.parse(xslt_file))

# Apply the transformation to the XML
result = transformer(xml_tree)

# Get the transformed XML as a string
transformed_xml = str(result)

# Extract only the XML tags from the transformed XML string
tags_only = re.findall(r'<[^>]+>', transformed_xml)

# Join the tags to form the final output
tags_output = ''.join(tags_only)

# Tags Output returns the xml build from the xslt code
print("Tags Output" + tags_output)

values = re.findall(r'>(.*?)<', transformed_xml)
filtered_array = [value for value in values if value != '']
# Values returns all the values extracted from the xml
print(filtered_array)

# Current output based on source files:

# Tags Output:
# <?xml version="1.0"?>
# <name></name>
# <Values>
#   <Value AttributeID="AttributeID_1">John Doe</Value>
#   <Value AttributeID="AttributeID_2">12345</Value>
#   <Value AttributeID="AttributeID_3">ABC123</Value>
#   <Value AttributeID="AttributeID_4">2023-06-27</Value>
#   <Value AttributeID="AttributeID_5">Jane Smith</Value>
#   <Value AttributeID="AttributeID_6">Example Value</Value>
#   <Value AttributeID="AttributeID_7">Status</Value>
#   <Value AttributeID="AttributeID_8">Type</Value>
#   <Value AttributeID="AttributeID_9">Category</Value>
#   <Value AttributeID="AttributeID_10">Code</Value>
#   <Value AttributeID="AttributeID_11">98765</Value>
#   <Value AttributeID="AttributeID_12">Unit</Value>
#   <Value AttributeID="AttributeID_13">XYZ</Value>
# </Values>

# Values Output:
# values = [
#     'John Doe',
#     '12345',
#     'ABC123',
#     '2023-06-27',
#     'Jane Smith',
#     'Example Value',
#     'Status',
#     'Type',
#     'Category',
#     'Code',
#     '98765',
#     'Unit',
#     'XYZ'
# ]

# XSLT file named output.xslt

# Idoc2Xml - Leonardo Canedo
