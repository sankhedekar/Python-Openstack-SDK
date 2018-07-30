class Create:
    def create_network_subnet(self, conn):
        try:
            print("\r\n---Create Subnet------")
            while True:
                try:
                    subnet_count = int(str(raw_input("Enter Number of Subnets to create: ")).strip()) + 1
                    # 2
                except ValueError:
                    print("Please enter number.")
                    continue
                else:
                    break

            for i in range(1, subnet_count):
                while True:
                    network_name_id = str(raw_input("Enter Network Name: ")).strip()
                    # Public01
                    # search_networks(name_or_id=None, filters=None)
                    networks = conn.search_networks(network_name_id)
                    if len(networks) == 0:
                        print("Network does not exists.")
                        continue
                    else:
                        print(network_name_id)
                        break

                subnet_name = str(raw_input("Enter Subnet Name: ")).strip()
                cidr_ip = str(raw_input("Enter Network Address: (eg. 192.168.0.0/24) : ")).strip()
                gateway_ip = str(raw_input("Enter Gateway IP: (eg. 192.168.0.1) : ")).strip()

                '''
                create_subnet(network_name_or_id, cidr=None, ip_version=4, enable_dhcp=False, subnet_name=None,
                              tenant_id=None, allocation_pools=None, gateway_ip=None, disable_gateway_ip=False,
                              dns_nameservers=None, host_routes=None, ipv6_ra_mode=None, ipv6_address_mode=None,
                              use_default_subnetpool=False)
                '''

                conn.create_subnet(network_name_or_id=network_name_id, ip_version='4', enable_dhcp=True, subnet_name=subnet_name, cidr=cidr_ip, gateway_ip=gateway_ip)
                print("Network " + network_name_id + " with subnet " + cidr_ip + " Created.\r\n")
        except Exception as e:
            print("Error in code: " + str(e))
