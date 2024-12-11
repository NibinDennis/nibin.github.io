from django.shortcuts import render
import requests
# Create your views here.
def index(request):
    response=requests.get("https://jsonplaceholder.typicode.com/users")
    users=response.json()
    -- print(users)
    return render(request,"index.html",{'users':users})
from django.shortcuts import render
import requests
from django.http import JsonResponse 
class TreeNode:
    def __init__(self, key, value):
        self.left = None
        self.right = None
        self.key = key  # Country name
        self.value = value  # Country data (including flag)

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key, value):
        if self.root is None:
            self.root = TreeNode(key, value)
        else:
            self._insert(self.root, key, value)

    def _insert(self, node, key, value):
        if key < node.key:
            if node.left is None:
                node.left = TreeNode(key, value)
            else:
                self._insert(node.left, key, value)
        else:
            if node.right is None:
                node.right = TreeNode(key, value)
            else:
                self._insert(node.right, key, value)

    def search(self, key):
        return self._search(self.root, key)

    def _search(self, node, key):
        if node is None or node.key == key:
            return node
        if key < node.key:
            return self._search(node.left, key)
        else:
            return self._search(node.right, key)
    def get_suggestions(self, prefix):
        suggestions = []
        self._collect_suggestions(self.root, prefix, suggestions)
        return suggestions

    def _collect_suggestions(self, node, prefix, suggestions):
        if node is None:
            return
        if node.key.lower().startswith(prefix.lower()):  # Compare prefix to node key
            suggestions.append(node.key)
        self._collect_suggestions(node.left, prefix, suggestions)
        self._collect_suggestions(node.right, prefix, suggestions)

def load_countries():
    response = requests.get("https://restcountries.com/v3.1/all")
    countries = response.json()

    # Create a Binary Search Tree and insert country names
    bst = BinarySearchTree()
    for country in countries:
        country_name = country['name']['common']
        bst.insert(country_name, country)

    return bst

def country_suggestions(request):
    bst = load_countries()
    search_term = request.GET.get('term', '')

    if search_term:
        suggestions = bst.get_suggestions(search_term)  # Get country names starting with 'search_term'
        return JsonResponse(suggestions, safe=False)

    return JsonResponse([], safe=False)
# Create your views here.

def flag(request):
    response = requests.get("https://restcountries.com/v3.1/all")
    countries = response.json()
    print(countries)
    # Create the Binary Search Tree and insert all countries
    bst = BinarySearchTree()
    for country in countries:
        country_name = country['name']['common']
        bst.insert(country_name, country)

    search_query = request.GET.get('q', '')  # Get the search query from the request
    country_data = None

    if search_query:
        # Search for the country in the BST
        result = bst.search(search_query)
        if result:
            country_data = result.value  # Get the country data if found

    return render(request, "flagapi.html", {"user": [country_data] if country_data else countries, "query": search_query})
