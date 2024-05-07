"""
sparrowDB 服务器端
"""
import json
from sparrowApi import SparrowApi
from sparrowApi import ContentType
from sparrowDB.sparrow import SparrowDB
from config import *

app = SparrowApi(__name__)
sparrow = SparrowDB()

password = input("Enter your password: ")
username = input("Enter your username: ")


class SparrowDBService(object):
    @staticmethod
    @app.post("/", content_type=ContentType.JSON)
    def main(data, headers):
        if headers.get("SparrowApi"):
            if headers.get("Password") == password and headers.get("Username") == username:
                command = data.get("command").replace("+", " ")
                command_list = command.split(" ")
                if command_list[0] == "set":
                    if len(command_list) == 3:
                        result = sparrow.set_key_value(command_list[1], command_list[2])
                        return json.dumps({"status": "ok", "data": result})
                    elif len(command_list) == 4:
                        try:
                            valid_time = float(command_list[3])
                            result = sparrow.set_key_value(command_list[1], command_list[2], valid_time)
                            return json.dumps({"status": "ok", "data": result})
                        except Exception as e:
                            print(e)
                            return json.dumps(
                                {"status": "bad", "data": f"{command} -> {command_list[3]} is Invalid time"})
                    else:
                        return json.dumps({"status": "bad", "data": f"{command} is Invalid command"})
                elif command_list[0] == "get":
                    if len(command_list) == 2:
                        result = sparrow.get_key_value(command_list[1])
                        return json.dumps({"status": "ok", "data": result})
                    else:
                        return json.dumps({"status": "bad", "data": f"{command} is Invalid command"})
                elif command_list[0] == "reset":
                    if len(command_list) == 3:
                        result = sparrow.reset_key_value(command_list[1], command_list[2])
                        return json.dumps({"status": "ok", "data": result})
                    elif len(command_list) == 4:
                        try:
                            valid_time = float(command_list[3])
                            result = sparrow.reset_key_value(command_list[1], command_list[2], valid_time)
                            return json.dumps({"status": "ok", "data": result})
                        except:
                            return json.dumps(
                                {"status": "bad", "data": f"{command} -> {command_list[3]} is Invalid time"})
                    else:
                        return json.dumps({"status": "bad", "data": f"{command} is Invalid command"})
                elif command_list[0] == "delete":
                    if len(command_list) == 2:
                        result = sparrow.delete_key_value(command_list[1])
                        return json.dumps({"status": "ok", "data": result})
                    else:
                        return json.dumps({"status": "bad", "data": f"{command} is Invalid command"})
                elif command_list[0] == "set_body":
                    body = [i for i in command_list[2].replace("%2C", ",").split(",")]
                    insert_dict = {}
                    for insert_body in body:
                        insert_dict[insert_body.replace("%3D", "=").split("=")[0]] = \
                            insert_body.replace("%3D", "=").split("=")[1]
                    if len(command_list) == 3:
                        result = sparrow.set_body(command_list[1], insert_dict)
                        return json.dumps({"status": "ok", "data": result})
                    elif len(command_list) == 4:
                        try:
                            valid_time = float(command_list[3])
                            result = sparrow.set_body(command_list[1], insert_dict, valid_time)
                            return json.dumps({"status": "ok", "data": result})
                        except:
                            return json.dumps(
                                {"status": "bad", "data": f"{command} -> {command_list[3]} is Invalid time"})
                    else:
                        return json.dumps({"status": "bad", "data": f"{command} is Invalid command"})
                elif command_list[0] == "reset_body_all":
                    body = [i for i in command_list[2].replace("%2C", ",").split(",")]
                    insert_dict = {}
                    for insert_body in body:
                        insert_dict[insert_body.replace("%3D", "=").split("=")[0]] = \
                            insert_body.replace("%3D", "=").split("=")[1]
                    if len(command_list) == 3:
                        result = sparrow.reset_body_all(command_list[1], insert_dict)
                        return json.dumps({"status": "ok", "data": result})
                    elif len(command_list) == 4:
                        try:
                            valid_time = float(command_list[3])
                            result = sparrow.reset_body_all(command_list[1], insert_dict, valid_time)
                            return json.dumps({"status": "ok", "data": result})
                        except:
                            return json.dumps(
                                {"status": "bad", "data": f"{command} -> {command_list[3]} is Invalid time"})
                    else:
                        return json.dumps({"status": "bad", "data": f"{command} is Invalid command"})
                elif command_list[0] == "reset_body":
                    print(command_list)
                    insert_dict = {"key": command_list[2].replace("%3D", "=").split("=")[0],
                                   "value": command_list[2].replace("%3D", "=").split("=")[1]}
                    if len(command_list) == 3:
                        result = sparrow.reset_body(command_list[1], insert_dict)
                        return json.dumps({"status": "ok", "data": result})
                    elif len(command_list) == 4:
                        try:
                            valid_time = float(command_list[3])
                            result = sparrow.reset_body(command_list[1], insert_dict, valid_time)
                            return json.dumps({"status": "ok", "data": result})
                        except:
                            return json.dumps(
                                {"status": "bad", "data": f"{command} -> {command_list[3]} is Invalid time"})
                    else:
                        return json.dumps({"status": "bad", "data": f"{command} is Invalid command"})
                elif command_list[0] == "get_body":
                    if len(command_list) == 2:
                        result = sparrow.get_body(command_list[1])
                        return json.dumps({"status": "ok", "data": result})
                    else:
                        return json.dumps({"status": "bad", "data": f"{command} is Invalid command"})
                elif command_list[0] == "delete_body":
                    if len(command_list) == 2:
                        result = sparrow.delete_body(command_list[1])
                        return json.dumps({"status": "ok", "data": result})
                    else:
                        return json.dumps({"status": "bad", "data": f"{command} is Invalid command"})
                elif command_list[0] == "set_body_time":
                    if len(command_list) == 3:
                        result = sparrow.set_body_valid_time(command_list[1], command_list[2])
                        return json.dumps({"status": "ok", "data": result})
                    else:
                        return json.dumps({"status": "bad", "data": f"{command} is Invalid command"})
                elif command_list[0] == "set_time":
                    if len(command_list) == 3:
                        result = sparrow.set_key_value_valid_time(command_list[1], command_list[2])
                        return json.dumps({"status": "ok", "data": result})
                    else:
                        return json.dumps({"status": "bad", "data": f"{command} is Invalid command"})
                elif command_list[0] == "get_all_body":
                    if len(command_list) == 1:
                        result = sparrow.get_all_body()
                        return json.dumps({"status": "ok", "data": result})
                    else:
                        return json.dumps({"status": "bad", "data": f"{command} is Invalid command"})
                elif command_list[0] == "get_all":
                    if len(command_list) == 1:
                        result = sparrow.get_all_by_key()
                        return json.dumps({"status": "ok", "data": result})
                    else:
                        return json.dumps({"status": "bad", "data": f"{command} is Invalid command"})
                elif command_list[0] == "test":
                    return json.dumps({"status": "ok", "data": "connect is successful"})
                else:
                    return json.dumps({"status": "bad", "data": f"{command} is Invalid command"})
            else:
                return json.dumps({"status": "bad", "data": "Password or Username is required"})
        else:
            return json.dumps({"status": "bad", "data": "headers is not required"})

    @staticmethod
    def run():
        app.run(host=HOST, port=PORT, try_model=TRY_MODEL, show_error=SHOW_ERROR, log_file=LOG_FILE,
                default_listen=DEFAULT_LISTEN, is_save_log=IS_SAVE_LOG)


if __name__ == "__main__":
    run = SparrowDBService()
    run.run()


