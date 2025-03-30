# Python
import chromadb
import chromadb.utils.embedding_functions as embedding_functions

print('Started Execution')
openai_ef = embedding_functions.OpenAIEmbeddingFunction(
                api_key="20891b095ec44cab8c2a84cae63de6c2",
                api_base="https://emx-openai-sweden-central.openai.azure.com",
                api_type="azure",
                api_version="2023-05-15",
                model_name="emx_embeddings_large")


# Example setup of the client to connect to your chroma server
#client = chromadb.HttpClient(host='localhost', port=8000)
client = chromadb.PersistentClient(path="/mnt/intonedb/chroma-data/chroma_db_master")

# Get the collection named 'collection_en_nl'
collection_name = 'collection_en_nl'
openai_ef = None  # Placeholder for the actual embedding function
collection = client.get_collection(name=collection_name, embedding_function=openai_ef)

# Query the collection for 'Market' data
query_results = collection.query(query_text='Market', n_results=5)

# Display the top 5 results
print("Top 5 results for 'Market':")
for result in query_results:
    print(result)
