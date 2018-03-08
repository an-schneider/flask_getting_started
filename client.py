import requests
import sys

# Get requests
r1 = requests.get("http://vcm-3607.vm.duke.edu:5000/name")
sys.stdout.write(r1.text)

r2 = requests.get("http://vcm-3607.vm.duke.edu:5000/hello/name")
sys.stdout.write(r2.text)

# Post requests
r3 = requests.post("http://vcm-3607.vm.duke.edu:5000/distance",
                   json={"a": [5, 6], "b": [9, 10]})
points_json = r3.json()
sys.stdout.write(r3.text)
