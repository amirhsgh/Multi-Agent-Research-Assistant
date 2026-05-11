import asyncio
from typing import List, Dict, Any, Callable, Coroutine
from datetime import datetime
import time


class AsyncExecutor:
    """اجرای ناهمزمان وظایف برای افزایش سرعت"""
    
    def __init__(self, max_concurrent: int = 5):
        self.max_concurrent = max_concurrent
        self.semaphore = asyncio.Semaphore(max_concurrent)
    
    async def execute_task(
        self, 
        task_func: Callable, 
        *args, 
        **kwargs
    ) -> Dict[str, Any]:
        """اجرای یک تسک با محدودیت همزمانی"""
        
        async with self.semaphore:
            start_time = time.time()
            
            try:
                if asyncio.iscoroutinefunction(task_func):
                    result = await task_func(*args, **kwargs)
                else:
                    result = await asyncio.to_thread(task_func, *args, **kwargs)
                
                return {
                    "status": "success",
                    "result": result,
                    "duration": time.time() - start_time
                }
            
            except Exception as e:
                return {
                    "status": "error",
                    "error": str(e),
                    "duration": time.time() - start_time
                }
    
    async def execute_parallel(
        self, 
        tasks: List[Dict[str, Any]]
    ) -> List[Dict[str, Any]]:
        """اجرای موازی چندین تسک"""
        
        coroutines = [
            self.execute_task(
                task["func"],
                *task.get("args", []),
                **task.get("kwargs", {})
            )
            for task in tasks
        ]
        
        results = await asyncio.gather(*coroutines, return_exceptions=True)
        
        return results