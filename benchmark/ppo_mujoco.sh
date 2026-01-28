#!/usr/bin/env bash
source ~/.bashrc
conda activate policy_comp

OMP_NUM_THREADS=1 xvfb-run -a python -m cleanrl_utils.benchmark \
    --env-ids Walker2d-v4 Hopper-v4 InvertedPendulum-v4  Humanoid-v4 Ant-v4 HalfCheetah-v4 Pusher-v4\
    --command "python cleanrl/ppo_continuous_action.py --track --run-evals" \
    --num-seeds 1 \
    --workers 9 \
    --slurm-gpus-per-task 1 \
    --slurm-ntasks 1 \
    --slurm-total-cpus 10 \
    --slurm-template-path benchmark/cleanrl_1gpu.slurm_template