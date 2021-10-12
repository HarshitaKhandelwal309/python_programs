from xmlrpc.server import SimpleXMLRPCServer
def mod(num1,num2):
    return num1 % num2
def add(num1,num2):
    return num1 + num2
def sub(num1,num2):
    return num1 - num2
def mul(num1,num2):
    return num1 * num2
def div(num1,num2):
    return num1 / num2
server = SimpleXMLRPCServer(("localhost",9999))
server.register_function(mod,"mod")
server.register_function(add,"add")
server.register_function(sub,"sub")
server.register_function(mul,"mul")
server.register_function(div,"div")
server.serve_forever()














# from xmlrpc.server import SimpleXMLRPCServer

# def is_even(n):
#     return n % 2 == 0

# server = SimpleXMLRPCServer(("localhost", 8000))
# print("Listening on port 8000...")
# server.register_function(is_even, "is_even")
# server.serve_forever()