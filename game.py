game = {'tool': 0, 'money':0}

tools = [
    {'name': 'teeth', 'profit': 1, 'cost': 0},
    {'name': 'rusty_scissors', 'profit': 5, 'cost': 5},
    {'name': 'push_lawnmower', 'profit': 50, 'cost': 25},
    {'name': 'fancy_lawnmower', 'profit': 100, 'cost': 250},
    {'name': 'starving_students', 'profit': 250, 'cost': 500}
]

def cut_lawn():
    tool = tools[game['tool']]
    game['money'] += tool['profit']
    print(f"You're using {tool['name']} to cut lawns and are making {tool['profit']}$ as your profit")

def upgrade():
    if (game['tool'] >= (len(tools) -1)):
        print('No upgrades')
        return 0 
    another_tool = tools[game['tool'] +1]
    if(another_tool == None):
        print('No more tools')
        return 0
    if (game['money'] < another_tool['cost']):
        print('you cannot afford this tool')
        return 0 
    print('upgrading your tool')

    game['money'] -= another_tool['cost']

    game['tool'] += 1 