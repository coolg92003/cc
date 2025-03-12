from flask import Flask, make_response
from flask import request, json, jsonify, send_file
import time

app=Flask(__name__)

TRACE_HEADERS_TO_PROPAGATE = [
    'X-Ot-Span-Context',
    'X-Request-Id',

    # Zipkin headers
    'X-B3-TraceId',
    'X-B3-SpanId',
    'X-B3-ParentSpanId',
    'X-B3-Sampled',
    'X-B3-Flags',

    # Jaeger header (for native client)
    "uber-trace-id",

    # SkyWalking headers.
    "sw8"
]

full_method_dlist = ['GET', 'POST']
#@app.route('/nbsf-management/v1/pcfBindings', methods=full_method_dlist, defaults={'name': 'Programmer'}) 
@app.route('/trace', methods=full_method_dlist, defaults={'name': 'Programmer'}) 
@app.route('/ses', methods=full_method_dlist, defaults={'name': 'Programmer'}) 
def greet(name): 
#print the request
    print("CFX, get message")
    print("method: " + request.method)
    print("scheme: " + request.scheme)
    print("full_path: " + str(request.full_path))
    print("headers: \n" + str(request.headers))
    print("\nreferrer: " + str(request.referrer))
    print("user_agent: " + str(request.user_agent))
    print("args: " + str(request.args))
    print("blueprint: " + str(request.blueprint))
    print("cookies: " + str(request.cookies))
    print("data: " + str(request.data))
    print("endpoint: " + str(request.endpoint))
    print("files: " + str(request.files))
    print("values: " + str(request.values))
    if request.is_json:
        #print("get_json: " + request.get_json(force=False, silent=False, cache=True))
        print("get_json: " + str(request.json))
#Set up response
#TRACE_HEADERS_TO_PROPAGATE

    response = make_response(jsonify(server='Return test response body'))
    response.mimetype = "application/json"
    #time.sleep(20)
    return response

full_method_list = ['GET', 'POST', 'PATCH', 'PUT', 'DELETE']
#full_method_list = ['POST', 'PATCH', 'PUT', 'DELETE']
@app.route('/npcf-policyauthorization/v1/<path:path>', methods=full_method_list)
def handle_message(path):
#print the request
    print("CFX, get message")
    print("method: " + request.method)
    print("scheme: " + request.scheme)
    print("full_path: " + str(request.full_path))
    print("headers: \n" + str(request.headers))
    print("\nreferrer: " + str(request.referrer))
    print("user_agent: " + str(request.user_agent))
    print("args: " + str(request.args))
    print("blueprint: " + str(request.blueprint))
    print("cookies: " + str(request.cookies))
    print("data: " + str(request.data))
    print("endpoint: " + str(request.endpoint))
    print("files: " + str(request.files))
    print("values: " + str(request.values))
    if request.is_json:
        print("get_json: " + str(request.json))
#Set up response
    response = make_response(jsonify(server='Flask cfx'))
    response.mimetype = "application/json"
    time.sleep(1)
    return response

if __name__ == "__main__":
    import socket
    socket.setdefaulttimeout(150) 
    from werkzeug.serving import WSGIRequestHandler
    WSGIRequestHandler.protocol_version = "HTTP/1.1"
    app.run(host='0.0.0.0', port=9443, ssl_context=('/home/cfx/test/tlss2/Server.cert', '/home/cfx/test/tlss2/Server.key'), debug=False, threaded=False)
