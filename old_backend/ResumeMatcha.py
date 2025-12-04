import random
import csv
from difflib import SequenceMatcher

# Job descriptions
job_descriptions = [
    "Sales Manager Intern",
    "Software Development Engineer (SDE) Intern",
    "Frontend Developer Intern",
    "Backend Developer Intern",
    "Full Stack Developer Intern",
    "Mobile Application Developer Intern",
    "DevOps Engineer Intern",
    "QA (Quality Assurance) / Test Engineer Intern",
    "Data Analyst Intern",
    "Data Scientist Intern",
    "Machine Learning Engineer Intern",
    "Artificial Intelligence Intern",
    "Cloud Engineer Intern",
    "Network Engineer Intern",
    "Cybersecurity Analyst Intern",
    "System Administrator (SysAdmin) Intern",
    "Embedded Systems Engineer Intern",
    "Product Management Intern (Technical)",
    "UI/UX Designer Intern",
    "Project Manager / IT Project Coordinator",
    "Management Consultant",
    "Scrum Master",
    "Product Marketing Manager",
    "SEO Specialist",
    "Customer Success Manager",
    "Implementation Consultant"
]

# Resume data - Batch 1
resumes_batch1 = [
    {"name": "Armaan Gogoi", "email": "armaangogoi2004@gmail.com", "cgpa": 9.89, 
    "skills": ["C", "C++", "Python", "JavaScript", "React", "Node.js", "Express.js", "MongoDB", "OpenCV"],
    "experience": ["GDSC - Core Member"], "projects": ["GDSC Website", "CampusHire", "Internship and Placement Portal"],
    "achievements": ["MERIT Scholarship-I: Full scholarship"]},
    
    {"name": "Kavya Mahajan", "email": "kmahajan1be23@thapar.edu", "cgpa": 9.81,
    "skills": ["C/C++", "Python", "JavaScript", "Django", "Flask", "FastAPI", "TensorFlow", "InceptionNet", "ResNet", "Docker"],
    "experience": ["Summer Intern - ML Research", "Research Intern - IoT Engineer"],
    "projects": ["Sampat Sevak", "Gesture Controlled 6 DoF Robotic Arm"],
    "achievements": ["Gold Medal / First Place in B.E. Computer Engineering"]},
    
    {"name": "Madhav Gupta", "email": "madhavgupta3205@gmail.com", "cgpa": 9.72,
    "skills": ["C", "C++", "Python", "JavaScript", "React", "Tailwind CSS", "MERN", "Pandas", "NumPy"],
    "experience": ["Full Stack Developer Intern", "Full Stack Web Developer", "NASA Space Apps - Local Lead"],
    "projects": ["Qwerty Type - Typing Test", "AI Voice Assistant"],
    "achievements": ["Merit scholarship for academic performance"]},
    
    {"name": "Dhruv Kamboj", "email": "dkamboj_be23@thapar.edu", "cgpa": 9.96,
    "skills": ["C/C++", "Python", "TensorFlow/Keras", "YOLO", "OpenCV", "pandas", "NumPy"],
    "experience": [], "projects": ["Robotic Buggy with Arduino", "Voice-Based Scene Classification", "Object Detection with YOLO & OpenCV"],
    "achievements": ["Active in sports and extracurriculars"]},
    
    {"name": "Dhruv Dhanuka", "email": "dhruvdhanuka315", "cgpa": 9.83,
    "skills": ["C++", "Python", "Flask", "MySQL", "HTML/CSS", "JavaScript", "React", "Git"],
    "experience": [], "projects": ["Fooddle—Campus Event Ordering Platform", "LibraryEase"],
    "achievements": ["350+ LeetCode problems solved"]},
    
    {"name": "Dhruv Sethi", "email": "dhruvsethi590@gmail.com", "cgpa": 9.76,
    "skills": ["Python", "scikit-learn", "pandas", "HTML/CSS", "JavaScript", "SQL", "R", "MATLAB"],
    "experience": [], "projects": ["Heart Disease Prediction using ML", "Blood Bank Management System"],
    "achievements": ["Reliance Foundation Undergraduate Scholarship"]},
    
    {"name": "Disha Malik", "email": "dishamalik792@gmail.com", "cgpa": 9.77,
    "skills": ["Python", "OpenCV", "Machine Learning", "SQL", "HTML/CSS", "JavaScript"],
    "experience": ["Marketing Executive - Saturnalia"],
    "projects": ["Face Detection", "StreamX – OTT Platform", "Delivery Route Optimization"],
    "achievements": ["Full tuition scholarship"]},
    
    {"name": "Bhumi Garg", "email": "bhumigarg52@gmail.com", "cgpa": 9.90,
    "skills": ["HTML", "CSS", "JavaScript", "React (in progress)", "UI/UX", "Netlify", "Power BI"],
    "experience": [], "projects": ["CampusMate – Smart Student Dashboard", "Personal Portfolio"],
    "achievements": ["High school percentages: 96.67%"]},
    
    {"name": "Gautam Jain", "email": "jaing7424@gmail.com", "cgpa": 9.73,
    "skills": ["C", "C++", "Dart", "Flutter", "Node.js", "Express", "MongoDB", "Firebase"],
    "experience": ["Flutter Developer Intern"],
    "projects": ["MedApp", "Attendity"],
    "achievements": ["Participant in HackTU 2025"]},
    
    {"name": "Hardik Tandon", "email": "htandon_be23@thapar.edu", "cgpa": 9.84,
    "skills": ["C/C++", "Python", "NumPy", "Pandas", "Scikit-learn", "YOLO", "Oracle SQL", "HTML/CSS"],
    "experience": [], "projects": ["Flight Management System", "Vehicle Detection and Counting System", "Disease Prediction System"],
    "achievements": ["Selected for Smart India Hackathon (SIH) 2024"]}
]

