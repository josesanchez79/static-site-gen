import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode



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
    
    def test_leaf_to_html_p(self):
        node6 = LeafNode("p", "Hello, world!")
        self.assertEqual(node6.to_html(), "<p>Hello, world!</p>")
    
    def test_leaf_to_html_a(self):
        node7 = LeafNode("a", "click me", {"href": "https://www.google.com"})
        self.assertEqual(node7.to_html(), "<a href=\"https://www.google.com\">click me</a>")

    def test_leaf_to_html_h1(self):
        node7 = LeafNode("h1", "THIS IS MY LAST WAR")
        self.assertEqual(node7.to_html(), "<h1>THIS IS MY LAST WAR</h1>")
    
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_multiple_children(self):
        child1 = LeafNode("b", "bold text")
        child2 = LeafNode(None, "plain text")
        parent = ParentNode("div", [child1, child2])
        self.assertEqual(parent.to_html(), "<div><b>bold text</b>plain text</div>")

    

if __name__ == "__main__":
    unittest.main()