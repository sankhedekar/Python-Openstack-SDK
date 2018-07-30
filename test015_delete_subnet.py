class Delete:
    def delete_network_subnet(self, conn):
        try:
            print("\r\n---Delete Subnet-------")
            subnet_name_id = str(raw_input("Please provide Subnet name or id to delete: ")).strip()
            # get_subnet(name_or_id, filters=None)
            subnet = conn.get_subnet(subnet_name_id)
            if subnet is not None:
                # delete_subnet(name_or_id)
                conn.delete_subnet(subnet.id)
                print("Subnet " + subnet_name_id + " deleted")
            else:
                print("Subnet " + subnet_name_id + " doesn't exists")
        except Exception as e:
            print("Error in code: " + str(e))
