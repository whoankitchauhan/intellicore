from langchain.tools import tool
import requests
from bs4 import BeautifulSoup
from tavily import TavilyClient
import os
from dotenv import load_dotenv
from rich import print
load_dotenv()

tavily = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))

@tool 
def web_search(query: str) -> str:
    """Search the web for recent information. 
    The query must consist of short, specific keywords or direct questions. 
    Avoid unnecessary conversational words like 'please', 'find', or 'search for'."""
    try:
        results = tavily.search(query=query, max_results=2)
    
        out = []
    
        for r in results['results']:
            out.append(f"Title: {r['title']}\nURL: {r['url']}\nSnippet: {r['content'][:300]}\n")  
        
        
        return "\n----\n".join(out)
    except Exception as e:
        return f"An error occurred while searching: {str(e)}"

print(web_search.invoke("latest advancements in AI technology"))