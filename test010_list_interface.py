class List:
    def list_router_interface(self, conn):
        try:
            print("\r\n---List Interfaces-------------")
            print("List of Interfaces:")
            router_name = str(raw_input("Enter Router Name: ")).strip()
            router = conn.get_router(router_name)
            if router is not None:
                # list_router_interfaces(router, interface_type=None)
                router_interfaces = conn.list_router_interfaces(router)
                for router_interface in router_interfaces:
                    print("Interface with Fixed IP: " + str(router_interface.fixed_ips[0]["ip_address"]))
            else:
                print("Router " + router_name + " doesn't exists")
        except Exception as e:
            print("Error in code: " + str(e))
