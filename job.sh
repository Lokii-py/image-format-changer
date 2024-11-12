#!/bin/bash

#--------------------------------------------------------------------------------

#  SBATCH CONFIG

#--------------------------------------------------------------------------------

#SBATCH --partition=gpu                           #name of the partition

#SBATCH --nodes=1                                       #nodes requested

#SBATCH --cpus-per-task=1                               #no. of cpu's per task

#SBATCH --gres gpu:2

#SBATCH --ntasks=8                                      #no. of tasks (cpu cores)

#SBATCH --mem=32G                                        #memory requested

#SBATCH --job-name=train_new_data                             #job name

#SBATCH --time=48:00:00                               #time limit in the form days-hours:minutes

#SBATCH --output=train_new_data_%j.out                        #out file with unique jobid

#SBATCH --error=train_new_data_%j.err                         #err file with unique jobid

#SBATCH --mail-type=BEGIN,FAIL,END                      #email sent to user during begin,fail and end of job

#SBATCH --mail-user=$dafgp@umsystem.edu                 #email id to be sent to(please change your email id)

# echo "### Starting at: $(date) ###"

python main_train_SwinFuSR.py --opt options/train_baseline2.json

# srun runfeko $1 --use-job-scheduler

# echo "### Ending at: $(date) ###"
