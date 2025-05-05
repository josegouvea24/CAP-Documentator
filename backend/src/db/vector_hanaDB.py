import os
import time
from typing import List
from hdbcli import dbapi
from models.chunk import DocChunk
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
            self.connection = None
            self.cursor = None
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
        
        self.connect_to_hana()
        self.initialized = True

    def connect_to_hana(self):
        retries = 3
        while retries > 0:
            try:
                self.connection = dbapi.connect(
                    address=self.HANA_HOST_VECTOR,
                    port=443,
                    user=self.HANA_VECTOR_USER,
                    password=self.HANA_VECTOR_PASS,
                    currentSchema=self.HANA_SCHEMA,
                    encrypt=True,
                    sslValidateCertificate=False
                )
                self.cursor = self.connection.cursor()
                print("✅ Connected to HANA")
                return
            except dbapi.Error as e:
                print(f"❌ Connection failed: {e}")
                retries -= 1
                time.sleep(5)
        raise ConnectionError("Failed to connect to HANA after several retries.")

    def add_summary(self, file: DocChunk):
        try:
            insert_sql = f"""
                INSERT INTO {self.HANA_TABLE} 
                (FILEPATH, CAPSECTION, FILETYPE, CONTENT, SUMMARY)
                VALUES (?, ?, ?, ?, ?)
            """
            self.cursor.execute(insert_sql, (
                file.path,
                file.section,
                file.type,
                file.content,
                file.metadata.get("summary", "")  # optional: fallback to empty summary
            ))
            self.connection.commit()
            print(f"✅ Inserted chunk {file.path} into {self.HANA_TABLE}")
        except Exception as e:
            print(f"❌ Error inserting summary: {e}")


     