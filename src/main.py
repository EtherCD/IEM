from dearpygui.dearpygui import *
import lang
import calc

REPLICAS = lang.get_replicas()

create_context()
create_viewport(title="Inverter Energy Monitor (Beta)", width=902, height=506, clear_color=[40, 40, 40])
enable_docking(dock_space=True)

# Values
# First Window
_fw = REPLICAS[0]
_fw_title = _fw["title"]
_fw_p = _fw["p"]
_fw_efficiency = _fw["efficiency"]
_fw_consumption = _fw["consumption"]
_fw_time = _fw["time"]
_fw_capacity = _fw["capacity"]
_fw_volt = _fw["volt"]
_fw_remainder = _fw["remainder"]
_fw_default_result = _fw["default_result"]
_fw_button = _fw["button"]
_fw_result = _fw["result"]
# Second Window
_sw = REPLICAS[1]
_sw_title = _sw["title"]
_sw_p = _sw["p"]
_sw_time = _sw["time"]
_sw_capacity = _sw["capacity"]
_sw_volt = _sw["volt"]
_sw_remainder = _sw["remainder"]
_sw_default_result = _sw["default_result"]
_sw_button = _sw["button"]
_sw_result = _sw["result"]
# End

# Register Values
#with font_registry():
#    font = add_font("res/Roboto-Light.ttf", 19)

with value_registry():
    add_string_value(tag="result", default_value=_fw_default_result)
    add_float_value(tag="efficiency", default_value=94)
    add_float_value(tag="consumption", default_value=1000)
    add_float_value(tag="time", default_value=1)
    add_float_value(tag="capacity", default_value=60)
    add_float_value(tag="volt", default_value=12)
    add_float_value(tag="remainder", default_value=100)

    add_string_value(tag="r_result", default_value=_sw_default_result)
    add_float_value(tag="r_time", default_value=1)
    add_float_value(tag="r_capacity", default_value=60)
    add_float_value(tag="r_volt", default_value=12)
    add_float_value(tag="r_remainder", default_value=60)
# End


# Callbacks
def _fw_calc():
    normal = calc.calculate_normal(get_value("efficiency"),
                                   get_value("consumption"),
                                   get_value("time"),
                                   get_value("volt"))
    time = calc.calculate_time(get_value("efficiency"),
                               get_value("consumption"),
                               get_value("capacity"),
                               get_value("volt"),
                               get_value("remainder"))
    set_value("result", f"{_fw_result[1]}\n"
              + f"{_fw_result[2]} {normal[0]}W\n"
              + f"{_fw_result[3]} {time[3]}A\n"
              + f"{_fw_result[4]} {normal[2]}Ah\n"
              + f"{_fw_result[5]} {normal[1]}Ah\n"
              + f"{_fw_result[6]} {time[0]}H {time[1]}M\n"
              + f"{_fw_result[7] if normal[1] - time[2] < 0 else _fw_result[8]}")


def _sw_calc():
    normal = calc.calculate_reverse(get_value("r_time"),
                                    get_value("r_capacity"),
                                    get_value("r_volt"),
                                    get_value("r_remainder"))
    set_value("r_result", f"{str(_sw_result[1])}\n" + f"{str(_sw_result[2])} {str(normal[0])}W\n")
# End

#bind_font(font)

with window(label=_fw_title, width=450, height=480, pos=[0, 0]):
    add_text(_fw_p)
    add_input_float(label=_fw_efficiency, source="efficiency", max_value=100, step=0.5)
    add_input_float(label=_fw_consumption, source="consumption", step=50)
    add_input_float(label=_fw_time, source="time", step=0.25)
    add_input_float(label=_fw_capacity, source="capacity", step=1)
    add_input_float(label=_fw_volt, source="volt", step=1)
    add_input_float(label=_fw_remainder, source="remainder", step=5, max_value=100)
    add_text(source="result")
    add_button(label=_fw_button, callback=_fw_calc)

with window(label=_sw_title, width=450, height=480, pos=[450, 0]):
    add_text(_sw_p)
    add_input_float(label=_sw_time, source="r_time", step=0.25)
    add_input_float(label=_sw_capacity, source="r_capacity", step=1)
    add_input_float(label=_sw_volt, source="r_volt", step=1)
    add_input_float(label=_sw_remainder, source="r_remainder", step=5, max_value=100)

    add_text(source="r_result")
    add_button(label=_sw_button, callback=_sw_calc)

setup_dearpygui()
show_viewport()
start_dearpygui()
destroy_context()
