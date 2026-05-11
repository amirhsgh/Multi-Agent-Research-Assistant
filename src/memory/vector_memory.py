import collections

from openai import embeddings
from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings
from langchain_core.documents import Document
from typing import List
import uuid


class VectorMemory:

    def __init__(
        self,
        persist_directory: str = "./chroma_db"):

        self.embeddings = OpenAIEmbeddings()

        self.vectorstore = Chroma(
            collection_name="research_memory",
            embedding_function=self.embeddings,
            persist_directory=persist_directory
        )

    def store_research(
        self,
        topic: str,
        content: str,
        metadata: dict = None
    ):
        """ذخیره تحقیق"""

        doc = Document(
            page_content=content,
            metadata={
                "topic": topic,
                "id": str(uuid.uuid4()),
                **(metadata or {})
            }
        )

        self.vectorstore.add_documents([doc])

    
    def search_memory(
        self,
        query: str,
        k: int = 5
    ) -> List[Document]:
        """جستجوی semantic"""

        return self.vectorstore.similarity_search(
            query=query,
            k=k
        )

    
    def get_context_for_topic(
        self,
        topic: str
    ) -> str:
        """بازیابی context مرتبط"""

        docs = self.search_memory(topic)

        if not docs:
            return ""

        return "\n\n".join([
            doc.page_content
            for doc in docs
        ])