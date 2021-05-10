class newSolution:
    
    def __init__(self):
        self.coun = Counter()
        self.d = {}
    
    def add_email(self, email: dict):
        from_,to,msg = email.values()
        # Only add if not in existing set of messages
        if (from_,msg) not in self.d.setdefault(to,set()):
            self.d[to].add((from_,msg))
            self.coun.update([to])
            
    def get_top_N(self, n: int) -> List[str]:
        return self.coun.most_common(n)