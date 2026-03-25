import os
import numpy as np
import shutil 
from pathlib import Path

datadir = Path("/n/fs/irom-testing/sbt/data/rl_new")
run_dir = Path("/n/fs/irom-testing/sbt/cleanrl/runs")

# Deleting empty directories
for run_name in os.listdir(run_dir):
    run_path = os.path.join(run_dir, run_name)
    npy_files = [f for f in os.listdir(run_path) if f.endswith(".npy")]
    if not npy_files:
        # delete runs without any .npy files
        shutil.rmtree(run_path)
        print(f"Deleting empty run directory: {run_path}")
    
# Find latest runs for each algorithm, environment, and seed combination
latest_runs = []
for run_name in os.listdir(run_dir):
    example = run_name.split("__", 1)[0]
    os.makedirs(os.path.join(datadir, example), exist_ok=True)
    algorithm = run_name.split("__")[1].split("_")[0]
    seed = run_name.split("__")[2]

    # Other folders with similar run names:
    similar_runs = [r for r in os.listdir(run_dir) if r.startswith(f"{example}__{algorithm}_continuous_action__{seed}__")]
    if similar_runs:
        # Find the latest run based on timestamp in the name
        latest_run = max(similar_runs, key=lambda r: int(r.split("__")[-1]))
        if latest_run not in latest_runs:
            latest_runs.append(latest_run)

# Only parse through latest runs
for run_name in os.listdir(run_dir):
    run_path = os.path.join(run_dir, run_name)
    
    npy_files = [f for f in os.listdir(run_path) if f.endswith(".npy")]
    if run_name in latest_runs:
        example = run_name.split("__", 1)[0]
        os.makedirs(os.path.join(datadir, example), exist_ok=True)
        algorithm = run_name.split("__")[1].split("_")[0]
        seed = run_name.split("__")[2]
        dest_dir = os.path.join(datadir, example, algorithm, seed)
        os.makedirs(dest_dir, exist_ok=True)
        if "episodic_returns.npy" not in npy_files:
            try:
                data_file = os.path.join(run_path, npy_files[0])
            except:
                breakpoint()
        else:
            data_file = os.path.join(run_path, "episodic_returns.npy")
        dest_file =  os.path.join(dest_dir, "episodic_returns.npy")
        
    
        # Copy file if it does not already exist
        if not os.path.isfile(dest_file):
            shutil.copy2(data_file, dest_file)
            print(f"Copied {data_file} to {dest_file}")
        else:
            print(f"File already exists, skipping: {dest_file}")
    # if os.path.isfile(data_file):
    #     with open(data_file, "rb") as file:
    #         data = np.load(file)
    #         breakpoint()