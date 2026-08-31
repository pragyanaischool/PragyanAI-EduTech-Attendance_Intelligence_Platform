import os
from langchain_groq import ChatGroq
from langchain.agents import create_sql_agent, AgentType
from langchain.sql_database import SQLDatabase
from langchain_community.agent_toolkits.sql.toolkit import SQLDatabaseToolkit
from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain.tools import Tool

class PragyanAgenticEngine:
    def __init__(self, db_path="sqlite:///pragyan_ai.db", persist_dir="./vector_store/policies_db"):
        self.api_key = os.getenv("GROQ_API_KEY", "gsk_dummy_key")
        self.llm = ChatGroq(
            temperature=0.1,
            groq_api_key=self.api_key,
            model_name="llama3-70b-8192"
        )
        
        # 1. Structured SQL Database connection
        self.sql_db = SQLDatabase.from_uri(db_path)
        
        # 2. Vector DB RAG for institutional policies
        self.embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
        
        if os.path.exists(persist_dir):
            self.vector_store = Chroma(persist_directory=persist_dir, embedding_function=self.embeddings)
        else:
            default_policies = [
                "Attendance Policy: Minimum mandatory attendance for semester exam eligibility is 75%.",
                "Medical Leave: Certified documents must be submitted within 3 days for up to 10% relaxation.",
                "Shortage Protocol: Automated warnings are triggered via WhatsApp/Email if attendance falls below 75%."
            ]
            self.vector_store = Chroma.from_texts(default_policies, self.embeddings, persist_directory=persist_dir)
            
        self.retriever = self.vector_store.as_retriever(search_kwargs={"k": 2})

    def get_agent_executor(self):
        """Builds agent binding SQL operational tools and vector document search RAG."""
        sql_toolkit = SQLDatabaseToolkit(db=self.sql_db, llm=self.llm)
        sql_tools = sql_toolkit.get_tools()
        
        def query_policy_kb(query: str) -> str:
            """Searches institutional rulebooks, bylaws, and exam eligibility guidelines."""
            docs = self.retriever.invoke(query)
            return "\n".join([d.page_content for d in docs])

        rag_tool = Tool(
            name="institutional_policy_search",
            func=query_policy_kb,
            description="Use for university attendance rules, detention policies, medical exemptions, or grading bylaws."
        )
        
        agent_executor = create_sql_agent(
            llm=self.llm,
            db=self.sql_db,
            extra_tools=[rag_tool],
            agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
            verbose=True,
            handle_parsing_errors=True
        )
        return agent_executor
