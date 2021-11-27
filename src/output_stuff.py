import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("root")

def output_with_error():
    print("THE-MSG")
    logger.warning("THE-LOG")
    print("THE-MSG-2")
    raise ValueError("THE-ERROR")
