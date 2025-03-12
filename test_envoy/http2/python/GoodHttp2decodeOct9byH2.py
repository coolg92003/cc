import h2.connection
import h2.config
import h2.events
import hexdump

# Initialize HTTP/2 connection
class cfx_log:
    def __init__(self, *vargs):
        pass
    def debug(self, *vargs):
        #print("\n~~~~~cfx_log:debug:\n")
        #print(vargs)
        #print("\n")
        pass
    def trace(self, *vargs):
        #print("\n~~~~~cfx_log:trace:\n")
        #print(vargs)
        #print("\n")
        pass
raw_cfx_bytes11 = b'PRI * HTTP/2.0\r\n\r\nSM\r\n\r\n\000\000\036\004\000\000\000\000\000\000\001\000\000\000\000\000\002\000\000\000\000\000\003\000\000\020\000\000\004\020\000\000\000\000\010\000\000\000\000\000\000\004\010\000\000\000\000\000\017\377\000\001\000\000\233\001\004\000\000\000\001\004\235b\252\311*\325\236\203\023\320\355L\347\260\336\306\223\036\246;\205\201\327Z\310*\020c\324\217\206A\212\010\235\\\013\201p\334y\347\237\203@\203A\351/\203Rs\370@\203\3618\323\204P\275\313g\\\203\010\037\017@\215\362\264\247\263\300\354\220\262-]\207I\377\203\235)\257@\211\362\265\205\355iP\225\215\'\232\014`~W\n\025\202\'\036Y\246_\"\303$\203X\2156\t_\214L\310\'?@\226\362\261j\356\177K\027\315e\"K\"\326vY&\244\247\265+R\217\204\013`\000?\000\004C\000\001\000\000\000\001 { \t\"ascReqData\":  \t{ \t\t\"afChargId\": \"PCSF:1-cfed-0-1-0000000063185a10-0000000000014f35\", \t\t\"gpsi\": \"msisdn00000000001\", \t\t\"medComponents\": \t\t{ \t\t\t\"1\": \t\t\t{ \t\t\t\t\"codecs\": [\"downlink\\r\\noffer\\r\\nm=audio 26512 RTP/AVP 8\\r\\n\", \"uplink\\r\\nanswer\\r\\nm=audio 4001 RTP/AVP 8\\r\\n\"], \t\t\t\t\"fStatus\": \"ENABLED\", \t\t\t\t\"marBwDl\": \"128000 bps\", \t\t\t\t\"marBwUl\": \"128000 bps\", \t\t\t\t\"medCompN\": 1, \t\t\t\t\"medSubComps\": \t\t\t\t{ \t\t\t\t\t\"1\": \t\t\t\t\t{ \t\t\t\t\t\t\"fDescs\": [\"permit in 17 from 135.2.207.203 4001 to 135.248.246.57 26512\", \"permit out 17 from 135.248.246.57 26512 to 135.2.207.203 4001\"], \t\t\t\t\t\t\"fNum\": 1 \t\t\t\t\t}, \t\t\t\t\t\"2\": \t\t\t\t\t{ \t\t\t\t\t\t\"fDescs\": [\"permit in 17 from 135.2.207.203 4002 to 135.248.246.57 26513\", \"permit out 17 from 135.248.246.57 26513 to 135.2.207.203 4002\"], \t\t\t\t\t\t\"fNum\": 2, \t\t\t\t\t\t\"flowUsage\": \t\t\t\t\t\t\"RTCP\"}}, \t\t\t\t\t\t\"medType\": \"AUDIO\" \t\t\t\t\t} \t\t\t}, \t\t\t\t\"notifUri\": \"http://127.0.0.1:8089/npcf-policyauthorization/v1/app-sessions/cngss-6677455584-pbwtt/pcsf-test.61965b530b1a0001;117;1;5.377749659.7.68378\", \t\t\t\t\"servInfStatus\": \"FINAL\", \t\t\t\t\"suppFeat\": \"10\", \t\t\t\t\"ueIpv4\": \"192.168.90.167\" \t\t} }'
raw_cfx_bytes12 = b'\000\000\014\004\000\000\000\000\000\000\004?\377\377\377\000\003\000\000\001\000\000\000\000\004\001\000\000\000\000\000\000\004\010\000\000\000\000\000?\377\000\000\000\000\036\001\004\000\000\000\001 \010\202\020\003\017\022\226\344Y>\224\010\224\302X\324\020\004\332\200\025\306\337\270&\224\305\243\177\000\000\000\000\001\000\000\000\001'
raw_cfx_bytes21 = b'\000\000D\001\004\000\000\000\003\004\235b\252\311*\325\236\203\023\320\355L\347\260\336\306\223\036\246;\205\201\327Z\310*\020c\324\217\206\304\203\303\302\301\300\177\000\232#\315\266\'\034\022\3164\323K4\323BZ9D\025\231m\307\231\014ex\214\265\277\000\004C\000\001\000\000\000\003 { \t\"ascReqData\":  \t{ \t\t\"afChargId\": \"PCSF:1-cfed-0-1-0000000063185a10-0000000000014f35\", \t\t\"gpsi\": \"msisdn00000000002\", \t\t\"medComponents\": \t\t{ \t\t\t\"1\": \t\t\t{ \t\t\t\t\"codecs\": [\"downlink\\r\\noffer\\r\\nm=audio 26512 RTP/AVP 8\\r\\n\", \"uplink\\r\\nanswer\\r\\nm=audio 4001 RTP/AVP 8\\r\\n\"], \t\t\t\t\"fStatus\": \"ENABLED\", \t\t\t\t\"marBwDl\": \"128000 bps\", \t\t\t\t\"marBwUl\": \"128000 bps\", \t\t\t\t\"medCompN\": 1, \t\t\t\t\"medSubComps\": \t\t\t\t{ \t\t\t\t\t\"1\": \t\t\t\t\t{ \t\t\t\t\t\t\"fDescs\": [\"permit in 17 from 135.2.207.203 4001 to 135.248.246.57 26512\", \"permit out 17 from 135.248.246.57 26512 to 135.2.207.203 4001\"], \t\t\t\t\t\t\"fNum\": 1 \t\t\t\t\t}, \t\t\t\t\t\"2\": \t\t\t\t\t{ \t\t\t\t\t\t\"fDescs\": [\"permit in 17 from 135.2.207.203 4002 to 135.248.246.57 26513\", \"permit out 17 from 135.248.246.57 26513 to 135.2.207.203 4002\"], \t\t\t\t\t\t\"fNum\": 2, \t\t\t\t\t\t\"flowUsage\": \t\t\t\t\t\t\"RTCP\"}}, \t\t\t\t\t\t\"medType\": \"AUDIO\" \t\t\t\t\t} \t\t\t}, \t\t\t\t\"notifUri\": \"http://127.0.0.1:8089/npcf-policyauthorization/v1/app-sessions/cngss-6677455584-pbwtt/pcsf-test.61965b530b1a0001;117;1;5.377749659.7.68378\", \t\t\t\t\"servInfStatus\": \"FINAL\", \t\t\t\t\"suppFeat\": \"10\", \t\t\t\t\"ueIpv4\": \"192.168.90.167\" \t\t} }'
raw_cfx_bytes22 = b'\000\000\035\001\004\000\000\000\003\010\202\020\003\017\022\226\344Y>\224\010\224\302X\324\020\004\332\200\025\306\337\270&\324\305\243\177\000\000\000\000\001\000\000\000\003'
raw_cfx_bytes31 = b'\000\000C\001\004\000\000\000\005\004\235b\252\311*\325\236\203\023\320\355L\347\260\336\306\223\036\246;\205\201\327Z\310*\020c\324\217\206\305\203\304\303\302\301~\232q\301\262!\215\265\236y\307\326h\021\276\263\355\312U\212\374\200\023R\270\321\036\037\300\000\004C\000\001\000\000\000\005 { \t\"ascReqData\":  \t{ \t\t\"afChargId\": \"PCSF:1-cfed-0-1-0000000063185a10-0000000000014f35\", \t\t\"gpsi\": \"msisdn00000000003\", \t\t\"medComponents\": \t\t{ \t\t\t\"1\": \t\t\t{ \t\t\t\t\"codecs\": [\"downlink\\r\\noffer\\r\\nm=audio 26512 RTP/AVP 8\\r\\n\", \"uplink\\r\\nanswer\\r\\nm=audio 4001 RTP/AVP 8\\r\\n\"], \t\t\t\t\"fStatus\": \"ENABLED\", \t\t\t\t\"marBwDl\": \"128000 bps\", \t\t\t\t\"marBwUl\": \"128000 bps\", \t\t\t\t\"medCompN\": 1, \t\t\t\t\"medSubComps\": \t\t\t\t{ \t\t\t\t\t\"1\": \t\t\t\t\t{ \t\t\t\t\t\t\"fDescs\": [\"permit in 17 from 135.2.207.203 4001 to 135.248.246.57 26512\", \"permit out 17 from 135.248.246.57 26512 to 135.2.207.203 4001\"], \t\t\t\t\t\t\"fNum\": 1 \t\t\t\t\t}, \t\t\t\t\t\"2\": \t\t\t\t\t{ \t\t\t\t\t\t\"fDescs\": [\"permit in 17 from 135.2.207.203 4002 to 135.248.246.57 26513\", \"permit out 17 from 135.248.246.57 26513 to 135.2.207.203 4002\"], \t\t\t\t\t\t\"fNum\": 2, \t\t\t\t\t\t\"flowUsage\": \t\t\t\t\t\t\"RTCP\"}}, \t\t\t\t\t\t\"medType\": \"AUDIO\" \t\t\t\t\t} \t\t\t}, \t\t\t\t\"notifUri\": \"http://127.0.0.1:8089/npcf-policyauthorization/v1/app-sessions/cngss-6677455584-pbwtt/pcsf-test.61965b530b1a0001;117;1;5.377749659.7.68378\", \t\t\t\t\"servInfStatus\": \"FINAL\", \t\t\t\t\"suppFeat\": \"10\", \t\t\t\t\"ueIpv4\": \"192.168.90.167\" \t\t} }'
raw_cfx_bytes32 = b'\000\000\035\001\004\000\000\000\005\010\202\020\003\017\022\226\344Y>\224\010\224\302X\324\020\004\332\200\025\306\337\270\'\024\305\243\177\000\000\000\000\001\000\000\000\005'
raw_cfx_bytes41 = b'\000\000D\001\004\000\000\000\007\004\235b\252\311*\325\236\203\023\320\355L\347\260\336\306\223\036\246;\205\201\327Z\310*\020c\324\217\206\306\203\305\304\303\302~\233}\371\\\225\340\264\260\037q\325\232nP\2540\276\372\322\266\353o\271#c\013n\377\301\000\004C\000\001\000\000\000\007 { \t\"ascReqData\":  \t{ \t\t\"afChargId\": \"PCSF:1-cfed-0-1-0000000063185a10-0000000000014f35\", \t\t\"gpsi\": \"msisdn00000000004\", \t\t\"medComponents\": \t\t{ \t\t\t\"1\": \t\t\t{ \t\t\t\t\"codecs\": [\"downlink\\r\\noffer\\r\\nm=audio 26512 RTP/AVP 8\\r\\n\", \"uplink\\r\\nanswer\\r\\nm=audio 4001 RTP/AVP 8\\r\\n\"], \t\t\t\t\"fStatus\": \"ENABLED\", \t\t\t\t\"marBwDl\": \"128000 bps\", \t\t\t\t\"marBwUl\": \"128000 bps\", \t\t\t\t\"medCompN\": 1, \t\t\t\t\"medSubComps\": \t\t\t\t{ \t\t\t\t\t\"1\": \t\t\t\t\t{ \t\t\t\t\t\t\"fDescs\": [\"permit in 17 from 135.2.207.203 4001 to 135.248.246.57 26512\", \"permit out 17 from 135.248.246.57 26512 to 135.2.207.203 4001\"], \t\t\t\t\t\t\"fNum\": 1 \t\t\t\t\t}, \t\t\t\t\t\"2\": \t\t\t\t\t{ \t\t\t\t\t\t\"fDescs\": [\"permit in 17 from 135.2.207.203 4002 to 135.248.246.57 26513\", \"permit out 17 from 135.248.246.57 26513 to 135.2.207.203 4002\"], \t\t\t\t\t\t\"fNum\": 2, \t\t\t\t\t\t\"flowUsage\": \t\t\t\t\t\t\"RTCP\"}}, \t\t\t\t\t\t\"medType\": \"AUDIO\" \t\t\t\t\t} \t\t\t}, \t\t\t\t\"notifUri\": \"http://127.0.0.1:8089/npcf-policyauthorization/v1/app-sessions/cngss-6677455584-pbwtt/pcsf-test.61965b530b1a0001;117;1;5.377749659.7.68378\", \t\t\t\t\"servInfStatus\": \"FINAL\", \t\t\t\t\"suppFeat\": \"10\", \t\t\t\t\"ueIpv4\": \"192.168.90.167\" \t\t} }'
raw_cfx_bytes42 = b'\000\000\035\001\004\000\000\000\007\010\202\020\003\017\022\226\344Y>\224\010\224\302X\324\020\004\332\200\025\306\337\270\'T\305\243\177\000\000\000\000\001\000\000\000\007'
raw_cfx_bytes51 = b'\000\000D\001\004\000\000\000\t\004\235b\252\311*\325\236\203\023\320\355L\347\260\336\306\223\036\246;\205\201\327Z\310*\020c\324\217\206\307\203\306\305\304\303~\233\224-\312\354`e`\275++5,\204Y\367\235*\317\2269##\3568\363r\177\302\000\004C\000\001\000\000\000\t { \t\"ascReqData\":  \t{ \t\t\"afChargId\": \"PCSF:1-cfed-0-1-0000000063185a10-0000000000014f35\", \t\t\"gpsi\": \"msisdn00000000005\", \t\t\"medComponents\": \t\t{ \t\t\t\"1\": \t\t\t{ \t\t\t\t\"codecs\": [\"downlink\\r\\noffer\\r\\nm=audio 26512 RTP/AVP 8\\r\\n\", \"uplink\\r\\nanswer\\r\\nm=audio 4001 RTP/AVP 8\\r\\n\"], \t\t\t\t\"fStatus\": \"ENABLED\", \t\t\t\t\"marBwDl\": \"128000 bps\", \t\t\t\t\"marBwUl\": \"128000 bps\", \t\t\t\t\"medCompN\": 1, \t\t\t\t\"medSubComps\": \t\t\t\t{ \t\t\t\t\t\"1\": \t\t\t\t\t{ \t\t\t\t\t\t\"fDescs\": [\"permit in 17 from 135.2.207.203 4001 to 135.248.246.57 26512\", \"permit out 17 from 135.248.246.57 26512 to 135.2.207.203 4001\"], \t\t\t\t\t\t\"fNum\": 1 \t\t\t\t\t}, \t\t\t\t\t\"2\": \t\t\t\t\t{ \t\t\t\t\t\t\"fDescs\": [\"permit in 17 from 135.2.207.203 4002 to 135.248.246.57 26513\", \"permit out 17 from 135.248.246.57 26513 to 135.2.207.203 4002\"], \t\t\t\t\t\t\"fNum\": 2, \t\t\t\t\t\t\"flowUsage\": \t\t\t\t\t\t\"RTCP\"}}, \t\t\t\t\t\t\"medType\": \"AUDIO\" \t\t\t\t\t} \t\t\t}, \t\t\t\t\"notifUri\": \"http://127.0.0.1:8089/npcf-policyauthorization/v1/app-sessions/cngss-6677455584-pbwtt/pcsf-test.61965b530b1a0001;117;1;5.377749659.7.68378\", \t\t\t\t\"servInfStatus\": \"FINAL\", \t\t\t\t\"suppFeat\": \"10\", \t\t\t\t\"ueIpv4\": \"192.168.90.167\" \t\t} }'
raw_cfx_bytes52 = b'\000\000\035\001\004\000\000\000\t\010\202\020\003\017\022\226\344Y>\224\010\224\302X\324\020\004\332\200\025\306\337\270\'\224\305\243\177\000\000\000\000\001\000\000\000\t'

