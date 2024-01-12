import os,sys,ctypes,shutil,configparser
import configparser
from colorama import Fore, Style
from tqdm import tqdm
from datetime import datetime

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

if not is_admin():
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
    sys.exit()

def load_config():
    config = configparser.ConfigParser()
    config.read('Config/cleaner_config.ini')
    return config

def save_config(config):
    with open('Config/cleaner_config.ini', 'w') as configfile:
        config.write(configfile)

def clean_temp_folder(temp_folder_path, folder_name):
    try:
        if os.path.isdir(temp_folder_path):
            total_files = sum([len(files) for root, dirs, files in os.walk(temp_folder_path)])
            with tqdm(total=total_files, unit="file", desc=f"Cleaning {folder_name}") as pbar:
                for root, dirs, files in os.walk(temp_folder_path):
                    for file in files:
                        file_path = os.path.join(root, file)

                        try:
                            os.unlink(file_path)
                        except Exception as e:
                            print(f"{Fore.YELLOW}[{folder_name} Warning]{Style.RESET_ALL} Unable to delete '{file_path}': {e}")

                        pbar.update(1)

            print(f"{Fore.GREEN}[{folder_name} CheckMark] {folder_name} cleaned successfully.{Style.RESET_ALL}")
        else:
            print(f"{Fore.RED}[{folder_name} X]{Style.RESET_ALL} '{temp_folder_path}' is not a valid directory.")

    except Exception as e:
        print(f"{Fore.RED}[{folder_name} X]{Style.RESET_ALL} An error occurred: {e}")

def clean_browser_cache(browser_cache_path, browser_name):
    try:
        if os.path.isdir(browser_cache_path):
            total_files = sum([len(files) for root, dirs, files in os.walk(browser_cache_path)])
            with tqdm(total=total_files, unit="file", desc=f"Cleaning {browser_name} Cache") as pbar:
                for root, dirs, files in os.walk(browser_cache_path):
                    for file in files:
                        file_path = os.path.join(root, file)

                        try:
                            os.unlink(file_path)
                        except Exception as e:
                            print(f"{Fore.YELLOW}[{browser_name} Cache Warning]{Style.RESET_ALL} Unable to delete '{file_path}': {e}")

                        pbar.update(1)

            print(f"{Fore.GREEN}[{browser_name} Cache CheckMark] {browser_name} cache cleaned successfully.{Style.RESET_ALL}")
        else:
            print(f"{Fore.RED}[{browser_name} Cache X]{Style.RESET_ALL} '{browser_cache_path}' is not a valid directory.")

    except Exception as e:
        print(f"{Fore.RED}[{browser_name} Cache X]{Style.RESET_ALL} An error occurred: {e}")

def clean_system_logs(logs_path, logs_name):
    try:
        if os.path.isdir(logs_path):
            total_files = sum([len(files) for root, dirs, files in os.walk(logs_path)])
            with tqdm(total=total_files, unit="file", desc=f"Cleaning {logs_name}") as pbar:
                for root, dirs, files in os.walk(logs_path):
                    for file in files:
                        file_path = os.path.join(root, file)

                        try:
                            os.unlink(file_path)
                        except Exception as e:
                            print(f"{Fore.YELLOW}[{logs_name} Warning]{Style.RESET_ALL} Unable to delete '{file_path}': {e}")

                        pbar.update(1)

            print(f"{Fore.GREEN}[{logs_name} CheckMark] {logs_name} cleaned successfully.{Style.RESET_ALL}")
        else:
            print(f"{Fore.RED}[{logs_name} X]{Style.RESET_ALL} '{logs_path}' is not a valid directory.")

    except Exception as e:
        print(f"{Fore.RED}[{logs_name} X]{Style.RESET_ALL} An error occurred: {e}")

def clean_temp_files(temp_files_path, temp_files_name):
    try:
        if os.path.isdir(temp_files_path):
            total_files = sum([len(files) for root, dirs, files in os.walk(temp_files_path)])
            with tqdm(total=total_files, unit="file", desc=f"Cleaning {temp_files_name}") as pbar:
                for root, dirs, files in os.walk(temp_files_path):
                    for file in files:
                        file_path = os.path.join(root, file)

                        try:
                            os.unlink(file_path)
                        except Exception as e:
                            print(f"{Fore.YELLOW}[{temp_files_name} Warning]{Style.RESET_ALL} Unable to delete '{file_path}': {e}")

                        pbar.update(1)

            print(f"{Fore.GREEN}[{temp_files_name} CheckMark] {temp_files_name} cleaned successfully.{Style.RESET_ALL}")
        else:
            print(f"{Fore.RED}[{temp_files_name} X]{Style.RESET_ALL} '{temp_files_path}' is not a valid directory.")

    except Exception as e:
        print(f"{Fore.RED}[{temp_files_name} X]{Style.RESET_ALL} An error occurred: {e}")

