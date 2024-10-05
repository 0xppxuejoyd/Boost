import requests
import json
import time
import uuid
import base64
import re
import os
import shutil
import subprocess  # To run git pull command

# --- Facebook API Constants ---
GRAPH_API_VERSION = 'v19.0'
GRAPH_API_URL = 'https://graph.facebook.com/graphql'

# --- File Paths ---
TOKAS_FILE = '/sdcard/Test/toka.txt'
TOKAS_ID_FILE = '/sdcard/Test/tokaid.txt'

# --- Logo ---
logo = (f'''
\033[1;34m          /$$$$$$$   /$$$$$$   /$$$$$$   /$$$$$$  /$$$$$$$$
\033[1;34m         | $$__  $$ /$$__  $$ /$$__  $$ /$$__  $$|__  $$__/
\033[1;34m         | $$  \\ $$| $$  \\ $$| $$  \\ $$| $$  \\__/   | $$   
\033[1;34m         | $$$$$$$ | $$  | $$| $$  | $$|  $$$$$$    | $$   
\033[1;34m         | $$__  $$| $$  | $$| $$  | $$ \\____  $$   | $$   
\033[1;34m         | $$  \\ $$| $$  | $$| $$  | $$ /$$  \\ $$   | $$   
\033[1;34m         | $$$$$$$/|  $$$$$$/|  $$$$$$/|  $$$$$$/   | $$   
\033[1;34m         |_______/  \\______/  \\______/  \\______/    |__/   
\033[1;34m                                                  
''')

# --- Colors ---
blue = "\033[1;34m"    # Bold blue
yellow = "\033[1;33m"  # Bold yellow
r = "\033[0m"         # Reset color

def clear_screen():
    os.system('clear')

def count_lines(file_path):
    try:
        with open(file_path, 'r') as f:
            return sum(1 for _ in f)
    except FileNotFoundError:
        return 0  # Return 0 if the file does not exist

