import yaml
import json

yaml_file = 'prompts/tsd-000-name.yaml'
json_file = 'prompts/tsd-000-name.json'

with open(yaml_file, 'r') as f:
    yaml_data = yaml.safe_load(f)

with open(json_file, 'w') as f:
    json.dump(yaml_data, f, indent=2)
