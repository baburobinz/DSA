HashKeys = type({}.keys())
class HashTable:

    def __init__(self):
        self.MAX = 10
        self.TABLE = [[] for i in range(self.MAX)]
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
        found=False
        for idx,element in enumerate(self.TABLE[h]):
             if len(element)==2 and element[0]==key:
                  self.TABLE[h][idx]=(key,val)
                  found=True

        if not found:
             self.TABLE[h].append((key,val))

    def __getitem__(self,key):
        h = self.get_hash_val(key)

        
        
        for element in self.TABLE[h]:
             
             if element[0]==key:
                  
                return element[1]
             
        raise Exception('Key error..!')
                
 
    def get_key(self):
        
        return self.key
    
    def __delitem__(self,key):
         
        h = self.get_hash_val(key)

        found = False

        for idx,element in enumerate(self.TABLE[h]):
            
            if element[0]==key:
                del self.TABLE[h][idx]
                found=True
        
        if not found:
             
             raise Exception('Key error..!')


        
    
    
    
    
    


obj = HashTable()
obj['may1']=100
obj['may1']=1000
obj['may3']=2000
obj['march 6']=10
obj['march 17']=20


print(obj.TABLE)

del obj['march 17']

print(obj.TABLE)



l=[]

l.insert(0,1)
l.insert(0,2)
l.insert(0,3)

print(l)
