# A RouteTrie will store our routes and their associated handlers
# Note: 
# Well the problem seems to be a little variante version of the trie implementation seen before, however I still struggled a lot to fully understand the logic behind it.
# I've used most codes in both the course work and those in Problem 5, and looked through the test cases to find out what the instructions are actually requiring us to do.
# The problem is an updated version of the trie implementation, just changing the "character" of a word into "word" of a path seqarated by "/". Basically, "/home/project/problem" is similar to "w o r d" in the previous version. So we will still use basic trie implementation here, with several modifications according to the instructor's notes, i.e., to add a handler function, to remove the "is_word" or "wordsEnd" function.

class RouteTrie:
    def __init__(self, handler):
        # Initialize the trie with an root node and a handler, this is the root path or home page node
        self.root = RouteTrieNode(handler)
        
    def insert(self, path_segments, handler):
        # Similar to our previous example you will want to recursively add nodes
        # Make sure you assign the handler to only the leaf (deepest) node of this path
        current_node = self.root
        for segment in path_segments:
            if segment not in current_node.children:
                current_node.children[segment] = RouteTrieNode()
            current_node = current_node.children[segment]
        current_node.handler = handler
        
    def find(self, path_segments):
        # Starting at the root, navigate the Trie to find a match for this path
        # Return the handler for a match, or None for no match
        current_node = self.root
        for segment in path_segments:
            if segment in current_node.children:
                current_node = current_node.children[segment]
            else:
                return None
        return current_node.handler

# A RouteTrieNode will be similar to our autocomplete TrieNode... with one additional element, a handler.
class RouteTrieNode:
    def __init__(self, handler = None):
        # Initialize the node with children as before, plus a handler
        self.children = {}
        self.handler = handler
        
    def insert(self, segment):
        # Insert the node as before
        self.children[segment] = RouteTrieNode()

# The Router class will wrap the Trie and handle 
class Router:
    def __init__(self, routes, not_found_handler):
        # Create a new RouteTrie for holding our routes
        # You could also add a handler for 404 page not found responses as well!
        self.new_routeTrie = RouteTrie(routes)
        self.not_found_handler = not_found_handler
        
    def add_handler(self, path, handler):
        # Add a handler for a path
        # You will need to split the path and pass the pass parts
        # as a list to the RouteTrie
        path_segment = self.split_path(path)
        self.new_routeTrie.insert(path_segment, handler)    
        
    def lookup(self, path):
        # lookup path (by parts) and return the associated handler
        # you can return None if it's not found or
        # return the "not found" handler if you added one
        # bonus points if a path works with and without a trailing slash
        # e.g. /about and /about/ both return the /about handler
        if self.new_routeTrie.find(self.split_path(path)):
            return self.new_routeTrie.find(self.split_path(path))
        return self.not_found_handler

    def split_path(self, path):
        # you need to split the path into parts for 
        # both the add_handler and loopup functions,
        # so it should be placed in a function here
        return path.strip('/').split('/')

# Test case 1:
# Here are some test cases and expected outputs you can use to test your implementation

# create the router and add a route
router = Router("root handler", "not found handler") # remove the 'not found handler' if you did not implement this
router.add_handler("/", "root handler")  # add a route
router.add_handler("/home/about", "about handler")  # add a route

# some lookups with the expected output
print(router.lookup("/")) # should print 'root handler'
print(router.lookup("/home")) # should print 'not found handler' or None if you did not implement one
print(router.lookup("/home/about")) # should print 'about handler'
print(router.lookup("/home/about/")) # should print 'about handler' or None if you did not handle trailing slashes
print(router.lookup("/home/about/me")) # should print 'not found handler' or None if you did not implement one

# Test case 2:
router.add_handler("/org", "org. root handler")
router.add_handler("/org/cgi-bin", "cgi-bin handler")
router.add_handler("/org/cgi-bin/carddisp", "carddisp handler")
router.add_handler("/org/cgi-bin/genecard", "genecard handler")

print(router.lookup("/org"))
# 'org. root handler'
print(router.lookup("/org/cgi-bin"))
# 'cgi-bin handler'
print(router.lookup("/org/cgi-bin/carddisp"))
# 'carddisp handler'
print(router.lookup("/org/cgi-bin/genecard"))
# 'genecard handler'
print(router.lookup("/org/genecard"))
# 'not found handler'
print(router.lookup("/cgi-bin"))
# 'not found handler'

# Test case 3:
router.add_handler(".com/", ".com root handler")
router.add_handler(".com/project/", "project handler")
router.add_handler(".com/project", "project handler")
router.add_handler(".com/project/1", "1 handler")

print(router.lookup(".com/"))
# '.com root handler'
print(router.lookup(".com/project/"))
# 'project handler'
print(router.lookup(".com/project"))
# 'project handler'
print(router.lookup(".com/project/1"))
# '1 handler'
print(router.lookup(".com/project/2"))
# 'not found handler'

