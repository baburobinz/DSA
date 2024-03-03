HashKeys = type({}.keys())
class HashTable:

    def __init__(self):
        self.MAX = 10
        self.TABLE = [None for i in range(self.MAX)]
        self.key = []

    def __repr__(self) -> str:
            return 'cust type'
    
    def get_hash_val(self,key):

        h=0

        for ch in key:

            h+=ord(ch)

        return h%10
    
    def __setitem__(self,key,val):

        h = self.get_hash_val(key)
        self.key.append(key)

        self.TABLE[h]=val


    def __getitem__(self,key):
        h = self.get_hash_val(key)
        return self.TABLE[h]
 
    def get_key(self):
        
        return self.key
    
    def __delitem__(self,key):
         
         h = self.get_hash_val(key)

         self.key.remove(key)

         self.TABLE[h]=None
    
    
    
    
    
    


obj = HashTable()
obj['may1']=100
obj['may2']=1000
obj['may3']=2000
print(obj.TABLE)

del obj['may2']

print(8%10)




