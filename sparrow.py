import time
from datetime import datetime, timedelta


class SparrowDB(object):
    def __init__(self):
        self._data_key_value_ = {}
        self._data_body_ = {}

    def _is_key_value_overdue_(self, key):
        try:
            valid_time = self._data_key_value_.get(key).get("valid_time")
            if valid_time is not None:
                valid_time = float(valid_time)
                set_time = float(self._data_key_value_.get(key).get("set_time"))
                set_timestamp = datetime.fromtimestamp(set_time)
                valid_time = set_timestamp + timedelta(seconds=float(valid_time))
                valid_timestamp = time.mktime(valid_time.timetuple())
                new_time = time.time()
                if new_time > valid_timestamp:
                    del self._data_key_value_[key]
        except:
            pass

    def _is_body_overdue_(self, key):
        try:
            valid_time = self._data_body_.get(key).get("valid_time")
            if valid_time is not None:
                valid_time = float(valid_time)
                set_time = float(self._data_body_.get(key).get("set_time"))
                set_timestamp = datetime.fromtimestamp(set_time)
                valid_time = set_timestamp + timedelta(seconds=float(valid_time))
                valid_timestamp = time.mktime(valid_time.timetuple())
                new_time = time.time()
                if new_time > valid_timestamp:
                    del self._data_body_[key]
        except:
            pass

    def set_key_value(self, key, value, valid_time=None):
        self._is_key_value_overdue_(key)
        if key in self._data_key_value_.keys():
            return f"{key} already in SparrowDB"
        else:
            self._data_key_value_[key] = {"value": value, "valid_time": valid_time, "set_time": time.time()}
            return self._data_key_value_[key]

    def reset_key_value(self, key, value, valid_time=None):
        self._is_key_value_overdue_(key)
        if key in self._data_key_value_.keys():
            self._data_key_value_[key] = {"value": value, "valid_time": valid_time, "set_time": time.time()}
            return self._data_key_value_[key]
        else:
            return f"{key} not found in SparrowDB"

    def get_key_value(self, key):
        self._is_key_value_overdue_(key)
        if key in self._data_key_value_.keys():
            return {key: self._data_key_value_[key]['value']}
        else:
            return f"{key} not found in SparrowDB"

    def delete_key_value(self, key):
        self._is_key_value_overdue_(key)
        if key in self._data_key_value_.keys():
            data = {"key": key, "value": self._data_key_value_[key]['value']}
            del self._data_key_value_[key]
            return data
        else:
            return f"{key} not found  in SparrowDB"

    def set_body(self, key, body, valid_time=None):
        self._is_body_overdue_(key)
        if key in self._data_body_.keys():

            return f"{key} already in SparrowDB"
        else:
            self._data_body_[key] = {"value": body, "valid_time": valid_time, "set_time": time.time()}
            return self._data_body_[key]

    def reset_body(self, key, body, valid_time=None):
        self._is_body_overdue_(key)
        if key in self._data_body_.keys():
            body_key = body.get("key")
            body_value = body.get("value")
            self._data_body_[key]["value"][body_key] = body_value
            self._data_body_[key]["valid_time"] = valid_time
            self._data_body_[key]["set_time"] = time.time()
            return self._data_body_[key]
        else:
            return f"{key} not found in SparrowDB"

    def get_body(self, key):
        self._is_body_overdue_(key)
        if key in self._data_body_.keys():
            return {key: self._data_body_[key]['value']}
        else:
            return f"{key} not found in SparrowDB"

    def delete_body(self, key):
        self._is_body_overdue_(key)
        if key in self._data_body_.keys():
            data = {"key": key, "value": self._data_body_[key]['value']}
            del self._data_body_[key]
            return data
        else:
            return f"{key} not found  in SparrowDB"

    def set_key_value_valid_time(self, key, valid_time):
        print(key)
        self._is_key_value_overdue_(key)
        if key in self._data_key_value_.keys():
            self._data_key_value_[key]["valid_time"] = valid_time
            self._data_key_value_[key]["set_time"] = time.time()
            return self._data_key_value_[key]
        else:
            return f"{key} not found in SparrowDB"

    def set_body_valid_time(self, key, valid_time):
        self._is_body_overdue_(key)
        if key in self._data_body_.keys():
            self._data_body_[key]["valid_time"] = valid_time
            self._data_body_[key]["set_time"] = time.time()
            return self._data_body_[key]
        else:
            return f"{key} not found in SparrowDB"

    def get_all_body(self):
        for key in self._data_body_.keys():
            self._is_body_overdue_(key)
        return self._data_body_

    def get_all_by_key(self):
        for key in self._data_key_value_.keys():
            self._is_key_value_overdue_(key)
        return self._data_key_value_
