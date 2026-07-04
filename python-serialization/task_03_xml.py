#!/usr/bin/env python3
import xml.etree.ElementTree as ET

def serialize_to_xml(dictionary, filename):
    """Serializes a Python dictionary into an XML file using a <data> root."""
    root = ET.Element("data")
    
    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)
        
    tree = ET.ElementTree(root)
    # Writing the tree to the specified filename
    tree.write(filename, encoding='utf-8')

def deserialize_from_xml(filename):
    """Parses the XML file and reconstructs the dictionary with string values."""
    try:
        tree = ET.parse(filename)
        root = tree.getroot()
        
        # Reconstruct the dictionary using the tag as key and text as value
        return {child.tag: child.text for child in root}
    except Exception:
        return None
