#!/usr/bin/env python3
import xml.etree.ElementTree as ET

def serialize_to_xml(dictionary, filename):
    """Serializes a Python dictionary into an XML file."""
    root = ET.Element("data")
    
    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)
        
    tree = ET.ElementTree(root)
    tree.write(filename, encoding='utf-8', xml_declaration=True)

def deserialize_from_xml(filename):
    """Parses an XML file and reconstructs the Python dictionary."""
    try:
        tree = ET.parse(filename)
        root = tree.getroot()
        
        result_dict = {}
        for child in root:
            val = child.text
            # Attempt basic type conversions for numbers/booleans
            if val == "True":
                result_dict[child.tag] = True
            elif val == "False":
                result_dict[child.tag] = False
            else:
                try:
                    if '.' in val:
                        result_dict[child.tag] = float(val)
                    else:
                        result_dict[child.tag] = int(val)
                except (ValueError, TypeError):
                    result_dict[child.tag] = val
                    
        return result_dict
    except Exception:
        return None
