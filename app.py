import streamlit as st
from langchain_experimental.agents.agent_toolkits import create_pandas_dataframe_agent  # Use experimental version
from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os
import pandas as pd

# Configure Streamlit page (must be the first Streamlit command)
st.set_page_config(page_title="Ask your CSV")

def main():
    # Load environment variables from .env file
    load_dotenv()

    # Load the Groq API key from the environment variable
    groq_api_key = os.getenv("GROQ_API_KEY")
    if not groq_api_key:
        st.error("GROQ_API_KEY is not set. Please set it in your .env file or environment variables.")
        st.stop()
    else:
        st.success("GROQ_API_KEY is set")

    # Set header
    st.header("Ask your CSV 📈")

    # File uploader for CSV
    csv_file = st.file_uploader("Upload a CSV file", type="csv")
    
    if csv_file is not None:
        try:
            # Read the CSV file into a pandas DataFrame
            df = pd.read_csv(csv_file)
            
            # Initialize Groq's LLaMA 3 model
            llm = ChatGroq(
                model="llama3-70b-8192",
                temperature=0,
                api_key=groq_api_key
            )

            # Create CSV agent
            agent = create_pandas_dataframe_agent(
                llm,
                df,  # Pass the DataFrame directly
                verbose=True,
                allow_dangerous_code=True  # Required for CSV agent to execute pandas code
            )

            # User input for question
            user_question = st.text_input("Ask a question about your CSV: ")

            if user_question and user_question.strip():
                with st.spinner(text="In progress..."):
                    try:
                        response = agent.invoke(user_question)
                        st.write(response['output'])
                    except Exception as e:
                        st.error(f"An error occurred while processing the question: {str(e)}")
        except Exception as e:
            st.error(f"An error occurred while reading the CSV file: {str(e)}")

if __name__ == "__main__":
    main()