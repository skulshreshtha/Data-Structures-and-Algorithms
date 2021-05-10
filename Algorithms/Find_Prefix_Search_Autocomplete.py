### Solution 1: Using Trie O(m) where m is the length of search string ###
import re
class Trie:
    
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = {}
        self.stop_character = '__s'
        
    def insert(self, bname: str) -> None:
        """
        Inserts a name into the trie.
        """
        bnames = self._parse_input(bname)
        for name in bnames:
            node = self.root
            for letter in name:
                node = node.setdefault(letter, {})
            node[self.stop_character] = True
        
    def search(self, word: str) -> bool:
        """
        Returns True if the word is in the trie.
        """
        node = self.root
        word = self._parse_input(word)[0]
        for letter in word:
            if letter not in node:
                return False
            node = node[letter]
        return node.get(self.stop_character, False)

    def listWords(self, node: dict) -> List[str]:
        """
        Return all words from current node
        """
        my_list = []
        if(node.get(self.stop_character,False)):
            my_list.append('')
            return my_list
        else:
            for k,v in node.items():
                for el in self.listWords(v):
                    my_list.append(k+el)
        
        return my_list           
            
    
    def startsWith(self, prefix: str) -> bool:
        """
        Returns all names starting with the given prefix.
        """
        node = self.root
        for letter in prefix:
            if letter not in node:
                return []
            node = node[letter]
        names = [prefix[0]+x for x in self.listWords(self.root[prefix[0]])]
        
        return self._fix_output(names)
    
    def _parse_input(self, name: str) -> List[str]:
    
        temp = []

        name = name.replace(" ","__w")
        name += "__e"

        temp.append(name)

        for pos in re.finditer("__w",name): 
            temp.append(name[pos.start()+3:] + name[:pos.start()+3])

        return temp

    def _fix_output(self, names: List[str]) -> List[str]:
        temp = set()
        for name in names:
            i = re.search("__e",name).end()
            if(i != len(name)):
                temp.add((name[i:] + name[:i-3]).replace("__w"," "))
            else:
                temp.add(name[:-3].replace("__w"," "))

        return list(temp)    

t = Trie()

t.insert("Papa Burgers")
t.insert("Burger's Johns")
t.insert("Pizza Italiana")

t.search("Papa Burgers")

t.startsWith("Bur")

### Solution 2: Brute Force O(n*m) M is length of name and n is number of businesses

businesses = ["Burger's Johns", "Papa Burgers", "Pizza Italiana"]

def search(businesses: List[str], term: str) -> List[str]:
    return [x for x in businesses if term in x]

search(businesses,"Bur")