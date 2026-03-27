from app.core.logging import get_logger

logger = get_logger(__name__)
def demo_service(demo):
    """
    Service function to process the demo request and generate a response.
    Args:
        demo: demoRequest object containing the demo request text.  
    Returns:
        String response generated based on the demo request.
    """
    logger.info(f"Processing demo request: {demo}")
    # For demonstration, we simply return a message based on the input text.    
    response = f"Received your demo request with text: '{demo.text}'. This is a response from the demo service."
    logger.info(f"Generated response: {response}")      
    return response
    