#Script to launch generation sign and verification on gcp
## The start index is give by  the second computer
###


import subprocess,sys
import multiprocessing
import multiprocessing as mp

NB_CPUS=mp.cpu_count()
TASK_PER_CPU=8 ##TASK PER CPU




##Start is used to parallelized processing
START=0
if len (sys.argv)>1:
    START = int(sys.argv[1])




def task(t,n,message_size,id):
    subprocess.call(["python3","gen_sign_verif_gcp.py",str(t),str(n), str(message_size),str(id + 1)])

MESSAGE_SIZES=[64,128]
N_VALUES=[5,10,15,50,100,500]
THRESHOLD_VALUES=[0.3,0.4,0.5,0.7,0.8,0.9]


for message_size in MESSAGE_SIZES:
    for n in N_VALUES:
        t_values= list(set( map(lambda ts:int(n*ts)+1,THRESHOLD_VALUES )) )## Unique corresponding t_values
        def f(t):
            return task(t,n,message_size,id)
        pool = mp.Pool(NB_CPUS, maxtasksperchild=int(NB_CPUS / len(t_values)) + 1)
        pool.map(f,t_values)
        pool.join()









