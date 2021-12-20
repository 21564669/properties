import json
from Properties.util import common_functions as cf


class Properties:
    def __init__(self, file_path):
        self.file_path = file_path
        self.properties = dict()
        # all_cases_list, enable_cases_list, disabled_cases_list = self.read_properties(c.sdc_cases_properties)

    def get_properties(self):
        file_content = cf.get_file_content(self.file_path)
        for line in file_content:
            line = line.strip()
            if not line.startswith('#') and "=" in line:
                property_name = line.split("=")[0].strip()
                property_value = line.split('=')[1].strip()
                self.properties[property_name] = property_value
        return self.properties

    def get_property(self, property_name):
        if not self.properties:
            self.properties = self.get_properties()
        if property_name in self.properties.keys():
            return self.properties[property_name]
        else:
            raise Exception(f"No such property name.({property_name})")

    def __str__(self):
        if not self.properties:
            self.properties = self.get_properties()
        return json.dumps(self.properties)

    def __copy__(self):
        return self.properties.copy()

    