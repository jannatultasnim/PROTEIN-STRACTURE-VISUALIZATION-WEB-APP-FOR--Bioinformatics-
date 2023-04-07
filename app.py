# importing packages

import streamlit as st
from st_speckmol import speck_plot
import glob
st.set_page_config(layout="wide")
st.markdown(
    '''# Molecule Stracture visualization (Md Jannatu Tasnim)	:microscope:  :flag-bd: 
    '''
)
# accessing the .xyz files directory using glob
x_file = glob.glob("mol/*.xyz")
#creating side bar
with st.sidebar:
    ex_xyz = st.selectbox('select a molecule',x_file)
    f= open(ex_xyz,"r")
    ex_xyz=f.read()
# features of the protine stracture
res  =speck_plot(ex_xyz,wbox_height="500px",wbox_width="800px",scroll=True)
#with st.sidebar.expander("Parameters",expanded=True):
    #outln = st.checkbox('Outline',value=True)
    #bond = st.checkbox('Bond',value=True)
    #bond_scale = st.slider('BondScale',min_value=0.0,max_value=1.0,value=0.8)
    #brightness = st.slider('Brightness'min_value=0.0,max_value=1.0,value=0.4)
    #relativeAtomScale = st.slider('RelativeAtomScale',min_value=0.0,max_value=1.0,value=0.64)
    #bondShade = st.slider('bondShade',min_value=0.0,max_value=1.0,value=0.5)