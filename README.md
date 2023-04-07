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

```
import ipyspeck
H2O='''3
Water molecule
O          0.00000        0.00000        0.11779
H          0.00000        0.75545       -0.47116
H          0.00000       -0.75545       -0.47116'''
h2o = ipyspeck.speck.Speck(data=H2O)
h2o
``` 
Ideally it should be used as part of a container widget (such as Box, VBox, Grid, ...)

![img1](https://warehouse-camo.ingress.cmh1.psfhosted.org/d592b19ad054bcf48d806f6eea438b2c84240a4e/68747470733a2f2f7261772e67697468756275736572636f6e74656e742e636f6d2f64656e7068692f737065636b2f6d61737465722f7769646765742f697079737065636b2f696d672f68326f632e706e67)

```
import ipywidgets as w
c = w.Box([h2o], layout=w.Layout(width="600px",height="400px"))
c
```
The visualization parameters can be modified

```
#Modify atoms size
h2o.atomScale = 0.3
#change bonds size
h2o.bondScale = 0.3
#highlight borders
h2o.outline = 0
```
To render molecules on different formats openbabel can be used to translate them as xyz
```
import openbabel
import requests
url = "https://files.rcsb.org/ligands/view/CO2_ideal.sdf"
r = requests.get(url)
obConversion = openbabel.OBConversion()
obConversion.SetInAndOutFormats("sdf", "xyz")
mol = openbabel.OBMol()
obConversion.ReadString(mol, r.text)
co2 = obConversion.WriteString(mol)
ipyspeck.speck.Speck(data=co2)
```
![img2](https://warehouse-camo.ingress.cmh1.psfhosted.org/d1b6084236ab677fb99f3f727bd517d5b7a7a4d8/68747470733a2f2f7261772e67697468756275736572636f6e74656e742e636f6d2f64656e7068692f737065636b2f6d61737465722f7769646765742f697079737065636b2f696d672f636f322e706e67)

### Installation

To install use pip
```
$ pip install ipyspeck
$ jupyter nbextension enable --py --sys-prefix ipyspeck
```
![img3](https://warehouse-camo.ingress.cmh1.psfhosted.org/b9fc0166b434a4160e970b9ae5843222b572a87c/68747470733a2f2f7261772e67697468756275736572636f6e74656e742e636f6d2f64656e7068692f737065636b2f6d61737465722f7769646765742f697079737065636b2f696d672f696d67312e706e67)

![img4](https://warehouse-camo.ingress.cmh1.psfhosted.org/9bf8166b928abf1964edc5adb23967caf6586b36/68747470733a2f2f7261772e67697468756275736572636f6e74656e742e636f6d2f64656e7068692f737065636b2f6d61737465722f7769646765742f697079737065636b2f696d672f696d67322e706e67)

![img5](https://warehouse-camo.ingress.cmh1.psfhosted.org/b5c53efcd272c141b9fb51b141a432d9f5a55240/68747470733a2f2f7261772e67697468756275736572636f6e74656e742e636f6d2f64656e7068692f737065636b2f6d61737465722f7769646765742f697079737065636b2f696d672f696d67342e706e67)
