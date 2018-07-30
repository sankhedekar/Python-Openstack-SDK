class List:
    def list_instance(self, conn):
        try:
            print("\r\n---List Instance-------------")
            print("List of Instances:")
            # list_servers(detailed=False, all_projects=False, bare=False, filters=None)
            instances = conn.list_servers()
            for instance in instances:
                print(instance.name)
        except Exception as e:
            print("Error in code: " + str(e))