def handle_event(events):
    print("\n\thandle_event: events.size()=", len(events))
    # Iterate over processed events
    for event in events:
        #print("\n******* raw event:", event)
        if isinstance(event, h2.events.RequestReceived):
            print("\n\t\t>>>>>>>>>>>>>>>>>>>>>>>>>Request Received")
            print("\t\tstream_id:", event.stream_id)
            print("\t\tstream_ended:", event.stream_ended)
            #print("\t\tRaw Headers:", event.headers)
            for header in event.headers:
                print("\t\t\t", header)
                if header[0] == b':path':
                    print("\t\t\t\t", header[1])
                #print("\n")

            # Decode HPACK headers
            #decoder = hpack.Decoder()
            #decoded_headers = decoder.decode(event.headers)
            #print("Decoded Headers:", decoded_headers)
        if isinstance(event, h2.events.ResponseReceived):
            print("\n\t<<<<<<<<<<<Response Received")
            print("\t\tstream_id:", event.stream_id)
            print("\t\tstream_ended:", event.stream_ended)
            print("\t\tRaw Headers:", event.headers)

        elif isinstance(event, h2.events.DataReceived):
            print("\n\tData Frame Received")
            print("\t\tstream_id:", event.stream_id)
            #print("\t\tstream_ended:", event.stream_ended)
            #print("\t\tPayload:", event.data.decode())  # Assuming UTF-8 text

        elif isinstance(event, h2.events.WindowUpdated):
            print("\n\tWindowUpdated")
            print(event)
        elif isinstance(event, h2.events.PingReceived):
            print("\n\tPingReceived")
            print(event)
        elif isinstance(event, h2.events.PingAckReceived):
            print("\n\PingAckReceived")
            print(event)
        elif isinstance(event, h2.events.StreamReset):
            print("\n\tStreamReset")
            print(event)
        elif isinstance(event, h2.events.SettingsAcknowledged):
            print("\n\SettingsAcknowledged")
            print(event)
        elif isinstance(event, h2.events.RemoteSettingsChanged):
            print("\n\tRemoteSettingsChanged")
            print(event)
        elif isinstance(event, h2.events.UnknownFrameReceived):
            print("\n\tUnknownFrameReceived")
            print(event)
        else:
            print("\n\t strange  ones UnknownFrame")
