import os
import shutil
import psutil   # For CPU, memory, and process monitoring
import platform  # For system information

def list_dir():
    return "\n".join(os.listdir())

def change_dir(path):
    try:
        os.chdir(path)
        return f"Changed directory to {os.getcwd()}"
    except FileNotFoundError:
        return f"No such directory: {path}"

def print_working_dir():
    return os.getcwd()

def make_dir(name):
    try:
        os.mkdir(name)
        return f"Directory '{name}' created."
    except FileExistsError:
        return f"Directory '{name}' already exists."

def remove(path):
    try:
        if os.path.isdir(path):
            shutil.rmtree(path)
            return f"Directory '{path}' removed."
        else:
            os.remove(path)
            return f"File '{path}' removed."
    except FileNotFoundError:
        return f"No such file or directory: {path}"

def system_stats():
    cpu = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory().percent
    return f"CPU Usage: {cpu}% | Memory Usage: {memory}%"

def list_processes():
    processes = []
    for p in psutil.process_iter(['pid', 'name']):
        processes.append(f"{p.info['pid']}: {p.info['name']}")
    return "\n".join(processes) if processes else "No running processes found."

def kill_process(pid):
    try:
        p = psutil.Process(int(pid))
        p.terminate()
        return f"Process {pid} terminated."
    except psutil.NoSuchProcess:
        return f"No such process with PID {pid}"
    except Exception as e:
        return f"Error terminating process: {str(e)}"

def system_info():
    return f"System: {platform.system()} {platform.release()} | Architecture: {platform.architecture()[0]}"

def help_menu():
    return """
Available Commands:
    ls                  - List files in current directory
    cd <dir>            - Change directory
    pwd                 - Print working directory
    mkdir <name>        - Create directory
    rm <file/dir>       - Remove file or directory
    stats               - Show CPU and memory usage
    ps                  - List running processes
    kill <pid>          - Kill process by PID
    info                - Show system information
    clear               - Clear the screen
    exit                - Exit terminal
    help                - Show this help menu
"""

def run_terminal():
    print("Python Command Terminal")
    print("Type 'help' to see available commands.")
    while True:
        try:
            command = input(f"{os.getcwd()} > ").strip().split()
            if not command:
                continue

            cmd, *args = command

            if cmd == "ls":
                print(list_dir())
            elif cmd == "cd":
                print(change_dir(args[0]) if args else "Usage: cd <directory>")
            elif cmd == "pwd":
                print(print_working_dir())
            elif cmd == "mkdir":
                print(make_dir(args[0]) if args else "Usage: mkdir <name>")
            elif cmd == "rm":
                print(remove(args[0]) if args else "Usage: rm <file/dir>")
            elif cmd == "stats":
                print(system_stats())
            elif cmd == "ps":
                print(list_processes())
            elif cmd == "kill":
                print(kill_process(args[0]) if args else "Usage: kill <pid>")
            elif cmd == "info":
                print(system_info())
            elif cmd == "clear":
                os.system('cls' if os.name == 'nt' else 'clear')
            elif cmd == "help":
                print(help_menu())
            elif cmd == "exit":
                print("Exiting terminal...")
                break
            else:
                print(f"Invalid command: {cmd}. Type 'help' for options.")

        except KeyboardInterrupt:
            print("\nUse 'exit' to quit the terminal.")
        except Exception as e:
            print(f"Error: {str(e)}")

if __name__ == "__main__":
    run_terminal()
