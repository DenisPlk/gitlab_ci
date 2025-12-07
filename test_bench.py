class TestBench:
    def __init__(self):
        self.is_powered_on = False
        self.voltage = 0.0
        self.current = 0.0
        self.temperature = 25.0  # Начальная температура

    def power_on(self):
        if not self.is_powered_on:
            self.is_powered_on = True
            print("Устройство включено.")
        else:
            print("Устройство уже включено.")

    def power_off(self):
        if self.is_powered_on:
            self.is_powered_on = False
            self.voltage = 0.0
            self.current = 0.0
            print("Устройство выключено.")
        else:
            print("Устройство уже выключено.")

    def set_voltage(self, voltage):
        if self.is_powered_on:
            self.voltage = voltage
            print(f"Напряжение установлено: {voltage} В.")
        else:
            print("Ошибка: устройство выключено!")

    def set_current(self, current):
        if self.is_powered_on:
            self.current = current
            print(f"Ток установлен: {current} А.")
        else:
            print("Ошибка: устройство выключено!")

    def measure_temperature(self):
        if self.is_powered_on:
            # Имитация изменения температуры в зависимости от тока
            self.temperature = 25.0 + (self.current * 2)
            print(f"Температура: {self.temperature:.1f} °C.")
        else:
            print("Ошибка: устройство выключено!")

    def status(self):
        print("\n--- Статус устройства ---")
        print(f"Питание: {'ВКЛ' if self.is_powered_on else 'ВЫКЛ'}")
        print(f"Напряжение: {self.voltage} В")
        print(f"Ток: {self.current} А")
        print(f"Температура: {self.temperature} °C\n")


def main():
    bench = TestBench()
    print("Добро пожаловать в тестовый стенд!")
    print("Доступные команды:")
    print("1. on - включить устройство")
    print("2. off - выключить устройство")
    print("3. set_v <напряжение> - установить напряжение")
    print("4. set_i <ток> - установить ток")
    print("5. temp - измерить температуру")
    print("6. status - показать статус")
    print("7. exit - выход")

    while True:
        cmd = input("\nВведите команду: ").strip().lower().split()
        if not cmd:
            continue

        if cmd[0] == "on":
            bench.power_on()
        elif cmd[0] == "off":
            bench.power_off()
        elif cmd[0] == "set_v" and len(cmd) == 2:
            try:
                voltage = float(cmd[1])
                bench.set_voltage(voltage)
            except ValueError:
                print("Ошибка: введите число!")
        elif cmd[0] == "set_i" and len(cmd) == 2:
            try:
                current = float(cmd[1])
                bench.set_current(current)
            except ValueError:
                print("Ошибка: введите число!")
        elif cmd[0] == "temp":
            bench.measure_temperature()
        elif cmd[0] == "status":
            bench.status()
        elif cmd[0] == "exit":
            print("Завершение работы...")
            break
        else:
            print("Неизвестная команда!")


if __name__ == "__main__":
    main()