def overview():
    print(logo)  # Print the logo
    print(f"{blue} ━━━━━━━━━━━━━━━━━━━━━━━━━━[{yellow}OVERVIEW{yellow}]━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    total_accounts = count_lines(TOKAS_FILE)
    total_pages = count_lines(TOKAS_ID_FILE)
    print(f"  {yellow}                   TOTAL ACCOUNTS: {yellow}{total_accounts}{yellow}")
    print(f'{yellow} ════════════════════════════════════════════════════════════════{r}')

def git_pull_repository():
    repo_path = '.'  # Assuming the script is in the repository you want to update
    try:
        print(f"{blue}Updating the repository...{r}")
        subprocess.run(['git', 'pull'], cwd=repo_path, check=True)
        print(f"{yellow}Repository updated successfully.{r}")
    except subprocess.CalledProcessError as e:
        print(f"{red}Error occurred while updating the repository: {e}{r}")

def clone_and_run(repo_url, script_name):
    repo_name = repo_url.split("/")[-1].replace(".git", "")
    
    if not os.path.exists(repo_name):
        os.system(f'git clone {repo_url}')
    
    os.chdir(repo_name)
    os.system(f'python {script_name}')
    os.chdir('..')

def main_menu():
    clear_screen()
    overview()  # Call the overview function here

    print(f"{yellow}[0] Update Tool{r}")
    print(f"{yellow}[1] Extract Account{r}")
    print(f"{yellow}[2] Auto Facebook Followers{r}")
    print(f"{yellow}[3] Auto Comments{r}")
    print(f"{yellow}[4] Auto Reply to Comments{r}")
    print(f"{yellow}[5] Auto Reacts{r}")
    print(f"{yellow}[6] Auto Create Page{r}")
    print(f"{yellow}[7] Auto React Comment{r}")
    print(f"{yellow}[8] Auto Reacts for Videos(NEW METHOD){r}")
    print(f"{yellow}[9] Auto Reacts for Reels {r}")
    print(f"{yellow}[10] Auto Join Groups{r}")
    print(f"{yellow}[R] Reset{r}")
    print(f"{yellow}[E] Exit{r}")

    choice = input(f"{yellow}Enter your choice: {r}").strip().upper()

    if choice == '0':
        update()  # Call the update function
    elif choice == '1':
        extract_account()
    elif choice == '2':
        auto_facebook_followers()
    elif choice == '3':
        auto_comments()
    elif choice == '4':
        auto_reply_to_comments()
    elif choice == '5':
        auto_reacts()
    elif choice == '6':
        auto_create_page()
    elif choice == '7':
        auto_react_comment()
    elif choice == '8':
        auto_working_vid()
    elif choice == '9':
        auto_reacts_reels()
    elif choice == '10':
        auto_join_groups()
    elif choice == 'R':
        reset()
    elif choice == 'E':
        print("Exiting...")
        exit()
    else:
        print("Invalid choice, please try again.")
        main_menu()

def update():
    git_pull_repository()  # Call the git pull function

def extract_account():
    repo_url = 'https://github.com/KYZER02435/BOOSTING'
    script_name = 'extract-acc.py'
    clone_and_run(repo_url, script_name)

def auto_facebook_followers():
    repo_url = 'https://github.com/KYZER02435/BOOSTING'
    script_name = 'auto-follow.py'
    clone_and_run(repo_url, script_name)

def auto_comments():
    repo_url = 'https://github.com/KYZER02435/BOOSTING'
    script_name = 'auto_comment.py'
    clone_and_run(repo_url, script_name)

def auto_reply_to_comments():
    repo_url = 'https://github.com/KYZER02435/BOOSTING'
    script_name = 'atrc.py'
    clone_and_run(repo_url, script_name)

def auto_reacts():
    repo_url = 'https://github.com/KYZER02435/BOOSTING'
    script_name = 'auto-reacts.py'
    clone_and_run(repo_url, script_name)

def auto_create_page():
    repo_url = 'https://github.com/KYZER02435/BOOSTING'
    script_name = 'atc_page.py'
    clone_and_run(repo_url, script_name)

def auto_react_comment():
    repo_url = 'https://github.com/KYZER02435/BOOSTING'
    script_name = 'auto-react-comment.py'
    clone_and_run(repo_url, script_name)

def auto_working_vid():
    repo_url = 'https://github.com/KYZER02435/BOOSTING'
    script_name = 'working-vid.py'
    clone_and_run(repo_url, script_name)

def auto_reacts_reels():
    repo_url = 'https://github.com/KYZER02435/BOOSTING'
    script_name = 'reels_reacts.py'
    clone_and_run(repo_url, script_name)

def auto_join_groups():
    repo_url = 'https://github.com/KYZER02435/BOOSTING'
    script_name = 'auto_join_group.py'
    clone_and_run(repo_url, script_name)

def reset():
    folder_path = '/sdcard/Test'
    
    # Check if the folder exists
    if os.path.exists(folder_path):
        try:
            # Delete the folder and all its contents
            shutil.rmtree(folder_path)
            print(f"Successfully deleted the folder: {folder_path}")
        except Exception as e:
            print(f"Error while deleting the folder: {e}")
    else:
        print(f"The folder {folder_path} does not exist.")

def get_ids_tokens(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file]

def get_profile_id(profile_link, access_token):
    # Check if it's a vanity URL or a numeric ID
    if profile_link.isdigit():
        return profile_link  # Already a numeric ID

    url = f'https://graph.facebook.com/{GRAPH_API_VERSION}/{profile_link}'
    params = {'access_token': access_token, 'fields': 'id'}
    response = requests.get(url, params=params)
    
    if response.status_code == 200:
        return response.json().get('id', 'Unknown ID')
    return 'Unknown ID'

def get_profile_username(profile_id, access_token):
    url = f'https://graph.facebook.com/{GRAPH_API_VERSION}/{profile_id}'
    params = {'access_token': access_token, 'fields': 'name'}
    response = requests.get(url, params=params)
    
    if response.status_code == 200:
        return response.json().get('name', 'Unknown Profile')
    return 'Unknown Profile'

def follow_facebook_profile():
    access_tokens = get_ids_tokens(TOKAS_FILE)

    profile_link = input('Enter the Facebook profile link: ')
    
    # Use the first token to resolve the profile link to an ID
    profile_id = get_profile_id(profile_link.split('/')[-1], access_tokens[0])
    
    # Ask the user how many followers they want to add
    num_followers = int(input('How many followers do you want to add? '))
    
    def follow_profile(profile_id, access_token):
        try:
            url = f'https://graph.facebook.com/{GRAPH_API_VERSION}/{profile_id}/subscribers'
            params = {'access_token': access_token}
            response = requests.post(url, params=params)
            
            if response.status_code == 200:
                return True
            return False
        except requests.exceptions.RequestException:
            return False

    follow_count = 0

    for i, access_token in enumerate(access_tokens):
        if follow_count >= num_followers:
            break  # Stop if we've added the requested number of followers
        
        profile_name = get_profile_username(profile_id, access_token)
        
        if follow_profile(profile_id, access_token):
            print(f"Success: Followed the profile '{profile_name}' with ID {i + 1}")
            follow_count += 1
        else:
            print(f"Failed: Could not follow the profile '{profile_name}' with ID {i + 1}")

    print(f"Successfully followed {follow_count} profiles out of {num_followers} requested.")

def remove_facebook_follower():
    access_tokens = get_ids_tokens(TOKAS_FILE)

    profile_link = input('Enter the Facebook profile link to remove: ')
    
    # Use the first token to resolve the profile link to an ID
    profile_id = get_profile_id(profile_link.split('/')[-1], access_tokens[0])

    def remove_follower(profile_id, access_token):
        try:
            url = f'https://graph.facebook.com/{GRAPH_API_VERSION}/{profile_id}/subscribers'
            params = {'access_token': access_token}
            response = requests.delete(url, params=params)
            
            if response.status_code == 200:
                return True
            return False
        except requests.exceptions.RequestException:
            return False

    remove_count = 0

    for i, access_token in enumerate(access_tokens):
        profile_name = get_profile_username(profile_id, access_token)
        
        if remove_follower(profile_id, access_token):
            print(f"Success: Removed the follower from profile '{profile_name}' with ID {i + 1}")
            remove_count += 1
        else:
            print(f"Failed: Could not remove the follower from profile '{profile_name}' with ID {i + 1}")

    print(f"Successfully removed {remove_count} followers.")

def Reaction(actor_id: str, post_id: str, comment_id: str, react: str, token: str):
    rui = requests.Session()
    feedback_id = str(base64.b64encode(('feedback:{}'.format(comment_id)).encode('utf-8')).decode('utf-8'))
    var = {
        "input": {
            "feedback_referrer": "native_newsfeed",
            "tracking": [None],
            "feedback_id": feedback_id,
            "client_mutation_id": str(uuid.uuid4()),
            "nectar_module": "newsfeed_ufi",
            "feedback_source": "native_newsfeed",
            "feedback_reaction_id": react,
            "actor_id": actor_id,
            "action_timestamp": str(time.time())[:10]
        }
    }
    data = {
        'access_token': token,
        'method': 'post',
        'pretty': False,
        'format': 'json',
        'server_timestamps': True,
        'locale': 'id_ID',
        'fb_api_req_friendly_name': 'ViewerReactionsMutation',
        'fb_api_caller_class': 'graphservice',
        'client_doc_id': '2857784093518205785115255697',
        'variables': json.dumps(var),
        'fb_api_analytics_tags': ["GraphServices"],
        'client_trace_id': str(uuid.uuid4())
    }

    pos = rui.post(GRAPH_API_URL, data=data).json()
    try:
        if react == '0':
            print(f"「Success」» Removed reaction from {actor_id} on {comment_id}")
            return True
        elif react in str(pos):
            print(f"「Success」» Reacted with » {actor_id} to {comment_id}")
            return True
        else:
            print(f"「Failed」» Reacted with » {actor_id} to {comment_id}")
            return False
    except Exception:
        print('Reaction failed due to an error.')
        return False

def choose_reaction():
    print("Please choose the reaction you want to use.\n")
    reactions = {
        '1': 'Like',
        '2': 'Love',
        '3': 'Haha',
        '4': 'Wow',
        '5': 'Care',
        '6': 'Sad',
        '7': 'Angry',
        '8': 'Remove Reaction'
    }
    for key, value in reactions.items():
        print(f"     「{key}」 {value}")
    
    rec = input('Choose a reaction: ')
    reaction_ids = {
        '1': '1635855486666999',  # Like
        '2': '1678524932434102',  # Love
        '3': '115940658764963',   # Haha
        '4': '478547315650144',   # Wow
        '5': '613557422527858',   # Care
        '6': '908563459236466',   # Sad
        '7': '444813342392137',   # Angry
        '8': '0'                 # Remove Reaction
    }
    return reaction_ids.get(rec)

def linktradio(comment_link: str) -> tuple:
    # Extract post ID and comment ID from the Facebook comment link
    match = re.search(r'/posts/(\w+).*?comment_id=(\d+)', comment_link)
