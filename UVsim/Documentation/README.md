
# UVsim User Manual

## Project Setup

### Initial Setup

1. **Clone the Repository**
   ```sh
   git clone https://github.com/your-username/UVsim.git
   cd UVsim
   ```

2. **Set Up Virtual Environment**
   ```sh
   python -m venv UVsimVenv
   ```

3. **Activate the Virtual Environment**
   ```sh
   UVsimVenv\Scripts\activate  # On Windows
   # For MacOS/Linux use:
   # source UVsimVenv/bin/activate
   ```

4. **Install Requirements**
   ```sh
   pip install -r requirements.txt
   ```

### Running the Application

To start the UVsim GUI, simply run:
```sh
python uvsim_gui.py
```

## Menu Options and Their Functions

### File Menu

- **New Main Tab**: Creates a new main tab.
- **Open**: Opens a program file. This converts any 4-digit operations to 6-digit format if necessary and loads the content into the text area.
- **Save**: Saves the current program to the existing file.
- **Save As**: Prompts the user to choose a file path and saves the current program to that location.
- **Quit**: Exits the application.

### Edit Menu

- **Cut**: Cuts the selected text in the current text area.
- **Copy**: Copies the selected text in the current text area.
- **Paste**: Pastes the text from the clipboard into the current text area.

### Settings Menu

- **Color Scheme**: Opens a dialog to change the color scheme of the application. The changes are applied immediately and saved for future sessions.

## Instructions on Changing the Color Scheme

1. **Open the Settings Menu**
   - Click on the `Settings` menu in the menu bar.
   - Select `Color Scheme`.

2. **Choose a Color Scheme**
   - A dialog will appear allowing you to select the primary and secondary colors.
   - After selecting the colors, click `Apply` to change the color scheme.

## Instructions on Saving the File

### Before Running the Program

1. **Save the Program**
   - Click on the `File` menu.
   - Select `Save` to save the current program to the existing file.
   - If you need to save to a new file, select `Save As` and choose the desired file path.

### After Running the Program

1. **Save the Program Output**
   - Ensure that any changes or outputs from the program execution are visible in the text area.
   - Click on the `File` menu.
   - Select `Save` or `Save As` to save the output as needed.

## Additional Notes

- Ensure that the program does not exceed 250 lines.
- If any errors occur during file operations, appropriate error messages will be displayed in the diagnostic output area.
