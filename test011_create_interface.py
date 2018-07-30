class Create:
    def create_router_interface(self, conn):
        try:
            print("\r\n---Create Interface-----")
            while True:
                try:
                    interface_count = int(str(raw_input("Enter Number of Interface to create: ")).strip()) + 1
                    # 2
                except ValueError:
                    print("Please enter number.")
                    continue
                else:
                    break

            for i in range(1, interface_count):
                router_name = str(raw_input("Enter Router Name: ")).strip()
                router = conn.get_router(router_name)
                if router is not None:
                    subnet_name_id = str(raw_input("Enter Subnet Name or ID: ")).strip()
                    # get_subnet(name_or_id, filters=None)
                    subnet = conn.get_subnet(subnet_name_id)
                    if subnet is not None:
                        # add_router_interface(router, subnet_id=None, port_id=None)
                        conn.add_router_interface(router, subnet_id=subnet.id)
                        print("Interfaced Router with Subnet " + subnet_name_id)
                    else:
                        print("Subnet " + subnet_name_id + " doesn't exists")
                else:
                    print("Router " + router_name + " doesn't exists")
        except Exception as e:
            print("Error in code: " + str(e))
