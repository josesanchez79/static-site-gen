import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode("h1", "Title text", [], {"title": "some tag"})
        node2 = HTMLNode("h1", "Title text", [], {"title": "some tag"})
        self.assertEqual(node, node2)
        
    
    def test_noteq(self):
        node3 = HTMLNode("h1", "Title text", [], {"title": "some tag"})
        node4 = HTMLNode("a", "Title text", [], {"href": "www.google.com"})
        self.assertNotEqual(node3, node4)

    def test_isNone(self):
        node5 = HTMLNode("h1", "Title text",)
        self.assertIsNone(node5.props)
    

if __name__ == "__main__":
    unittest.main()