# Resume data - Batch 2
resumes_batch2 = [
    {"name": "Khushnoor Kaur", "email": "khushnoorgoraya@gmail.com", "cgpa": 9.91,
    "skills": ["C++", "Python", "R", "SQL", "HTML/CSS", "JavaScript", "NumPy", "Pandas", "Scikit-learn", "IndicBERT", "LightGBM", "XGBoost"],
    "experience": [], "projects": ["Emotion Aware Virtual Assistant for Indic Languages", "AI Powered Hospital Navigation System"],
    "achievements": ["1st rank in Computer Engineering branch", "Merit 1 Scholarship"]},
    
    {"name": "Kritika", "email": "kkritika_be23@thapar.edu", "cgpa": 9.73,
    "skills": ["C", "C++", "Python", "SQL", "HTML/CSS", "JavaScript", "React", "NumPy", "Pandas", "OpenCV", "Matplotlib", "Vision Transformers"],
    "experience": ["Summer Intern (Research) - IIT Jodhpur"],
    "projects": ["Malicious PDF Detector", "Election Voting System"],
    "achievements": ["Co-author in NTIRE 2025 CVPR Workshop paper", "Merit-1 Scholarship"]},
    
    {"name": "Darshan Subedi", "email": "subedidarshan02@gmail.com", "cgpa": 9.70,
    "skills": ["JavaScript", "TypeScript", "React", "Next.js", "Node.js", "Express", "FastAPI", "MongoDB", "Prisma", "Docker"],
    "experience": [], "projects": ["Dropin - Secure File Sharing", "Rinflow - AI Loan Origination", "Trimly - Media Compression"],
    "achievements": ["Merit-II Scholarship", "300+ DSA problems solved"]},
    
    {"name": "Kangan Arora", "email": "kanganarora6@gmail.com", "cgpa": 9.76,
    "skills": ["Python", "C/C++", "R", "SQL", "HTML/CSS", "JavaScript", "Pandas", "Scikit-learn"],
    "experience": [], "projects": ["AI Based Obstacle Detection System", "House Price Prediction with Regularization"],
    "achievements": ["District Topper in Class 12", "University Scholarship"]},
    
    {"name": "Namanmeet Singh", "email": "namanmeet@example.com", "cgpa": 9.68,
    "skills": ["Python", "C", "C++", "JavaScript", "Django", "Node.js", "React", "Three.js", "Docker", "Redis", "GCP/AWS", "OpenCV", "LLMs/GenAI"],
    "experience": ["Cybersecurity & ML Research Intern - C3i Hub IIT Kanpur", "PRISM Research Intern - Samsung R&D", "Drone Engineer - Indian Army"],
    "projects": ["Anti Drone System for Indian Army", "3D Virtual Museum"],
    "achievements": ["Top selections in AlgoUniversity", "Class 10: 99.2%"]},
    
    {"name": "Pooja Bisht", "email": "poojabishtdoon@gmail.com", "cgpa": 9.83,
    "skills": ["C++", "C", "Python", "Java", "HTML/CSS", "JavaScript", "Scikit-learn", "OpenCV", "React", "Tailwind CSS"],
    "experience": ["AI-ML Research Intern - DRDO"],
    "projects": ["AIxCHANGE – AI Marketplace", "Motionmatics"],
    "achievements": ["Merit-1 scholarship", "Runner-up in CCS Coding Marathon"]},
    
    {"name": "Arshia Bagchi", "email": "arshiabagchi@gmail.com", "cgpa": 9.68,
    "skills": ["PyTorch", "TensorFlow", "Vision Transformers", "Deep Learning", "Computer Vision", "Python", "MATLAB", "Cloud (IBM)"],
    "experience": ["Summer Intern - IIST Trivandrum", "IBM SkillsBuild Internship"],
    "projects": ["Deep Learning Framework for Phase Unwrapping"],
    "achievements": ["ICSE 97.6%, ISC 96.75%", "Multiple ML bootcamp certifications"]},
    
    {"name": "Eshika", "email": "eshikajindal2412@gmail.com", "cgpa": 9.76,
    "skills": ["Python", "C", "C++", "R", "HTML", "SQL"],
    "experience": [], "projects": ["Loan Approval System", "Fake Review Detector"],
    "achievements": ["12th: 96%, 10th: 97%"]},
    
    {"name": "Parth Arora", "email": "partharora0123@gmail.com", "cgpa": 9.74,
    "skills": ["Go", "C++", "Python", "Docker", "AWS", "PostgreSQL", "Oracle", "gRPC", "REST APIs"],
    "experience": [], "projects": ["AI-Based Traffic Management System", "AI-Based Face Detection", "Auction Bidding System"],
    "achievements": ["College scholarship holder", "State gold medalist in shooting"]},
    
    {"name": "Prabhsimar Singh Batra", "email": "simarprabh095@gmail.com", "cgpa": 9.79,
    "skills": ["C", "C++", "Python", "JavaScript", "R", "SQL", "PL/SQL", "Scikit-learn", "PyPDF2"],
    "experience": [], "projects": ["Malicious PDF Detector", "Car Rental Management System"],
    "achievements": ["Merit-III Scholarship"]}
]

# Resume data - Batch 3 (NEW - from document 2)
resumes_batch3 = [
    {"name": "Mannan Jain", "email": "mannanjain2005@gmail.com", "cgpa": 9.58,
    "skills": ["C++", "Python", "NumPy", "Pandas", "Scikit-learn", "TensorFlow", "Keras", "HTML", "CSS", "JavaScript", "R", "SQL", "Git"],
    "experience": ["Research Intern (Cybersecurity) - IIT Delhi", "Product Development Intern - Wiom"],
    "projects": ["Loan Approval and Risk Analysis System", "Automated Attendance System", "AutoMetaML"],
    "achievements": ["Gold medalist", "Scholar Badge holder", "10.0 GPA in 2nd semester"]},
    
    {"name": "Ajay Goyal", "email": "ajaygoyal6081@gmail.com", "cgpa": 9.64,
    "skills": ["C", "C++", "Python", "SQL", "Machine Learning", "PL/SQL"],
    "experience": [], "projects": ["Credit Card Fraud Detection System", "Insurance Management System (DBMS)", "Autonomous Buggy"],
    "achievements": ["200+ solved problems on LeetCode", "NVIDIA certified getting started with deep learning"]},
    
    {"name": "Ananya Pahwa", "email": "ananyapahwa.jobs@gmail.com", "cgpa": 9.58,
    "skills": ["C", "C++", "Python", "JavaScript", "Node.js", "Express", "React", "SQL", "OracleDB", "Docker"],
    "experience": ["Backend Intern - Medlr"],
    "projects": ["DSA Questions Organizer", "PhysioCare Portal", "Airport Management System"],
    "achievements": ["Second Runner-Up at Israel-Indian Hackathon", "Core member, Google Developer Student Club"]},
    
    {"name": "Bhoomika", "email": "bhoomika007b@gmail.com", "cgpa": 9.65,
    "skills": ["Python", "C/C++", "R", "SQL", "NumPy", "Pandas", "Scikit-learn", "Arduino", "SolidWorks"],
    "experience": [], "projects": ["EatWise – AI Restaurant Recommender", "IoT Obstacle & Thermal Sensing", "Nvis 3302 Robocar"],
    "achievements": ["Completed Deloitte Data Analytics virtual internship", "Nvidia Deep Learning workshop attendee"]},
    
    {"name": "Siddharth Jaswal", "email": "sjaswal1_be23@thapar.edu", "cgpa": 9.60,
    "skills": ["C", "C++", "Python", "Node.js", "Express", "MongoDB", "React", "OpenCV", "Flask"],
    "experience": [], "projects": ["Venti-Cure", "Camp-Ground Explorer", "Disease Prediction System"],
    "achievements": ["Top 3 in Israeli-Indian Hackathon", "LeetCode global rank top 3%", "Merit-3 Scholarship"]},
    
    {"name": "Fareen Garg", "email": "fgarg_be23@thapar.edu", "cgpa": 9.63,
    "skills": ["C", "C++", "Python", "Oracle SQL", "R", "MATLAB", "React (in progress)", "Tailwind"],
    "experience": [], "projects": ["Huffman File Zipper", "Bitcoin Price Predictor (LSTM)", "Password Generator Web App"],
    "achievements": ["Core member of Linux Users Group", "merit-based scholarship"]},
    
    {"name": "Iri Rawal", "email": "irirawal@gmail.com", "cgpa": 9.62,
    "skills": ["Python", "C", "C++", "R", "Dart", "TensorFlow", "ViT", "BERT", "XGBoost", "SQL", "PL/SQL", "Flutter"],
    "experience": [], "projects": ["Multimodal Stress Detection", "Airport Operations Database System", "Intelligent Crop Advisor"],
    "achievements": ["Active in OWASP and EDC", "research and publication in multimodal fusion"]},
    
    {"name": "Lakshay Sawhney", "email": "lsawhney07@gmail.com", "cgpa": 9.58,
    "skills": ["Python", "C", "C++", "SQL", "Django", "REST", "BM25", "E5", "MiniLM", "XGBoost", "Docker", "AWS"],
    "experience": ["AI Intern - NLP & IR - DRDO"],
    "projects": ["Thapar Go W", "Stock Pulse W"],
    "achievements": ["Merit-I scholarship", "multiple hackathon awards"]},
    
    {"name": "Nishtha Gupta", "email": "nishtha19gupta@gmail.com", "cgpa": 9.59,
    "skills": ["Python", "C", "C++", "MySQL", "Pandas", "Scikit-learn", "NumPy", "OpenCV"],
    "experience": [], "projects": ["Movie Recommendation System", "Credit Card Fraud Detection", "Air Canvas – Virtual Drawing App"],
    "achievements": ["Merit Scholarship recipient", "active in Linux user group"]},
    
    {"name": "Akshat Aggarwal", "email": "aaggarwal2_be23@thapar.edu", "cgpa": 9.67,
    "skills": ["Python", "C/C++", "JavaScript", "React", "PyTorch", "OpenCV", "Next.js", "TailwindCSS"],
    "experience": [], "projects": ["Sehaj – Medical Platform", "LLM Student Model (Distillation)"],
    "achievements": ["Finalist HackTU 5.0", "executive board member for Fine Arts & Photography Society"]}
]

