#### Data Management Practices

This directory (`data/raw`) is used for storing raw, unprocessed data for the ACME-LO project. It serves as the initial repository for data collected from various sources before any preprocessing or transformation occurs.

#### Data Formats

The raw data stored in this directory can be in various formats, including:

- CSV (Comma-Separated Values)
- JSON (JavaScript Object Notation)
- Image files (e.g., PNG, JPEG)
- Text files (e.g., TXT)

#### Storage Conventions

To maintain organization and traceability, we follow the following storage conventions:

- Each dataset is stored in its own subdirectory within `data/raw`.
- Filenames are descriptive and include relevant metadata, such as the date of acquisition or source information.

#### Preprocessing Steps

Raw data in this directory may require preprocessing before it can be used for training models or analysis. Preprocessing steps may include:

- Data cleaning and quality checks
- Data normalization and scaling
- Feature extraction
- Handling missing values
- Encoding categorical variables

#### Data Privacy and Security

Data stored in this directory may contain sensitive or private information. It is essential to follow best practices for data privacy and security:

- Access to this directory should be restricted to authorized personnel only.
- Ensure compliance with relevant data protection regulations (e.g., GDPR).
- Anonymize or pseudonymize data when necessary to protect privacy.
- Regularly audit and monitor access to the data.
