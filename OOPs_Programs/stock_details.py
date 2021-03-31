import json


class StockDetails:
    def __init__(self):
        self.stock_name = []
        self.number_of_share = []
        self.share_price = []
        self.total = []

    def json_handler(self):
        """
        This method is used to handle json file.
        :return: None
        """
        with open('stock_details.json', 'r') as json_file:
            data = json.load(json_file)
        # Getting the details from json and calculate total.
        for details in data['stock_details']:
            self.stock_name.append(details['stock_name'])
            self.number_of_share.append(details['number_of_share'])
            self.share_price.append(details['share_price'])
            self.total.append(str(int(details['number_of_share']) * int(details['share_price'])))
        # Assigned the total into the json file.
        index = 0
        for details in data['stock_details']:
            details['stock_name'] = self.stock_name[index]
            details['number_of_share'] = self.number_of_share[index]
            details['share_price'] = self.share_price[index]
            details['total'] = self.total[index]
            index += 1
        with open("stock_details.json", "w") as json_file:
            json.dump(data, json_file, indent=2)