# FROM mitmproxy/mitmproxy:latest

# CMD ["sh","-c","mitmdump --showhost --mode transparent --set block_global=false"]

FROM python:3.6-slim

ARG maxmind_key

RUN apt-get update && apt-get install -y --no-install-recommends \
    iptables \
    iputils-ping \
    wget


ENV PYTHONPATH /home/lisa

WORKDIR /home/lisa

RUN pip install mitmproxy
COPY ./mitm_proxy.sh /mitm_proxy.sh
RUN chmod +x /mitm_proxy.sh;/mitm_proxy.sh &
CMD ["sh" ,"-c","bash"]
