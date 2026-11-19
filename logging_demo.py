
import logging

from order import calculate_order_total

logging.basicConfig(
    filename="application.log",
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
    force=True,
)

def process_order(price, discount):
    logging.debug("Starting order processing")

    try:
        logging.info("Processing order")

        total = calculate_order_total(price, discount)

        logging.info("Order processed successfully")
        logging.debug("Final order amount: %s", total)

        return total

    except ValueError as error:
        logging.error("Order processing failed: %s", error)
        return None


if __name__ == "__main__":
    logging.warning("Order processing application started")

    process_order(1000, 10)
    process_order(-100, 10)

    logging.info("Order processing application finished")
