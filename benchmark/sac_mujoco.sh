#!/usr/bin/env bash
source ~/.bashrc
conda activate policy_comp

python -m cleanrl_utils.benchmark \
    --env-ids InvertedPendulum-v4 \
    --command "python cleanrl/sac_continuous_action.py --evaluate --track" \
    --num-seeds 1 \
    --workers 18 \
    --slurm-gpus-per-task 1 \
    --slurm-ntasks 1 \
    --slurm-total-cpus 10 \
    --slurm-template-path benchmark/cleanrl_1gpu.slurm_template