# Resume data - Batch 4 (NEW - from document 3)
resumes_batch4 = [
    {"name": "Aditya Dhyani", "email": "adhyani_be23@thapar.edu", "cgpa": 9.74,
    "skills": ["C", "C++", "Python", "SQL", "MySQL", "Arduino IDE", "Ubuntu", "OpenCV"],
    "experience": [],
    "projects": ["Live Paint Cam", "Agent Response to Dynamic Environments", "Collaborative Reading Platform"],
    "achievements": ["Strong communication and teamwork", "High adaptability"]},
    
    {"name": "Aditya Paliwal", "email": "adityapaliwal2004@gmail.com", "cgpa": 9.77,
    "skills": ["C", "C++", "Python", "SQL", "MATLAB", "R", "Git", "AutoCAD"],
    "experience": ["AI/ML Intern - CNH Industrial"],
    "projects": ["Flight Management System", "Student Performance Predictor"],
    "achievements": ["NDA AIR-188"]},
    
    {"name": "Ananya Gupta", "email": "guptaananya770@gmail.com", "cgpa": 9.68,
    "skills": ["Python", "C/C++", "HTML/CSS", "R", "SQL", "JavaScript", "TensorFlow", "OpenCV"],
    "experience": ["Python-ML Intern - IGDTUW"],
    "projects": ["Smart Fleet Optimizer", "Brain Tumor Classification", "Face-Recognition Attendance System"],
    "achievements": ["Merit scholarship recipient"]},
    
    {"name": "Pranshu Goel", "email": "pranshugoel250405@gmail.com", "cgpa": 9.66,
    "skills": ["Python", "Java", "C++", "JavaScript", "React", "Node.js", "MongoDB", "Docker"],
    "experience": ["SWE Co-op Intern - AlgoUniversity"],
    "projects": ["FlashCard App", "Student Placement Predictor"],
    "achievements": ["Built online judge platform and compiler server"]},
    
    {"name": "Rohan Nijhawan", "email": "rohannijhawan02@gmail.com", "cgpa": 9.68,
    "skills": ["C++", "C", "Python", "SQL", "PHP", "Pandas", "NumPy", "Seaborn"],
    "experience": ["Project Intern - Rubiscape Inteliment"],
    "projects": ["Mindspace – Mood Analysis Chatbot", "Hotel Management System"],
    "achievements": ["Built data pipelines and ETL processes"]},
    
    {"name": "Ritika Kaushik", "email": "rkaushik_be23@thapar.edu", "cgpa": 9.69,
    "skills": ["Python", "Java", "C", "C++", "MySQL", "Oracle", "NLP", "Gemini API", "LangChain"],
    "experience": [],
    "projects": ["Invoice Data Extraction System", "Calorie Tracker", "TaskGenie Chatbot"],
    "achievements": ["Gold medalist in Maths Olympiad", "Merit scholarship holder"]},
    
    {"name": "Saanvi Wadhwa", "email": "saanviwadhwa09@gmail.com", "cgpa": 9.65,
    "skills": ["Python", "C", "C++", "R", "SQL", "HTML/CSS", "scikit-learn", "Streamlit"],
    "experience": [],
    "projects": ["Product Feature Extraction & Similarity Search", "SMS Multi-Label Intent & Emotion Classifier"],
    "achievements": ["Reliance Foundation Scholar", "GirlScript Summer of Code contributor"]},
    
    {"name": "Sandeep Kaur", "email": "sandeepkaur1952004@gmail.com", "cgpa": 9.77,
    "skills": ["Python", "C/C++", "SQL", "PL/SQL", "Streamlit", "MLflow", "Node.js", "Express.js"],
    "experience": ["Software Engineering Virtual Internship - J.P. Morgan"],
    "projects": ["Emotion-Aware Virtual Assistant", "Real-Estate Price Predictor"],
    "achievements": ["Merit scholarship holder"]},
    
    {"name": "Shivank Bhatia", "email": "bhatiashivank834@gmail.com", "cgpa": 9.85,
    "skills": ["C/C++", "Python", "Dart", "JavaScript", "R", "MySQL", "React", "NextAuth", "MongoDB"],
    "experience": [],
    "projects": ["Measurements Recording App", "AI Visual Accuracy Tester"],
    "achievements": ["JPMC CFG'25 Shortlisted", "500+ LeetCode problems"]},
    
    {"name": "Varad Pandey", "email": "varad0404@gmail.com", "cgpa": 9.70,
    "skills": ["C++", "Python", "C", "React", "Express.js", "Node.js", "MongoDB", "MySQL"],
    "experience": [],
    "projects": ["Healthcare Monitoring Hackathon Project", "ChatSphere", "Weather App"],
    "achievements": ["Merit-3 Scholarship", "3rd place in Israel-India Hackathon"]}
]

# Resume data - Batch 5 (NEW - from provided JSON)
resumes_batch5 = [
    {"name": "Harpuneet Singh", "email": "hsingh_be23@thapar.edu", "cgpa": 9.73,
    "skills": ["Python", "C", "C++", "Scikit-learn", "Pandas", "NumPy", "TensorFlow", "Keras", "MATLAB", "SQL", "Django", "REST APIs"],
    "experience": [], 
    "projects": ["AI Assistant using Attention Mechanism", "Skin Cancer Classification", "Breast Cancer Detection"],
    "achievements": ["Academic merit scholarship holder", "Solved 150+ DSA problems"]},

    {"name": "Sarvagya Srivastava", "email": "ssrivastava_be23@thapar.edu", "cgpa": 9.59,
    "skills": ["Python", "C", "C++", "SQL", "R", "Pandas", "NumPy", "Matplotlib", "Scikit-learn", "Time Series Analysis"],
    "experience": [],
    "projects": ["LSTM-Based Stock Market Prediction", "Movie Recommendation System", "Air Canvas (Virtual Drawing)"],
    "achievements": ["Merit Scholarship Holder", "Participated in multiple hackathons"]},

    {"name": "Ishan Satya Prakash", "email": "ishansp@gmail.com", "cgpa": 9.63,
    "skills": ["C", "C++", "Python", "R", "Next.js", "React", "Node.js", "MongoDB", "MySQL", "Cloud", "Docker", "OpenCV", "Data Structures"],
    "experience": [],
    "projects": ["AUTOBiz AI Assistant", "CampusBridge", "Real-Time Video Analysis"],
    "achievements": ["Fellowship with Startup India", "Published research work"]},

    {"name": "Devkaran Singh", "email": "ddevkaran05@gmail.com", "cgpa": 9.53,
    "skills": ["Python", "C", "C++", "R", "SQL", "Pandas", "Scikit-learn"],
    "experience": [],
    "projects": ["Flight Management System (DBMS)", "Student Performance Predictor"],
    "achievements": ["Scholarship recipient", "Strong academic record"]},

    {"name": "Sukhmanpreet Kaur", "email": "sukhmanpreetkaur0404@gmail.com", "cgpa": 9.41,
    "skills": ["Python", "C++", "JavaScript", "HTML", "CSS", "MongoDB", "React", "Node.js", "SQL"],
    "experience": [],
    "projects": ["Face Recognition-Based System", "Malicious PDF Detector"],
    "achievements": ["Active participation in coding competitions", "Good academic performance"]},

    {"name": "Aryan Lamba", "email": "lambaryan2005@gmail.com", "cgpa": 9.59,
    "skills": ["Python", "C++", "FastAPI", "React", "MongoDB", "Node.js", "SQL", "Graph Neural Networks", "OpenCV"],
    "experience": [],
    "projects": ["House Price Prediction", "GNN Face Verification", "AI Document Parser"],
    "achievements": ["Participated in multiple AI/ML hackathons", "Strong coding background"]},

    {"name": "Vani Mohindru", "email": "vmohindru_be23@thapar.edu", "cgpa": 9.64,
    "skills": ["Python", "C++", "SQL", "MongoDB", "HTML", "CSS", "JS", "ML"],
    "experience": [],
    "projects": ["House Price Predictor", "Credit Card Fraud Detection", "Document Categorization System"],
    "achievements": ["Merit scholarship holder"]},

    {"name": "Vihaan Agarwal", "email": "vaggarwal_be23@thapar.edu", "cgpa": 9.77,
    "skills": ["Python", "C/C++", "JavaScript", "React", "Node.js", "Scikit-learn", "TensorFlow", "LangChain", "Docker", "Bash"],
    "experience": [],
    "projects": ["Personal RAG Chatbot", "Parallel Backup System", "Image Classifier"],
    "achievements": ["Multiple ML/AI projects with high accuracy", "Strong coding and problem-solving skills"]}
]

