class Delete:
    def delete_router_interface(self, conn):
        try:
            print("\r\n---Delete Interface-------")
            router_name = str(raw_input("Enter Router Name: ")).strip()
            router = conn.get_router(router_name)
            if router is not None:
                subnet_name_id = str(raw_input("Enter Subnet Name or ID: ")).strip()
                # get_subnet(name_or_id, filters=None)
                subnet = conn.get_subnet(subnet_name_id)
                if subnet is not None:
                    # remove_router_interface(router, subnet_id=None, port_id=None)
                    conn.remove_router_interface(router, subnet_id=subnet.id)
                    print("Router with interface " + subnet_name_id + " removed.")
                else:
                    print("Subnet " + subnet_name_id + " doesn't exists")
            else:
                print("Router " + router_name + " doesn't exists")
        except Exception as e:
            print("Error in code: " + str(e))
