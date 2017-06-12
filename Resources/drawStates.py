class us_states(object):
    def __init__(self, file_name):
        with open(file_name, 'r') as content_file:
            content = content_file.read()
        self.us_borders = json.loads(content)

def get_state_border(self, name=None, abbr=None):
    if name:
        key = name
        key_type = 'name'
    elif code:
        key = code
        key_type = 'code
    else
        #import sys to use the bellow method
        sys.exit(0)
    
    for state in self.us_borders:
        if state[key_type] == key:
            return state['borders']
    return[]

color = color_helper('file path')
states = us_states('file path')

print(colors.get_color_rgb('pink'))