import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode("This is a text node", TextType.BOLD)
        node2 = HTMLNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
        
    
    def test_noteq(self):
        node3 = TextNode("This is a text node", TextType.BOLD)
        node4 = TextNode("This is not a text node", TextType.BOLD)
        self.assertNotEqual(node3, node4)

    def test_isNone(self):
        node5 = TextNode("This is not a text node", TextType.ITALIC)
        self.assertIsNone(node5.url)

    def test_isProperty(self):
        node6 = TextNode("this is?", TextType.ITALIC)
        self.assertIsInstance(node6.text_type, TextType)

if __name__ == "__main__":
    unittest.main()