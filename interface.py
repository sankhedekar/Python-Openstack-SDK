import connect
import test010_list_interface
import test011_create_interface
import test012_delete_interface

try:
    c = connect.create_connection('http://127.0.0.1/identity', 'admin', 'admin', 'secret', 'RegionOne', 'default', 'default')

    while True:
        print("\r\n---Manage Interfaces----------------------------------")
        print("Select one of the following option:")
        print("Select 1 to List Interfaces\r\nSelect 2 to Create Interfaces\r\nSelect 3 to Delete Interfaces\r\nSelect 0 to Exit\r\n")
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
            list_int = test010_list_interface.List()
            list_int.list_router_interface(c)
        elif selection == 2:
            create_int = test011_create_interface.Create()
            create_int.create_router_interface(c)
        elif selection == 3:
            delete_int = test012_delete_interface.Delete()
            delete_int.delete_router_interface(c)
except Exception as e:
    print("Error in code: " + str(e))
