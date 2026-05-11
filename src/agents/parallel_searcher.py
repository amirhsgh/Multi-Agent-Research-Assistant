import asyncio
from typing import List, Dict
from tavily import TavilyClient
from langchain_core.messages import HumanMessage


class ParallelSearchAgent:
    """عامل جستجوی موازی - اجرای همزمان چندین جستجو"""
    
    def __init__(self, tavily_api_key: str, max_parallel: int = 3):
        self.tavily = TavilyClient(api_key=tavily_api_key)
        self.max_parallel = max_parallel
    
    async def search_single_query(self, query: str) -> Dict:
        """جستجوی یک کوئری"""
        
        try:
            # Tavily همزمان نیست، پس در thread جداگانه اجرا می‌کنیم
            result = await asyncio.to_thread(
                self.tavily.search,
                query=query,
                max_results=5
            )
            
            return {
                "query": query,
                "status": "success",
                "results": result.get("results", [])
            }
        
        except Exception as e:
            return {
                "query": query,
                "status": "error",
                "error": str(e),
                "results": []
            }
    
    async def search_parallel(self, queries: List[str]) -> List[Dict]:
        """جستجوی موازی چندین کوئری"""
        
        # محدود کردن تعداد جستجوهای همزمان
        semaphore = asyncio.Semaphore(self.max_parallel)
        
        async def bounded_search(query: str):
            async with semaphore:
                return await self.search_single_query(query)
        
        tasks = [bounded_search(q) for q in queries]
        results = await asyncio.gather(*tasks)
        
        return results
    
    def format_results(self, search_results: List[Dict]) -> str:
        """فرمت کردن نتایج برای خروجی"""
        
        formatted = []
        
        for search in search_results:
            query = search["query"]
            
            if search["status"] == "success":
                formatted.append(f"\n### Query: {query}")
                
                for idx, result in enumerate(search["results"], 1):
                    formatted.append(
                        f"{idx}. {result.get('title', 'No title')}\n"
                        f"   URL: {result.get('url', 'N/A')}\n"
                        f"   {result.get('content', 'No content')[:200]}..."
                    )
            else:
                formatted.append(
                    f"\n### Query: {query}\n"
                    f"   Error: {search.get('error', 'Unknown error')}"
                )
        
        return "\n".join(formatted)
    
    def get_all_sources(self, search_results: List[Dict]) -> List[Dict]:
        """استخراج تمام منابع برای citation"""
        
        sources = []
        
        for search in search_results:
            if search["status"] == "success":
                for result in search["results"]:
                    sources.append({
                        "title": result.get("title", "Unknown"),
                        "url": result.get("url", ""),
                        "query": search["query"]
                    })
        
        return sources
