class EmptyMixin:
    def add_xpath_if_empty(self, field_name, xpath, *processors, **kw):
        if not self.get_output_value(field_name):
            self.add_xpath(field_name, xpath, *processors, **kw)

    def add_value_if_empty(self, field_name, value, *processors, **kw):
        if not self.get_output_value(field_name):
            self.add_value(field_name, value, *processors, **kw)
