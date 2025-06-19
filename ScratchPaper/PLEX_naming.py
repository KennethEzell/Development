import pandas as pd
import os
import re

def get_user_input():
    """
    Prompts the user for show information and validates input.
    
    Returns:
        tuple: (title, episodes, season) - cleaned and formatted user inputs
    """
    # Get show title and format it with title case (first letter of each word capitalized)
    title = input("What is the title of your show?: ").strip().title()
    
    # Get number of episodes with input validation
    while True:
        try:
            episodes = int(input("How many episodes in the season?: "))
            if episodes <= 0:
                print("Please enter a positive integer.")
            else:
                break  # Valid input received, exit the loop
        except ValueError:
            print("Invalid input. Please enter a positive integer.")
    
    # Get season number and format it with leading zero (e.g., "1" becomes "01")
    season = input("Which season is it?: ").zfill(2)
    
    return title, episodes, season

def generate_episode_names(title, episodes, season):
    """
    Generates a list of episode names in Plex naming format.
    
    Args:
        title (str): The show title
        episodes (int): Number of episodes in the season
        season (str): Season number (zero-padded)
    
    Returns:
        list: List of formatted episode names (e.g., "Show Name-s01e01")
    """
    # Create list of episode names using list comprehension
    # Format: "Title s##e##" where ## are zero-padded numbers
    ep_names = [f"{title}-s{season}e{x:02d}" for x in range(1, episodes+1)]
    return ep_names

def create_plex_df(ep_names):
    """
    Creates a pandas DataFrame from the episode names list.
    
    Args:
        ep_names (list): List of episode names
    
    Returns:
        DataFrame: Pandas DataFrame with episode names in 'Name' column
    """
    # Create DataFrame with episode names in a column called 'Name'
    plex_df = pd.DataFrame(ep_names, columns=['Name'])
    return plex_df

def save_to_excel(df, title):
    """
    Saves the DataFrame to an Excel file in the specified directory.
    
    Args:
        df (DataFrame): The DataFrame to save
        title (str): The show title (used for filename)
    """
    # Define the target directory where Excel files should be saved
    target_directory = r"C:\SUMMER-2024-PROGRAMMING-CONCEPTS\Plex Excel Output"
    
    # Create the directory if it doesn't exist
    if not os.path.exists(target_directory):
        os.makedirs(target_directory)
        print(f"Created directory: {target_directory}")
    
    # Clean the title to make it safe for use as a filename
    # Remove or replace characters that are invalid in Windows filenames
    safe_title = re.sub(r'[<>:"/\\|?*]', '_', title)
    
    # Create the full file path
    filename = f"{safe_title}.xlsx"
    full_path = os.path.join(target_directory, filename)
    
    # Display the full path where the file will be saved
    print(f"Saving file to: {full_path}")
    
    try:
        # Save the DataFrame to Excel file
        df.to_excel(full_path, index=False)
        print(f"✓ File successfully saved as: {filename}")
        print(f"✓ Location: {target_directory}")
    except Exception as e:
        print(f"✗ Error saving file: {e}")

def main():
    """
    Main function that orchestrates the entire process.
    """
    print("=== Kenneth's Awesome Plex Episode Naming Tool ===")
    print("This tool generates episode names for Plex media server.\n")
    
    # Step 1: Get user input
    title, episodes, season = get_user_input()
    
    # Step 2: Generate episode names
    ep_names = generate_episode_names(title, episodes, season)
    
    # Step 3: Display the generated episode names
    print(f"\nGenerated {len(ep_names)} episode names:")
    print("-" * 40)
    print("\n".join(ep_names))
    print("-" * 40)
    
    # Step 4: Create DataFrame
    plex_df = create_plex_df(ep_names)
    
    # Step 5: Display DataFrame preview
    print(f"\nDataFrame Preview:")
    print(plex_df)
    
    # Step 6: Save to Excel
    print(f"\nSaving to Excel...")
    save_to_excel(plex_df, title)
    
    print("\n=== Process Complete ===")

# Entry point - only run if this script is executed directly (not imported)
if __name__ == "__main__":
    main()