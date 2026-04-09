"""
Utility functions and helper tools that support the main engine (e.g., text cleaning, file I/O).
"""

import json
import os
from datetime import datetime

def save_result_to_json(data, filename_prefix="result"):
    """
    Saves the extracted AI data into a JSON file with a timestamp.
    """

    # Create 'output' directory if it doesn't exist
    output_dir = "output"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Generate a unique filename using the current time
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{filename_prefix}_{timestamp}.json"
    file_path = os.path.join(output_dir, filename)

    # Write data to the file
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

    print(f"--- Result successfully saved to: {file_path} ---")
    return file_path