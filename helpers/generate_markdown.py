import yaml

yaml_path = 'fm_list.yaml'
md_template = """# Title

`Tag`

### Description

Add description here

### Examples

- Example 1
- Example 2

### Further reading

- Link 1
- Link 2

### Acknowledgements

- Ack 1
- Ack 2
"""

with open(yaml_path, 'r') as yaml_file:
    data = yaml.safe_load(yaml_file)
    
    for fm in data:
        md = md_template.replace("Title", fm['Mechanism']).replace("Tag", fm['Type'])
        outpath = "../draft/" + fm['Filename'].strip() + ".md"
        with open(outpath, 'w') as f:
            f.write(md)