# Resume data - Batch 6 (NEW - from provided JSON)
resumes_batch6 = [
    {"name": "Aarzoo Mehta", "email": "amehta_be23@thapar.edu", "cgpa": 9.21,
     "skills": ["JavaScript", "React", "Node.js", "Express", "MongoDB", "Tailwind CSS", "HTML/CSS", "Git"],
     "experience": [], 
     "projects": ["Triplanr — AI itinerary generator", "DSA Visualizer", "SkillMingle — Skill-based job matcher"],
     "achievements": ["Merit scholarship (top 10% of branch)", "1st place Intra-Society Hackathon"]},

    {"name": "Aman Wadhwa", "email": "amanwadhwa0707@gmail.com", "cgpa": 9.14,
     "skills": ["Python", "Django", "Flask", "Node.js", "React", "Firebase", "DSA", "RAG", "LLMs"],
     "experience": [], 
     "projects": ["AI Customer Service Platform", "House Marketplace"],
     "achievements": ["Selected for Salesforce FutureForce AI Challenge", "500+ LeetCode solves"]},

    {"name": "Arshdeep Kaur", "email": "akaur3_be23@thapar.edu", "cgpa": 9.0,
     "skills": ["C/C++", "Data Structures", "SQL", "OOP", "HTML/CSS", "JavaScript"],
     "experience": [], 
     "projects": ["Advanced Music Player", "DBMS for IPL", "Spam vs Non-Spam Detector"],
     "achievements": ["Strong communication and leadership skills"]},

    {"name": "Avani Singh", "email": "asingh48_be23@thapar.edu", "cgpa": 9.11,
     "skills": ["Python", "PyTorch", "YOLO", "Ultralytics", "OpenCV", "MATLAB", "SQL"],
     "experience": ["CERC Intern (Summer 2025)"], 
     "projects": ["RADD — Railway Autonomous Defect Detection", "Women Safety Analytics"],
     "achievements": ["Analyzed legal/regulatory documents for ethical GenAI"]},

    {"name": "Banipreet Kaur", "email": "banipreetkaur029@gmail.com", "cgpa": 9.20,
     "skills": ["Python", "Flask", "Oracle SQL", "PL/SQL", "OpenCV", "UI/UX", "Figma"],
     "experience": [], 
     "projects": ["ML-Based Stress Level Detection Webpage", "Organ Donation Management System"],
     "achievements": ["NPTEL Graphic Design certificate", "Deloitte Forage simulation completion"]},

    {"name": "Bhavika Gupta", "email": "bhavikaguptabg18@gmail.com", "cgpa": 9.41,
     "skills": ["C++", "C", "Python", "Algorithms", "HTML/CSS", "SQL"],
     "experience": [], 
     "projects": ["Competitive Programming & Projects"],
     "achievements": ["Coding Ninjas: Data Structures & Algorithms", "Intro to C++"]},

    {"name": "Dhruv Goyal", "email": "dhruv621999goyal@gmail.com", "cgpa": 9.16,
     "skills": ["Next.js", "React", "Node.js", "Python", "TensorFlow", "Docker", "MongoDB", "SQL"],
     "experience": ["SDE Internship"], 
     "projects": ["Arogyam — Hospital Portal", "GoSnap — Image Processing Platform"],
     "achievements": ["Merit scholarship (₹7+ Lakh)", "Finalist at SatHack"]},

    {"name": "Edwin Raphael", "email": "edwinraphae01@gmail.com", "cgpa": 9.16,
     "skills": ["Python", "Arduino", "MATLAB", "AutoCAD", "SolidWorks", "TensorFlow"],
     "experience": [], 
     "projects": ["UAV Path Optimization", "CHIKITSA — Healthcare Companion App"],
     "achievements": ["10.0 CGPA in first semester", "Multiple wins in engineering competitions"]},

    {"name": "Kanishk Kumar Agarwal", "email": "agarwalkanishk9@gmail.com", "cgpa": 9.11,
     "skills": ["Python", "React", "Node.js", "Oracle SQL", "MySQL", "TensorFlow", "VGG16", "Docker"],
     "experience": ["Research Intern (Solar PV)", "Backend Engineer Intern"], 
     "projects": ["RinFlow — Loan Origination Backend", "Blood Bank Management System"],
     "achievements": ["Selected for Amazon ML Summer School 2025", "300+ LeetCode solved"]},

    {"name": "Kashish Gupta", "email": "guptakashish1012@gmail.com", "cgpa": 9.13,
     "skills": ["C", "C++", "Java", "Python", "SQL", "UI/UX", "Figma"],
     "experience": [], 
     "projects": ["Skill Barter Exchange System (DBMS)", "Pacman AI", "Nari Shield — Women Safety Platform"],
     "achievements": ["Qualified for Amazon ML Summer School 2025", "Joint Secretary ACM TIET"]}
]

