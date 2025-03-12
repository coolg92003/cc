import struct
import hpack
from io import BytesIO

# Decode HPACK-encoded headers
def decode_headers(headers_data):
    """
    Decodes HPACK-encoded headers.
    """
    decoder = hpack.Decoder()
    headers = decoder.decode(headers_data)
    return headers

# Helper function to decode HTTP/2 Frame Header
def decode_frame_header(data):
    """
    Decodes the first 9 bytes of an HTTP/2 frame (frame header).
    """
    # ! network byte order
    # Length is 3 bytes, Type is 1 byte, Flags is 1 byte, Stream ID is 4 bytes.
    length, type_, flags, stream_id = struct.unpack('!3s B B I', data[:9])

    # Convert length (3 bytes) to an integer
    length = struct.unpack('!I', b'\x00' + length)[0]
    
    return length, type_, flags, stream_id

def decode_http2_frame_all_types(raw_data):
    """
    Decodes all HTTP/2 frames from raw HTTP/2 data.
    """
    print("\tdecode_http2_frame_all_types:")
    buffer = BytesIO(raw_data)
    frames = []

    while True:
        # Read the first 9 bytes for the frame header
        frame_header = buffer.read(9)
        if not frame_header:
            break  # End of data
        
        length, type_, flags, stream_id = decode_frame_header(frame_header)
        print(f"\t\tCurrent frame length={length}, type={type_}, flag={flags}, stream_id={stream_id}")
        frame_data = buffer.read(length)  # Read the frame data (based on the length)
        if type_ == 0x1:  # HEADERS frame (type 0x1)
            print("\t\tHeader:")
            headers = decode_headers(frame_data)  # Decode headers with HPACK
            frames.append({'type': 'HEADERS', 'headers': headers})
            for item in headers:
                print(f"\t\t\t{item}")
        else:
            #frames.append({'type': 'OTHER', 'data': frame_data})  # Store other frame data
            print(f"\t\tother frame and type is {type_}")
    
    #print(frames)
    return frames  # Return all frames (both HEADERS and other frames)