def configure_directories(config):
    print("Configuring directories to clean:")
    directories = config.get('Cleaning', 'directories', fallback='').split(',')

    while True:
        print("Current Directories:")
        for i, directory in enumerate(directories, start=1):
            print(f"{i}. {directory}")

        print("Menu:")
        print("1. Add Directory")
        print("2. Remove Directory")
        print("3. Save and Exit")
        choice = input("Enter your choice (1, 2, or 3): ")

        if choice == '1':
            new_directory = input("Enter the new directory path: ")
            directories.append(new_directory)
        elif choice == '2':
            try:
                index_to_remove = int(input("Enter the index of the directory to remove: ")) - 1
                directories.pop(index_to_remove)
            except (ValueError, IndexError):
                print(f"{Fore.RED}[ X ]{Style.RESET_ALL} Invalid index. Please enter a valid index.")
        elif choice == '3':
            config.set('Cleaning', 'directories', ','.join(directories))
            save_config(config)
            print("Configuration saved. Returning to the menu.")
            break
        else:
            print(f"{Fore.RED}[ X ]{Style.RESET_ALL} Invalid choice. Please enter 1, 2, or 3.")

# Load configuration
config = load_config()
user_temp_folder = os.path.join(os.environ['LOCALAPPDATA'], 'Temp')

# Logo
logo = r"""
  _____       _     _ _          
 |  __ \     | |   | (_)         
 | |__) |   _| |__ | |_ _ __ ___ 
 |  ___/ | | | '_ \| | | '__/ _ \
 | |   | |_| | |_) | | | | |  __/
 |_|    \__,_|_.__/|_|_|_|  \___|


                    Made By pick info below.
                    Discord : pick6666
                    Tiktok : pick
                    Instagram : _kingkillv6
"""

# Menu
os.system("cls")
while True:
    os.system("cls")
    print(f"{Fore.CYAN}{logo}{Style.RESET_ALL}")
    print("Menu:")
    print("1. Clean Temp Folders")
    print("2. Clean Browser Caches")
    print("3. Clean System Logs")
    print("4. Clean Temporary Files")
    print("5. Clean All")
    print("6. Configure Directories")
    print("7. View Cleaning Log")
    print("8. Exit")
    choice = input("Enter your choice (1-8): ")

    if choice == '1':
        clean_temp_folder(user_temp_folder, "User Temp")
        input("Press Enter to return to the menu...")

        input("Press Enter to return to the menu...")
    elif choice == '2':
        # Add cleaning for browser caches (modify paths based on your browser installations)
        chrome_cache_path = os.path.join(os.getenv('LOCALAPPDATA'), 'Google', 'Chrome', 'User Data', 'Default', 'Cache')
        firefox_cache_path = os.path.join(os.getenv('APPDATA'), 'Mozilla', 'Firefox', 'Profiles')

        clean_browser_cache(chrome_cache_path, "Google Chrome")
        clean_browser_cache(firefox_cache_path, "Mozilla Firefox")

        input("Press Enter to return to the menu...")
    elif choice == '3':
        # Add cleaning for system logs
        windows_logs_path = os.path.join(os.getenv('WINDIR'), 'Logs')
        clean_system_logs(windows_logs_path, "Windows Logs")

        input("Press Enter to return to the menu...")
    elif choice == '4':
        # Add cleaning for temporary files
        temp_files_path = os.path.join(os.getenv('WINDIR'), 'Temp')
        clean_temp_files(temp_files_path, "Temporary Files")

        input("Press Enter to return to the menu...")
    elif choice == '5':
        # Clean all
        for directory in config.get('Cleaning', 'directories', fallback='').split(','):
            clean_temp_folder(directory.strip(), os.path.basename(directory.strip()))

        clean_browser_cache(chrome_cache_path, "Google Chrome")
        clean_browser_cache(firefox_cache_path, "Mozilla Firefox")

        clean_system_logs(windows_logs_path, "Windows Logs")

        clean_temp_files(temp_files_path, "Temporary Files")

        input("Press Enter to return to the menu...")
    elif choice == '6':
        configure_directories(config)
    elif choice == '7':
        # View cleaning log
        log_file_path = 'cleaning_log.txt'
        if os.path.exists(log_file_path):
            with open(log_file_path, 'r') as log_file:
                print("Cleaning Log:")
                print(log_file.read())
        else:
            print("No cleaning log found.")
        os.system("cls")
        input("Press Enter to return to the menu...")
    elif choice == '8':
        break
    else:
        os.system("cls")
        print(f"{Fore.RED}[ X ]{Style.RESET_ALL} Invalid choice. Please enter a valid option (1-8).")

# Save configuration
save_config(config)