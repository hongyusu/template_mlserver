# -*- coding: utf-8 -*-
import logging
import json

__all__ = ['set_logger']


def set_logger(context, verbose=False):
    logger = logging.getLogger(context)
    logger.setLevel(logging.DEBUG if verbose else logging.INFO)
    formatter = logging.Formatter(
        '%(asctime)s' + '%20s' % context +
        '%(filename)15s %(funcName)20s %(levelname)s %(lineno)3d: %(message)s',
        datefmt='%m-%d %H:%M:%S')
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG if verbose else logging.INFO)
    console_handler.setFormatter(formatter)
    logger.handlers = []
    logger.addHandler(console_handler)
    return logger


def send_celery_log(logger_func, msg, logstash_tag='innobot.system:'):
    """Helper function to manupilate log sent to our logstash.

    This is to wrap a string with a simple json string
    along with the logstash tag we configured in our logstash config.

    Args:
        logger_func: The celery task logger function
            logger = by calling get_task_logger(__name__)
            logger_func = logger.info
        level: The log level string
            e.g. debug, info, warning, critical, exception
        logstash_tag: The necessary tag to annotate our log to pass the filter
            Default = 'innobot.system:'
        msg: The original log string.

    Return:
        None
    """
    log_dict = {'msg': msg}
    logger_func(logstash_tag + json.dumps(log_dict))
