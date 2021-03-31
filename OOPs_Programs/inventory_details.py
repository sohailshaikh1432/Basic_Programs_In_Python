import json
from Log_Configuration import log_config_file

logger = log_config_file.get_logger()


class JsonClass:

    @staticmethod
    def calculate(rice_weight_in_kg, rice_price_per_kg):
        """
        Calculate total cost of product
        :param rice_weight_in_kg: weight
        :param rice_price_per_kg: price
        # :return: total
        """
        total = rice_weight_in_kg / rice_price_per_kg
        print(f"Total cost : ", total)
        return total

    @staticmethod
    def get_json():
        """
        Get json object from json file
        :return:
        """
        json_file = open('inventory_details.json')
        json_object = json.load(json_file)
        # print(json_object)

        rice_input = input("\nFor Basmati type - 1, "
                           "\nFor Indrayani type - 2  "
                           "\nPlease select type of rice :")
        if rice_input == 1:
            rice_weight_in_kg = json_object['rice'][0]['weight_in_kg']
            rice_price_per_kg = json_object['rice'][0]['price_per_kg']
            json_class_object.calculate(rice_weight_in_kg, rice_price_per_kg)
        else:
            rice_weight_in_kg = json_object['rice'][0]['weight_in_kg']
            rice_price_per_kg = json_object['rice'][0]['price_per_kg']
            json_class_object.calculate(rice_weight_in_kg, rice_price_per_kg)

        wheat_input = input("\nFor 'Khapli' type - 1, "
                            "\nFor 'Sharbati' type - 2  "
                            "\nPlease select type of rice :")
        if rice_input == 1:
            wheat_weight_in_kg = json_object['wheat'][0]['weight_in_kg']
            wheat_price_per_kg = json_object['wheat'][0]['price_per_kg']
            json_class_object.calculate(wheat_weight_in_kg, wheat_price_per_kg)
        else:
            wheat_weight_in_kg = json_object['wheat'][0]['weight_in_kg']
            wheat_price_per_kg = json_object['wheat'][0]['price_per_kg']
            json_class_object.calculate(wheat_weight_in_kg, wheat_price_per_kg)

        pulses_input = input("\nFor 'Yellow_pigeon_peas' type - 1, "
                             "\nFor 'Split_bengal_gram' type - 2  "
                             "\nPlease select type of rice :")
        if pulses_input == 1:
            pulses_weight_in_kg = json_object['pulses'][0]['weight_in_kg']
            pulses_price_per_kg = json_object['pulses'][0]['price_per_kg']
            json_class_object.calculate(pulses_weight_in_kg, pulses_price_per_kg)
        else:
            pulses_weight_in_kg = json_object['pulses'][0]['weight_in_kg']
            pulses_price_per_kg = json_object['pulses'][0]['price_per_kg']
            json_class_object.calculate(pulses_weight_in_kg, pulses_price_per_kg)


# Creating object of class & calling method
try:
    json_class_object = JsonClass()
    json_class_object.get_json()
except Exception as e:
    logger.exception(e)
