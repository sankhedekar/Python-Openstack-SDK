class List:
    def list_network_subnet(self, conn):
        try:
            print("\r\n---List Subnets---------")
            print("List of Subnets:")
            # list_subnets(filters=None)
            subnets = conn.list_subnets()
            for subnet in subnets:
                print(subnet.name)
        except Exception as e:
            print("Error in code: " + str(e))
