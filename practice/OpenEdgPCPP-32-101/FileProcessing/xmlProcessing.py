import xml.etree.ElementTree

# Available modules in xml library: xml.etree.ElementTree, xml.dom, xml.dom.minidom, xml.dom.pulldom, xml.sax,
# xml.parsers.expat.

## XML format:
# - prolog: optional, specify version and character encoding: <?xml version = "1.0" encoding = "utf-8"?>.
# - Doctype: optional, specify document name, and Metadocument DTD <!DOCTYPE <xml_documenr_name> <SYSTEM|PUBLIC> "<dtd_uri>">.
# - root element: must have one and only one. contains all other elements.
# - elements: opening/closing tags. Contain text, attributes, children.
# - attributes: placed in element tag.

## Parsing.
# From a string: xml.etree.ElementTree.fromstring. Directly get the root element.
rootString = xml.etree.ElementTree.fromstring(
    '<?xml version="1.0"?>\
    <root>\
        <book title="Le corsaire de la république">\
            <author>Bod Denard</author>\
            <isbn>0123456789</isbn>\
        </book>\
        <book title="Viva">\
            <author>Patrick Deville</author>\
            <isbn>9876543210</isbn>\
        </book>\
    </root>'
)

# Simple access.
print(rootString.tag)  # root.
print(rootString[0][0].text)  # Bod Denard.
print(rootString[0].attrib['title'])  # Le corsaire de la république.
print(rootString[0].get('title'))  # Le corsaire de la république.

# iter(<tag>): search direct/nested children by tag.
for author in rootString.iter('author'):
    print(author.text)

print('##############################')

# From a file: xml.etree.ElementTree.parse: load the file, getroot(): get root element.
cars_for_sale = xml.etree.ElementTree.parse('cars.xml').getroot()
print(cars_for_sale.tag)

# element.findall(<tag_name>): Find all children where tag is <tag_name>.
for car in cars_for_sale.findall('car'):
    print('\t', car.tag)
    for element in car:
        # element.tag: child element tag.
        print('\t\t', element.tag, end='')
        #
        if element.tag == 'price':
            # element.attrib: dictionary of child element attributes.
            print(element.attrib, end='')

        # element.text: child element content.
        print(' =', element.text)

# xml.etree.ElementTree.dump(<element>): dump element.
xml.etree.ElementTree.dump(cars_for_sale)
print('##############################')


## Updating.
tree = xml.etree.ElementTree.parse('cars.xml')
cars_for_sale = tree.getroot()

for car in cars_for_sale.findall('car'):
    # Find the car element tag = 'brand' and text = 'Ford' and... (find => returns one element).
    if car.find('brand').text == 'Ford' and car.find('model').text == 'Mustang':
        # Remove: delete the element.
        cars_for_sale.remove(car)
    else:
        # set an element attribute.
        car.set('attributeKey', 'attributeValue')


# xml.etree.ElementTree.Element: create a new element.
new_car = xml.etree.ElementTree.Element('car')
# xml.etree.ElementTree.SubElement(<parentElement>, <tag>, <attribs>): add a sub element to an element.
xml.etree.ElementTree.SubElement(new_car, 'id').text = '4'
xml.etree.ElementTree.SubElement(new_car, 'brand').text = 'Maserati'
xml.etree.ElementTree.SubElement(new_car, 'model').text = 'Mexico'
xml.etree.ElementTree.SubElement(new_car, 'production_year').text = '1970'
xml.etree.ElementTree.SubElement(new_car, 'price', {'currency': 'EUR'}).text = '61800'
# <element>.append(<newElement>): add the new element to an element.
cars_for_sale.append(new_car)

# tree.write: write an xml file.
tree.write('newcars.xml', 'UTF-8', True)


## XPath.
tree = xml.etree.ElementTree.parse('universities.xml')
root = tree.getroot()
results = tree.find('.//university')

print(results)