# Resume data - Batch 7 (NEW - from provided JSON)
resumes_batch7 = [
    {"name": "Laksha Singla", "email": "lsingla_be23@thapar.edu", "cgpa": 9.2,
     "skills": ["Python", "TensorFlow", "PyTorch", "RoBERTa", "OpenCV", "Flask", "PostgreSQL", "Streamlit", "Flutter"],
     "experience": [], 
     "projects": ["SoulScribe - Emotion-Aware Journaling", "AI Yoga Mat Feedback Module", "Railway Management System"],
     "achievements": ["Finalist - Adobe India Hackathon 2025", "Organizer in DebSoc"]},

    {"name": "Manas Goyal", "email": "manasgoyal02@gmail.com", "cgpa": 9.08,
     "skills": ["Python", "LangChain", "PyPDF2", "Streamlit", "Scikit-learn", "Pandas", "MySQL"],
     "experience": ["Summer Intern - ONGC"], 
     "projects": ["AI Chat Assistant for Document Analysis", "Smart Crop Advisor", "Airport Operations Management"],
     "achievements": ["Built scalable PDF semantic-search tools"]},

    {"name": "Noor Tandon", "email": "noortandon1234@gmail.com", "cgpa": 9.22,
     "skills": ["Python", "OpenCV", "Caffe", "Oracle SQL", "PL/SQL", "NumPy", "Pandas"],
     "experience": [], 
     "projects": ["Gender & Age Detection", "VideoTube (DBMS-focused YouTube clone)"],
     "achievements": ["Microsoft Learn Student Chapter contributor", "YouTube content creator (50k+ views)"]},

    {"name": "Aadi Jain", "email": "19aadijain@gmail.com", "cgpa": 9.12,
     "skills": ["C++", "Python", "Flask", "ChromaDB", "FAISS", "TensorFlow", "PyTorch", "SQL"],
     "experience": ["Software Engineering Intern - Guenstiger India"], 
     "projects": ["University Appointment Booking Web App", "Alzheimer’s Detection (MRI)"],
     "achievements": ["Built scalable image classification API"]},

    {"name": "Priya Verma", "email": "vermapriyaa26@gmail.com", "cgpa": 9.05,
     "skills": ["Python", "NumPy", "Pandas", "SQL", "AutoCAD", "Tableau", "Arduino"],
     "experience": [], 
     "projects": ["Smart Gym Management System", "EatWise – Restaurant Recommender", "Autocad & Mangonel Design"],
     "achievements": ["NVIDIA Fundamentals of Deep Learning certification"]},

    {"name": "Raiza Duggal", "email": "raizaduggal1@gmail.com", "cgpa": 9.20,
     "skills": ["Python", "OpenCV", "Scikit-learn", "Pandas", "NumPy", "SQL"],
     "experience": [], 
     "projects": ["Sign Language Detection", "Bank Management System"],
     "achievements": ["Executive Member - LEAD Society"]},

    {"name": "Riya Gupta", "email": "riya.gupta070705@gmail.com", "cgpa": 9.14,
     "skills": ["React", "Node.js", "Express", "MySQL", "Python", "Scikit-learn", "Firebase"],
     "experience": ["Joint Secretary - Thapar Literary Society"], 
     "projects": ["Hospital Management System", "Car Price Predictor"],
     "achievements": ["Led design team of 5 members"]},

    {"name": "Gaurang Garg", "email": "gaurang020106@gmail.com", "cgpa": 9.09,
     "skills": ["Python", "LangChain", "OpenCV", "BM25", "E5", "MiniLM", "FastAPI", "Docker"],
     "experience": [], 
     "projects": ["AI Travel Planner", "Virtual Interview Assistant", "Eye Cursor & Virtual Piano"],
     "achievements": ["Winner - Zelestra x AWS '25 Asian Hackathon", "150+ solved DSA problems"]},

    {"name": "Aishita Kumar", "email": "aishitakumar137@gmail.com", "cgpa": 9.19,
     "skills": ["Python", "XGBoost", "TensorFlow", "Keras", "Scikit-learn", "SQL", "MATLAB"],
     "experience": ["Deloitte Data Analytics Virtual Internship", "JPMC Software Engineering Virtual Internship"], 
     "projects": ["Solar Flare Classification", "Insulator Fault Detection"],
     "achievements": ["Research on few-shot learning"]},

    {"name": "Harshleen Kaur Bhangu", "email": "harshleenkaur781@gmail.com", "cgpa": 9.16,
     "skills": ["JavaScript", "React", "Node.js", "Express", "PostgreSQL", "MongoDB", "Bootstrap", "REST APIs"],
     "experience": [], 
     "projects": ["Food Delivery Web Application", "Spa & Wellness Booking Website", "VIRSA Society Website"],
     "achievements": ["Selected for JPMC Code for Good 2025", "Silver Medal in SOF Olympiad"]}
]
# Resume data - Batch 8 (NEW - from provided JSON)
resumes_batch8 = [
    {"name": "Kashvi Mittal", "email": "kashvimittal31@gmail.com", "cgpa": 9.28,
     "skills": ["Python", "C++", "SQL", "HTML", "CSS", "JavaScript", "ML algorithms", "Pandas", "NumPy"],
     "experience": [], 
     "projects": ["Credit Card Fraud Detection", "DBMS-Based Cafe Management System"],
     "achievements": ["Completed multiple online ML courses", "Active participant in coding events"]},

    {"name": "Pranav Goyal", "email": "N/A", "cgpa": 9.0, # Defaulted due to missing data
     "skills": ["Python", "C++", "SQL", "DBMS", "Machine Learning"],
     "experience": [], 
     "projects": ["Technical Projects (Python, SQL, ML)"],
     "achievements": ["Good communication and analytical skills"]},

    {"name": "Tanya Jaswal", "email": "tanyajaswal609@gmail.com", "cgpa": 9.37,
     "skills": ["Python", "C++", "SQL", "DBMS", "HTML", "CSS"],
     "experience": [], 
     "projects": ["Personality Prediction System", "Cafe Management System (DBMS)"],
     "achievements": ["Student Coordinator in cultural fest", "Data analytics certification"]},

    {"name": "Avni Gupta", "email": "avniguptatiet@gmail.com", "cgpa": 9.24,
     "skills": ["Python", "C++", "NumPy", "Pandas", "Scikit-learn", "LangChain", "Flask", "SQL"],
     "experience": [], 
     "projects": ["Bills AI – Document Extraction System", "Loan Approval Predictor", "Music Emotion Classifier"],
     "achievements": ["Reliance Foundation Scholar", "JPMC Forage Internship Simulation"]},

    {"name": "Rhythm Garg", "email": "rgarg_be23@thapar.edu", "cgpa": 9.20,
     "skills": ["Python", "C++", "R", "SQL", "PL/SQL", "DBMS", "Scikit-learn"],
     "experience": [], 
     "projects": ["Disaster Prediction System", "ATM Management System"],
     "achievements": ["Certified in Data Analytics", "Completed MATLAB and ML courses"]},

    {"name": "Rhythm (v2)", "email": "rgarg_be23@thapar.edu", "cgpa": 9.20,
     "skills": ["Python", "C++", "SQL", "DBMS", "ML basics"],
     "experience": [], 
     "projects": ["Disaster Classification Model", "ATM Management SQL System"],
     "achievements": ["Completed several data analytics workshops"]},

    {"name": "Sharnya Goel", "email": "sharnyagoel3@gmail.com", "cgpa": 9.31,
     "skills": ["Python", "TensorFlow", "OCR", "Transformers", "Streamlit", "SQL", "PL/SQL", "Pandas", "NumPy"],
     "experience": [], 
     "projects": ["AI Document Visualizer", "Crop Recommendation System", "E-commerce Website"],
     "achievements": ["Completed Google Data Analytics course", "Strong academic performance"]},

    {"name": "Tanjot Chawla", "email": "tanjotchawla03@gmail.com", "cgpa": 9.25,
     "skills": ["C++", "Python", "HTML", "CSS", "SQL", "DBMS", "ML basics"],
     "experience": [], 
     "projects": ["Portfolio Website", "Restaurant Recommender"],
     "achievements": ["Completed foundational ML coursework", "Active in technical societies"]},

    {"name": "Tarun Krishna Shastri", "email": "tarunkrishnashastri@gmail.com", "cgpa": 9.10,
     "skills": ["Python", "C++", "HTML", "CSS", "JavaScript", "Bootstrap", "SQL"],
     "experience": [], 
     "projects": ["Image Steganography Tool", "Weather App"],
     "achievements": ["Volunteered in multiple university events"]},

    {"name": "Vansh Gupta", "email": "Vanshgupta762002@gmail.com", "cgpa": 9.18,
     "skills": ["Python", "C++", "SQL", "HTML", "CSS", "DBMS"],
     "experience": [], 
     "projects": ["Café Billing System (DBMS)", "Personality Prediction"],
     "achievements": ["Completed several online technical certifications"]}
]

