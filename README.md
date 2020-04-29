# travian_build_order
the goal is to find the build order maximizing cultural points within a limited period.

For now, use main_explore with terminal. For example.
python main_explore.py --day 5 --method scid --max_iter 5000 --plot true

if you want to save the result for re running optimization, use --savename and --loadname and at each step the build order will be loaded 
instead of starting a new random one. 
