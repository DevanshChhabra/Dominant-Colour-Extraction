# Dominant Colour Extraction

Deployment Link: [Dominant Colour Extraction](https://dominant-colour-extraction.onrender.com/)

This Streamlit application allows users to upload an image and extract the dominant colors using KMeans clustering. Here's a guide to understand and use the application effectively.

### Setup Instructions

1. **Clone the Repository**
    ```sh
    git clone https://github.com/DevanshChhabra/Dominant-Colour-Extraction.git
    cd Dominant-Colour-Extraction
    ```

2. **Install Dependencies**
    Ensure you have Python installed. Install required packages using pip:
    ```sh
    pip install streamlit scikit-learn numpy matplotlib Pillow
    ```

3. **Run the Application**  
    Execute the following command to start the Streamlit application:
    ```sh
    streamlit run master.py
    ```
    This will open a local server where you can interact with the application in your web browser.

### Usage Instructions

1. **Upload Image**

- Click on the "Choose an image" button to upload an image from your local machine.
- Supported formats include JPG, PNG, and others compatible with PIL.

2. **Select Number of Colors**

- Use the slider to select the number of dominant colors to extract from the image (from 1 to 10).

3. **View Results**

- The application displays the original image and below it, the modified image with reduced colors based on your selection.

### Customization

- **CSS Styling**

The application uses custom CSS for styling. You can modify the `designing.css` file to change the appearance of various elements like backgrounds, text colors, and gradients.

### Project Structure

- **master.py**: Contains the main Streamlit application code, including image processing and KMeans clustering.
- **designing.css**: Custom CSS file for styling elements within the Streamlit app.

### Dependencies

- **Streamlit**: Frontend framework for building interactive web applications with Python.
- **scikit-learn**: Used for KMeans clustering.
- **numpy**: Fundamental package for scientific computing with Python.
- **matplotlib**: Library for creating static, animated, and interactive visualizations in Python.
- **Pillow**: Python Imaging Library (PIL fork) for opening, manipulating, and saving many different image file formats.

### Notes

- Ensure that the Python environment where you run the application has all necessary packages installed.
- For production deployment, consider hosting the application on platforms like Heroku or AWS after adjusting configurations as necessary.

### Example

For a live demonstration, visit [Streamlit](https://streamlit.io/) and learn how to deploy Streamlit apps in the [documentation](https://docs.streamlit.io/).

### Credits

- This project utilizes Streamlit, scikit-learn, numpy, matplotlib, and Pillow, all of which are open-source libraries. Thanks to their contributors!

### License

- This project is licensed under [MIT License](LICENSE) - feel free to modify and distribute the code.
