from PIL import ImageGrab
import pytesseract
import re


# Function to capture the screen area and process the image for better OCR results
def capture_and_process_screen_area(x1, y1, x2, y2):
    screenshot = ImageGrab.grab(bbox=(x1, y1, x2, y2))
    processed_image = screenshot.convert("L")  # Convert to grayscale
    return processed_image


# Function to extract and parse text to find the number of items sold
def extract_num_items_sold(image):
    text = pytesseract.image_to_string(image)
    # Regular expression to match numbers and formats like '2.2k'
    num_sold_match = re.search(r"(\d+(\.\d+)?)(k)? sold", text, re.IGNORECASE)

    if num_sold_match:
        num_sold_str, _, is_thousand = num_sold_match.groups()
        num_sold = float(num_sold_str) * 1000 if is_thousand else float(num_sold_str)
        num_sold = int(num_sold)  # Convert to integer if it's a whole number
    else:
        num_sold = "Number of items sold not found"

    return num_sold


# Function to append the number of items sold to a text file and keep a running total
def append_to_file(num_sold, filename="items_sold.txt"):
    try:
        # If the file exists and is not empty, calculate the running total
        with open(filename, "r+") as file:
            lines = file.readlines()
            last_line = lines[-1] if lines else "Total Sold: 0"
            # Extract only the number from the last line
            current_total = int(re.search(r"(\d+)", last_line).group())
            new_total = current_total + int(num_sold)
            file.write(f"{num_sold} (New Total: {new_total})\n")
    except FileNotFoundError:
        # If the file does not exist, start a new file and write the first entry
        with open(filename, "w") as file:
            file.write(f"{num_sold} (New Total: {num_sold})\n")
    except ValueError:
        # Handle cases where the number cannot be converted to int
        with open(filename, "a") as file:
            file.write(f"{num_sold} (Unable to calculate total due to format error)\n")


# Main flow
def main():
    # Capture part of the screen where the number of items sold is located
    screenshot_image = capture_and_process_screen_area(600, 250, 1000, 500)

    # Extract and parse the text for the number of items sold
    num_items_sold = extract_num_items_sold(screenshot_image)

    # Append the number of items sold to the text file
    append_to_file(num_items_sold)

    # Print the extracted information
    print(f"Number of Items Sold: {num_items_sold}")


# Run the main function
main()
