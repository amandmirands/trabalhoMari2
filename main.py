from kivy.app import App
from mainwidget import MainWidget
from kivy.lang.builder import Builder


class MainApp(App):
    """
    Classe com o aplicativo
    """

    def build(self):
        """
        Método que gera o aplicativo com base no widget principal
        """
        self._widget = MainWidget(
            scan_time=1000,                     
            server_ip='192.168.0.11', #INTERNO
            server_port=502,

            # server_ip='10.15.20.17', #EXTERNO
            # server_port=10011,

            # server_ip='localhost', #SIMULADOR
            # server_port=502,
            modbus_addrs=self.getTagsConfigs()
        )

        return self._widget

    def getTagsConfigs(self):
        return {
                # adicionar variáveis da
            "torque": {"type": "mainLabel", "address": 1420, "div": 100, "unit": "N.m"}, # tipo FP
            "carga": {"type": "mainLabel", "address": 710, "div": 1, "unit": "kgf/cm3"}, # tipo FP
            "freq_rot": {"type": "mainLabel", "address": 884, "div": 1, "unit": "RPM"}, # tipo FP
            "vel_est": {"type": "mainLabel", "address": 724, "div": 1, "unit": "m/min"}, # tipo FP
            "freq": {"type": "motorInfo", "address": 830, "div": 100, "unit": "Hz"}, # tipo 4X
            "current": {"type": "motorInfo", "address": 845, "div": 100, "unit": "A", "ymax": 5}, # tipo 4X
            "P": {"type": "motorInfo", "address": 855, "div": 1, "unit": "W", "ymax": 1500}, # tipo 4X
            "Q": {"type": "negative", "address": 859, "div": 1, "unit": "VAr", "ymax": 1000}, # tipo 4X
            "S": {"type": "motorInfo", "address": 863, "div": 1, "unit": "VA", "ymax": 2000}, # tipo 4X
            "startType": {"type": "startType", "address": 1216, "div": 1}, # tipo 4X
            "activeMotor": {"type": "activeMotor", "address": 1330, "bit": 0}, # tipo 4X
            "inversorFreq": {"type": "inversorFreq", "address": 1313, "div": 10}, # tipo 4X
            "accTime": {"type": "accDccTime", "address": 1317, "div": 1}, # tipo 4X
            "desaccTime": {"type": "accDccTime", "address": 1318, "div": 1}, # tipo 4X
            "temp_R": {"type": "TempMotor", "address": 700, "div": 10, "unit": "°C"}, # tipo FP
            "temp_S": {"type": "TempMotor", "address": 702, "div": 10, "unit": "°C"}, # tipo FP
            "temp_T": {"type": "TempMotor", "address": 704, "div": 10, "unit": "°C"}, # tipo FP
            "temp_C": {"type": "TempMotor", "address": 706, "div": 10, "unit": "°C"}, # tipo FP
            "corr_R": {"type": "CurrentMotor", "address": 840, "div": 100, "unit": "A"}, # tipo 4X
            "corr_S": {"type": "CurrentMotor", "address": 841, "div": 100, "unit": "A"}, # tipo 4X
            "corr_T": {"type": "CurrentMotor", "address": 842, "div": 100, "unit": "A"}, # tipo 4X
            "corr_N": {"type": "CurrentMotor", "address": 843, "div": 100, "unit": "A"}, # tipo 4X
            "ddp_RS": {"type": "DDPMotor", "address": 847, "div": 10, "unit": "V"}, # tipo 4X
            "ddp_ST": {"type": "DDPMotor", "address": 848, "div": 10, "unit": "V"}, # tipo 4X
            "ddp_TR": {"type": "DDPMotor", "address": 849, "div": 10, "unit": "V"},  # tipo 4X
            "sel_pid": {"type": "controlType", "address": 1332, "div": 1},  # tipo 4X
            "mv_escreve": {"type": "vm", "address": 1310, "div": 1} # tipo FP
         }

    def on_stop(self):
        """
        Método executado quando a aplicação é fechada
        """
        self._widget.stopRefresh()


if __name__ == '__main__':
    Builder.load_string(open("mainwidget.kv", encoding="utf-8").read(), rulesonly=True)
    Builder.load_string(open("popups.kv", encoding="utf-8").read(), rulesonly=True)
    MainApp().run()