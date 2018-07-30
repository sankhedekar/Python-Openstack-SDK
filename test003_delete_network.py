class Delete:
    def delete_network(self, conn):
        try:
            print("\r\n---Delete Network-------")
            network_name_id = str(raw_input("Please provide Network name or id to delete: ")).strip()
            # get_network(name_or_id, filters=None)
            network = conn.network.find_network(network_name_id)
            if network is not None:
                if len(network.subnet_ids) > 0:
                    for subnet_id in network.subnet_ids:
                        # delete_subnet(name_or_id)
                        conn.delete_subnet(subnet_id)
                    print("Subnet deleted")
                # delete_network(name_or_id)
                conn.delete_network(network_name_id)
                print("Network " + network_name_id + " deleted")
            else:
                print("Network " + network_name_id + " doesn't exists")
        except Exception as e:
            print("Error in code: " + str(e))
