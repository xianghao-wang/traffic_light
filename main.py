import RPi.GPIO as GPIO
import json
import time

CONFIG_PATH = "./lights.json"

# read configurations
def read_config():
    with open(CONFIG_PATH, "r") as f:
        contents = f.read()
    
    return json.loads(contents)

# set the target ON, and others OFF
def set_lights(pins, target):
    for pin in pins:
        GPIO.output(pin, GPIO.LOW)
    
    GPIO.output(target, GPIO.HIGH)

# Control the three lights
def control(red, yellow, green):
    while True:
        print("Turning on RED")
        set_lights([red, green, yellow], red)
        time.sleep(5)

        print("Turning on YELLOW")
        set_lights([red, green, yellow], yellow)
        time.sleep(1)

        print("Turning on GREEN")
        set_lights([red, green, yellow], green)
        time.sleep(5)

def main():
    config = read_config()

    # Choose the mode
    mode = config['mode']
    if mode == "BCM":
        GPIO.setmode(GPIO.BCM)
    else:
        GPIO.setmode(GPIO.BOARD)

    # Map each pin to a constant
    RED = config['red']
    YELLOW = config['yellow']
    GREEN = config['green']
    PINS = [RED, YELLOW, GREEN]

    # Set pins to OUT
    for pin in PINS:
        GPIO.setup(pin, GPIO.OUT)

    # Control the lights
    control(RED, YELLOW, GREEN)

    GPIO.cleanup()



if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt as e:
        print("Good bye")
        GPIO.cleanup()

