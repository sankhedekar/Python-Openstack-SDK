class List:
    def list_router(self, conn):
        try:
            print("\r\n---List Routers---------")
            print("List of Routers:")
            # list_routers(filters=None)
            routers = conn.list_routers()
            for router in routers:
                print(router.name)
        except Exception as e:
            print("Error in code: " + str(e))
