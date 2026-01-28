#!/bin/bash
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=4
#SBATCH --mem=20G
#SBATCH --gres=gpu:1
#SBATCH --time=23:59:59
#SBATCH --job-name=parse_images
#SBATCH --output=logs/test-%J.log
#SBATCH --mail-type=end
#SBATCH --mail-type=fail
#SBATCH --mail-user=ab5832@princeton.edu

# load modules or conda environments here
source ~/.bashrc
# active conda environment
conda activate policy_comp
# Run Jupyters
cd /n/fs/irom-testing/sbt/cleanrl

# Single sim
python data_parser.py