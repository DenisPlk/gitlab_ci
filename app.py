from flask import Flask, render_template, request, jsonify
from test_bench import TestBench  # Импорт вашего класса test

app = Flask(__name__)
bench = TestBench()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/command", methods=["POST"])
def handle_command():
    data = request.json
    cmd = data.get("command")
    arg = data.get("argument")

    response = {"success": False, "message": ""}

    if cmd == "on":
        bench.power_on()
        response["message"] = "Устройство включено."
        response["success"] = True
    elif cmd == "off":
        bench.power_off()
        response["message"] = "Устройство выключено."
        response["success"] = True
    elif cmd == "set_v":
        try:
            voltage = float(arg)
            bench.set_voltage(voltage)
            response["message"] = f"Напряжение: {voltage} В"
            response["success"] = True
        except ValueError:
            response["message"] = "Ошибка: введите число!"
    elif cmd == "set_i":
        try:
            current = float(arg)
            bench.set_current(current)
            response["message"] = f"Ток: {current} А"
            response["success"] = True
        except ValueError:
            response["message"] = "Ошибка: введите число!"
    elif cmd == "temp":
        bench.measure_temperature()
        response["message"] = f"Температура: {bench.temperature} °C"
        response["success"] = True
    elif cmd == "status":
        status = {
            "power": "ВКЛ" if bench.is_powered_on else "ВЫКЛ",
            "voltage": bench.voltage,
            "current": bench.current,
            "temperature": bench.temperature,
        }
        response["status"] = status
        response["success"] = True
    else:
        response["message"] = "Неизвестная команда!"

    return jsonify(response)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
