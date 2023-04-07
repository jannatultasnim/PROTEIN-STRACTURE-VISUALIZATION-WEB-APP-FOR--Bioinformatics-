# PROTEIN-STRACTURE-VISUALIZATION-WEB-APP-FOR--Bioinformatics-
MOLECULE STRACTURE VISUALIZATION WEB-APP using PYTHON and STREAMLIT 


### Speck
### Speck is a molecule renderer with the goal of producing figures that are as attractive as they are practical. Express your molecule clearly and with style.

![my image](https://warehouse-camo.ingress.cmh1.psfhosted.org/0a00837ad40ada1d127b1e7cd7fee5f064b092a4/68747470733a2f2f7261772e67697468756275736572636f6e74656e742e636f6d2f7777777479726f2f737065636b2f67682d70616765732f7374617469632f73637265656e73686f74732f64656d6f2d322e706e67)

### ipypeck

Ipyspeck is a ipywidget wrapping speck to be used on a Jupyter notebook as a regular widget.

### Usage

The ipyspeck widget renders xyz molecules.
![img](https://warehouse-camo.ingress.cmh1.psfhosted.org/0f6c82c45095b3b6f95c24588ca1144cc8b124cf/68747470733a2f2f7261772e67697468756275736572636f6e74656e742e636f6d2f64656e7068692f737065636b2f6d61737465722f7769646765742f697079737065636b2f696d672f68326f2e706e67)

```import ipyspeck

H2O='''3
Water molecule
O          0.00000        0.00000        0.11779
H          0.00000        0.75545       -0.47116
H          0.00000       -0.75545       -0.47116'''
h2o = ipyspeck.speck.Speck(data=H2O)
h2o```python 
