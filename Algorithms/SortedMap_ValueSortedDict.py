emails = [{'from':"user1",'to':'user2','message':'abcd'}
         ,{'from':"user3",'to':'user2','message':'lalala'}
         ,{'from':"user2",'to':'user1','message':'kuch bhi'}
         ,{'from':"user2",'to':'user1','message':'kuch bhi'}
         ,{'from':"user3",'to':'user1','message':'abcd'}
         ,{'from':"user4",'to':'user1','message':'naya mail'}]

###### Expected Output #########
# get_top_N(1)
# ['user1']
# get_top_N(2)
# ['user1', 'user2']

"""
Every user will have its own dictionary, having num_msg (number of messages receieved), set of messages(from, content).
And we will maintain a Sorted Map to have the users sorted by num_msg at all times.
"""
from sortedcollections import ValueSortedDict
from typing import List
class Solution:
    
    def extract_key(self, user: dict) -> int:
        return user["num_msg"]
    
    def __init__(self):
        self._d = ValueSortedDict(self.extract_key)
        
    def add_email(self, email: dict):
        """
        Add the new email to our data.
        """
        from_, to, msg = email.values()
        if to not in self._d:
            # Create new entry in dict
            self._d[to] = {'num_msg':-1, 'messages':{(from_,msg)}}
#             print(self._d[to]['num_msg'])
#             print(self._d[to]['messages'])
        else:
            # Update if receiver exists in dict
            if (from_,msg) not in self._d[to]["messages"]:
                num_msg, messages = self._d[to].values()
                num_msg -= 1
                messages.add((from_,msg))
                self._d[to] = {"num_msg":num_msg, "messages":messages}
#             print(self._d[to]['num_msg'])
#             print(self._d[to]['messages'])
    
    def get_top_N(self, n: int) -> List[str]:
        """
        Return the top N users by number of emails received
        """
        temp = []
        
        for key,val in self._d.items():
#             print(key,"=>",val)
            if(n==0):
                break
            temp.append(key)
            n -= 1
        return temp

s = Solution()
for em in emails:
    s.add_email(em)

s.get_top_N(2)