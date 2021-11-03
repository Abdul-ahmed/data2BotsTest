import json
import fileinput
from genson import SchemaBuilder

# Read data_1 file
with open('peep\data\data_1.json', 'r') as openjsonfile1:
    loadjsonfile1 = json.load(openjsonfile1)

# Read data_2 file
with open('peep\data\data_2.json', 'r') as openjsonfile2:
    loadjsonfile2 = json.load(openjsonfile2)

# Sniffing the schema of data_1
builder1 = SchemaBuilder()
builder1.add_object(loadjsonfile1['message'])
outputSchema1 = json.dumps(builder1.to_schema(), indent=4)

# Sniffing the schema of data_2
builder2 = SchemaBuilder()
builder2.add_object(loadjsonfile2['message'])
outputSchema2 = json.dumps(builder2.to_schema(), indent=4)

# Write schema_1 file
with open('peep\schema\schema_1.json', 'w') as openschemafile1:
    if openschemafile1.write(outputSchema1):
        print("Schema1 Generated Successfully")
    else:
        print("Error Generating Schema1")

# Write schema_2 file
with open('peep\schema\schema_2.json', 'w') as openschemafile2:
    if openschemafile2.write(outputSchema2):
        print("Schema2 Generated Successfully")
    else:
        print("Error Generating Schema2")

# Padding "tag" and "description" keys with schema_1
schema_1file = "peep/schema/schema_1.json"
for line in fileinput.FileInput(schema_1file, inplace=1):
    if "type" in line:
        line = line.rstrip()
        if "archetype" in line:
            line = line.replace(line, line + "\n")
        elif line[-1] == ",":
            line = line.replace(line, line + '\n"tag": "",' + '\n' + '"description": "",\n')
        else:
            line = line.replace(line, line + ',\n"tag": "",' + '\n' + '"description": ""\n')
    print(line, end="")

# Padding "tag" and "description" keys with schema_2
schema_2file = "peep/schema/schema_2.json"
for line in fileinput.FileInput(schema_2file, inplace=1):
    if "type" in line:
        line = line.rstrip()
        if line[-1] == ",":
            line = line.replace(line, line + '\n"tag": "",' + '\n' + '"description": "",\n')
        else:
            line = line.replace(line, line + ',\n"tag": "",' + '\n' + '"description": ""\n')
    print(line, end="")
