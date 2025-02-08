
# Chatbot-Mixtral

## 🚀 Project Overview  

TalentScout is an AI-Powered hiring assistant chatbot designed to streamline the recruitment process by:  
- **Collecting candidate information** such as name, contact details, experience, and desired position.  
- **Generating technical questions** tailored to the candidate’s declared tech stack.  
- **Engaging with candidates** through an interactive chatbot.  
- **Maintaining conversation context** for a seamless user experience.

## 🌍 Live Demo using Streamlit Cloud

🎯 Try the chatbot in action: **[TalentScout - Live Demo](https://chatbot-mixtral-onfbh6g8krzuvqpfkluwfq.streamlit.app/)**  



## 🛠️ Installation Instructions  

**1️⃣ Clone the Repository**  
```bash
git clone https://github.com/yourusername/TalentScout.git
cd TalentScout  
```

2️⃣ **Set Up Virtual Environment (Optional but Recommended)**  
```bash
python -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate  # Windows
```

3️⃣ **Install Dependencies**
```bash
pip install -r requirements.txt
```

4️⃣ **Set up API Keys**
Create a .env file and add your GROQ API Key :
```bash
GROQ_API_KEY=your_groq_api_key_here
```
5️⃣ **Run the Application**
```
streamlit run app.py

---
```

## 📖 Usage Guide  

### **Tabs Overview**  

1️⃣ **👋 Introduction:**  
   - Provides an overview of the chatbot and its role in hiring process.  

2️⃣ **📝 Candidate Info & Questions:**  
   - Enter personal details such as name, email, experience, location, etc.  
   - Declare tech stack (Python, TensorFlow, SQL, etc.).  
   - Generate **3-5 technical questions** based on the provided tech stack.  

3️⃣ **🤖 Chatbot:**  
   - **Interact** with the AI assistant.  
   - **Ask questions** and receive AI-generated responses.  
   - **Chat History is optional** and only visible when selected.



## 🏗️ Technical Details  

- **Framework:** Streamlit  
- **LLM Model:** Groq API (Mixtral-8x7B-32768)  
- **Programming Language:** Python  
- **Libraries Used:**  
  - `streamlit` (Frontend UI)  
  - `groq` (LLM API)  
  - `dotenv` (Environment variable management)

## 🧠 Prompt Design  

The chatbot is designed to **effectively gather information** and **generate technical questions** using well-structured prompts.  

**1️⃣ Information Gathering Prompt:**  

You are a hiring assistant. Collect the following candidate details:  
- Full Name  
- Email  
- Phone Number  
- Years of Experience  
- Desired Position  
- Current Location  
- Tech Stack (Programming languages, frameworks, databases)

 **2️⃣ Technical Question Generation**

Generate 3-5 technical questions based on the candidate’s declared tech stack.  
Example:  
- If they list Python and Django, generate questions related to Python programming and Django framework.  
- If they list SQL and PostgreSQL, generate database-related questions.

**3️⃣ Context Handling Prompt**
Maintain the conversation context to ensure a smooth and coherent flow.  
Handle follow-up questions based on previous inputs.

**4️⃣ Fallback Mechanism:**
If the user input is unclear, respond with:  
"I'm sorry, I didn’t understand that. Could you please rephrase?"

**5️⃣ Ending the conversation**
When a conversation-ending phrase is detected (e.g., "thank you," "exit," or "goodbye"),  
respond with:  
"Thank you for your time! We’ll review your answers and get back to you soon."

---


## 🔥 Challenges & Solutions  

### **1️⃣ Chat History Display**  
**Issue:** Initially, chat history was automatically displayed, cluttering the UI.  
**Solution:** Implemented an **optional "Show Chat History" button** to keep it hidden by default.  

**2️⃣ Generated Questions Appearing in Chatbot Tab**  
**Issue:** The generated technical questions were mistakenly displayed in the chatbot tab.  
**Solution:** Ensured that **questions are only displayed in the Candidate Info tab**.  

**3️⃣ Input Field Going Below After Response**  
**Issue:** The user input field was moving below after each response.  
**Solution:** Used `st.experimental_rerun()` properly to **maintain UI structure**.  

 **4️⃣ Maintaining Context in Chatbot**  
**Issue:** Responses were not retaining previous interactions.  
**Solution:** Used **session state** to maintain context throughout the conversation.



## 📌 Future Enhancements  

✅ Cloud Deployment (AWS/GCP)  
✅ Integration with Resume Parsing  
✅ Customizable Question Bank  
✅ Candidate Report Generation

## 🤝 Contributing  

Feel free to fork this project and submit pull requests! 🚀

## 📜 License  

This project is **open-source** under the MIT License.  
