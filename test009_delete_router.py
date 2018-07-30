class Delete:
    def delete_router(self, conn):
        try:
            print("\r\n---Delete Router--------")
            router_name_id = str(raw_input("Please provide Router name to delete: "))

            router = conn.get_router(router_name_id)
            if router is not None:
                # delete_router(name_or_id)
                conn.delete_router(router_name_id)
                print("Router " + router_name_id + " deleted")
            else:
                print("Router " + router_name_id + " doesn't exists")
        except Exception as e:
            print("Error in code: " + str(e))
