#!/bin/bash
#SBATCH --nodes=1
#SBATCH --job-name=CT-3D-Fine-mesh
#SBATCH --tasks-per-node=32
#SBATCH --exclusive
#SBATCH --time=5-00:00:00
#SBATCH -o %x.out
#SBATCH --partition=thrust2 #general #thrust2

# load the modules required for you program - customise for your program
module load ABAQUS/2019

envFile=abaqus_v6.env 
node_list=`scontrol show hostname $SLURM_NODELIST | sort | uniq `
echo $node_list 

mp_host_list="["
for i in  ${node_list} ; do
    mp_host_list="${mp_host_list}['$i', 32],"
done

mp_host_list=`echo ${mp_host_list} | sed -e "s/,$//"`
mp_host_list="${mp_host_list}]"

#export MP_HOST_LIST=mp_host_list

echo "mp_host_list=${mp_host_list}"  >> abaqus_v6.env

unset SLURM_GTIDS

abaqus input=CT-3D-Fine-mesh.inp \
       job=CT-3D-Fine-mesh \
	   cpus=32 \
	   scratch=. \
     output_precision=full \
	   mp_mode=mpi \
	   interactive
sed -i "/mp_host_list/d" $envFile

