import sys
GREENOK_BG = '\x1b[6;30;42m'
RED_NOTOK_BG = '\x1b[6;30;41m'
END_COLOR_CHANGE = '\x1b[0m'
NONAME_STRING = "Mr. Nobody"
NAME_STRING = "Don't Mess With The Zohan"
GITHUB_REPO = ''
DEFAULT_SNAME = 'Python'
DEFAULT_SVALUE = '1'
DEFAULT_CNAME = 'Azure'
DEFAULT_CVALUE = '1'
DEFAULT_GVALUE = '1'
DEFAULT_LVALUE = '1'
GREETINGS = '''  ________                      __  .__                          
 /  _____/______   ____   _____/  |_|__| ____    ____  ______    
/   \  __\_  __ \_/ __ \_/ __ \   __\  |/    \  / ___\/  ___/    
\    \_\  \  | \/\  ___/\  ___/|  | |  |   |  \/ /_/  >___ \     
 \______  /__|    \___  >\___  >__| |__|___|  /\___  /____  >    
        \/            \/     \/             \//_____/     \/  '''


# Secret:
# cat name.txt | grep Zohan >/dev/null && echo "Zohan exists in name.txt" || echo "Zohan doesn't exist in name.txt"
# cat no_name.txt | grep Zohan >/dev/null && echo "Zohan exists in name.txt" || echo "Zohan doesn't exist in no_name.txt"


def get_files_context(file_name):
    ''':param file_name: string
    This function will print the text from the file if the file exists, if not, it will create the file and print it'''
    try:
        with open(file_name) as first_file:
            text = first_file.read()
    except FileNotFoundError:
        print(f'file name {file_name} not found. Creating new file.')
        if file_name == 'name.txt':
            with open(file_name, 'w') as new_file:
                new_file.write(NAME_STRING)
            text = get_files_context(file_name)
        else:
            with open(file_name, 'w') as new_file:
                new_file.write(NONAME_STRING)
            text = get_files_context(file_name)
    else:
        print(f'{file_name}: {text}')
    return text


def print_file_contents():
    get_files_context('name.txt')
    get_files_context('no_name.txt')


def print_title():
    print(GREETINGS)


def found(s):
    print(GREENOK_BG + f'The string {s} exists in the file name.txt' + END_COLOR_CHANGE)


def not_found(s):
    print(RED_NOTOK_BG + f'The string {s} doesn\'t exist in the file no_name.txt' + END_COLOR_CHANGE)


def check(looking_for, file_name):
    print(f'Checking if the string \"{looking_for}\" exists in file {file_name}')
    exists = False
    try:
        with open(file_name) as file:
            text = file.read()
            if looking_for in text:
                exists = True
    except FileNotFoundError:
        print('Sorry, file not found')
    else:
        if exists:
            found(looking_for)
        else:
            not_found(looking_for)


def block_of_text(script_name=DEFAULT_SNAME, cloud_name=DEFAULT_CNAME, script_value=DEFAULT_SVALUE,
                  git_value=DEFAULT_GVALUE, linux_value=DEFAULT_LVALUE, cloud_value=DEFAULT_CVALUE):
    return f'''Script Coding skill: {script_name}, {script_value}
                     Git Skills: {git_value}
                     Linux Skills: {linux_value}
                     Cloud Skills: {cloud_name}, {cloud_value}\n\n'''


def answers():
    '''This function uses args. first value: scripting language name. second value: cloud service and the next 4'''
    # in case were sending argv, that is we want to have the answers
    if len(sys.argv) > 1:
        # slice the file name and unneeded values
        values = sys.argv[1:7]
        # just to make AWS abbreviation
        if values[1].lower() == 'aws':
            values[1] = values[1].upper()
        else:
            values[1] = values[1].capitalize()
        print(block_of_text(values[0].capitalize(), values[1], values[2], values[3], values[4], values[5]))


def greeting():
    print_title()
    print(f'''My name is Kostyantin, but everyone calls me Kostya!
I like learning new things. If you would like to see how I over-engineered,
this assignment follow this link: {GITHUB_REPO}''')


if __name__ == '__main__':
    # created this for the answers, it will be easier just to send it all in one image,
    # however if we send no args we will simply skip this step and print only greeting.
    if len(sys.argv) > 1:
        # in case we sent params, then we want the answers displayed
        answers()
    greeting()
    print()
    print_file_contents()
    print()
    check("Zohan", "name.txt")
    check("Zohan", "no_name.txt")
