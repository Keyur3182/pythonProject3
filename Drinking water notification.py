import time
from plyer import notification

if __name__ == "__main__":
    while True:
        notification.notify(
            title="please Drink water right now",
            timeout=12,
            message="the water is very important for health "
        )
        time.sleep(60)
