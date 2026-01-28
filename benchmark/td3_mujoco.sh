#!/usr/bin/env bash
source ~/.bashrc
conda activate policy_comp

python -m cleanrl_utils.benchmark \
    --env-ids HalfCheetah-v4 Walker2d-v4 Hopper-v4 InvertedPendulum-v4 Humanoid-v4 Pusher-v4 Ant-v4\
    --command "python cleanrl/td3_continuous_action.py --track --save_model --upload_model --capture_video" \
    --num-seeds 3 \
    --workers 18 \
    --slurm-gpus-per-task 1 \
    --slurm-ntasks 1 \
    --slurm-total-cpus 10 \
    --slurm-template-path benchmark/cleanrl_1gpu.slurm_template