class List:
    def list_network(self, conn):
        try:
            print("\r\n---List Network-------------")
            print("List of Networks:")
            # list_networks(filters=None)
            networks = conn.list_networks()
            for network in networks:
                print(network.name)
        except Exception as e:
            print("Error in code: " + str(e))
