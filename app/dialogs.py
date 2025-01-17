from tkinter import Tk
from tkinter.filedialog import askopenfilename

def open_file_dialog(multiple=False):
    """Open file dialog to select a single image file."""
    root = Tk()
    root.withdraw()  # Hide the root window

    if multiple:
        file_paths = askopenfilename(
            title = "select image files",
            filetypes = [("Image files", "*.jpg;*.jpeg;*.png")]
        )
    else:
        file_paths = askopenfilename(
            title="Select an Image File",
            filetypes=[("Image files", "*.jpg;*.jpeg;*.png")]
        )
    root.destroy()  # Destroy the root window
    return file_paths
