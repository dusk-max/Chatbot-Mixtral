import streamlit as st
import groq
from dotenv import load_dotenv
import os

# Load API Key from .env file
load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# Initialize Groq Client
client = groq.Client(api_key=GROQ_API_KEY)

# Function to get AI-generated responses with error handling
def get_groq_response(prompt):
    """
    Sends a request to the Groq API and retrieves a response.

    Args:
        prompt (str): The user input or AI-generated question.

    Returns:
        str: AI-generated response or an error message if the request fails.
    """
    try:
        response = client.chat.completions.create(
            model="mixtral-8x7b-32768",
            messages=[{"role": "system", "content": "You are a hiring assistant helping screen technical candidates."},
                      {"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error: Unable to fetch response due to {str(e)}"

# Initialize Streamlit page settings
st.set_page_config(page_title="TalentScout Hiring Assistant", layout="wide")

# Session State Initialization
if "conversation" not in st.session_state:
    st.session_state.conversation = []
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
if "user_question" not in st.session_state:
    st.session_state.user_question = ""
if "show_chat_history" not in st.session_state:
    st.session_state.show_chat_history = False
if "generated_questions" not in st.session_state:
    st.session_state.generated_questions = ""

# Function to render Introduction Tab
def render_intro_tab():
    """Renders the Introduction tab with an overview of the TalentScout chatbot."""
    st.title("👋 Welcome to TalentScout Hiring Assistant!")
    st.markdown("""
    **Hello!**  
    I’m **TalentScout**, your AI-powered **hiring assistant**.  
    My role is to streamline the **initial candidate screening process** by:
    
    1️⃣ **Collecting your details** – Basic info such as your name, contact details, experience, and position.  
    2️⃣ **Generating technical questions** – Based on your **tech stack**, I’ll prepare relevant questions.  
    3️⃣ **Providing a seamless experience** – I’ll maintain context to ensure smooth interactions.  

    🚀 **Let’s begin your hiring journey!**
    """)

# Function to render Candidate Info Tab
def render_candidate_info_tab():
    """Renders the Candidate Information & Technical Questions tab."""
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
    tech_stack = st.text_area("Enter programming languages, frameworks, and tools (comma-separated)")

    # Step 3: Generate Technical Questions Based on Tech Stack
    if st.button("Generate Questions"):
        if not tech_stack:
            st.warning("Please enter your tech stack before proceeding.")
        else:
            tech_prompt = f"Generate 3-5 technical interview questions for a candidate proficient in {tech_stack}."
            st.session_state.generated_questions = get_groq_response(tech_prompt)  # Store questions separately

    # Display Generated Questions
    if st.session_state.generated_questions:
        st.subheader("Generated Technical Questions")
        st.write(st.session_state.generated_questions)

# Function to render Chatbot Tab
def render_chatbot_tab():
    """Renders the Chatbot tab for candidate interactions."""
    st.title("🤖 Chatbot Assistant")

    # User Input Section
    st.subheader("Ask the Hiring Assistant")
    user_input = st.text_input("Type your question here:", key="user_input")

    # Process User Input
    if st.button("Send"):
        if user_input:
            # Exit Condition
            if user_input.lower() in ["exit", "quit", "end"]:
                st.session_state.conversation.append(("Bot", "Thank you for using TalentScout. Goodbye!"))
                st.session_state.chat_history.append(("Bot", "Thank you for using TalentScout. Goodbye!"))
                st.rerun()  # Restart Streamlit to reset UI

            # Get AI Response
            response = get_groq_response(user_input)

            # Store conversation history
            st.session_state.conversation.append(("You", user_input))
            st.session_state.conversation.append(("Bot", response))
            st.session_state.chat_history.append(("You", user_input))
            st.session_state.chat_history.append(("Bot", response))

            # Reset Input Field
            st.session_state.user_question = ""
            st.rerun()

    # Display Latest Response Separately
    if st.session_state.conversation:
        st.subheader("Generated Response")
        last_response = st.session_state.conversation[-1][1] if st.session_state.conversation[-1][0] == "Bot" else ""
        st.write(last_response)

    # Chat History Toggle
    if st.button("Show Chat History" if not st.session_state.show_chat_history else "Hide Chat History"):
        st.session_state.show_chat_history = not st.session_state.show_chat_history

    # Display Chat History
    if st.session_state.show_chat_history:
        st.subheader("Chat History")
        for role, message in st.session_state.chat_history:
            st.markdown(f"**{role}:** {message}")

# Main UI Tabs
tab1, tab2, tab3 = st.tabs(["👋 Introduction", "📝 Candidate Info & Questions", "🤖 Chatbot"])
with tab1: render_intro_tab()
with tab2: render_candidate_info_tab()
with tab3: render_chatbot_tab()