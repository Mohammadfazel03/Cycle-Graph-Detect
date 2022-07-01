# Cycle graph
A python library for detect cycle graph
# How install it?
```
pip install git+https://github.com/Mohammadfazel03/Cycle-Graph-Detect
```
# How to use it?
```python
from graph import is_cycle
from graph import Vertices
graph = [Vertices(1,2),Vertices(2,3),Vertices(3,1)]
is_cycle(graph)
