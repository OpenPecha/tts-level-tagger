import pandas as pd

# Define the syllable counting function
def count_syllables(text):
    """
    Counts the syllables in a text based on specific Tibetan delimiters.

    Args:
        text (str): Input text.

    Returns:
        int: Number of syllables in the text.
    """
    return text.count('་') + text.count('།') - text.count('་།')

# Define the level determination function
def determine_level(syllable_count):
    """
    Determines the difficulty level based on the syllable count.

    Args:
        syllable_count (int): Count of syllables in the text.

    Returns:
        str: Difficulty level ('easy', 'medium', or 'hard').
    """
    if syllable_count <= 17:
        return 'easy'
    elif 17 < syllable_count <= 34:
        return 'medium'
    else:
        return 'hard'

# Main function
def add_level_based_on_syllable_count(input_file, output_file):
    """
    Adds a 'level' column to the CSV based on syllable count in the 'target' column.

    Args:
        input_file (str): Path to the input CSV file.
        output_file (str): Path to save the updated CSV file.
    """
    try:
        # Load the CSV file
        df = pd.read_csv(input_file)

        # Ensure 'target' column exists
        if 'target' not in df.columns:
            raise KeyError("The input file must contain a 'target' column.")

        # Calculate syllable counts and difficulty levels
        df['syllable_count'] = df['target'].apply(count_syllables)
        df['level'] = df['syllable_count'].apply(determine_level)

        # Drop the intermediate syllable_count column if not needed
        df = df.drop(columns=['syllable_count'])

        # Save the updated DataFrame to a new CSV file
        df.to_csv(output_file, index=False)

        print(f"Updated CSV with 'level' column saved to {output_file}. Total rows: {len(df)}")
    except FileNotFoundError:
        print("Input file not found. Please check the file path.")
    except KeyError as e:
        print(f"KeyError: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Example usage
input_csv = "data/contribution/training - training (1).csv"  # Replace with your input file path
output_csv = "data/contribution/level.csv"  # Replace with your desired output file path

add_level_based_on_syllable_count(input_csv, output_csv)
