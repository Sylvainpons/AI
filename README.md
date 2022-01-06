# T-AIA-901_msc2022_group-2

# Autogen requirements.txt (src : https://stackoverflow.com/questions/31684375/automatically-create-requirements-txt)
Install autogen package
```
pip install pipreqs
```

Run autogeneration 
```
pipreqs /path/to/project
```

# Workflow (every command from root repo)
## Preprocessing / Data cleaning
First clean the data
```
python preprocessing/cleanData.py 
```

## Data vizualisation of train stations
Generate html file for viz :

```
python dataviz/dataviz.py
```

This generates `edges_with_weights.html`, just run it on a browser.








