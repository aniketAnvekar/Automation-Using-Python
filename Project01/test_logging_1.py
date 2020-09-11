import logging

def test_logging():
    logger = logging.getLogger(__name__)
    filehandler = logging.FileHandler('logFile.log')

    format = logging.Formatter('%(asctime)s :%(levelname)s :%(name)s :%(message)s')
    filehandler.setFormatter(format)

    logger.addHandler(filehandler)

    logger.setLevel(logging.INFO)
    logger.debug("A debug statement is executed")
    logger.info("Info statement")
    logger.warning("Something is in warning mode")
    logger.error("A major error has happened")
    logger.critical("Critical issue")
