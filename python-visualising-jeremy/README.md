1. histogram time people stay in same place:

(1)x: how long they stay 
(2)y: how may time it happen

to run: saty_point_histogram.py

2. grouping:


(1). random a id
(2). show the group of this id & plot trajectory 

distacne: script.analyse.trajectory_distance

init method compute the re-sample, Euclidean distance  

to run:
single group: distance_group_plot.py
overall group: find_groups.py

grouping: Triangle inequlity 

References:
<Similarity Search Over Time Series and Trajectory Data> Lei Chen  P108, P78-80


3.gui/plot

plot 1: 
	x: time 
	y: hom many people stay in certain atraction

plot 2: 
	x: time 
	y: how long they stay 



to run:

gui: attraction_occupation.py

plot:place_occupation.py

aggregation: place_occupants_examples.py   parametric: category, attraction id, start, end, line 
 
4. prediction:
to run:
plot: next_place.py
parametric: predict_examples


Reference:
http://scikit-learn.org/stable/supervised_learning.html#supervised-learning
http://scikit-learn.org/stable/modules/ensemble.html#forests-of-randomized-trees
http://scikit-learn.org/stable/modules/model_evaluation.html#model-evaluation
