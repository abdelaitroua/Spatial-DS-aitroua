import json
def getColor(jasonColors):
    return jasonColors[name]



# put a path for where is the jason file
with open('../colors.json', 'r') as contentFile:
    content = json.loads(content)
jasonColors = {}
for color in content:
    print(color)
    jsonColors[color['name']] = (color['rgb'][0], color['rgb'][1], color['rgb'][3])

print(jasonColors)

print(getColor(jasonColors, 'palevioletred'))

f = open('f:/4553/...your own path..new_colors.json', 'w')
f.write(json.dumps(jsonColors, sort_key = true, indent = 4, indent = None ))
f.close