import connect
import test001_list_network
import test002_create_network
import test003_delete_network

try:
    c = connect.create_connection('http://127.0.0.1/identity', 'admin', 'admin', 'secret', 'RegionOne', 'default', 'default')

    while True:
        print("\r\n---Manage Networks---------------------------------------")
        print("Select one of the following option:")
        print("Select 1 to List Networks\r\nSelect 2 to Create Networks\r\nSelect 3 to Delete Networks\r\nSelect 0 to Exit\r\n")
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
            list_nw = test001_list_network.List()
            list_nw.list_network(c)
        elif selection == 2:
            create_nw = test002_create_network.Create()
            create_nw.create_network(c)
        elif selection == 3:
            delete_nw = test003_delete_network.Delete()
            delete_nw.delete_network(c)
        else:
            print("Please select one of the option.")

except Exception as e:
    print("Error in code: " + str(e))
