from app.ui.input_ui import get_user_input

def main():
    # Step 1: Get user input
    input_mode, file_data = get_user_input()

    # Placeholder for next steps
    if st.button("Next"):
        st.write(f"Proceeding with input mode: {input_mode}.")
        if input_mode in ["Single File", "Batch Processing"] and file_data:
            st.write("Processing uploaded files...")
        elif input_mode == "Real-Time Camera Feed":
            st.write("Setting up camera feed...")

if __name__ == "__main__":
    main()
