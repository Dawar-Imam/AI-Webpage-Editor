"""
Questions endpoints module.
Defines API routes related to question processing and LLM interactions.
"""

from fastapi import APIRouter
from app.schemas.schema import DemoRequest
from app.services.demo import demo_service
from app.core.logging import get_logger

demo_router = APIRouter()
logger = get_logger(__name__)

@demo_router.post("/demo_api")
async def demo_endpoint(demo: DemoRequest):
    """
    Demo endpoint for testing LLM interactions and response generation.
    Args:
        demo: DemoRequest object containing the demo request text.

    Returns:
        Json or a https response.
    """
    logger.info(f"Received demo request: {demo}")
    
    message = demo_service(demo)

    logger.info(f"Returning response: {message}")
    return {"answer": message}