# Example Usage
#raw_http2_data = b'\x00\x00\x1f\x01\x00\x00\x00\x00\x01'  # An example raw HTTP/2 data (HEADERS frame)
raw_http2_data = b'\000\000\014\004\000\000\000\000\000\000\004?\377\377\377\000\003\000\000\001\000\000\000\000\004\001\000\000\000\000\000\000\004\010\000\000\000\000\000?\377\000\000\000\000\036\001\004\000\000\000\013 \010\202\020\003\017\022\226\344Y>\224\010\224\302X\324\020\004\332\200\025\306\201p\002S\026\215\377\000\000\000\000\001\000\000\000\001'
#raw_http2_rea = b'\000\000\036\004\000\000\000\000\000\000\001\000\000\000\000\000\002\000\000\000\000\000\003\000\000\020\000\000\004\020\000\000\000\000\010\000\000\000\000\000\000\004\010\000\000\000\000\000\017\377\000\001\000\000\233\001\004\000\000\000\001\004\235b\252\311*\325\236\203\023\320\355L\347\260\336\306\223\036\246;\205\201\327Z\310*\020c\324\217\206A\212\010\235\\\013\201p\334y\347\237\203@\203A\351/\203Rs\370@\203\3618\323\204P\275\313g\\\203\010\037\017@\215\362\264\247\263\300\354\220\262-]\207I\377\203\235)\257@\211\362\265\205\355iP\225\215\'\232\014`~W\n\025\202\'\036Y\246_\"\303$\203X\2156\t_\214L\310\'?@\226\362\261j\356\177K\027\315e\"K\"\326vY&\244\247\265+R\217\204\013`\000?\000\004C\000\001\000\000\000\001 { \t\"ascReqData\":  \t{ \t\t\"afChargId\": \"PCSF:1-cfed-0-1-0000000063185a10-0000000000014f35\", \t\t\"gpsi\": \"msisdn00000000001\", \t\t\"medComponents\": \t\t{ \t\t\t\"1\": \t\t\t{ \t\t\t\t\"codecs\": [\"downlink\\r\\noffer\\r\\nm=audio 26512 RTP/AVP 8\\r\\n\", \"uplink\\r\\nanswer\\r\\nm=audio 4001 RTP/AVP 8\\r\\n\"], \t\t\t\t\"fStatus\": \"ENABLED\", \t\t\t\t\"marBwDl\": \"128000 bps\", \t\t\t\t\"marBwUl\": \"128000 bps\", \t\t\t\t\"medCompN\": 1, \t\t\t\t\"medSubComps\": \t\t\t\t{ \t\t\t\t\t\"1\": \t\t\t\t\t{ \t\t\t\t\t\t\"fDescs\": [\"permit in 17 from 135.2.207.203 4001 to 135.248.246.57 26512\", \"permit out 17 from 135.248.246.57 26512 to 135.2.207.203 4001\"], \t\t\t\t\t\t\"fNum\": 1 \t\t\t\t\t}, \t\t\t\t\t\"2\": \t\t\t\t\t{ \t\t\t\t\t\t\"fDescs\": [\"permit in 17 from 135.2.207.203 4002 to 135.248.246.57 26513\", \"permit out 17 from 135.248.246.57 26513 to 135.2.207.203 4002\"], \t\t\t\t\t\t\"fNum\": 2, \t\t\t\t\t\t\"flowUsage\": \t\t\t\t\t\t\"RTCP\"}}, \t\t\t\t\t\t\"medType\": \"AUDIO\" \t\t\t\t\t} \t\t\t}, \t\t\t\t\"notifUri\": \"http://127.0.0.1:8089/npcf-policyauthorization/v1/app-sessions/cngss-6677455584-pbwtt/pcsf-test.61965b530b1a0001;117;1;5.377749659.7.68378\", \t\t\t\t\"servInfStatus\": \"FINAL\", \t\t\t\t\"suppFeat\": \"10\", \t\t\t\t\"ueIpv4\": \"192.168.90.167\" \t\t} }'
raw_http2_rea = b'PRI * HTTP/2.0\r\n\r\nSM\r\n\r\n\000\000\036\004\000\000\000\000\000\000\001\000\000\000\000\000\002\000\000\000\000\000\003\000\000\020\000\000\004\020\000\000\000\000\010\000\000\000\000\000\000\004\010\000\000\000\000\000\017\377\000\001\000\000\233\001\004\000\000\000\001\004\235b\252\311*\325\236\203\023\320\355L\347\260\336\306\223\036\246;\205\201\327Z\310*\020c\324\217\206A\212\010\235\\\013\201p\334y\347\237\203@\203A\351/\203Rs\370@\203\3618\323\204P\275\313g\\\203\010\037\017@\215\362\264\247\263\300\354\220\262-]\207I\377\203\235)\257@\211\362\265\205\355iP\225\215\'\232\014`~W\n\025\202\'\036Y\246_\"\303$\203X\2156\t_\214L\310\'?@\226\362\261j\356\177K\027\315e\"K\"\326vY&\244\247\265+R\217\204\013`\000?\000\004C\000\001\000\000\000\001 { \t\"ascReqData\":  \t{ \t\t\"afChargId\": \"PCSF:1-cfed-0-1-0000000063185a10-0000000000014f35\", \t\t\"gpsi\": \"msisdn00000000001\", \t\t\"medComponents\": \t\t{ \t\t\t\"1\": \t\t\t{ \t\t\t\t\"codecs\": [\"downlink\\r\\noffer\\r\\nm=audio 26512 RTP/AVP 8\\r\\n\", \"uplink\\r\\nanswer\\r\\nm=audio 4001 RTP/AVP 8\\r\\n\"], \t\t\t\t\"fStatus\": \"ENABLED\", \t\t\t\t\"marBwDl\": \"128000 bps\", \t\t\t\t\"marBwUl\": \"128000 bps\", \t\t\t\t\"medCompN\": 1, \t\t\t\t\"medSubComps\": \t\t\t\t{ \t\t\t\t\t\"1\": \t\t\t\t\t{ \t\t\t\t\t\t\"fDescs\": [\"permit in 17 from 135.2.207.203 4001 to 135.248.246.57 26512\", \"permit out 17 from 135.248.246.57 26512 to 135.2.207.203 4001\"], \t\t\t\t\t\t\"fNum\": 1 \t\t\t\t\t}, \t\t\t\t\t\"2\": \t\t\t\t\t{ \t\t\t\t\t\t\"fDescs\": [\"permit in 17 from 135.2.207.203 4002 to 135.248.246.57 26513\", \"permit out 17 from 135.248.246.57 26513 to 135.2.207.203 4002\"], \t\t\t\t\t\t\"fNum\": 2, \t\t\t\t\t\t\"flowUsage\": \t\t\t\t\t\t\"RTCP\"}}, \t\t\t\t\t\t\"medType\": \"AUDIO\" \t\t\t\t\t} \t\t\t}, \t\t\t\t\"notifUri\": \"http://127.0.0.1:8089/npcf-policyauthorization/v1/app-sessions/cngss-6677455584-pbwtt/pcsf-test.61965b530b1a0001;117;1;5.377749659.7.68378\", \t\t\t\t\"servInfStatus\": \"FINAL\", \t\t\t\t\"suppFeat\": \"10\", \t\t\t\t\"ueIpv4\": \"192.168.90.167\" \t\t} }'
#raw_http2_jstring = b'\u0000\u0000\u001e\u0004\u0000\u0000\u0000\u0000\u0000\u0000\u0001\u0000\u0000\u0000\u0000\u0000\u0002\u0000\u0000\u0000\u0000\u0000\u0003\u0000\u0000\u0010\u0000\u0000\u0004\u0010\u0000\u0000\u0000\u0000\b\u0000\u0000\u0000\u0000\u0000\u0000\u0004\b\u0000\u0000\u0000\u0000\u0000\u000f \u0000\u0001\u0000\u0000 \u0001\u0004\u0000\u0000\u0000\u0001\u0004 b  ՞ \u0013 L Ɠ\u001e ;    \u0010cԏ A \b \\\u000b p 矃@ A  Rs @  ӄP  \\ \b\u001f\u000f@ 򴧳   -] I   ) @  iP  ' \u0000 19\u001c 4 Y  *єbY  ' y @   K\u0017 \"K\" Y&   +R  \u000b`\u0000?\u0000\u0004C\u0000\u0001\u0000\u0000\u0000\u0001 { \t\"ascReqData\":  \t{ \t\t\"afChargId\": \"PCSF:1-cfed-0-1-0000000063185a10-0000000000014f35\", \t\t\"gpsi\": \"msisdn00000000001\", \t\t\"medComponents\": \t\t{ \t\t\t\"1\": \t\t\t{ \t\t\t\t\"codecs\": [\"downlink\\r\\noffer\\r\\nm=audio 26512 RTP/AVP 8\\r\\n\", \"uplink\\r\\nanswer\\r\\nm=audio 4001 RTP/AVP 8\\r\\n\"], \t\t\t\t\"fStatus\": \"ENABLED\", \t\t\t\t\"marBwDl\": \"128000 bps\", \t\t\t\t\"marBwUl\": \"128000 bps\", \t\t\t\t\"medCompN\": 1, \t\t\t\t\"medSubComps\": \t\t\t\t{ \t\t\t\t\t\"1\": \t\t\t\t\t{ \t\t\t\t\t\t\"fDescs\": [\"permit in 17 from 135.2.207.203 4001 to 135.248.246.57 26512\", \"permit out 17 from 135.248.246.57 26512 to 135.2.207.203 4001\"], \t\t\t\t\t\t\"fNum\": 1 \t\t\t\t\t}, \t\t\t\t\t\"2\": \t\t\t\t\t{ \t\t\t\t\t\t\"fDescs\": [\"permit in 17 from 135.2.207.203 4002 to 135.248.246.57 26513\", \"permit out 17 from 135.248.246.57 26513 to 135.2.207.203 4002\"], \t\t\t\t\t\t\"fNum\": 2, \t\t\t\t\t\t\"flowUsage\": \t\t\t\t\t\t\"RTCP\"}}, \t\t\t\t\t\t\"medType\": \"AUDIO\" \t\t\t\t\t} \t\t\t}, \t\t\t\t\"notifUri\": \"http://127.0.0.1:8089/npcf-policyauthorization/v1/app-sessions/cngss-6677455584-pbwtt/pcsf-test.61965b530b1a0001;117;1;5.377749659.7.68378\", \t\t\t\t\"servInfStatus\": \"FINAL\", \t\t\t\t\"suppFeat\": \"10\", \t\t\t\t\"ueIpv4\": \"192.168.90.167\" \t\t} }'
# remove http2 preface
raw_http2_datar = raw_http2_rea[24:]
#print(raw_http2_datar)
headers = decode_http2_frame_all_types(raw_http2_datar)
headers = decode_http2_frame_all_types(raw_http2_data)
http2_preface = b'PRI * HTTP/2.0\r\n\r\nSM\r\n\r\n'
print("jstring")
#headers = decode_http2_frame_all_types(raw_http2_data)
print("jbytes")
#headers = decode_http2_frame_all_types(raw_http2_data)
import base64

