import os
from google.cloud import bigquery_migration_v2
from google.cloud.bigquery_migration_v2 import MigrationServiceClient


def translate_sqlite_to_bigquery(sqlite_query, credentials_path=None):
    """
    Translates SQLite queries to BigQuery SQL using the BigQuery Migration API.
    
    Args:
        sqlite_query (str): The SQLite query to translate
        credentials_path (str, optional): Path to the service account JSON key file.
            If None, uses application default credentials.
        
    Returns:
        str: Translated BigQuery SQL query
    """
    try:
        # Set up authentication
        if credentials_path:
            # Set environment variable for credentials
            os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = credentials_path
        
        # Initialize the client
        client = MigrationServiceClient()
        
        # Get available methods to see what we can use
        print("Available methods in MigrationServiceClient:")
        translation_methods = [m for m in dir(client) if 'translate' in m.lower() and not m.startswith('_')]
        for method in translation_methods:
            print(f"- {method}")
            
        # Use the appropriate method based on what's available
        # First try to see if translate_query method exists
        if hasattr(client, 'translate_query'):
            print("Using translate_query method")
            
            # Determine project from credentials or environment
            project_id = os.environ.get("GOOGLE_CLOUD_PROJECT")
            parent = f"projects/{project_id}/locations/us"
            
            response = client.translate_query(
                request={
                    "parent": parent,
                    "query": sqlite_query,
                    "source_dialect": "SQL_SQLITE",
                    "target_dialect": "SQL_BIGQUERY"
                }
            )
            return response.translated_query
            
        # If we have other methods that might work, try them here
        # For example, if there's a method with similar name
        
        # If we can't find appropriate methods, print instructions
        print("\nCouldn't find appropriate translation methods in your version of the library.")
        print("Please check your library version and consider upgrading:")
        print("pip install --upgrade google-cloud-bigquery-migration")
        print("\nAlternative approach: You can use the BigQuery web console for translation:")
        print("1. Go to https://console.cloud.google.com/bigquery")
        print("2. Use the 'Query editor' and click on 'Conversion' tab")
        print("3. Select SQLite as source dialect and paste your query")
        
        return "Translation method not available in the installed library version"
        
    except Exception as e:
        print(f"Error: {str(e)}")
        
        # Check if the client was initialized
        if 'client' not in locals():
            print("\nFailed to initialize the client. Verify your authentication:")
            print("1. Check if your service account key is valid")
            print("2. Ensure the service account has the necessary permissions")
            print("3. Verify that the BigQuery Migration API is enabled in your project")
            print("\nTo enable the API, visit: https://console.cloud.google.com/apis/library/bigquerymigration.googleapis.com")
        
        return f"Translation failed: {str(e)}"


# Example usage
if __name__ == "__main__":
    sqlite_query = """
    SELECT strftime('%Y-%m-%d', created_at) AS formatted_date 
    FROM users 
    WHERE age > 25;
    """
    
    # Path to your service account key file
    credentials_path = "D:/GCP/key.json"
    
    result = translate_sqlite_to_bigquery(sqlite_query, credentials_path)
    print("\nTranslation Result:")
    print(result)