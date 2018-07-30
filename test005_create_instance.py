class Create:
    def create_instance(self, conn):
        try:
            print("\r\n---Create Instance------")
            while True:
                try:
                    instance_count = int(str(raw_input("Enter Number of Instance to create: ")).strip()) + 1
                    # 2
                except ValueError:
                    print("Please enter number.")
                    continue
                else:
                    break

            for i in range(1, instance_count):
                while True:
                    image_name_id = str(raw_input("Enter Image Name or Id: ")).strip()
                    # cirros-0.3.5-x86_64-disk
                    # get_image(name_or_id, filters=None)
                    image = conn.get_image(image_name_id)
                    if image is None:
                        print("Image not found. Please enter other Image Name.")
                        continue
                    else:
                        print(image.name)
                        break

                while True:
                    flavor_name_id = str(raw_input("Enter Flavor Name or Id: ")).strip()
                    # m1.micro
                    # get_flavor(name_or_id, filters=None, get_extra=True)
                    flavor = conn.get_flavor(flavor_name_id)
                    if flavor is None:
                        print("Flavor not found. Please enter other Flavor Name.")
                        continue
                    else:
                        print(flavor.name)
                        break

                while True:
                    instance_name = str(raw_input("Enter Instance Name: ")).strip()
                    # Instance01
                    if instance_name == "":
                        print("Please provide Instance Name.")
                        continue
                    else:
                        # get_server(name_or_id=None, filters=None, detailed=False, bare=False, all_projects=False)
                        instance = conn.get_server(instance_name)
                        if instance is not None:
                            print("Instance " + instance_name + " already exists.")
                            continue
                        else:
                            print(instance_name)
                            break

                while True:
                    network_name_id = str(raw_input("Enter Network Name: ")).strip()
                    # Public01
                    # # get_network(name_or_id, filters=None)
                    network = conn.get_network(network_name_id)
                    if network is None:
                        print("Network not found. Please enter other Network Name or exit and create a new Network.")
                        continue
                    else:
                        print(network.name)
                        break

                if image is not None and flavor is not None and network is not None and instance_name != "":
                    '''
                    create_server(name, image=None, flavor=None, auto_ip=True, ips=None, ip_pool=None,
                                  root_volume=None, terminate_volume=False, wait=False, timeout=180, reuse_ips=True,
                                  network=None, boot_from_volume=False, volume_size='50', boot_volume=None,
                                  volumes=None, nat_destination=None, group=None, **kwargs)
                    '''
                    conn.create_server(name=instance_name, image=image_name_id, flavor=flavor_name_id, auto_ip=True, network=network_name_id)
                    print("Instance " + str(instance_name) + " created.\r\n")
                else:
                    print("Please enter correct Image name or Flavor name or Instance name.\r\n")
        except Exception as e:
            print("Error in code: " + str(e))
