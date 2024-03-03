class Graph:
    def __init__(self,edges):
        self.edges = edges
        self.edges_dict = {}

        for start,end in self.edges:

            if start not in self.edges_dict:
                self.edges_dict[start]=[end]

            else:
                self.edges_dict[start].append(end)

    def get_paths(self,start,end,path=[]):

        path=path+[start]

        if start == end:
            return [path]
        if start not in self.edges_dict:
            return []      
        paths = []
        
        for node in self.edges_dict[start]:
            if node not in path:
                new_path = self.get_paths(node,end,path)
                for p in new_path:
                    paths.append(p)

        return paths

    
    def get_shortest_path(self,start,end,path=[]):

        path=path+[start]

        if start==end:
            return path
        if start not in self.edges_dict:
            return None
        
        shortest_path = None

        for node in self.edges_dict[start]:

            if node not in path:

                sp = self.get_shortest_path(node,end,path)

                if sp:
                    if shortest_path is None or len(sp)<shortest_path:
                        shortest_path=sp

        return shortest_path


        

if __name__=='__main__':
      routes = [
        ("Mumbai","Pune"),
        ("Mumbai", "Surat"),
        ("Surat", "Bangaluru"),
        ("Pune","Hyderabad"),
        ("Pune","Mysuru"),
        ("Hyderabad","Bangaluru"),
        ("Hyderabad", "Chennai"),
        ("Mysuru", "Bangaluru"),
        ("Chennai", "Bangaluru")
    ]
      
      graph = Graph(routes)

      start = "Mumbai"
      end = "Bangaluru"

      paths = graph.get_paths(start,end)

      print(paths)

      

