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

## 📸 Result

<details>
<summary>Click to view screenshots</summary>

![1](https://github.com/user-attachments/assets/97c2a4fe-15ba-4856-af9a-87e4a5ad79b7)

![2](https://github.com/user-attachments/assets/0b3aee98-8a49-4638-bd91-24e7c139be81)

![Resumi-1-images-0](https://github.com/user-attachments/assets/dc352ae2-3efb-4577-954a-b5609eb79cec)

![Resumi-1-images-1](https://github.com/user-attachments/assets/0d7e9e0d-8afc-4622-8127-908213680a2a)

![Resumi-1](https://github.com/user-attachments/assets/989b6357-2b55-4b9d-80f8-db64aff5cfc3)

![Resumi-1b](https://github.com/user-attachments/assets/99c5d6f9-3f70-4867-93be-800600e5626b)

![Resumi-3](https://github.com/user-attachments/assets/48fd73d9-178c-4a0f-b1dd-cd378325da9e)

![Resumi-3](https://github.com/user-attachments/assets/d6f29466-88ce-4cf3-9be0-ff208b3dcb9d)

![Resumi-3b](https://github.com/user-attachments/assets/ea3a9f49-0cd5-4cfb-9033-5242439ba154)

![Resumi-4](https://github.com/user-attachments/assets/4302655b-e978-41cd-b162-26b97c48ea3e)

![Resumi-4](https://github.com/user-attachments/assets/b76a5eca-c1ba-49d4-b71c-1696cd5bbf3b)

![Resumi-4b](https://github.com/user-attachments/assets/0570fad2-05b9-477a-a8ee-588ee1b415a2)

</details>


## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- pip package manager
- Google GenerativeAI API key

### Installation
```bash
# Clone the repository
git clone https://github.com/engrmumtazali0112/personality-prediction-system.git

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
This project is licensed under the MIT License - see the [LICENSE](https://github.com/engrmumtazali0112/Code_Clause_Internship_Artificial_Intelligence/blob/main/Personality-Prediction-System-via-CV-Analysis/LICENSE) file for details.



## 🙏 Acknowledgments
- NLTK for NLP capabilities
- Google GenerativeAI for personality insights
- Flask framework
- Open source community

## 📞 Contact

Mumtaz Ali - [engrmumtazali01@gmail.com](mailto:engrmumtazali01@gmail.com)

<p align="center">
  <a href="mailto:engrmumtazali01@gmail.com"><img src="https://img.shields.io/badge/Email-D14836?style=for-the-badge&logo=gmail&logoColor=white"/></a>
  <a href="https://www.linkedin.com/in/mumtaz-ali"><img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white"/></a>
  <a href="https://www.instagram.com/its_maliyzi"><img src="https://img.shields.io/badge/Instagram-E4405F?style=for-the-badge&logo=instagram&logoColor=white"/></a>
  <a href="https://x.com/mumtazali1223/status/1846913595021328672?s=51"><img src="https://img.shields.io/badge/X-1DA1F2?style=for-the-badge&logo=x&logoColor=white"/></a>
  <a href="https://discord.gg/DZgwHzEb"><img src="https://img.shields.io/badge/Discord-7289DA?style=for-the-badge&logo=discord&logoColor=white"/></a>
  <a href="https://wa.me/923476338292" target="_blank"><img src="https://img.shields.io/badge/WhatsApp-25D366?style=for-the-badge&logo=whatsapp&logoColor=white"/></a>
</p>

<p align="center">Made with ❤️ by Mumtaz Ali</p>
