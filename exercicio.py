#!/usr/bin/python
from mininet.log import setLogLevel, info
from mn_wifi.cli import CLI
from mn_wifi.net import Mininet_wifi


def topology(remote_controller):
    "Create a network."
    net = Mininet_wifi()

    info("*** Adding datacenter\n")

    server1 = net.addHost("server1", ip="10.0.1.10", mac="00:00:00:00:01:01")
    server2 = net.addHost("server2", ip="10.0.1.11", mac="00:00:00:00:01:02")
    switchDC1 = net.addSwitch("switchDC1")
    switchDC1.cmd(
        'ovs-ofctl add-flow {} "actions=output:NORMAL"'.format(switchDC1.name)
    )

    info("*** Adding switches de nucleo\n")

    switchAG1 = net.addSwitch("switchAG1")
    switchAG1.cmd(
        'ovs-ofctl add-flow {} "actions=output:NORMAL"'.format(switchAG1.name)
    )

    info("*** Adding stations/AP/switches BLOCO 1\n")

    staBL101 = net.addStation(
        "staBL101",
        ip="10.0.1.111",
        mac="00:00:00:00:02:21",
        position="42,90,0",
    )
    staBL102 = net.addStation(
        "staBL102",
        ip="10.0.1.112",
        mac="00:00:00:00:02:22",
        position="55,80,0",
    )
    staBL103 = net.addStation(
        "staBL103",
        ip="10.0.1.113",
        mac="00:00:00:00:02:23",
        position="42,30,0",
    )
    staBL104 = net.addStation(
        "staBL104",
        ip="10.0.1.114",
        mac="00:00:00:00:02:24",
        position="55,20,0",
    )
    apBL101 = net.addAccessPoint(
        "apBL101",
        failMode="standalone",
        mac="00:00:00:00:00:10",
        ssid="BLOCO1",
        mode="g",
        channel="1",
        position="50,100,0",
    )
    apBL102 = net.addAccessPoint(
        "apBL102",
        failMode="standalone",
        mac="00:00:00:00:00:11",
        ssid="BLOCO1",
        mode="g",
        channel="11",
        position="50,10,0",
    )

    info("*** Adding stations/AP/switches BLOCO 2\n")
    staBL201 = net.addStation(
        "staBL201",
        ip="10.0.1.211",
        mac="00:00:00:00:02:25",
        position="250,170,0",
    )
    staBL202 = net.addStation(
        "staBL202",
        ip="10.0.1.212",
        mac="00:00:00:00:02:26",
        position="250,160,0",
    )
    staBL203 = net.addStation(
        "staBL203",
        ip="10.0.1.213",
        mac="00:00:00:00:02:27",
        position="200,130,0",
    )
    staBL204 = net.addStation(
        "staBL204",
        ip="10.0.1.214",
        mac="00:00:00:00:02:28",
        position="200,120,0",
    )
    apBL201 = net.addAccessPoint(
        "apBL201",
        failMode="standalone",
        mac="00:00:00:00:00:12",
        ssid="BLOCO2",
        mode="g",
        channel="3",
        position="250,150,0",
    )
    apBL202 = net.addAccessPoint(
        "apBL202",
        failMode="standalone",
        mac="00:00:00:00:00:13",
        ssid="BLOCO2",
        mode="g",
        channel="10",
        position="200,100,200",
    )

    info("*** Adding stations/AP/switches BLOCO 3\n")
    staBL301 = net.addStation(
        "staBL301",
        ip="100.0.1.311",
        mac="00:00:00:00:02:29",
        position="105,300,0",
    )
    staBL302 = net.addStation(
        "staBL302",
        ip="100.0.1.312",
        mac="00:00:00:00:02:30",
        position="105,320,0",
    )
    staBL303 = net.addStation(
        "staBL303",
        ip="100.0.1.313",
        mac="00:00:00:00:02:31",
        position="140,230,0",
    )
    staBL304 = net.addStation(
        "staBL304",
        ip="100.0.1.314",
        mac="00:00:00:00:02:32",
        position="140,240,0",
    )
    apBL301 = net.addAccessPoint(
        "apBL301",
        failMode="standalone",
        mac="00:00:00:00:00:14",
        ssid="BLOCO3",
        mode="g",
        channel="4",
        position="105,280,0",
    )
    apBL302 = net.addAccessPoint(
        "apBL302",
        failMode="standalone",
        mac="00:00:00:00:00:15",
        ssid="BLOCO3",
        mode="g",
        channel="8",
        position="140,210,0",
    )

    info("*** Adding stations/AP/switches BLOCO 4\n")
    staBL401 = net.addStation(
        "staBL401",
        ip="110.0.1.411",
        mac="00:00:00:00:02:33",
        position="315,460,0",
    )
    staBL402 = net.addStation(
        "staBL402",
        ip="110.0.1.412",
        mac="00:00:00:00:02:34",
        position="315,470,0",
    )
    staBL403 = net.addStation(
        "staBL403",
        ip="110.0.1.413",
        mac="00:00:00:00:02:35",
        position="350,420,0",
    )
    staBL404 = net.addStation(
        "staBL404",
        ip="110.0.1.414",
        mac="00:00:00:00:02:36",
        position="350,430,0",
    )
    apBL401 = net.addAccessPoint(
        "apBL401",
        failMode="standalone",
        mac="00:00:00:00:00:16",
        ssid="BLOCO4",
        mode="g",
        channel="5",
        position="315,480,0",
    )
    apBL402 = net.addAccessPoint(
        "apBL402",
        failMode="standalone",
        mac="00:00:00:00:00:17",
        ssid="BLOCO4",
        mode="g",
        channel="13",
        position="350,410,0",
    )
    
    info("*** Adding stations/AP/switches BLOCO 5\n")
    staBL501 = net.addStation(
        "staBL501",
        ip="110.0.1.511",
        mac="00:00:00:00:02:37",
        position="410,80,0",
    )
    staBL502 = net.addStation(
        "staBL502",
        ip="110.0.1.512",
        mac="00:00:00:00:02:38",
        position="410,90,0",
    )
    staBL503 = net.addStation(
        "staBL503",
        ip="110.0.1.513",
        mac="00:00:00:00:02:39",
        position="412,20,0",
    )
    staBL504 = net.addStation(
        "staBL504",
        ip="110.0.1.514",
        mac="00:00:00:00:02:40",
        position="412,30,0",
    )
    apBL501 = net.addAccessPoint(
        "apBL501",
        failMode="standalone",
        mac="00:00:00:00:00:18",
        ssid="BLOCO5",
        mode="g",
        channel="1",
        position="410,90,0",
    )
    apBL502 = net.addAccessPoint(
        "apBL502",
        failMode="standalone",
        mac="00:00:00:00:00:19",
        ssid="BLOCO5",
        mode="g",
        channel="6",
        position="412,10,0",
    )

    switchBL1 = net.addSwitch("switchBL1")
    switchBL1.cmd(
        'ovs-ofctl add-flow {} "actions=output:NORMAL"'.format(switchAG1.name)
    )
    switchBL2 = net.addSwitch("switchBL2")
    switchBL2.cmd(
        'ovs-ofctl add-flow {} "actions=output:NORMAL"'.format(switchAG1.name)
    )
    switchBL3 = net.addSwitch("switchBL3")
    switchBL3.cmd(
        'ovs-ofctl add-flow {} "actions=output:NORMAL"'.format(switchAG1.name)
    )
    switchBL4 = net.addSwitch("switchBL4")
    switchBL4.cmd(
        'ovs-ofctl add-flow {} "actions=output:NORMAL"'.format(switchAG1.name)
    )
    switchBL5 = net.addSwitch("switchBL5")
    switchBL5.cmd(
        'ovs-ofctl add-flow {} "actions=output:NORMAL"'.format(switchAG1.name)
    )


    info("*** Configuring propagation model\n")
    net.setPropagationModel(model="logDistance", exp=4)

    info("*** Configuring WiFi Nodes\n")
    net.configureWifiNodes()

    info("*** Creating links\n")

    info("**** Creating links DC\n")
    net.addLink(server1, switchDC1, bw=1000)
    net.addLink(server2, switchDC1, bw=1000)

    info("**** Creating links DC-AG\n")
    net.addLink(switchDC1, switchAG1, bw=1000)

    info("**** Creating links AG-BLOCOS\n")
    net.addLink(switchAG1, switchBL1, bw=1000)
    net.addLink(switchAG1, switchBL2, bw=1000)
    net.addLink(switchAG1, switchBL3, bw=1000)
    net.addLink(switchAG1, switchBL4, bw=1000)
    net.addLink(switchAG1, switchBL5, bw=1000)


    info("**** Creating links BLOCO 1\n")
    net.addLink(apBL101, switchBL1, bw=100)
    net.addLink(apBL102, switchBL1, bw=100)
    net.addLink(staBL101, apBL101)
    net.addLink(staBL102, apBL101)
    net.addLink(staBL103, apBL102)
    net.addLink(staBL104, apBL102)

    info("**** Creating links BLOCO 2\n")
    net.addLink(apBL201, switchBL2, bw=100)
    net.addLink(apBL202, switchBL2, bw=100)
    net.addLink(staBL201, apBL201)
    net.addLink(staBL202, apBL201)
    net.addLink(staBL203, apBL202)
    net.addLink(staBL204, apBL202)

    info("**** Creating links BLOCO 3\n")
    net.addLink(apBL301, switchBL3, bw=100)
    net.addLink(apBL302, switchBL3, bw=100)
    net.addLink(staBL301, apBL301)
    net.addLink(staBL302, apBL301)
    net.addLink(staBL303, apBL302)
    net.addLink(staBL304, apBL302)

    info("**** Creating links BLOCO 4\n")
    net.addLink(apBL401, switchBL4, bw=100)
    net.addLink(apBL402, switchBL4, bw=100)
    net.addLink(staBL401, apBL401)
    net.addLink(staBL402, apBL401)
    net.addLink(staBL403, apBL402)
    net.addLink(staBL404, apBL402)

    info("**** Creating links BLOCO 5\n")
    net.addLink(apBL501, switchBL5, bw=100)
    net.addLink(apBL502, switchBL5, bw=100)
    net.addLink(staBL501, apBL501)
    net.addLink(staBL502, apBL501)
    net.addLink(staBL503, apBL502)
    net.addLink(staBL504, apBL502)

    info("*** Starting network\n")
    net.plotGraph(max_x=500, max_y=500)
    net.start()
    net.staticArp()

    info("*** Running CLI\n")
    CLI(net)

    info("*** Stopping network\n")
    net.stop()


if __name__ == "__main__":
    setLogLevel("info")
    remote_controller = False
    topology(remote_controller)
