import streamlit as st

def get_user_input():
    """
    Function to handle user input selection.
    Returns:
        input_mode (str): The selected input mode.
        file_data (UploadedFile/List[UploadedFile]/None): The uploaded file(s) or None.
    """
    # Title
    st.title("Image Enhancement Tool")

    # Step 1: Choose Input Mode
    st.subheader("Choose Input Mode:")
    input_mode = st.radio(
        "Select how you want to input the images:",
        ("Single File", "Batch Processing", "Real-Time Camera Feed")
    )

    file_data = None
    if input_mode == "Single File":
        file_data = st.file_uploader("Upload a single image", type=["jpg", "jpeg", "png"])
        if file_data:
            st.write("You have uploaded a single file.")

    elif input_mode == "Batch Processing":
        file_data = st.file_uploader("Upload multiple images", type=["jpg", "jpeg", "png"], accept_multiple_files=True)
        if file_data:
            st.write(f"You have uploaded {len(file_data)} files.")

    elif input_mode == "Real-Time Camera Feed":
        st.write("Real-time camera feed option selected.")
        st.write("Click 'Next' to set up the camera feed.")

    return input_mode, file_data
