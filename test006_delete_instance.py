class Delete:
    def delete_instance(self, conn):
        try:
            print("\r\n---Delete Instance------")
            instance_name_id = str(raw_input("Please provide Instance name or id to delete: ")).strip()
            # get_server(name_or_id=None, filters=None, detailed=False, bare=False, all_projects=False)
            instance = conn.get_server(instance_name_id)
            if instance is not None:
                # delete_server(name_or_id, wait=False, timeout=180, delete_ips=False, delete_ip_retry=1)
                conn.delete_server(instance_name_id)
                print("Instance " + instance_name_id + " deleted")
            else:
                print("Instance " + instance_name_id + " doesn't exists")
        except Exception as e:
            print("Error in code: " + str(e))
