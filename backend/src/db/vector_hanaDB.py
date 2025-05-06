import os
import time
from typing import List
from hdbcli import dbapi
from langchain_core.documents import Document
from langchain_community.vectorstores.hanavector import HanaDB
from gen_ai_hub.proxy.langchain.init_models import init_embedding_model


class CAPVectorDBHelper:
    _instance = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super(CAPVectorDBHelper, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        if not hasattr(self, "initialized"):
            self.embedding_model = None
            self.db = None
            self.connection = None
            self.initialized = False
            self.init_db()

    def init_db(self):
        self.HANA_HOST_VECTOR = os.getenv("HANA_HOST_VECTOR")
        self.HANA_VECTOR_USER = os.getenv("HANA_VECTOR_USER")
        self.HANA_VECTOR_PASS = os.getenv("HANA_VECTOR_PASS")
        self.HANA_SCHEMA = os.getenv("HANA_SCHEMA")
        self.HANA_TABLE = os.getenv("HANA_TABLE")
        self.HANA_EMBEDDING_COLUMN = os.getenv("HANA_EMBEDDING_COLUMN")
        self.HANA_METADATA_COLUMN = os.getenv("HANA_METADATA_COLUMN")
        self.HANA_TEXT_COLUMN = os.getenv("HANA_TEXT_COLUMN")

        self.embedding_model = init_embedding_model(os.getenv("MODEL_EMBEDDING"))
        self.connect_db()
        self.initialized = True

    def connect_to_hana(self):
        if self.connection:
            return self.connection
        retries = 3
        while retries > 0:
            try:
                conn = dbapi.connect(
                    address=self.HANA_HOST_VECTOR,
                    port=443,
                    user=self.HANA_VECTOR_USER,
                    password=self.HANA_VECTOR_PASS,
                    currentSchema=self.HANA_SCHEMA,
                )
                print("✅ Connected to HANA")
                return conn
            except dbapi.Error as e:
                print(f"❌ Connection failed: {e}")
                retries -= 1
                time.sleep(5)
        raise ConnectionError("Failed to connect to HANA after several retries.")

    def connect_db(self):
        self.connection = self.connect_to_hana()
        self.db = HanaDB(
            connection=self.connection,
            embedding=self.embedding_model,
            table_name=self.HANA_TABLE,
            content_column=self.HANA_TEXT_COLUMN,
            metadata_column=self.HANA_METADATA_COLUMN,
            vector_column=self.HANA_EMBEDDING_COLUMN,
        )

    def add_summary(self, content: str, metadata: dict):
        try:
            doc = Document(page_content=content, metadata=metadata)
            self.db.add_documents([doc])
            print("✅ Summary added to vector DB")
        except Exception as e:
            print(f"❌ Failed to add summary: {e}")