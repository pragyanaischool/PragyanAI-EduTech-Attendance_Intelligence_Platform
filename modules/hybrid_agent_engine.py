import os
from langchain_groq import ChatGroq
from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings

class PragyanAgenticEngine:
    def __init__(self, db_path="sqlite:///pragyan_ai.db", persist_dir="./vector_store/policies_db"):
        self.api_key = os.getenv("GROQ_API_KEY", "gsk_dummy_key")
        self.llm = ChatGroq(
            temperature=0.1,
            groq_api_key=self.api_key,
            model_name="llama3-70b-8192"
        )
        
        # 1. Vector DB RAG for institutional policies & bylaws
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
        """Returns a robust execution wrapper that handles queries via Groq LLM and vector RAG."""
        class RobustAgentExecutor:
            def __init__(self, llm, retriever):
                self.llm = llm
                self.retriever = retriever

            def run(self, query_text: str) -> str:
                # Retrieve relevant policy documents
                docs = self.retriever.invoke(query_text)
                policy_context = "\n".join([d.page_content for d in docs])
                
                prompt = (
                    f"You are PragyanAI, an intelligent university attendance platform assistant. "
                    f"Answer the user query accurately using institutional guidelines and data context.\n\n"
                    f"Relevant Institutional Policies:\n{policy_context}\n\n"
                    f"User Query: {query_text}\n\n"
                    f"Provide a helpful, professional, and clear response:"
                )
                response = self.llm.invoke(prompt)
                return response.content

        return RobustAgentExecutor(self.llm, self.retriever)
