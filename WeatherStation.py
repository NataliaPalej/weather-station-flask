from flask import Flask, render_template
from sense_hat import SenseHat

app = Flask(__name__)


@app.route('/')
def index():
    sense = SenseHat()

    celsius = round(sense.get_temperature(), 1)
    fahrenheit = round(1.8 * celsius + 32, 1)
    humidity = sense.get_humidity_from_humidity()
    pressure = sense.get_pressure_from_pressure()
    h = sense.get_humidity()
    p = sense.get_pressure()

    return render_template('weather.html', celsius=celsius, fahrenheit=fahrenheit, pressure=pressure, humidity=humidity)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

