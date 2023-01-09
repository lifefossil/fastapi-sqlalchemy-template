import logging
import datetime
# logging.basicConfig(format="%(asctime)s :: %(levelname)s :: %(name)s :: %(message)s", datefmt="%Y-%m-%d %H:%M:%S")
console_logger = logging.getLogger(__name__)
console_logger.propagate = False
sm = logging.StreamHandler()
smfmt = logging.Formatter(fmt="%(asctime)s -- %(levelname)s -- %(name)s -- %(message)s", datefmt="%Y-%m-%d %H:%M:%S")
sm.setFormatter(smfmt)
console_logger.addHandler(sm)
# log_file_handle = logging.FileHandler(filename='filelog.log')
# log_file_format = logging.Formatter(fmt="%(asctime)s :: %(levelname)s :: %(message)s", datefmt="%Y-%m-%d %H:%M:%S")
# log_file_handle.setFormatter(log_file_format)
# logger.addHandler(log_file_handle)
