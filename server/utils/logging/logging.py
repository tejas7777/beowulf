import logging

logging.basicConfig(
    level=logging.INFO,    # Set the logging level (e.g., DEBUG, INFO, ERROR)
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    filename='app.log',    # Specify the log file name
    filemode='w'           # Specify the file mode (w for writing, a for appending)
)

logger = logging