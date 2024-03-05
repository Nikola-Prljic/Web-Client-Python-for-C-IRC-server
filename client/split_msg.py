class splitMsg:

    def __init__(self):
        return
    
    def handelJoin(self, args:str):
        if len(args[0]) < 2:
            return args
        if "JOIN" not in args[0]:
            print("not found")
            return args
        args = args[0].split(" ")
        return "You joined " + args[2] + "\n"

    def handelData(self, data):
        msg = str(data.decode())
        msg = list(msg.split(":"))

        if msg[0] == "":
            msg.remove(msg[0])
        print(msg)
        msg = self.handelJoin(msg)
        if isinstance(msg, str):
            return msg
        if len(msg) == 1:
            return msg[0]
        return msg[1]