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

def stats():
    tool = tools[game['tool']]
    print(f'You have {gmae['money']} and are using a {tool['name']}')

def user_win():
    if (game['tool'] == 4 and game['money'] >= 1000):
        print('you have won!')
        return True
    return False

while(True):
    i = input('[1] Mow Lawn [2] Check Stats [3] Upgrade [Q] Quit')
    i = int(i)

    if (i == 1):
        cut_lawn()

    if (i == 2):
        stats()

    if (i == 3):
        upgrade()

    if (i == Q):
        print('Game Over')
        break
    
    if (user_win()):
        break
