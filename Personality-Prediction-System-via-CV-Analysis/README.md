# Personality Prediction System

## Overview
The Personality Prediction System is an AI-powered Flask application that analyzes resumes to predict personality traits of candidates, helping recruiters make data-driven hiring decisions. The system uses natural language processing (NLP) and machine learning techniques to extract information from resumes and generate personality insights.

## Features

- **Resume Analysis**: Supports multiple file formats (PDF, DOCX, TXT)
- **Information Extraction**: 
  - Personal Details
  - Contact Information
  - Educational Background
  - Work Experience
  - Skills Assessment
- **Personality Trait Prediction**: AI-driven analysis of candidate traits
- **History Management**: Track and export analysis results
- **Interactive Web Interface**: User-friendly resume upload and results display

## Prerequisites

- Python 3.8+
- Flask
- NLTK
- Pandas
- Google GenerativeAI API key

## Installation

1. Clone the repository:
```bash
git clone https://github.com/engrmumtazali0112/personality-prediction-system.git
cd personality-prediction-system
```

2. Create and activate a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install required dependencies:
```bash
pip install -r requirements.txt
```

4. Set up your Google GenerativeAI API key:
   - Visit https://makersuite.google.com/app/apikey
   - Create a new API key
   - Store it securely in your environment variables

## Project Structure

```
# TASK3/
# └── myenv/
#     └── Personality-Prediction/
#         ├── _pycache_/
#         ├── .idea/
#         ├── static/
#         ├── templates/
#         ├── uploads/
#         ├── .gitignore
#         ├── ai_prediction.py
#         ├── app.py
#         ├── education.txt
#         ├── extracted_data.csv
#         ├── LICENSE
#         ├── prediction.py
#         ├── README.md
#         ├── requirements.txt
#         ├── resume_dataset.csv
#         ├── resume_extraction.py
#         ├── skills.txt
#         ├── traits.txt
#         ├── workExp.txt
#         └── analyze
```

## Usage

1. Start the Flask server:
```bash
python app.py
```

2. Access the web interface:
   - Open a browser and navigate to `http://localhost:5000`
   - Upload a resume file
   - View the analyzed results

## API Endpoints

- `POST /analyze`: Submit a resume for analysis
- `GET /history`: Retrieve analysis history
- `POST /clear_history`: Clear analysis history
- `GET /export_data`: Export analysis data as CSV

## Technical Implementation

### Resume Processing Pipeline

1. **File Upload**:
   - Supports multiple document formats
   - Secure file handling
   - Temporary storage in uploads folder

2. **Text Extraction**:
   - Format-specific extraction using PyPDF2, textract, or docx
   - Text preprocessing and cleaning
   - NLTK tokenization

3. **Information Extraction**:
   - Named entity recognition for personal details
   - Pattern matching for contact information
   - Section-based parsing for education and experience
   - Skill identification and categorization

4. **Personality Analysis**:
   - Trait assignment based on extracted information
   - AI-powered personality description generation
   - Result compilation and presentation

### Data Management

- CSV-based storage for analysis history
- Export functionality for data portability
- History clearing capability

## Error Handling

The system includes comprehensive error handling for:
- Invalid file formats
- Missing files
- Processing errors
- API failures
- Database operations

## Security Considerations

- Secure file upload handling
- Input validation and sanitization
- Private data protection
- Temporary file cleanup

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/YourFeature`)
3. Commit your changes (`git commit -m 'Add YourFeature'`)
4. Push to the branch (`git push origin feature/YourFeature`)
5. Open a Pull Request

## Future Enhancements

- Machine learning model integration for improved predictions
- Multi-language support
- Batch processing capability
- Advanced visualization of personality traits
- API authentication
- Cloud storage integration
- Custom trait definition support

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- NLTK for natural language processing
- Google GenerativeAI for personality insights
- Flask framework for web implementation
- Open-source community for various supporting libraries

## Support

For support, please open an issue in the GitHub repository or contact the development team.