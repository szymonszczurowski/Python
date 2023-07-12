import os
import datetime

print(os.getcwd())

data_input_catalog = "C:\\Users\szczu\\PycharmProjects\\pythonLearn\\InputOutputOperation\\data_input"
data_output_catalog = "C:\\Users\szczu\\PycharmProjects\\pythonLearn\\InputOutputOperation\\data_output"

today = datetime.date.today()
today = str(today)
print(today)
# today = today.strftime("%Y.%m.%d")

today_output_catalog = os.path.join(data_output_catalog, today)
print(today_output_catalog)

is_input_catalog_ok = os.path.isdir(data_input_catalog) and os.path.exists(data_input_catalog)
is_output_catalog_ok = os.path.isdir(data_output_catalog) and os.path.exists(data_output_catalog)
is_today_output_catalog_ok = not (os.path.isdir(today_output_catalog) or os.path.isfile(today_output_catalog))


if is_input_catalog_ok and is_output_catalog_ok and is_today_output_catalog_ok:
    print('Conditions met! We can continue!')
else:
    print(
        "Input catalog must exist!: {}\nOutput catalog must exist! {}\nToday's output %s cannot exist (neither as file nor as directory)!: {}".format(is_input_catalog_ok,
                                                                                                   is_output_catalog_ok,
                                                                                                   is_today_output_catalog_ok))

# if is_input_catalog_ok and is_output_catalog_ok and is_today_output_catalog_ok:
#     print('Conditions met! We can continue!')
# else:
#     print('Prerequisites not met! Check the paths!')
#
#     # display detailed error conditions
#     if not is_input_catalog_ok:
#         print("Input catalog %s must exist!" % data_input_catalog)
#     if not is_output_catalog_ok:
#         print("Output catalog %s must exist!" % data_output_catalog)
#     if not is_today_output_catalog_ok:
#         print("Today's output %s cannot exist (neither as file nor as directory)!" % today_output_catalog)
