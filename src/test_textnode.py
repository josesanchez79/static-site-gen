import unittest

from textnode import TextNode, TextType, text_node_to_html_node


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
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
    
    def test_text_normal(self):
        node = TextNode("This is a text node", TextType.NORMAL)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")
    
    def test_text_bold(self):
        node = TextNode("This is a text node", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is a text node")
    
    def test_text_italic(self):
        node = TextNode("This is a text node", TextType.ITALIC)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "i")
        self.assertEqual(html_node.value, "This is a text node")

    def test_text_code(self):
        node = TextNode("This is a text node", TextType.CODE)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "code")
        self.assertEqual(html_node.value, "This is a text node")

    def test_text_link(self):
        node = TextNode("This is a text node", TextType.LINK, "https://www.google.com")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "This is a text node")
        self.assertEqual(html_node.props, {"href": "https://www.google.com"})

    def test_text_image(self):
        node = TextNode("This is a text node", TextType.IMAGE, "https://www.giantbomb.com/imageepoch/3010-6329/developed/")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(html_node.props, {"src": "https://www.giantbomb.com/imageepoch/3010-6329/developed/", "alt": "This is a text node"})

if __name__ == "__main__":
    unittest.main()