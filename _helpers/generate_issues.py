"""
Generate a CSV file of issues to import into Github
Makes use of: https://github.com/gavinr/github-csv-tools

"""


import os
import pandas as pd
import yaml

yaml_path = 'fm_list.yaml'
outpath = 'github_issues.csv'

pathnames = []
filenames = []
for (root, _, files) in os.walk('../', topdown=True):
    for fname in files:
        if fname.endswith('.md') and fname != 'README.md':
            p = os.path.join(root, fname)
            pathnames.append(p)
            filenames.append(fname)

csv_data = []
with open(yaml_path, 'r') as yaml_file:
    data = yaml.safe_load(yaml_file)
    
    for fm in data:
        f = fm['Filename'] + '.md'
        if f in filenames:
            csv_data.append(dict(
                title = f"edit: {f}",
                body = f"Edit entry for {fm['Mechanism']}",
                label = f"entry-{fm['Type'].lower()}"        
            ))
        else:
            print("Could not find:", f)
            
pd.DataFrame(csv_data).to_csv(outpath)            