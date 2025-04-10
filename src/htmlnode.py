class HTMLNode():
    def __init__(self, tag = None, value = None, children = None, props = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def to_html(self):
        raise NotImplementedError()
    
    def props_to_html(self):
        if self.props is None:
            return ""
        
        prop_string = ""
        for prop in self.props:
            value = self.props[prop]
            prop_string += f' {prop}="{value}"'
        return prop_string
    
    def __eq__(self, other):
    # Check if other is an HTMLNode and has the same attributes
        return (isinstance(other, HTMLNode) and self.tag == other.tag and self.value == other.value and self.children == other.children and self.props == other.props)

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"
    
class LeafNode(HTMLNode):
    def __init__(self, tag, value, props = None):
        super().__init__(tag, value, [], props)
    
    def to_html(self):
        if self.value is None:
            raise ValueError("LeafNode must have a value")
        if self.tag == None:
            return self.value
        else:
            props_str = ""
            if self.props:
                for prop_name, prop_value in self.props.items():
                    props_str += f' {prop_name}="{prop_value}"'
            return f"<{self.tag}{props_str}>{self.value}</{self.tag}>"
    


        
class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        self.tag = tag
        self.children = children  # Explicit assignment
        self.props = props

    def to_html(self):
        if self.tag is None:
            raise ValueError("ParentNode must have a tag")
        if self.children is None:
            raise ValueError("ParentNode must have children")
        props_str = ""
        if self.props:
            for prop_name, prop_value in self.props.items():
                props_str += f' {prop_name}="{prop_value}"'

        complete = ""
        for child in self.children:
            complete += child.to_html()

        return f"<{self.tag}{props_str}>{complete}</{self.tag}>"