class Create:
    def create_network(self, conn):
        try:
            print("\r\n---Create Network-----------")
            while True:
                try:
                    network_count = int(raw_input("Please enter no of networks to create: ")) + 1
                    # 2
                except ValueError:
                    print("Please enter number.")
                    continue
                else:
                    break

            for i in range(1, network_count):
                while True:
                    network_name_id = str(raw_input("Enter Network Name: ")).strip()
                    # Public01
                    # search_networks(name_or_id=None, filters=None)
                    networks = conn.search_networks(network_name_id)
                    if len(networks) != 0:
                        print("Network already exists. Please enter other Network Name.")
                        continue
                    else:
                        print(network_name_id)
                        break

                while True:
                    subnet_create = str(raw_input("Do you want to create subnet for this network? (y/n): ")).strip()
                    if subnet_create == "Y" or subnet_create == "y":
                        subnet_name = str(raw_input("Enter Subnet Name: ")).strip()
                        cidr_ip = str(raw_input("Enter Network Address: (eg. 192.168.0.0/24) : ")).strip()
                        gateway_ip = str(raw_input("Enter Gateway IP: (eg. 192.168.0.1) : ")).strip()
                        break
                    elif subnet_create == "N" or subnet_create == "n":
                        print("No Subnet will be created.")
                        subnet_name = ""
                        cidr_ip = ""
                        gateway_ip = ""
                        break

                '''
                create_network(name, shared=False, admin_state_up=True, external=False, provider=None,
                project_id=None, availability_zone_hints=None)
                '''
                network = conn.create_network(name=network_name_id, admin_state_up='True')
                print("Network " + network.name + " Created.\r\n")
                if subnet_create == "Y" or subnet_create == "y":
                    '''
                    create_subnet(network_name_or_id, cidr=None, ip_version=4, enable_dhcp=False, subnet_name=None,
                    tenant_id=None, allocation_pools=None, gateway_ip=None, disable_gateway_ip=False,
                    dns_nameservers=None, host_routes=None, ipv6_ra_mode=None, ipv6_address_mode=None,
                    use_default_subnetpool=False)
                    '''
                    conn.create_subnet(network_name_or_id=network_name_id, ip_version='4', enable_dhcp=True, subnet_name=subnet_name, cidr=cidr_ip, gateway_ip=gateway_ip)
                    print("Network " + network.name + " with subnet " + cidr_ip + " Created.\r\n")
        except Exception as e:
            print("Error in code: " + str(e))
