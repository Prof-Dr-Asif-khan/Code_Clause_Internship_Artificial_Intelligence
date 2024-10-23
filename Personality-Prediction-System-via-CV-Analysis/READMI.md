# Personality Prediction System
![Python](https://img.shields.io/badge/python-3.8+-blue.svg)
![Framework](https://img.shields.io/badge/framework-flask-green.svg)
![License](https://img.shields.io/badge/license-MIT-blue.svg)

## 🎯 Project Overview
An AI-powered system that analyzes resumes to predict personality traits, helping recruiters make data-driven hiring decisions. The system uses Natural Language Processing (NLP) and Machine Learning to extract information from CVs and generate personality insights.

## ✨ Key Features
- 📄 Multi-format resume parsing (PDF, DOCX, TXT)
- 🤖 AI-powered personality trait prediction
- 📊 Comprehensive candidate analysis
- 💾 Analysis history management
- 📱 Responsive web interface

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- pip package manager
- Google GenerativeAI API key

### Installation
```bash
# Clone the repository
git clone https://github.com/yourusername/personality-prediction-system.git

# Navigate to project directory
cd personality-prediction-system

# Create virtual environment
python -m venv myenv

# Activate virtual environment
# For Windows:
myenv\Scripts\activate
# For Unix/Linux:
source myenv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Set up environment variables
cp .env.example .env
# Add your Google GenerativeAI API key to .env file
```

### Running the Application
```bash
python app.py
```
Visit `http://localhost:5000` in your browser.

## 📁 Project Structure
```
personality-prediction-system/
├── myenv/
├── _pycache_/
├── .idea/
├── static/
│   ├── css/
│   ├── js/
│   └── img/
├── templates/
│   ├── index.html
│   └── result.html
├── uploads/
├── ai_prediction.py
├── app.py
├── prediction.py
├── resume_extraction.py
├── education.txt
├── extracted_data.csv
├── requirements.txt
├── resume_dataset.csv
├── skills.txt
├── traits.txt
├── workExp.txt
├── analyze
├── .gitignore
├── LICENSE
└── README.md
```

## 💻 Usage

1. **Upload Resume**
   - Support for PDF, DOCX, and TXT formats
   - Secure file handling

2. **View Analysis**
   - Extracted information display
   - Personality trait predictions
   - AI-generated insights

3. **Manage History**
   - View previous analyses
   - Export data as CSV
   - Clear history

## 🛠️ Technical Implementation

### Resume Processing Pipeline
1. **File Upload & Validation**
2. **Text Extraction & Preprocessing**
3. **Information Extraction**
4. **Personality Analysis**
5. **Result Generation**

### API Endpoints
```python
POST /analyze          # Submit resume for analysis
GET /history          # Retrieve analysis history
POST /clear_history   # Clear analysis history
GET /export_data      # Export analysis data
```

## 🤝 Contributing

1. Fork the repository
2. Create feature branch (`git checkout -b feature/YourFeature`)
3. Commit changes (`git commit -m 'Add YourFeature'`)
4. Push to branch (`git push origin feature/YourFeature`)
5. Open Pull Request

## 📋 Development Roadmap

- [ ] Enhanced ML model integration
- [ ] Multi-language support
- [ ] Batch processing
- [ ] Advanced visualization
- [ ] API authentication
- [ ] Cloud storage integration

## 📄 License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments
- NLTK for NLP capabilities
- Google GenerativeAI for personality insights
- Flask framework
- Open source community

## 📧 Contact
- GitHub: [@yourusername](https://github.com/yourusername)
- Email: your.email@example.com

---