# Resume data - Batch 9 (NEW - Mega Batch from JSON)
resumes_batch9 = [
    {"name": "Arsh Garg", "email": "agarg14_be23@thapar.edu", "cgpa": 9.41,
     "skills": ["C", "C++", "Python", "SQL", "React", "Node.js", "OpenCV", "NumPy", "Pandas"],
     "experience": [],
     "projects": ["Malicious PDF Detector", "Food App", "Election Voting System"],
     "achievements": ["Co-author on NTIRE 2025 CVPR Workshop publication", "Top 32 in CVPR NTIRE 2025 Challenge"]},

    {"name": "Aryan Singh", "email": "asingh42_be23@thapar.edu", "cgpa": 9.36,
     "skills": ["Python", "C", "C++", "SQL", "React", "Node.js", "Express.js", "MongoDB"],
     "experience": [],
     "projects": ["Ziddi: Online Thrift Store", "Football Match Result Prediction", "Wordle Clone"],
     "achievements": ["First Position in CodeSprint", "President of Enigma Quizzing Society"]},

    {"name": "Harshika Anand", "email": "hanand_be23@thapar.edu", "cgpa": 9.36,
     "skills": ["C++", "React.js", "Node.js", "Next.js", "Flutter", "MongoDB", "TypeScript"],
     "experience": [],
     "projects": ["Hostel Mart - E-commerce Platform", "Geolocation-Based Attendance System", "Saturnalia’24 Website"],
     "achievements": ["Finalist at JPMC Code for Good 2025", "DSA mentor for 50+ students"]},

    {"name": "Krishiv Goyal", "email": "krishiv19m@gmail.com", "cgpa": 9.49,
     "skills": ["HTML", "CSS", "React", "Node.js", "Express", "MongoDB", "Python", "TypeScript"],
     "experience": [],
     "projects": ["TaskSync – Team Task Management", "Cryptocurrency Web App", "Finance Management App"],
     "achievements": ["Strong academic record"]},

    {"name": "Yash Agnihotri", "email": "yagnihotri_be23@thapar.edu", "cgpa": 9.38,
     "skills": ["C++", "TypeScript", "React", "Next.js", "Node.js", "AWS", "MongoDB", "SQL"],
     "experience": [],
     "projects": ["Sehaj - Holistic Medical Brand", "SoberSafalta - Anti-Substance Abuse Platform"],
     "achievements": ["Finalist at HackTU 5.0", "Team Lead at HackTU 4.0"]},

    {"name": "Aahil Khan", "email": "aahilminookhan@gmail.com", "cgpa": 9.54,
     "skills": ["Python", "Next.js", "Node.js", "PostgreSQL", "Redis", "Qdrant", "LangChain", "GPT-4"],
     "experience": [],
     "projects": ["SkillMap — Personalized Learning Engine", "Vehicle Parking App"],
     "achievements": ["Led Thapar Edutube serving 10,000+ students"]},

    {"name": "Harshpreet Singh Kwatra", "email": "hkwatra_be23@thapar.edu", "cgpa": 9.44,
     "skills": ["C++", "Python", "ROS", "Gazebo", "React", "SQL", "RViz"],
     "experience": [],
     "projects": ["MazeEscape Game (ROS)", "Autonomous TurtleBot Navigation", "Spearow Website"],
     "achievements": ["Technical Coordinator, Microsoft Learn Student Chapter"]},

    {"name": "Ishwin", "email": "syal.ishwin@gmail.com", "cgpa": 9.36,
     "skills": ["C++", "Python", "SQL", "React", "TensorFlow", "Keras", "Scikit-learn"],
     "experience": [],
     "projects": ["Agri Space - Precision Agriculture", "VentiCare - AI ICU Assistance", "Order Assistant Bot"],
     "achievements": ["MLH Track Winner at HACKTU ’25", "NPTEL Deep Learning Silver certificate"]},

    {"name": "Khushveer Kaur", "email": "kkaur3_be23@thapar.edu", "cgpa": 9.38,
     "skills": ["C++", "Python", "SQL", "React", "Node.js", "OpenCV", "MongoDB"],
     "experience": [],
     "projects": ["Online Examination System (DBMS)", "AI Face Recognition Attendance", "Auto Notes Generator"],
     "achievements": ["Merit-3 Scholarship", "Completed Data Science bootcamp"]},

    {"name": "Krishna Sharma", "email": "krishnasharma182530@gmail.com", "cgpa": 9.49,
     "skills": ["C/C++", "Python", "React", "Tailwind CSS", "Node.js", "MongoDB", "SQL"],
     "experience": [],
     "projects": ["SM Bath Fittings Website", "Blumi Thrift Store Frontend", "F1 Race Result Predictor"],
     "achievements": ["Merit-3 Scholarship", "3rd place in movie-making competition"]},

    {"name": "Kunal Sharma", "email": "kunalkomal1710@gmail.com", "cgpa": 9.39,
     "skills": ["C", "C++", "Python", "React", "Node.js", "Arduino", "Tailwind CSS", "MongoDB"],
     "experience": [],
     "projects": ["Use-Popcorn (Movie Search)", "Pack-Me (Trip Planner)", "Autonomous Buggy Simulation"],
     "achievements": ["National Science Congress participation", "Full scholarship holder"]},

    {"name": "Muskaan Katyal", "email": "muskaankatyal2005@gmail.com", "cgpa": 9.36,
     "skills": ["Elixir", "Python", "SQL", "Pandas", "Scikit-learn", "PostgreSQL"],
     "experience": [],
     "projects": ["LifeLink (Emergency Healthcare)", "Gender Stereotype Detection", "Engineering Design (Arduino)"],
     "achievements": ["LinkedIn Coaching Program Mentee (Top 80)", "High SAT/PTE scores"]},

    {"name": "Nimish Agrawal", "email": "nimish4agrawal@gmail.com", "cgpa": 9.36,
     "skills": ["React", "Figma", "SQL", "Python", "C++", "HTML", "CSS"],
     "experience": [],
     "projects": ["Smart Cart (React)", "Social Media App Design", "Travel Website Landing Page"],
     "achievements": ["Selected for JP Morgan Code for Good 2025", "Led sponsorship for URJA'25"]},

    {"name": "Raghav Khurana", "email": "raghav8work@outlook.com", "cgpa": 9.49,
     "skills": ["Python", "Embedded Vision", "TensorFlow", "OpenCV", "Django", "Docker", "Raspberry Pi"],
     "experience": [],
     "projects": ["Autonomous Drone Swarm", "Railway Track Fault Detection", "IPL Result Prediction"],
     "achievements": ["Airbus SDC Third Place", "Selected for NIDAR competition"]},

    {"name": "Pranjal Satti", "email": "pranjalsatti@gmail.com", "cgpa": 9.40,
     "skills": ["Node.js", "Express.js", "MongoDB", "Socket.IO", "AWS", "Docker", "React"],
     "experience": [],
     "projects": ["RealChatApp — Real-Time Chat", "CampusConnect — Community Backend"],
     "achievements": ["GDSC Core Team Member", "Solved 250+ DSA problems"]},

    {"name": "Pratiksha Kumari Sah", "email": "N/A", "cgpa": 9.46,
     "skills": ["Java", "Python", "SQL", "PyTorch", "Flask", "NLP", "Matplotlib"],
     "experience": [],
     "projects": ["Financial Sentiment Lexicon", "Stock Market News Analysis", "Image Recognition (SVM)"],
     "achievements": ["TIET Merit Scholarship (50% tuition)", "House Captain"]},

    {"name": "Priyansh Chowhan", "email": "priyanshchowhan@gmail.com", "cgpa": 9.39,
     "skills": ["Node.js", "React", "Python", "AWS EC2", "Docker", "MongoDB", "Oracle SQL"],
     "experience": [],
     "projects": ["Money-Mirror (Financial Analytics)", "Anomaly Detection in Smart Buildings", "Rinflow"],
     "achievements": ["Merit I Scholarship", "Published IEEE research paper"]},

    {"name": "Gaurav Prakash Srivastava", "email": "gsrivastava_be23@thapar.edu", "cgpa": 9.46,
     "skills": ["C++", "Next.js", "React", "XGBoost", "OpenCV", "Streamlit", "Oracle"],
     "experience": ["Research Intern at IIT Delhi", "Front-End Intern at TIET"],
     "projects": ["DEA Dashboard", "Cluster-Based DEA Dashboard", "Credit Card Fraud Detection"],
     "achievements": ["Tabla performer (SUR TIET)"]},

    {"name": "Shrey Rawat", "email": "shreyrawat59@gmail.com", "cgpa": 9.36,
     "skills": ["Python", "SQL", "PL/SQL", "Deep Learning", "Microservices", "React"],
     "experience": [],
     "projects": ["EEG-Based Schizophrenia Detection", "Credit Card Fraud Detection", "Flight Management System"],
     "achievements": ["Winner — UN All India Essay Competition", "National gold medalist in debating"]},

    {"name": "Manas Devgan", "email": "mdevgan_be23@thapar.edu", "cgpa": 9.47,
     "skills": ["C++", "Python", "Arduino", "PL/SQL", "Scikit-Learn", "MongoDB"],
     "experience": [],
     "projects": ["Breast Cancer Classification", "RoboCar (NVIS3302ARD)", "Job Portal for Rural Areas"],
     "achievements": ["Senior Coordinator, CTD TIET"]},

    {"name": "Sayyam Wadhwa", "email": "sayyam.wad@gmail.com", "cgpa": 9.38,
     "skills": ["Python", "PyTorch", "NLP", "Flask", "PostgreSQL", "Docker", "GCP"],
     "experience": ["Amazon ML Summer School 2025"],
     "projects": ["Social Media Sentiment Analysis", "OTT Streaming Platform", "Sudoku Solver"],
     "achievements": ["Academic Merit Scholarship"]},

    {"name": "Siya Khosla", "email": "skhosla_be23@thapar.edu", "cgpa": 9.37,
     "skills": ["C++", "SQL", "React", "Arduino", "MATLAB", "Flask", "Django"],
     "experience": [],
     "projects": ["Library Management System", "AI Interview Bot", "E-Commerce Bag Website"],
     "achievements": ["SIH 2024 participation", "Conducted DSA workshop"]},

    {"name": "Sneha Upadhyay", "email": "supadhyay_be23@thapar.edu", "cgpa": 9.38,
     "skills": ["Python", "OpenCV", "TensorFlow", "Deep Learning", "YOLO", "Full Stack"],
     "experience": ["AI/ML Intern – ShadowFox", "AI/ML Intern – COE DSAI"],
     "projects": ["Interactive Face Detection App", "Chess Engine with AI", "URL Shortener"],
     "achievements": ["Implemented LGBM/YOLOv8 in production"]},

    {"name": "Khushi Goyal", "email": "goyalkhushi3844@gmail.com", "cgpa": 9.40,
     "skills": ["Python", "FastAPI", "SQL", "React", "Node.js", "NLP", "Arduino"],
     "experience": ["Cisco NetAcad Cybersecurity Internship"],
     "projects": ["AI-Based Recipe Recommender", "College Society Event Portal", "Lost & Found System"],
     "achievements": ["Global Scaling Challenge 2024 finalist"]},

    {"name": "Vishnu", "email": "vvishnu_be23@thapar.edu", "cgpa": 9.38,
     "skills": ["MERN Stack", "WebRTC", "Socket.IO", "Tailwind CSS", "SQL"],
     "experience": [],
     "projects": ["LynkUp (Video Calling)", "Recruitment Portal", "Skill Mingle"],
     "achievements": ["Hack for Impact Finalist", "Most Innovative Hack (Makeathon 6)"]},

    {"name": "Vani Goyal", "email": "vgoyal_be23@thapar.edu", "cgpa": 9.41,
     "skills": ["C++", "Python", "TensorFlow", "GenAI", "MySQL", "DSA"],
     "experience": [],
     "projects": ["Few-Shot Keyword Spotting", "ConverseX (GenAI Matchmaking)", "Cosmetics Shop System"],
     "achievements": ["LinkedIn CoachIn Mentee", "SheFi Scholar"]},

    {"name": "Avani Agarwal", "email": "agarwalavani29@gmail.com", "cgpa": 9.49,
     "skills": ["SQL", "Tableau", "Node.js", "Python", "MongoDB", "Excel"],
     "experience": ["Deloitte Australia Data Analytics Virtual Experience"],
     "projects": ["Task Manager Web App", "Calculator (Python)"],
     "achievements": ["HackerRank Problem Solving Certificate"]},

    {"name": "Kinshuk Kala", "email": "kinshuk17kala@gmail.com", "cgpa": 9.40,
     "skills": ["Oracle SQL", "Python", "Arduino", "ML", "R", "MATLAB"],
     "experience": [],
     "projects": ["Music Recommendation System", "College DBMS", "Mangonel", "Robocar"],
     "achievements": ["Gold Medal – International French Olympiad"]},

    {"name": "Pariza Singh Kandol", "email": "pkandol_be23@thapar.edu", "cgpa": 9.44,
     "skills": ["ROS", "Python", "SQL", "RAG", "AutoCAD", "Linux"],
     "experience": ["ELC Summer Internship"],
     "projects": ["Loan Default Prediction", "UAV Navigation (ROS)", "RAG System for Legal"],
     "achievements": ["Coursera Data Science Elective"]},

    {"name": "Ritigya Singh", "email": "rsingh7_be23@thapar.edu", "cgpa": 9.49,
     "skills": ["Django", "Python", "NLP", "Gemini API", "TensorFlow", "SQL"],
     "experience": ["Data Science Intern at Davise Lab", "Software Engineering Intern – Saarathi Finance"],
     "projects": ["Invoice Validation App", "Gemini Chatbot UI", "Automated MCQ Generator"],
     "achievements": ["TEDx Design Team"]}
]

