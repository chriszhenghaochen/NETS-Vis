# NeST-Vis #

## overview
NeST-Vis is a ***Neural Net based Framework of Time-Spatial Visualization***

* The main algorithms of it are ***Self-Organizing Map*** and ***Recurrent Neural Net***,

* the front end of front-end contain Heat Map, Dynamic Time Warping, 3D cube and other Visualization Tools

* The data base used for this is ***Neo4j***

## Data
* VAST 2017 challenge data(http://vacommunity.org/VAST+Challenge+2017)
* VAST 2015 challenge data(http://vacommunity.org/VAST+Challenge+2015)
* Mobile Phone Connection Data in China


## Document

* Thesis and presentation slides are under documents folder
* See publication for more detail

## Members
* Zhenghao Chen (zhenghao.chen@sydney.edu.au)
* Jeremy Swanson (jeremy.swanson@nicta.com.au)
* Dr Jianlong Zhou (jianlong.zhou@data61.csiro.au)
* Dr Xiuying Wang (xiu.wang@sydney.edu.au)

You are alwayws welcome to contact any of us if you have any ideas or feel free to have your pull request.

## Libraries Requirement:

### SOM Cluster:
 * Python 2
 * Java > 6
 * Scipy(numpy, pandas, matplotlib)
 * Scikit Learn
 * sompy https://github.com/sevamoo/SOMPY (I modify this library, thanks to Dr Vahid Moosavi)
 * fast DTW https://pypi.python.org/pypi/fastdtw/0.3.0

### Visualization Tool:
 * Python 3
 * Scipy(numpy, pandas, matplotlib)
 * Scikit Learn
 * PyQt

### RNN predict:
 * Visualization Tool
 * Tensorflow
 * Keras

### DataBase
 * Neo4j
  
I would suggest you just download 3 different to execute all of them.
 * Annaconda: https://www.continuum.io/
 * Tensorflow: https://www.tensorflow.org/
 * Neo4j: https://neo4j.com/
 * Keras: https://keras.io/

## Publication:
International Joint Conference of Nerual Network(IJCNN) 2017

http://ieeexplore.ieee.org/abstract/document/7965979/

## Acknowledgement:
This work is sponsored by CSIRO https://www.csiro.au/ and USYD http://sydney.edu.au/
