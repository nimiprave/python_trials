import numpy as np
import simpleaudio as sa
import time


def generate_click_sound(frequency=800, duration=0.05, volume=0.5):
    """
    Generates a short click-like sound.

    Args:
        frequency (int): The frequency of the sound in Hz.
        duration (float): The duration of the sound in seconds.
        volume (float): The volume of the sound (0.0 to 1.0).

    Returns:
        numpy.ndarray: A numpy array representing the sound waveform.
    """
    # Audio properties
    sample_rate = 44100  # samples per second
    t = np.linspace(0, duration, int(sample_rate * duration), False)

    # Generate a sine wave for the click sound
    # We'll use a decaying amplitude to make it sound more like a click
    amplitude_envelope = np.exp(-15 * t)  # Exponential decay
    audio = volume * np.sin(frequency * t * 2 * np.pi) * amplitude_envelope

    # Normalize to 16-bit range and convert to integers
    audio *= 32767 / np.max(np.abs(audio))
    audio = audio.astype(np.int16)
    return audio


def display_table_with_sound(data):
    """
    Displays a table in the console, playing a keyboard sound for each row.

    Args:
        data (list of dict): A list of dictionaries, where each dictionary
                              represents a row and its keys are column headers.
    """
    if not data:
        print("No data to display.")
        return

    # Generate the click sound once
    click_sound = generate_click_sound()

    # Get column headers from the first dictionary
    headers = list(data[0].keys())
    # Calculate maximum width for each column
    column_widths = {header: len(header) for header in headers}
    for row in data:
        for header in headers:
            column_widths[header] = max(
                column_widths[header], len(str(row.get(header, ''))))

    # Print header row
    header_line = " | ".join(
        f"{header:<{column_widths[header]}}" for header in headers)
    print("-" * len(header_line))
    print(header_line)
    print("-" * len(header_line))

    # Print data rows with sound
    for row_data in data:
        # Play the sound before printing the row
        play_obj = sa.play_buffer(click_sound, 1, 2, 44100)
        play_obj.wait_done()  # Wait for the sound to finish before printing the next row
        time.sleep(0.05)  # Small delay to simulate typing rhythm

        row_str = " | ".join(
            f"{str(row_data.get(header, '')):<{column_widths[header]}}" for header in headers)
        print(row_str)


# --- Example Usage ---
if __name__ == "__main__":
    # Sample data for the table
    sample_data = [
        {"Name": "Alice", "Age": 30, "City": "New York"},
        {"Name": "Bob", "Age": 24, "City": "Los Angeles"},
        {"Name": "Charlie", "Age": 35, "City": "Chicago"},
        {"Name": "Diana", "Age": 28, "City": "Houston",
            "Occupation": "Engineer"},  # Example with an extra column
        {"Name": "Eve", "Age": 22, "City": "Miami"}
    ]

    print("Displaying table with keyboard sounds...\n")
    display_table_with_sound(sample_data)
    print("\nTable display complete.")
