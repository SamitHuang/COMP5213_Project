# Train 
experiment_dir="experiments/xxx"
python run_hybrid_atari_experiment.py --model_dir=$experiment_dir

# Test
python test_model.py --model_dir=$experiment_dir--display_screen=True
