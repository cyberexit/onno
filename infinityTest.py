#!/usr/bin/python

import mitmproxy

def response(flow):
    flow.response.content = flow.response.content.replace(b"</body>",b"</body><script>location = 'https://www.fbi.gov/investigate/cyber'</script>")

#infinityTest.py
