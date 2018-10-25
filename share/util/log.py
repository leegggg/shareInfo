import logging


def getLogger(config: dict=None):

    isUseJournald = config.get("journald")
    handler = logging.StreamHandler()
    if isUseJournald:
        try:
            from systemd.journal import JournaldLogHandler
            handler = JournaldLogHandler()
        except:
            print("systemd not installed giveup using journald. Using StreamHandler stdout/stderr as fallback.")
            pass

    logger = logging.getLogger()
    formatter = logging.Formatter(
        '%(asctime)s - %(levelname)s %(filename)s(%(lineno)d) %(funcName)s(): \t %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.setLevel(config.get('log_level'))

    return logger