# Combine all batches (Final Mega Update)
all_resumes = resumes_batch1 + resumes_batch2 + resumes_batch3 + resumes_batch4 + resumes_batch5 + resumes_batch6 + resumes_batch7 + resumes_batch8 + resumes_batch9

jd_requirements = {
    "Sales Manager Intern": {
        "skills": ["communication", "marketing", "negotiation", "sales", "business development", "presentation"],
        "keywords": ["team", "leadership", "sponsorship", "client", "marketing", "business", "revenue", "pitch", "strategy", "growth", "executive"]
    },
    "Software Development Engineer (SDE) Intern": {
        "skills": ["C", "C++", "Python", "Java", "JavaScript", "algorithms", "data structures", "DSA", "Git"],
        "keywords": ["DSA", "LeetCode", "problem solving", "software", "coding", "development", "algorithms", "testing", "Git", "debug"]
    },
    "Frontend Developer Intern": {
        "skills": ["React", "HTML", "CSS", "JavaScript", "TypeScript", "UI", "UX", "Tailwind", "Next"],
        "keywords": ["responsive", "UI", "website", "frontend", "components", "web", "design", "interface", "dashboard"]
    },
    "Backend Developer Intern": {
        "skills": ["Node.js", "Express", "Python", "Flask", "Django", "SQL", "MongoDB", "API", "REST"],
        "keywords": ["REST", "API", "database", "server", "backend", "endpoint", "queries", "system"]
    },
    "Full Stack Developer Intern": {
        "skills": ["React", "Node.js", "MongoDB", "Express", "JavaScript", "MERN", "Full Stack", "database"],
        "keywords": ["MERN", "full stack", "deployment", "web development", "frontend", "backend", "platform"]
    },
    "Mobile Application Developer Intern": {
        "skills": ["Flutter", "Dart", "React Native", "Firebase", "Mobile", "Android", "iOS"],
        "keywords": ["Android", "iOS", "mobile", "app", "Flutter", "platform"]
    },
    "DevOps Engineer Intern": {
        "skills": ["Docker", "Git", "CI/CD", "AWS", "GCP", "Kubernetes", "automation"],
        "keywords": ["deployment", "Docker", "automation", "cloud", "DevOps", "infrastructure", "AWS", "container"]
    },
    "QA (Quality Assurance) / Test Engineer Intern": {
        "skills": ["testing", "automation", "Python", "Java", "test", "QA"],
        "keywords": ["test", "testing", "quality", "QA", "automation", "validation"]
    },
    "Data Analyst Intern": {
        "skills": ["Python", "SQL", "Pandas", "NumPy", "Power BI", "R", "Excel", "analytics"],
        "keywords": ["data", "analysis", "visualization", "SQL", "analytics", "dashboard", "reports"]
    },
    "Data Scientist Intern": {
        "skills": ["Python", "Machine Learning", "TensorFlow", "scikit-learn", "Pandas", "ML", "predictive"],
        "keywords": ["ML", "model", "prediction", "algorithm", "data science", "forecast", "analytics"]
    },
    "Machine Learning Engineer Intern": {
        "skills": ["Python", "TensorFlow", "Keras", "PyTorch", "scikit-learn", "Neural Networks", "ML"],
        "keywords": ["ML", "neural network", "model", "training", "deep learning", "deployment"]
    },
    "Artificial Intelligence Intern": {
        "skills": ["Python", "TensorFlow", "OpenCV", "NLP", "Computer Vision", "AI", "deep learning"],
        "keywords": ["AI", "computer vision", "NLP", "deep learning", "neural", "OpenCV", "image", "vision", "LLM", "detection"]
    },
    "Cloud Engineer Intern": {
        "skills": ["Docker", "AWS", "Azure", "GCP", "Kubernetes", "Cloud"],
        "keywords": ["cloud", "deployment", "infrastructure", "AWS", "Azure", "GCP"]
    },
    "Network Engineer Intern": {
        "skills": ["networking", "TCP/IP", "routing", "Cisco"],
        "keywords": ["network", "routing", "TCP/IP", "protocols"]
    },
    "Cybersecurity Analyst Intern": {
        "skills": ["Security", "Python", "Network Security", "Penetration Testing"],
        "keywords": ["security", "cybersecurity", "threat", "vulnerability", "penetration", "malicious", "detection"]
    },
    "System Administrator (SysAdmin) Intern": {
        "skills": ["Linux", "Windows", "scripting", "Bash", "system"],
        "keywords": ["system", "admin", "Linux", "Windows", "server", "management"]
    },
    "Embedded Systems Engineer Intern": {
        "skills": ["C", "C++", "Arduino", "microcontroller", "embedded"],
        "keywords": ["embedded", "microcontroller", "Arduino", "IoT", "hardware", "buggy", "robotic"]
    },
    "Product Management Intern (Technical)": {
        "skills": ["Product Management", "Communication", "Technical", "Agile"],
        "keywords": ["product", "roadmap", "strategy", "management", "Agile", "requirements"]
    },
    "UI/UX Designer Intern": {
        "skills": ["UI/UX", "Figma", "Design", "Prototyping"],
        "keywords": ["UI", "UX", "design", "user experience", "interface", "prototype", "wireframe", "dashboard"]
    },
    "Project Manager / IT Project Coordinator": {
        "skills": ["project management", "Agile", "Scrum", "organization"],
        "keywords": ["project", "management", "coordination", "Agile", "tracking", "lead"]
    },
    "Management Consultant": {
        "skills": ["consulting", "strategy", "analysis", "problem solving"],
        "keywords": ["consulting", "strategy", "business", "analysis", "advisory", "optimization"]
    },
    "Scrum Master": {
        "skills": ["Agile", "Scrum", "facilitation"],
        "keywords": ["Scrum", "Agile", "sprint", "facilitation", "team"]
    },
    "Product Marketing Manager": {
        "skills": ["marketing", "product", "communication"],
        "keywords": ["marketing", "product", "messaging", "launch", "campaign", "executive"]
    },
    "SEO Specialist": {
        "skills": ["SEO", "HTML", "analytics"],
        "keywords": ["SEO", "search", "keyword", "ranking", "optimization", "analytics"]
    },
    "Customer Success Manager": {
        "skills": ["communication", "customer service", "problem solving"],
        "keywords": ["customer", "success", "support", "relationship", "retention"]
    },
    "Implementation Consultant": {
        "skills": ["consulting", "SQL", "configuration"],
        "keywords": ["implementation", "configuration", "setup", "client", "deployment", "system"]
    }
}

