"""
Utility module for logging in PocketFlow.

This module provides a configurable logging system for the PocketFlow framework.
It allows for easy control of log verbosity across modules.
"""

import logging
import sys
from typing import Union, Optional

# Create a logger for the PocketFlow framework
logger = logging.getLogger("pocketflow")

# Default configuration
DEFAULT_FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
DEFAULT_LEVEL = logging.INFO


def configure_logging(
    level: Union[int, str] = DEFAULT_LEVEL,
    format_str: str = DEFAULT_FORMAT,
    log_file: Optional[str] = None
) -> None:
    """
    Configure the logging system.
    
    Args:
        level: Logging level (DEBUG, INFO, WARNING, ERROR, CRITICAL)
        format_str: Format string for log messages
        log_file: Optional file path to write logs to
    """
    # Convert string level to numeric if needed
    if isinstance(level, str):
        level = getattr(logging, level.upper())
    
    # Reset handlers to avoid duplicates
    logger.handlers = []
    
    # Set the logging level
    logger.setLevel(level)
    
    # Create formatter
    formatter = logging.Formatter(format_str)
    
    # Add console handler
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)
    
    # Add file handler if requested
    if log_file:
        file_handler = logging.FileHandler(log_file)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)


def set_log_level(level: Union[int, str]) -> None:
    """
    Set the logging level.
    
    Args:
        level: Either a string ('DEBUG', 'INFO', etc.) or a logging constant
    """
    if isinstance(level, str):
        level = getattr(logging, level.upper())
    logger.setLevel(level)


def get_logger(name: Optional[str] = None) -> logging.Logger:
    """
    Get a logger instance.
    
    Args:
        name: Optional name for the logger (will be prefixed with 'pocketflow.')
    
    Returns:
        A configured logger instance
    """
    if name:
        return logging.getLogger(f"pocketflow.{name}")
    return logger


# Configure the default logger
configure_logging()