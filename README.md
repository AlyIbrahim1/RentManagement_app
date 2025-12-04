# RentManager

## Overview
RentManager is a desktop application designed to help property managers track tenant status and generate printable PDF invoices. It uses a local SQLite database to store data and Python's ReportLab library to render documents.

## Features
*   **Database Management:** Add, Edit, and Delete tenant records.
*   **Tracking:** Monitor 'Months Late' and 'Amount Due'.
*   **Invoice Generation:** One-click PDF generation for specific properties.
*   **Data Persistence:** All data is saved locally to `rent_data.db`.

## Installation

1.  **Install Python:** Ensure Python 3.8+ is installed.
2.  **Install Dependencies:**
    Open your terminal or command prompt and run:
    ```bash
    pip install reportlab
    ```
3.  **Run the Application:**
    Navigate to the root directory and run:
    ```bash
    python main.py
    ```

## Usage Guide

### Adding a Renter
1.  Fill in the **Property Number** (Must be unique).
2.  Enter **Renter Name**, **Last Payment Date** (YYYY-MM-DD), **Months Late**, and **Amount Due**.
3.  Click **Save Record**.

### Generating an Invoice
1.  Select a renter from the list (or search by Property Number).
2.  Click the **Generate Invoice** button.
3.  The PDF will be created in the `invoices/` folder.

### Updating Data
1.  Click on any row in the data table to load the information into the input fields.
2.  Modify the data (e.g., update Amount Due).
3.  Click **Save Record** to update the existing entry.

## Project Structure
*   `src/database.py`: Handles all SQL interactions.
*   `src/invoice.py`: Contains the logic for drawing PDF forms.
*   `src/ui.py`: Contains the Tkinter GUI code.

## License
Private/Personal Use.
