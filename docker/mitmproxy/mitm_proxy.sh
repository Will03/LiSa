# sysctl -w net.ipv4.ip_forward=1
apt-get update
apt install iptables -y
useradd --create-home mitmproxyuser
# su mitmproxyuser -H bash -c 'cd ~ && pip install --user mitmproxy'

# iptables -t nat -A OUTPUT -p tcp -m owner ! --uid-owner mitmproxyuser --dport 80 -j REDIRECT --to-port 8080
# iptables -t nat -A OUTPUT -p tcp -m owner ! --uid-owner mitmproxyuser --dport 443 -j REDIRECT --to-port 8080
# ip6tables -t nat -A OUTPUT -p tcp -m owner ! --uid-owner mitmproxyuser --dport 80 -j REDIRECT --to-port 8080
# ip6tables -t nat -A OUTPUT -p tcp -m owner ! --uid-owner mitmproxyuser --dport 443 -j REDIRECT --to-port 8080

# su mitmproxyuser -c 'mitmdump --mode transparent --showhost --set block_global=false | tee /tmp/traffic' &

# iptables -t nat -A OUTPUT -p tcp -m iprange -s --dport 80 -j DNAT --to-destination 172.44.0.15:8080
# iptables -t nat -A OUTPUT -p tcp -m iprange --src-range 10.50.10.20-172.44.0.14 --dport 443 -j DNAT --to-destination 172.44.0.15:8080