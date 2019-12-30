import logging
import logging.handlers
import datetime

log = logging.getLogger('log_custom')

log.setLevel(logging.DEBUG)
log.propagate = True

formatter = logging.Formatter("%(asctime)s %(levelname)s %(message)s")

fileHandler = logging.handlers.TimedRotatingFileHandler(
    filename='store_alarm.log',
    when='D',
    atTime=datetime.time(0, 0, 0)
)

consoleHandler = logging.StreamHandler()

fileHandler.setLevel(logging.DEBUG)
fileHandler.setFormatter(formatter)

log.addHandler(fileHandler)
log.addHandler(consoleHandler)