print("\n\nSSSSSSSSS*************************Process raw data")
def clientSide():
    client_config = h2.config.H2Configuration(client_side=True, header_encoding=None, validate_outbound_headers=False, normalize_outbound_headers=False, validate_inbound_headers=False, normalize_inbound_headers=False, logger=cfx_log)
    client_conn = h2.connection.H2Connection(config=client_config)
    client_conn.initiate_connection()  # Start HTTP/2 connection
    event_cnt = 0
    stream_id = -1 
    for raw_frame in [raw_cfx_bytes12, raw_cfx_bytes22, raw_cfx_bytes32, raw_cfx_bytes42, raw_cfx_bytes52]:
        event_cnt = event_cnt + 1
        print(f"\n****** Client EVENT.{event_cnt} Start to Process single single raw data\n")
        stream_id = stream_id + 2
        print(f"\n\tSend headers and data for stream {stream_id}")
        headers = [ (':method', 'GET'), (':scheme', 'https'), (':authority', 'localhost'), (':path', '/') ]
        data = b'cliff fu xuan Chen'
        client_conn.send_headers(stream_id, headers, end_stream=False)
        client_conn.send_data(stream_id, data, end_stream=True)
        try:
            events = client_conn.receive_data(raw_frame)  # Correctly retrieve events
        except Exception as e:
            print(f"\n***** EVENT.{event_cnt} ERROR< {e} >")
            continue
        
        handle_event(events)
        print(f"\n****** EVENT.{event_cnt}  Done to Process single single raw data\n\n")

def serverSide():
    server_config = h2.config.H2Configuration(client_side=False, header_encoding=None, validate_outbound_headers=False, normalize_outbound_headers=False, validate_inbound_headers=False, normalize_inbound_headers=False, logger=cfx_log)
    server_conn = h2.connection.H2Connection(config=server_config)
    server_conn.initiate_connection()  # Start HTTP/2 connection
    event_cnt = 0
    for raw_frame in [raw_cfx_bytes11, raw_cfx_bytes21, raw_cfx_bytes31, raw_cfx_bytes41, raw_cfx_bytes51]:
        event_cnt = event_cnt + 1
        print(f"\n****** Server EVENT.{event_cnt} Start to Process single single raw data\n")
        try:
            events = server_conn.receive_data(raw_frame)  # Correctly retrieve events
        except Exception as e:
            print(f"\n***** EVENT.{event_cnt} ERROR< {e} >")
            continue
        
        handle_event(events)
        print(f"\n****** EVENT.{event_cnt}  Done to Process single single raw data\n\n")
print("Main: start\n")
print("Main: client start\n")
clientSide()
print("Main: Server start\n")
serverSide()
