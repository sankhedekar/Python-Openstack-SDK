class Create:
    def create_router(self, conn):
        try:
            print("\r\n---Create Router--------")
            while True:
                try:
                    router_count = int(raw_input("Please enter no of routers to create: ")) + 1
                    # 2
                except ValueError:
                    print("Please enter number.")
                    continue
                else:
                    break

            for i in range(1, router_count):
                router_name = str(raw_input("Enter Router Name: ")).strip()
                ext_network = str(raw_input("Enter External Network Name: ")).strip()

                # get_network(name_or_id, filters=None)
                ext_gateway_net = conn.get_network(ext_network)
                ext_gateway_net_id = ext_gateway_net.id
                # create_router(name=None, admin_state_up=True, ext_gateway_net_id=None, enable_snat=None,
                # ext_fixed_ips=None, project_id=None, availability_zone_hints=None)
                router = conn.create_router(name=router_name, admin_state_up=True, ext_gateway_net_id=ext_gateway_net_id)

                print("Router " + router.name + " Created.\r\n")
        except Exception as e:
            print("Error in code: " + str(e))
