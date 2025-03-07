# farsi_synthetic_data
Create synthetic data Farsi language
## Overview
This repository contains a script to generate synthetic Farsi language data for OCR (Optical Character Recognition) purposes.

## Requirements
- Python 3.x
- Required Python packages (listed in `requirements.txt`)
## Features
- Generates synthetic Farsi text images for OCR training.
- Supports multiple fonts and background images.
- Customizable parameters for number of samples, font directory, and background directory.

## Configuration
Before running the script, ensure that you have the following directories and files:
- `fonts/`: Directory containing Farsi `.ttf` font files.
- `backgrounds/`: Directory containing background images (optional).

## Logging
The script logs its activities to `sentatic_data_generator.log` for debugging and tracking purposes.
## Installation
1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/farsi_synthetic_data.git
    ```
2. Navigate to the project directory:
    ```sh
    cd farsi_synthetic_data
    ```
3. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

## Usage
To generate synthetic data, run the following command:
```sh
python sentatic_data_generator.py --output_dir /path/to/output
```
You can specify additional parameters as needed:
- `--num_samples`: Number of synthetic images to generate (default: 1000)
- `--font_dir`: Directory containing Farsi fonts (default: `./fonts`)
- `--background_dir`: Directory containing background images (default: `./backgrounds`)

Example:
```sh
python sentatic_data_generator.py --output_dir ./output --num_samples 500 --font_dir ./fonts --background_dir ./backgrounds
```

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements
Special thanks to the contributors and the open-source community for their valuable resources and support.