b64_message = b"UFJJICogSFRUUC8yLjANCg0KU00NCg0KAAAeBAAAAAAAAAEAAAAAAAIAAAAAAAMAABAAAAQQAAAAAAgAAAAAAAAECAAAAAAAD/8AAQAAmwEEAAAAAQSdYqrJKtWegxPQ7UznsN7Gkx6mO4WB11rIKhBj1I+GQYoInVwLgXDceeefg0CDQekvg1Jz+ECD8TjThFC9y2dcgwgfD0CN8rSns8DskLItXYdJ/4OdKa9AifK1he1pUJWNJ5pxlsDcjYFngDeWaZbfWeG8RZuOQbL8oBOlB0CW8rFq7n9LF81lIksi1nZZJqSntStSj4QLYAA/AARDAAEAAAABIHsgCSJhc2NSZXFEYXRhIjogIAl7IAkJImFmQ2hhcmdJZCI6ICJQQ1NGOjEtY2ZlZC0wLTEtMDAwMDAwMDA2MzE4NWExMC0wMDAwMDAwMDAwMDE0ZjM1IiwgCQkiZ3BzaSI6ICJtc2lzZG4wMDAwMDAwMDAwMSIsIAkJIm1lZENvbXBvbmVudHMiOiAJCXsgCQkJIjEiOiAJCQl7IAkJCQkiY29kZWNzIjogWyJkb3dubGlua1xyXG5vZmZlclxyXG5tPWF1ZGlvIDI2NTEyIFJUUC9BVlAgOFxyXG4iLCAidXBsaW5rXHJcbmFuc3dlclxyXG5tPWF1ZGlvIDQwMDEgUlRQL0FWUCA4XHJcbiJdLCAJCQkJImZTdGF0dXMiOiAiRU5BQkxFRCIsIAkJCQkibWFyQndEbCI6ICIxMjgwMDAgYnBzIiwgCQkJCSJtYXJCd1VsIjogIjEyODAwMCBicHMiLCAJCQkJIm1lZENvbXBOIjogMSwgCQkJCSJtZWRTdWJDb21wcyI6IAkJCQl7IAkJCQkJIjEiOiAJCQkJCXsgCQkJCQkJImZEZXNjcyI6IFsicGVybWl0IGluIDE3IGZyb20gMTM1LjIuMjA3LjIwMyA0MDAxIHRvIDEzNS4yNDguMjQ2LjU3IDI2NTEyIiwgInBlcm1pdCBvdXQgMTcgZnJvbSAxMzUuMjQ4LjI0Ni41NyAyNjUxMiB0byAxMzUuMi4yMDcuMjAzIDQwMDEiXSwgCQkJCQkJImZOdW0iOiAxIAkJCQkJfSwgCQkJCQkiMiI6IAkJCQkJeyAJCQkJCQkiZkRlc2NzIjogWyJwZXJtaXQgaW4gMTcgZnJvbSAxMzUuMi4yMDcuMjAzIDQwMDIgdG8gMTM1LjI0OC4yNDYuNTcgMjY1MTMiLCAicGVybWl0IG91dCAxNyBmcm9tIDEzNS4yNDguMjQ2LjU3IDI2NTEzIHRvIDEzNS4yLjIwNy4yMDMgNDAwMiJdLCAJCQkJCQkiZk51bSI6IDIsIAkJCQkJCSJmbG93VXNhZ2UiOiAJCQkJCQkiUlRDUCJ9fSwgCQkJCQkJIm1lZFR5cGUiOiAiQVVESU8iIAkJCQkJfSAJCQl9LCAJCQkJIm5vdGlmVXJpIjogImh0dHA6Ly8xMjcuMC4wLjE6ODA4OS9ucGNmLXBvbGljeWF1dGhvcml6YXRpb24vdjEvYXBwLXNlc3Npb25zL2NuZ3NzLTY2Nzc0NTU1ODQtcGJ3dHQvcGNzZi10ZXN0LjYxOTY1YjUzMGIxYTAwMDE7MTE3OzE7NS4zNzc3NDk2NTkuNy42ODM3OCIsIAkJCQkic2VydkluZlN0YXR1cyI6ICJGSU5BTCIsIAkJCQkic3VwcEZlYXQiOiAiMTAiLCAJCQkJInVlSXB2NCI6ICIxOTIuMTY4LjkwLjE2NyIgCQl9IH0="
# Decode Base64
decoded_bytes = base64.b64decode(b64_message)
#print(decoded_bytes[24:])
headers = decode_http2_frame_all_types(decoded_bytes[24:])


print("Done")
