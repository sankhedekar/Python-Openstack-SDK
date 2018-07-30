import connect
import test004_list_instance
import test005_create_instance
import test006_delete_instance

try:
    c = connect.create_connection('http://127.0.0.1/identity', 'admin', 'admin', 'secret', 'RegionOne', 'default', 'default')

    while True:
        print("\r\n---Manage Instances----------------------------------")
        print("Select one of the following option:")
        print("Select 1 to List Instances\r\nSelect 2 to Create Instances\r\nSelect 3 to Delete Instances\r\nSelect 0 to Exit\r\n")
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
            list_inst = test004_list_instance.List()
            list_inst.list_instance(c)
        elif selection == 2:
            create_inst = test005_create_instance.Create()
            create_inst.create_instance(c)
        elif selection == 3:
            delete_inst = test006_delete_instance.Delete()
            delete_inst.delete_instance(c)
except Exception as e:
    print("Error in code: " + str(e))
