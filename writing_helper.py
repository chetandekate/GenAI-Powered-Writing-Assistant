from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import os
import streamlit as st
from dotenv import load_dotenv
from typing import Final

MAX_CHARS : Final[int]=  500 #define constant
Style_Options : Final[tuple[str, ...]]=(
    "Email",
    "Twitter",
    "LinkedIn",
    "Facebook",
    "Instagram",
    "Blog"
)

def load_environment() -> None:
    load_dotenv()

    #"""Get OpenAI_API_KEY and LANGCHAIN_API_KEY from .env"""
    if os.getenv("OPENAI_API_KEY"):
        os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
    else:
        raise EnvironmentError(
            "OPENAI_API_KEY is missing in .env file, Add it to your .env file"
        )
    if os.getenv("LANGCHAIN_API_KEY"):
        os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
    else:
        raise EnvironmentError(
            "LANGCHAIN_API_KEY is missing in .env file, add it to your .env file"
        )

def build_chain():
    """Create and return the LangChain pipeline."""
    prompt = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                f"""You are a professional writing assistant.

            Write a clear, polite, and engaging response based on the user's topic and selected style/platform.

            Rules:
            - Keep the response within {MAX_CHARS} characters maximum.
            - Match the tone and format to the selected style (Email, LinkedIn, Twitter, Instagram, Facebook).
            - Do not invent facts or add unsupported details.
            - If the user's topic is vague, write a general response without assumptions.
            - Return only the final write-up, with no explanations.

            Style guidance:
            - Email: professional and polite, complete sentences.
            - LinkedIn: professional, thoughtful, business/career-oriented.
            - Twitter: concise, punchy, attention-grabbing.
            - Instagram: engaging, social, friendly tone.
            - Facebook: conversational and community-friendly.
            """,
                        ),
                        (
                            "user",
                            """Topic/Question: {question}
            Style: {style}

            Write a polished response based on the topic in the requested style.""",
            ),
        ]
    )

    llm = ChatOpenAI(
        model="gpt-3.5-turbo",
        temperature=0.7,
        max_tokens=500
        )
    output_parse = StrOutputParser()

    return prompt | llm | output_parse

def genrate_writeup(chain, question : str, style : str) -> str:
        result = chain.invoke(
             {
                'question' : question,
                'style' : style
             }
        )
        return result

def main():
    st.set_page_config(
          page_title = "Generic Writeing help",
          page_icon = "✍️",
          layout = "centered"
    )
    st.title("Generic Writeing help ✍️")
    try:
          load_environment()
          chain = build_chain()
    except Exception as exec:
         st.error("Error in start-up {exec}")
         st.stop()
         
    question = st.text_input(
         "Provide topic of your write-up",
         placeholder="e.g., Launch announcement for my portfolio website"
    )
    style = st.selectbox(
         "Choose your writing style/platform",
         Style_Options,
         index = None,
         placeholder = "Select a style"
    )

    if st.button("Genrate", type="primary"):
         if question and style:
              try:
                    with st.spinner("Generating..."):
                        result = genrate_writeup(chain, question, style)
                    st.subheader("Genrated Writeup")
                    st.write(result)
              except Exception as exec:
                   st.error("Genration Error : {exec}")
         else:
              st.warning("Please enter both Question & Style")
              st.stop()
if __name__ == "__main__":
    main()