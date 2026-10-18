import os
from pathlib import Path
import platform

def get_root_paths():
    """Get all root search paths based on OS"""
    system = platform.system()

    if system == "Windows":
        # Get all available drives in Windows
        import string
        drives = [
            f"{d}:\\" for d in string.ascii_uppercase
            if os.path.exists(f"{d}:\\")
        ]
        return drives

    elif system == "Darwin":  # Mac
        return ["/"]

    else:  # Linux
        return ["/"]


def find_file(filename: str) -> None:
    print("=" * 50)
    print(f"  Searching for : '{filename}'")
    print(f"  OS Detected   : {platform.system()}")
    print("=" * 50)

    root_paths   = get_root_paths()
    found_files  = []
    search_count = 0
    skip_dirs    = {
        # Windows skip dirs
        "Windows", "System32", "$Recycle.Bin", "ProgramData",
        "AppData", "SysWOW64", "WinSxS",
        # Mac/Linux skip dirs
        "proc", "sys", "dev", "run", "private",
        "cores", "Library", "System"
    }

    print(f"  Searching in  : {root_paths}\n")

    for root_path in root_paths:
        for root, dirs, files in os.walk(root_path):

            # Skip system directories for speed
            dirs[:] = [
                d for d in dirs
                if d not in skip_dirs and not d.startswith('.')
            ]

            search_count += 1

            # Show live search progress every 500 dirs
            if search_count % 500 == 0:
                print(f"  Searching... {root}", end="\r")

            # Check if file exists in current directory
            if filename in files:
                full_path = Path(root) / filename
                file_size = os.path.getsize(full_path)
                found_files.append({
                    "path"      : full_path,
                    "directory" : root,
                    "size"      : file_size
                })

    # Print results
    print("\n" + "=" * 50)
    if found_files:
        print(f"  ✅ Found {len(found_files)} match(es) for '{filename}':\n")
        for i, file in enumerate(found_files, 1):
            print(f"  {i}. File      : {file['path']}")
            print(f"     Directory : {file['directory']}")
            print(f"     Size      : {format_size(file['size'])}")
            print()
    else:
        print(f"  ❌ '{filename}' not found anywhere on the system!")
    print("=" * 50)


def format_size(size_bytes: int) -> str:
    """Convert bytes to human readable format"""
    if size_bytes < 1024:
        return f"{size_bytes} B"
    elif size_bytes < 1024 ** 2:
        return f"{size_bytes / 1024:.2f} KB"
    elif size_bytes < 1024 ** 3:
        return f"{size_bytes / 1024 ** 2:.2f} MB"
    else:
        return f"{size_bytes / 1024 ** 3:.2f} GB"


def main():
    print("\n========== File Finder ==========")
    filename = input("  Enter filename to search : ").strip()

    if not filename:
        print("  ❌ Error: Filename cannot be empty!")
        return

    find_file(filename)


if __name__ == "__main__":
    main()