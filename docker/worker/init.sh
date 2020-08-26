#!/bin/sh

echo "nameserver 8.8.8.8" | cat - /etc/resolv.conf > /tmp/resolv.conf && cat /tmp/resolv.conf > /etc/resolv.conf
echo "precedence ::ffff:0:0/96  100" > /etc/gai.conf

if [ -n "${VPN}" ]; then
  echo "Connecting to VPN."
  openvpn --config "${VPN}/config.ovpn" --daemon
  sleep 3

  if [ $(ip link | grep tun0 | wc -l) -lt 1 ]; then
    echo "Error connecting to VPN."
    exit 2
  fi
fi

echo "ip addr"
ip addr

echo "/etc/hosts"
cat /etc/hosts

echo "/etc/resolv.conf"
cat /etc/resolv.conf

#--mitm proxy--
useradd --create-home mitmproxyuser
iptables -t nat -A OUTPUT -p tcp -m owner ! --uid-owner mitmproxyuser --dport 80 -j REDIRECT --to-port 8080
iptables -t nat -A OUTPUT -p tcp -m owner ! --uid-owner mitmproxyuser --dport 443 -j REDIRECT --to-port 8080
touch /tmp/http_traffic
chmod 777 /tmp/http_traffic
su mitmproxyuser -c 'mitmdump --mode transparent -s /home/lisa/docker/mitmproxy/http_dump.py --showhost --set block_global=false | tee /tmp/total_traffic' &

# wait for mitmproxy start
sleep 20
mkdir /usr/share/ca-certificates/extra/
wget http://mitm.it/cert/pem -O /usr/share/ca-certificates/extra/mitm.crt
echo "extra/mitm.crt"  >> /etc/ca-certificates.conf
update-ca-certificates
#--mitm proxy--

su - lisa -c "celery -A lisa.web_api.tasks worker --loglevel=info --concurrency=1 -n lisa-worker@%h"
