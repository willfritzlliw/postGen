# PostGen

## Description
PostGen is a Python application designed to automate the creation of social media posts by combining images with inspirational quotes. It processes images, overlays text, and saves the generated posts, making it ideal for content creators, motivational accounts, or anyone looking to quickly generate engaging visual content.

## Features
- **Image Processing**: Automatically crops images to a standard size (1080x1350 pixels) suitable for various social media platforms.
- **Text Overlay**: Overlays randomly selected quotes onto the processed images.
- **Dynamic Text Wrapping**: Adjusts quote text to fit within the image boundaries.
- **Automated Content Generation**: Generates posts from a collection of images and quotes.
- **File Management**: Deletes original images after post generation to prevent reuse and manage storage.

## Requirements
- Python 3.x
- `Pillow` library
- `textwrap3` library
- `schedule` library

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/postgen.git
   cd postgen
   ```
2. Install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
1. Place your desired images in the `Mount/img` directory.
2. Add your quotes, one per line, in the `Mount/quotes.txt` file.
3. Run the `main.py` script:
   ```bash
   python main.py
   ```
   The generated posts will be saved in the `Mount/output` directory.

## Contributing
Contributions are welcome! Please feel free to submit pull requests or open issues for bugs and feature requests.

## License
This project is licensed under the MIT License - see the LICENSE file for details.