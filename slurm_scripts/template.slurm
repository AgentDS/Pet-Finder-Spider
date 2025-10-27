#!/bin/bash
#SBATCH --job-name=common_voice_debug_job
#SBATCH --mail-user=leungsqshiloh@gmail.com
#SBATCH --mail-type=BEGIN,END
#SBATCH --cpus-per-task=2
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --mem-per-cpu=8G
#SBATCH --time=10:00
#SBATCH --account=jiayuz0
#SBATCH --partition=standard
#SBATCH --output=/nfs/turbo/si-jiayuz/common-voice-data/log_output/debug/%x-%j.log
#SBATCH --error=/nfs/turbo/si-jiayuz/common-voice-data/log_output/debug/%x-%j.error

WORK_HOME=/home/siqilian/Projects/Common-Voice
cd $WORK_HOME

module load mamba
source /home/siqilian/.bashrc
conda activate common_voice
conda list
which python
python -V

srun bash scripts/debug_run_feature_extraction.sh
