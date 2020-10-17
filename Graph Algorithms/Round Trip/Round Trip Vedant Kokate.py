import time
import bisect
import math
import sys
import random as r
from collections import defaultdict 
from heapq import heapify, heappush, heappop 
def get_ints(): return map(int, sys.stdin.readline().strip().split())
def inp_int(): return int(sys.stdin.readline().strip())
def inp_str(): return(sys.stdin.readline().strip())
def out(output): sys.stdout.write(str(output))
def get_strs(): return  sys.stdin.readline().strip().split()
sys.setrecursionlimit(10**6)
 
 
 
from collections import defaultdict 
 
class Graph: 
 
	def __init__(self,vertices): 
		self.V= vertices
		self.graph = defaultdict(list)
 
 
	# function to add an edge to graph 
	def addEdge(self,v,w): 
		self.graph[v].append(w)
		self.graph[w].append(v) 
	def isCyclicUtil(self,v,visited,parent,ans):
		ans+=str(v+1)+" "
		
		visited[v]= True
 
		#Recur for all the vertices adjacent to this vertex 
		for i in self.graph[v]: 
			# If the node is not visited then recurse on it 
			if visited[i]==False : 
				if(self.isCyclicUtil(i,visited,v,ans)):
                                    
					return True
 
			elif parent!=i:
                            
				Ans=ans.split()
				#print(Ans,i)
				for j in range(len(Ans)):
					if Ans[j]==str(i+1):
						break
				
				Ans=Ans[j:]
                                
				Ans.append(i+1)
				print(len(Ans))
				for i in Ans:print(i,end=" ")
				
				return True
		
		return False
		
 
	def isCyclic(self): 
 
		visited =[False]*(self.V) 
		# Call the recursive helper function to detect cycle in different 
		#DFS trees 
		for i in range(self.V): 
			if visited[i] ==False: #Don't recur for u if it is already visited 
				if(self.isCyclicUtil(i,visited,-1,""))== True: 
					return True
		
		return False
 
 
 
 
 
#This code is contributed by Neelam Yadav 
 
n,m=get_ints()
g=Graph(n)
Ans=[]
for i in range(m):
    a,b=get_ints()
    g.addEdge(b-1, a-1)
 
    
if not g.isCyclic():
    print("IMPOSSIBLE")
