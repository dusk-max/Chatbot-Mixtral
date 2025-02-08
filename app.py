import streamlit as st
import groq
from dotenv import load_dotenv
import os

# Load API Key
load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# Initialize Groq Client
client = groq.Client(api_key=GROQ_API_KEY)

# Function to get AI-generated responses
def get_groq_response(prompt):
    response = client.chat.completions.create(
        model="mixtral-8x7b-32768",
        messages=[{"role": "system", "content": "You are a hiring assistant helping screen technical candidates."},
                  {"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content

# Streamlit UI
st.set_page_config(page_title="TalentScout Hiring Assistant", layout="wide")

# Create Horizontal Tabs
tab1, tab2, tab3 = st.tabs(["👋 Introduction", "📝 Candidate Info & Questions", "🤖 Chatbot"])

# Session State Initialization
if "conversation" not in st.session_state:
    st.session_state.conversation = []
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
if "user_question" not in st.session_state:
    st.session_state.user_question = ""
if "show_chat_history" not in st.session_state:
    st.session_state.show_chat_history = False  # Default: Chat history is hidden
if "generated_questions" not in st.session_state:
    st.session_state.generated_questions = ""  # Store generated technical questions separately

# Tab 1: Introduction
with tab1:
    st.title("👋 Welcome to TalentScout Hiring Assistant!")
    
    st.markdown("""
    **Hello!**  
    I’m **TalentScout**, your AI-powered **hiring assistant**.  
    My role is to streamline the **initial candidate screening process** by:
    
    1. **Collecting your details** – I'll ask for basic information such as your name, contact details, experience, and desired position.
    2. **Generating technical questions** – Based on your declared **tech stack**, I'll prepare relevant questions to assess your proficiency.
    3. **Providing a seamless experience** – I’ll maintain context throughout our conversation to ensure smooth interactions.
    
    #### How to Use:
    - Navigate to **Candidate Info & Questions** to enter your details and generate questions.
    - Switch to **Chatbot** to interact with me, ask queries, and proceed with the screening process.
    
    🚀 **Let’s begin your hiring journey!**
    """)

# Tab 2: Candidate Information & Technical Questions
with tab2:
    st.title("📝 Candidate Information & Technical Questions")

    # Step 1: Gather Candidate Information
    st.subheader("Candidate Information")
    name = st.text_input("Full Name")
    email = st.text_input("Email Address")
    phone = st.text_input("Phone Number")
    experience = st.number_input("Years of Experience", min_value=0, max_value=50, step=1)
    position = st.text_input("Desired Position")
    location = st.text_input("Current Location")

    # Step 2: Tech Stack Declaration
    st.subheader("Tech Stack")
    tech_stack = st.text_area("Enter programming languages, frameworks, and tools you are proficient in (comma-separated)")

    # Step 3: Generate Technical Questions Based on Tech Stack
    if st.button("Generate Questions"):
        if not tech_stack:
            st.warning("Please enter your tech stack before proceeding.")
        else:
            tech_prompt = f"Generate 3-5 technical interview questions for a candidate proficient in {tech_stack}."
            st.session_state.generated_questions = get_groq_response(tech_prompt)  # Store questions separately

    # Display Generated Questions (only in this tab)
    if st.session_state.generated_questions:
        st.subheader("Generated Technical Questions")
        st.write(st.session_state.generated_questions)

# Tab 3: Chatbot
with tab3:
    st.title("🤖 Chatbot Assistant")

    # User Input Section (Always on Top)
    st.subheader("Ask the Hiring Assistant")
    user_input = st.text_input("Type your question here:", key="user_input")  # Unique key to avoid modification issues

    # Process User Input
    if st.button("Send"):
        if user_input:
            # Exit Condition
            if user_input.lower() in ["exit", "quit", "end"]:
                st.session_state.conversation.append(("Bot", "Thank you for using TalentScout. Goodbye!"))
                st.session_state.chat_history.append(("Bot", "Thank you for using TalentScout. Goodbye!"))
                st.rerun()  # Restart Streamlit to reset UI

            # Get Response from AI
            response = get_groq_response(user_input)

            # Append conversation history
            st.session_state.conversation.append(("You", user_input))
            st.session_state.conversation.append(("Bot", response))
            st.session_state.chat_history.append(("You", user_input))
            st.session_state.chat_history.append(("Bot", response))

            # Reset Input Field (Safe way)
            st.session_state.user_question = ""  # No direct modification of widget key
            st.rerun()

    # Display the Latest Generated Response Separately
    if st.session_state.conversation:
        st.subheader("Generated Response")
        last_response = st.session_state.conversation[-1][1] if st.session_state.conversation[-1][0] == "Bot" else ""
        st.write(last_response)

    # Chat History Toggle Button
    if st.button("Show Chat History" if not st.session_state.show_chat_history else "Hide Chat History"):
        st.session_state.show_chat_history = not st.session_state.show_chat_history  # Toggle state

    # Chat History Section (Only shown when enabled)
    if st.session_state.show_chat_history:
        st.subheader("Chat History")
        for role, message in st.session_state.chat_history:
            if role == "You":
                st.markdown(f"**You:** {message}")
            else:
                st.markdown(f"**Bot:** {message}")