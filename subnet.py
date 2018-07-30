import connect
import test013_list_subnet
import test014_create_subnet
import test015_delete_subnet

try:
    c = connect.create_connection('http://127.0.0.1/identity', 'admin', 'admin', 'secret', 'RegionOne', 'default', 'default')

    while True:
        print("\r\n---Manage Subnet----------------------------------")
        print("Select one of the following option:")
        print("Select 1 to List Subnets\r\nSelect 2 to Create Subnets\r\nSelect 3 to Delete Subnets\r\nSelect 0 to Exit\r\n")
        while True:
            try:
                selection = int(raw_input("Your input: "))
            except ValueError:
                print("Please select one of the option.")
                continue
            else:
                break

        if selection == 0:
            print("Exit Program.")
            exit()
        elif selection == 1:
            list_sub = test013_list_subnet.List()
            list_sub.list_network_subnet(c)
        elif selection == 2:
            create_sub = test014_create_subnet.Create()
            create_sub.create_network_subnet(c)
        elif selection == 3:
            delete_sub = test015_delete_subnet.Delete()
            delete_sub.delete_network_subnet(c)
except Exception as e:
    print("Error in code: " + str(e))
