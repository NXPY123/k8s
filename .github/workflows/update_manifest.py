
import os
import yaml

def update_image_version(yaml_file, new_version):
    # Load YAML file
    with open(yaml_file, 'r') as file:
        yaml_data = yaml.safe_load(file)

    # Update image version
    for container in yaml_data['spec']['template']['spec']['containers']:
        if 'image' in container:
            container['image'] = container['image'].split(':')[0] + ':' + new_version

    # Write updated YAML back to file
    with open(yaml_file, 'w') as file:
        yaml.dump(yaml_data, file, default_flow_style=False)

# Get root directory
root_dir = os.getcwd()
print("Root directory: " + root_dir)
yaml_file = root_dir + "/yaml/testapp-rollout.yaml"
new_version = os.getenv('GITHUB_SHA')
update_image_version(yaml_file, new_version)