# Improved fuzzy matching with lower threshold
def fuzzy_match(text, target, threshold=0.5):
    """Returns True if fuzzy similarity >= threshold (lowered from 0.6)"""
    return SequenceMatcher(None, text.lower(), target.lower()).ratio() >= threshold

def fuzzy_skill_match(candidate_skills, required_skills, threshold=0.6):
    """Count how many required skills fuzzy match with candidate skills (lowered from 0.7)"""
    matches = 0
    for req_skill in required_skills:
        for cand_skill in candidate_skills:
            if fuzzy_match(cand_skill, req_skill, threshold):
                matches += 1
                break
    return matches

def fuzzy_keyword_match(resume, keywords, threshold=0.6):
    """Count how many keywords fuzzy match in experience/projects/achievements (lowered from 0.7)"""
    text = ' '.join(resume['experience'] + resume['projects'] + resume['achievements']).lower()
    matches = 0
    for keyword in keywords:
        if any(fuzzy_match(word, keyword, threshold) for word in text.split()):
            matches += 1
    return matches

def count_quantified_achievements(resume):
    """Count numeric quantifiers in achievements/experience/projects"""
    text = ' '.join(resume['experience'] + resume['projects'] + resume['achievements'])
    import re
    quantifiers = re.findall(r'\d+[\+%]?', text)
    return len(quantifiers)

def compute_match_score(resume, jd):
    """Improved scoring with better weights and bonuses"""
    requirements = jd_requirements.get(jd, {"skills": [], "keywords": []})
    
    # Fuzzy skill matching
    skill_matches = fuzzy_skill_match(resume['skills'], requirements['skills'])
    skill_ratio = skill_matches / max(len(requirements['skills']), 1)
    
    # Fuzzy keyword matching
    keyword_matches = fuzzy_keyword_match(resume, requirements['keywords'])
    keyword_ratio = keyword_matches / max(len(requirements['keywords']), 1)
    
    # Enhanced bonuses
    experience_bonus = min(len(resume['experience']) * 0.15, 0.3)  # Up to 30%
    cgpa_bonus = (resume['cgpa'] - 9.0) * 0.15  # Increased weight
    quantified_bonus = min(count_quantified_achievements(resume) * 0.08, 0.25)  # More generous
    project_bonus = min(len(resume['projects']) * 0.05, 0.2)  # Project count matters
    
    # Rebalanced weights to reduce weak matches
    base_score = (skill_ratio * 0.35) + (keyword_ratio * 0.25) + experience_bonus + cgpa_bonus + quantified_bonus + project_bonus
    
    
    return min(max(base_score * 100, 0), 100)

def smart_jd_assignment(resume):
    """Smart JD assignment based on resume skills and experience"""
    resume_text = ' '.join(resume['skills'] + resume['experience'] + resume['projects']).lower()
    
    # Calculate scores for all JDs
    jd_scores = {}
    for jd in job_descriptions:
        score = compute_match_score(resume, jd)
        jd_scores[jd] = score
    
    # Get top 3 matches
    top_jds = sorted(jd_scores.items(), key=lambda x: x[1], reverse=True)[:3]
    
    # Weighted random selection from top 3 (70% best, 20% second, 10% third)
    weights = [0.7, 0.2, 0.1]
    selected_jd = random.choices([jd for jd, _ in top_jds], weights=weights, k=1)[0]
    
    return selected_jd

# Generate labels with improved matching
def generate_labels():
    random.seed(42)
    labeled_data = []
    
    for idx, resume in enumerate(all_resumes):
        # Smart JD assignment instead of random
        assigned_jd = smart_jd_assignment(resume)
        
        # Compute match score
        match_score = compute_match_score(resume, assigned_jd)
        
        # Compute individual features
        requirements = jd_requirements.get(assigned_jd, {"skills": [], "keywords": []})
        skill_matches = fuzzy_skill_match(resume['skills'], requirements['skills'])
        skill_ratio = (skill_matches / max(len(requirements['skills']), 1)) * 100
        
        keyword_matches = fuzzy_keyword_match(resume, requirements['keywords'])
        keyword_ratio = (keyword_matches / max(len(requirements['keywords']), 1)) * 100
        
        quantified = count_quantified_achievements(resume)
        experience_years = len(resume['experience']) * 0.5
        
        # Adjusted thresholds for better distribution
        if match_score >= 65:  # Lowered from 70
            label = "Strong Match"
        elif match_score >= 45:  # Lowered from 50
            label = "Moderate Match"
        else:
            label = "Weak Match"
        
        labeled_data.append({
            "Candidate Name": resume['name'],
            "Email": resume['email'] or "N/A",
            "Assigned JD": assigned_jd,
            "Match Score": round(match_score, 2),
            "CGPA": resume['cgpa'],
            "Experience Years": experience_years,
            "Skill Match %": round(skill_ratio, 1),
            "Keyword Coverage %": round(keyword_ratio, 1),
            "Quantified Achievements": quantified,
            "Label": label
        })
    
    return labeled_data

# Write to CSV
def save_to_csv(data, filename="resume_labels_improved.csv"):
    if not data:
        print("No data to save!")
        return
    
    keys = data[0].keys()
    with open(filename, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=keys)
        writer.writeheader()
        writer.writerows(data)
    
    print(f"✅ Saved {len(data)} labeled resumes to {filename}")

# Main execution
if __name__ == "__main__":
    print("🚀 Generating labels with improved fuzzy matching...")
    print(f"📊 Total resumes loaded: {len(all_resumes)}\n")
    
    labels = generate_labels()
    
    # Print summary
    strong = sum(1 for l in labels if l['Label'] == 'Strong Match')
    moderate = sum(1 for l in labels if l['Label'] == 'Moderate Match')
    weak = sum(1 for l in labels if l['Label'] == 'Weak Match')
    
    print(f"\n📊 Distribution Summary:")
    print(f"   Strong Matches: {strong} ({strong/len(labels)*100:.1f}%)")
    print(f"   Moderate Matches: {moderate} ({moderate/len(labels)*100:.1f}%)")
    print(f"   Weak Matches: {weak} ({weak/len(labels)*100:.1f}%)")
    print(f"   Total: {len(labels)}\n")
    
    # Save to CSV
    save_to_csv(labels)
    
    # Print first 5 examples
    print("\n📋 Sample outputs:")
    for i, label in enumerate(labels[:5], 1):
        print(f"\n{i}. {label['Candidate Name']} → {label['Assigned JD']}")
        print(f"   Score: {label['Match Score']}% | Label: {label['Label']}")
        print(f"   Skills: {label['Skill Match %']}% | Keywords: {label['Keyword Coverage %']}%")
        print(f"   Experience: {label['Experience Years']} years | CGPA: {label['CGPA']}")