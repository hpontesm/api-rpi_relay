from flask import Flask, jsonify, request
import RPi.GPIO as GPIO
import time

GPIO_PIN = 11

app = Flask(__name__)

# Set up GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(GPIO_PIN, GPIO.OUT)  # Assuming pin 11 for demonstration purposes

@app.route('/gpio/control', methods=['GET'])
def control_gpio():
    duration = request.args.get('duration', 1)  # Default duration is 1 second

    # Toggle GPIO pin state
    GPIO.output(GPIO_PIN, not GPIO.input(GPIO_PIN))
    time.sleep(float(duration))
    GPIO.output(GPIO_PIN, not GPIO.input(GPIO_PIN))

    return jsonify({'message': f'GPIO toggled for {duration} seconds'})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port="3000")
