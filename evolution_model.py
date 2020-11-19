
import numpy as np
import matplotlib.pyplot as plt
class species():
    def __init__(self):
        self.survival=True
        self.entropy=0
        self.compete=1
        self.potential=0
        self.strag=''
        self.trace=[]
    def set_strag(self):
        p=np.random.rand()
        if p<=0.5:
            self.strag='P'
        else:
            self.strag='C'
        self.trace.append(self.strag)

        
    def get_resource(self,resource,total):
         return (self.compete/total)*resource
    def allocate_resource(self,reward):
        if self.strag=='P':
            self.potential+=0.8*reward
            self.compete+=0.2*reward
        else:
            self.potential+=0.2*reward
            self.compete+=0.8*reward
        self.entropy+=2*self.compete+0.5*self.potential
    def execute(self,threshold):
        if self.entropy>=threshold:
            self.survival=False
#evolution
environment_entropy=0
environment_load=50000
species_list=[species() for i in range(1000)]
resource=2000
while(environment_entropy<=environment_load):
        total=np.array([i.compete for i in species_list]).sum()
        for each_spec in species_list:
            each_spec.set_strag()
            reward=each_spec.get_resource(resource,total)
            each_spec.allocate_resource(reward)
            each_spec.execute(environment_load*0.01)
        environment_entropy=np.array([i.entropy for i in species_list]).sum()
        species_list=[i for i in species_list if i.survival==True]
potential_list=[i.potential for i in species_list]
potential_list.sort()
potential_threshold=potential_list[int(len(potential_list)*0.75)]
compete_list=[i.compete for i in species_list]
compete_list.sort()
compete_threshold=compete_list[int(len(compete_list)*0.75)]
select=[i for i in species_list if (i.compete>=compete_threshold)&(i.potential>=potential_threshold)]
c_matrix=np.array([[0 if j=='P' else 1 for j in i.trace] for i in select])
p_matrix=np.array([[1 if j=='P' else 0 for j in i.trace] for i in select])
plt.figure(figsize=(6,4))
plt.bar(np.arange(6),c_matrix.sum(axis=0))
plt.xticks(np.arange(6),np.arange(1,7))
plt.title('compete in all iterations')
plt.savefig('F:/friends/c.png')
plt.clf()
plt.figure(figsize=(6,4))
plt.bar(np.arange(6),p_matrix.sum(axis=0))
plt.xticks(np.arange(6),np.arange(1,7))
plt.title('potential in all iterations')
plt.savefig('F:/friends/p.png')
plt.clf()